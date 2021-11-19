import tensorflow as tf

from ..model_unit import BaseModel
from ..model_unit.GraphModelLayers import GCL
from ..train import Optimizer

class ST_MGCN(BaseModel):
    """

    References:
        - `Spatiotemporal multi-graph convolution network for ride-hailing demand forecasting (Geng Xu, et al., 2019)
          <http://www-scf.usc.edu/~yaguang/papers/aaai19_multi_graph_convolution.pdf>`_.
        - `A PyTorch implementation of the ST-MGCN model  (shawnwang-tech)
          <https://github.com/shawnwang-tech/ST-MGCN-pytorch>`_.

    Args:
        T(int): Input sequence length
        input_dim(int): Input feature dimension
        num_graph(int): Number of graphs used in the model.
        gcl_k(int): The highest order of Chebyshev Polynomial approximation in GCN.
        gcl_l(int): Number of GCN layers.
        lstm_units(int): Number of hidden units of RNN.
        lstm_layers(int): Number of LSTM layers.
        lr(float): Learning rate
        external_dim(int): Dimension of the external feature, e.g. temperature and wind are two dimension.
        code_version(str): Current version of this model code, which will be used as filename for saving the model
        model_dir(str): The directory to store model files. Default:'model_dir'.
        gpu_device(str): To specify the GPU to use. Default: '0'.
    """

    def __init__(self,
                 num_node,
                 T,
                 input_dim,
                 num_graph,
                 gcl_k,
                 gcl_l,
                 lstm_units,
                 lstm_layers,
                 lr,
                 external_dim,
                 code_version,
                 model_dir,
                 gpu_device,
                 closeness_len,
                 period_len,
                 trend_len,
                 external_lstm_len,
                 external_method="not-not-not",
                 embedding_dim=[8, 1, 8, 8],
                 poi_dim=None,
                 classified_external_feature_dim=[],
                 decay_param=None, **kwargs):

        super(ST_MGCN, self).__init__(code_version=code_version,
                                      model_dir=model_dir,
                                      gpu_device=gpu_device)

        self._num_node = num_node
        self._T = T
        self._input_dim = input_dim
        self._num_graph = num_graph
        self._gcl_k = gcl_k
        self._gcl_l = gcl_l
        self._lstm_units = lstm_units
        self._lstm_layers = lstm_layers
        self._lr = lr
        # add decay func
        self._optimizer = Optimizer(decay_param=decay_param,lr=self._lr)

        self._external_dim = external_dim
        self._poi_dim = poi_dim
        self._closeness_len = int(closeness_len)
        self._period_len = int(period_len)
        self._trend_len = int(trend_len)
        if "lstm" in external_method:
            self._external_lstm_len = int(external_lstm_len)
        else:
            self._external_lstm_len = None
        
        # external modelling method
        # ordered by 'representation-alignment-fusion' and split by '-'
        # eg. 'lstm-not-add'
        self.external_method = external_method.lower().split('-')

        self.earlyconcatFlag = True if len(self.external_method) == 1 and self.external_method[0] == "earlyconcat" else False
        if self.earlyconcatFlag:
            print("**** Using Early Concat Fusion Modeling techniques ****")
        
        self.earlyaddFlag = True if len(self.external_method) == 1 and self.external_method[0] == "earlyadd" else False
        if self.earlyaddFlag:
            print("**** Using Early Add Fusion Modeling techniques ****")

        # external dimension after one-hot orderd by weather/holiday/temporal position
        self._classified_external_feature_dim = classified_external_feature_dim 

        # embedding size
        if self._poi_dim is not None and self._poi_dim > 0:
            self._embedding_dim = embedding_dim
        else:
            self._embedding_dim = embedding_dim[:len(classified_external_feature_dim)]


    def build(self, init_vars=True, max_to_keep=5):
        with self._graph.as_default():
            # [batch, T, num_stations, input_dim]
            traffic_flow = tf.placeholder(tf.float32, [None, self._T, None, self._input_dim])
            self._input['traffic_flow'] = traffic_flow.name
            laplacian_matrix = tf.placeholder(tf.float32, [self._num_graph, None, None])
            self._input['laplace_matrix'] = laplacian_matrix.name
            target = tf.placeholder(tf.float32, [None, None, 1])
            self._input['target'] = target.name

            if self.earlyconcatFlag or self.earlyaddFlag:
                # with shape (slots, feature_dim, C P T len, 1)
                external_closeness = tf.placeholder(tf.float32, [None, None, self._closeness_len, 1],
                                                    name='external_closeness')
                self._input['external_closeness'] = external_closeness.name
                external_period = tf.placeholder(tf.float32, [None, None, self._period_len, 1],
                                                 name='external_period')
                self._input['external_period'] = external_period.name
                external_trend = tf.placeholder(tf.float32, [None, None, self._trend_len, 1],
                                                name='external_trend')
                self._input['external_trend'] = external_trend.name
            
            if self._external_dim is not None and self._external_dim > 0:
                external_input = tf.placeholder(tf.float32, [None, self._external_dim])
                self._input['external_feature'] = external_input.name

            if self._poi_dim is not None and self._poi_dim > 0:
                poi_feature = tf.placeholder(tf.float32, [None, self._num_node, self._poi_dim])
                self._input['poi_feature'] = poi_feature.name
                self._classified_external_feature_dim.append(self._poi_dim)

            if self._external_lstm_len is not None and self._external_lstm_len > 0:
                external_lstm_hidden = tf.placeholder(tf.float32, [None, None, self._external_lstm_len, 1],
                                               name='external_lstm_hidden')
                self._input['external_lstm_hidden'] = external_lstm_hidden.name



            station_number = tf.shape(traffic_flow)[-2]

            outputs = []

            for graph_index in range(self._num_graph):
                with tf.variable_scope('CGRNN_Graph%s' % graph_index, reuse=False):
                    f_k_g = GCL.add_multi_gc_layers(tf.reshape(traffic_flow, [-1, station_number, self._input_dim]),
                                                    gcn_k=1, gcn_l=1, output_size=self._input_dim,
                                                    laplacian_matrix=laplacian_matrix[graph_index],
                                                    activation=tf.nn.tanh)

                    f_k_g = tf.reshape(f_k_g, [-1, self._T, station_number, self._input_dim])

                    x_hat = tf.concat([f_k_g, traffic_flow], axis=-1)

                    z = tf.reduce_mean(x_hat, axis=-2, keepdims=True)

                    s = tf.layers.dense(tf.layers.dense(z, units=4, use_bias=False, activation=tf.nn.relu),
                                        units=1, use_bias=False, activation=tf.nn.sigmoid)

                    x_rnn = tf.multiply(traffic_flow, tf.tile(s, [1, 1, station_number, self._input_dim]))

                    x_rnn = tf.reshape(tf.transpose(x_rnn, perm=[0, 2, 1, 3]), [-1, self._T, self._input_dim])

                    for lstm_layer_index in range(self._lstm_layers):
                        x_rnn = tf.keras.layers.LSTM(units=self._lstm_units,
                                                     activation='tanh',
                                                     dropout=0.1,
                                                     kernel_regularizer=tf.contrib.layers.l2_regularizer(1e-4),
                                                     return_sequences=True if lstm_layer_index<self._lstm_layers-1
                                                                      else False)\
                                                    (x_rnn)

                    H = tf.reshape(x_rnn, [-1, station_number, self._lstm_units])

                    outputs.append(H)

            # outputs = tf.reduce_sum(outputs, axis=0)
            dense_inputs = tf.reduce_sum(outputs, axis=0)

            # external dims
            if len(self.external_method) > 1:
                if self.external_method[2] == "not":
                    print("**** This model didn't use external features ****")
                else:
                    print("**** Using Late Fusion Modeling techniques ****")
                    # representation stage
                    print("poi_dim",self._poi_dim)
                    print("external_dim",self._external_dim)

                    if self._external_dim is not None and self._external_dim > 0:
                        external_dense = tf.tile(tf.reshape(external_input, [-1, 1, self._external_dim]), [1, self._num_node, 1])

                    if self._poi_dim is not None and self._poi_dim > 0:
                        poi_dense = tf.reshape(poi_feature, [-1, self._num_node, self._poi_dim])
                        # if have external dimention
                        if self._external_dim is not None and self._external_dim > 0:
                            external_dense = tf.concat(
                                [external_dense, poi_dense], axis=-1)
                            print("Concat POI to External Features {} >> {}".format(self._external_dim,self._external_dim+self._poi_dim))
                            self._external_dim += self._poi_dim
                        else:
                            external_dense = poi_dense
                            #self._external_dim = self._poi_dim

                    if self.external_method[0] == "not":
                        print("**** This model doesn't have representation stage.****")
                        
                    elif self.external_method[0] == "emb":
                        if isinstance(self._embedding_dim, int):
                            pass
                        elif isinstance(self._embedding_dim[0], int):
                            self._embedding_dim = self._embedding_dim[0]
                        else:
                            ValueError(
                                "using one Embedding layer, the embedding_dim or its first element should be `int` type")
                        print(
                            "**** Using one embedding layer >> {} ****".format(self._embedding_dim))
                        external_dense = tf.keras.layers.Dense(units=self._embedding_dim, kernel_regularizer=tf.keras.regularizers.l2(
                            0.01), bias_regularizer=tf.keras.regularizers.l2(0.01))(external_dense)
                        #reshape_size = self._embedding_dim

                    elif self.external_method[0] == "multi":
                        print("classi",self._classified_external_feature_dim)
                        print("emb",self._embedding_dim)
                        if len(self._classified_external_feature_dim) != len(self._embedding_dim):
                            raise ValueError("external feature dim is not equal to specified embedding_dim, modify `embedding_dim`")
                        else:        
                            print("**** Using classified embedding layers {} >> {} ****".format(self._classified_external_feature_dim, self._embedding_dim))
                            embedding_output = []
                            ind = 0
                            for i,tmp in enumerate(self._classified_external_feature_dim):
                                tensor_slice = tf.strided_slice(external_dense,[0,0,ind],[tf.shape(external_dense)[0],tf.shape(external_dense)[1],ind+tmp],[1,1,1])
                                tensor_slice = tf.reshape(tensor_slice,[tf.shape(external_dense)[0],tf.shape(external_dense)[1], tmp])
                                extern_embedding = tf.keras.layers.Dense(units=self._embedding_dim[i],kernel_regularizer=tf.keras.regularizers.l2(0.01),bias_regularizer=tf.keras.regularizers.l2(0.01))(tensor_slice)
                                embedding_output.append(extern_embedding)
                                ind += tmp
                            external_dense = tf.concat(embedding_output,axis=-1)
                        #reshape_size = np.sum(self._embedding_dim)
                            
                    elif self.external_method[0] == "lstm":
                        context_lstm_hidden = 16
                        print("**** Using LSTM in Weather features and window size is {}. Mapping {} >> {} ****".format(self._external_lstm_len,self._external_dim,context_lstm_hidden))
                        cell = tf.keras.layers.LSTMCell(units=context_lstm_hidden)
                        multi_layer_gru = tf.keras.layers.StackedRNNCells([cell] * 1)
                        external_dense = tf.keras.layers.RNN(multi_layer_gru)(
                            tf.reshape(external_lstm_hidden, [-1, self._external_lstm_len, self._external_dim]))
                        reshape_size = context_lstm_hidden
                        external_dense = tf.tile(tf.reshape(external_dense, [-1, 1, reshape_size]),[1, self._num_node, 1])

                    else:
                        raise ValueError("The first `external method` parameter is wrong.")

                    # alignment stage
                    #external_dense = tf.tile(tf.reshape(external_dense, [-1, 1, 1, reshape_size]),[1, tf.shape(dense_inputs)[1], tf.shape(dense_inputs)[2], 1])
                    
                    if self.external_method[1] == "not":
                        print("**** This model doesn't have alignment stage.****")

                    elif self.external_method[1] == "linear":
                        external_dense = tf.keras.layers.Dense(units=dense_inputs.get_shape()[-1].value,activation=None,kernel_regularizer=tf.keras.regularizers.l2(0.01),bias_regularizer=tf.keras.regularizers.l2(0.01))(external_dense)
                    
                    else:
                        raise ValueError("The second `external method` parameter is wrong.")
                    
                    # fusion stage
                    if self.external_method[2] == "concat":
                        dense_inputs = tf.concat([dense_inputs, external_dense], axis=-1)

                    elif self.external_method[2] == "add":
                        dense_inputs = tf.add(dense_inputs,external_dense)

                    elif self.external_method[2] == "gating":
                        dense_inputs = tf.multiply(dense_inputs,external_dense)
                    
                    else:
                        raise ValueError("The third `external method` parameter is wrong.")

            prediction = tf.layers.dense(dense_inputs, units=1)

            loss = tf.sqrt(tf.reduce_mean(tf.square(prediction - target)), name='loss')

            # train_operation = tf.train.AdamOptimizer(self._lr).minimize(loss, name='train_op')
            train_operation, global_step_name, learning_rate_name = self._optimizer.build(loss_pre=loss)
            self._input['global_step'] = global_step_name

            # record output
            self._output['prediction'] = prediction.name
            self._output['loss'] = loss.name

            # record train operation
            self._op['train_op'] = train_operation.name

            super(ST_MGCN, self).build(init_vars=init_vars, max_to_keep=max_to_keep)

    # Step 1 : Define your '_get_feed_dict function‘, map your input to the tf-model
    def _get_feed_dict(self,
                       traffic_flow, 
                       laplace_matrix, 
                       external_lstm_hidden=None,
                       external_closeness=None,
                       external_period=None,
                       external_trend=None,
                       target=None, 
                       external_feature=None, 
                       poi_feature=None):
        feed_dict = {
            'traffic_flow': traffic_flow,
            'laplace_matrix': laplace_matrix,
        }
        if target is not None:
            feed_dict['target'] = target
        # if external_feature is not None:
        #     feed_dict['external_feature'] = external_feature
        
        if self._external_dim is not None and self._external_dim > 0:
            feed_dict['external_feature'] = external_feature
        if self._external_dim is not None and self._external_dim > 0:
            feed_dict['external_feature'] = external_feature
        if self._poi_dim is not None and self._poi_dim > 0:
            feed_dict['poi_feature'] = poi_feature
        if self._external_lstm_len is not None and self._external_lstm_len > 0:
            feed_dict['external_lstm_hidden'] = external_lstm_hidden
        if self.earlyconcatFlag or self.earlyaddFlag:
            feed_dict['external_closeness'] = external_closeness
            feed_dict['external_period'] = external_period
            feed_dict['external_trend'] = external_trend
        return feed_dict
