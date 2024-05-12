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
                 temporal_external_dim, # temporal external feature dimensions
                 spatial_external_dim, # spatial external feature dimensions
                 T,
                 input_dim,
                 num_graph,
                 gcl_k,
                 gcl_l,
                 lstm_units,
                 lstm_layers,
                 lr,
                 code_version,
                 model_dir,
                 gpu_device,
                 closeness_len,
                 period_len,
                 trend_len,
                 external_lstm_len,
                 external_method="not-not-not",
                 temporal_embedding_dim = [10, 1, 5], # dim of multiple embedding layer for temporal features
                 spatial_embedding_dim = [8, 32, 5, 8], # dim of multiple embedding layer for spatial features
                 single_embedding_dim = 16, # dim of single embedding layer
                 classified_temporal_feature_dim = [],
                 classified_spatial_feature_dim = [],
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

        self._temporal_external_dim = temporal_external_dim
        self._spatial_external_dim = spatial_external_dim
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
        self.external_method = external_method.split('-')

        self.earlyconcatFlag = True if len(self.external_method) == 1 and self.external_method[0] == "earlyconcat" else False
        if self.earlyconcatFlag:
            print("**** Using Early Concat Fusion Modeling techniques ****")
        
        self.earlyaddFlag = True if len(self.external_method) == 1 and self.external_method[0] == "earlyadd" else False
        if self.earlyaddFlag:
            print("**** Using Early Add Fusion Modeling techniques ****")

        # external dimension after one-hot orderd by weather/holiday/temporal position
        self._classified_temporal_feature_dim = classified_temporal_feature_dim 

        # external dimension after one-hot orderd by POIs/spatial position/demographic/road
        self._classified_spatial_feature_dim = classified_spatial_feature_dim 

        # embedding size
        self._temporal_embedding_dim = temporal_embedding_dim[:len(self._classified_temporal_feature_dim)]
        self._spatial_embedding_dim = spatial_embedding_dim[:len(self._classified_spatial_feature_dim)]
        self._single_embedding_dim = single_embedding_dim


    def build(self, init_vars=True, max_to_keep=5):
        with self._graph.as_default():
            # [batch, T, num_stations, input_dim]
            
            def MLP(hidden_state, input_tensor, activation=None):
                return tf.keras.layers.Dense(units=hidden_state,kernel_regularizer=tf.keras.regularizers.l2(0.01),bias_regularizer=tf.keras.regularizers.l2(0.01), activation=activation)(input_tensor)
            
            def multiple_embedding_layer(input_tensor, feature_dim_list, embedding_dim_list, agg_axis=-1, new_axis=False):
                '''
                input_tensor: input tensor with shape (batch_size, num_node, feature_dim)
                feature_dim_list: feature length for each type of context (e.g., [26, 2, 24]), sum(feature_dim_list) = feature_dim
                embedding_dim_list: embedding dim for each type of context (e.g., [8, 1, 8])
                agg_axis: axis for concatenation (default: -1)
                new_axis: concat to make a new axis in the last feature dimension
                '''
                output = []
                ind = 0
                for i,tmp in enumerate(feature_dim_list):
                    tensor_slice = tf.strided_slice(input_tensor,[0,0,ind],[tf.shape(input_tensor)[0],tf.shape(input_tensor)[1],ind+tmp],[1,1,1])
                    tensor_slice = tf.reshape(tensor_slice,[tf.shape(input_tensor)[0],tf.shape(input_tensor)[1], tmp])
                    extern_embedding = tf.keras.layers.Dense(units=embedding_dim_list[i],kernel_regularizer=tf.keras.regularizers.l2(0.01),bias_regularizer=tf.keras.regularizers.l2(0.01))(tensor_slice)
                    output.append(extern_embedding)
                    ind += tmp
                if new_axis:
                    return tf.stack(output,axis=-1)
                else:
                    return tf.concat(output,axis=agg_axis)

            def attention(inputs, attention_units):    
                query = tf.keras.layers.Dense(units=attention_units, activation=tf.nn.tanh)(inputs)
                key = tf.keras.layers.Dense(units=attention_units, activation=tf.nn.tanh)(inputs)
                value = tf.keras.layers.Dense(units=attention_units, activation=tf.nn.tanh)(inputs)

                d_k = tf.cast(tf.shape(key)[-1], dtype=tf.float32)
                
                attention_weights = tf.nn.softmax(tf.divide(tf.matmul(query, key, transpose_b=True), tf.sqrt(d_k)))
                attention_output = tf.matmul(attention_weights, value)
                
                return attention_output
            
            
            traffic_flow = tf.placeholder(tf.float32, [None, self._T, None, self._input_dim])
            self._input['traffic_flow'] = traffic_flow.name
            laplacian_matrix = tf.placeholder(tf.float32, [self._num_graph, None, None])
            self._input['laplace_matrix'] = laplacian_matrix.name
            target = tf.placeholder(tf.float32, [None, None, 1])
            self._input['target'] = target.name

            if self.earlyconcatFlag or self.earlyaddFlag:
                # with shape (slots, feature_dim, C P T len, 1)
                external_closeness = tf.placeholder(tf.float32, [None, None, self._closeness_len, 1],name='external_closeness')
                self._input['external_closeness'] = external_closeness.name
                external_period = tf.placeholder(tf.float32, [None, None, self._period_len, 1],name='external_period')
                self._input['external_period'] = external_period.name
                external_trend = tf.placeholder(tf.float32, [None, None, self._trend_len, 1],name='external_trend')
                self._input['external_trend'] = external_trend.name

                earlyfusion_external_input = tf.transpose(tf.concat([external_closeness, external_period, external_trend], axis=-2), [0, 2, 3, 1]) #  #  with shape (slots, C+P+T, 1, external_feature_dim)
                earlyfusion_external_input = tf.reshape(earlyfusion_external_input, [tf.shape(earlyfusion_external_input)[0], self._T, 1, self._temporal_external_dim])
                
            self.temporalFeatureFlag = False
            self.spatialFeatureFlag = False
            
            if self._temporal_external_dim is not None and self._temporal_external_dim > 0:
                # if exist temporal contextual features
                self.temporalFeatureFlag = True
                temporal_external_input = tf.placeholder(tf.float32, [None, self._temporal_external_dim])
                self._input['temporal_external_feature'] = temporal_external_input.name
        
            if self._spatial_external_dim is not None and self._spatial_external_dim > 0:
                # if exist temporal contextual features
                self.spatialFeatureFlag = True
                spatial_external_input = tf.placeholder(tf.float32, [self._num_node, self._spatial_external_dim])
                self._input['spatial_external_feature'] = spatial_external_input.name

            if self._external_lstm_len is not None and self._external_lstm_len > 0: # if use LSTM variant in late fusion
                past_temporal_context_for_LSTM = tf.placeholder(tf.float32, [None, None, self._external_lstm_len, 1], name='past_temporal_context_for_LSTM')
                self._input['past_temporal_context_for_LSTM'] = past_temporal_context_for_LSTM.name



            station_number = tf.shape(traffic_flow)[-2]

            outputs = []
            
            ####### Early Fusion #######
            if self.earlyconcatFlag:
                
                after_earlyconcat_dims = 1
             
                if self.temporalFeatureFlag:
                    early_concat_temporal_embedding_dim = 16
                    after_earlyconcat_dims += early_concat_temporal_embedding_dim
                    temporal_context_embedding = MLP(early_concat_temporal_embedding_dim, earlyfusion_external_input)
                    temporal_external_tile = tf.tile(temporal_context_embedding, [1, 1, self._num_node, 1])
                    traffic_flow = tf.concat([traffic_flow, temporal_external_tile], axis = -1)
                
                if self.spatialFeatureFlag:
                    early_concat_spatial_embedding_dim = 16
                    after_earlyconcat_dims += early_concat_spatial_embedding_dim
                    spatial_context_embedding = MLP(early_concat_spatial_embedding_dim, tf.reshape(spatial_external_input, [1, 1, self._num_node, self._spatial_external_dim]))
                    spatial_external_tile = tf.tile(spatial_context_embedding, [tf.shape(traffic_flow)[0], self._T, 1, 1])
                    traffic_flow = tf.concat([traffic_flow, spatial_external_tile], axis = -1)

            if self.earlyaddFlag:
                if self.temporalFeatureFlag:
                    temporal_context_embedding = MLP(1, earlyfusion_external_input, activation=tf.nn.tanh) # with shape (slots, C+P+T, 1, 1)
                    traffic_flow = tf.add(traffic_flow, temporal_context_embedding)
                
                if self.spatialFeatureFlag:
                    spatial_context_embedding = MLP(1, spatial_external_input, activation=tf.nn.tanh)
                    spatial_context_embedding = tf.tile(tf.reshape(spatial_context_embedding, [1, 1, self._num_node, 1]), [1, self._T, 1, 1])
                    traffic_flow = tf.add(traffic_flow, spatial_context_embedding)

            for graph_index in range(self._num_graph):
                with tf.variable_scope('CGRNN_Graph%s' % graph_index, reuse=False):
                    
                    if self.earlyconcatFlag:
                        self._input_dim =  after_earlyconcat_dims
                        
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

            #### Late Fusion
            if not self.earlyconcatFlag and not self.earlyaddFlag:
                

                if self.external_method[2] == "not":
                    print("**** This model didn't use external features ****")
                else:
                    print("**** Using Late Fusion Modeling techniques ****")
                    
                    ############################################################
                    ### temporal duplication for spatial contex
                    ############################################################
                    external_dense = []
                    if self.temporalFeatureFlag:
                        ### spatial duplication for temporal context
                        duplicated_temporal_features = tf.tile(tf.reshape(temporal_external_input, [-1, 1, self._temporal_external_dim]), [1, self._num_node, 1])
                        external_dense.append(duplicated_temporal_features)
                    if self.spatialFeatureFlag:
                        ### temporal duplication for spatial context
                        duplicated_spatial_features = tf.tile(tf.reshape(spatial_external_input, [1, self._num_node, self._spatial_external_dim]), [tf.shape(dense_inputs)[0], 1, 1])
                        external_dense.append(duplicated_spatial_features)

                    if len(external_dense) > 1:
                        external_dense = tf.concat(external_dense, axis=-1)
                    elif len(external_dense) == 1:
                        external_dense = external_dense[0]
                    else:
                        raise ValueError("No external features are used.")

                    self._external_dim = self._temporal_external_dim + self._spatial_external_dim
                   
                   # external_dense with shape (batch_size, num_node, 1, external_dim)
                    external_dense = tf.reshape(external_dense, [-1, self._num_node, self._external_dim])


                    ####################
                    ## representation stage
                    ####################

                    if self.external_method[0] == "not":
                        print("**** This model doesn't have representation stage.****")
                        
                    elif self.external_method[0] == "emb":
                        
                        print("**** Using one embedding layer >> {} ****".format(self._single_embedding_dim))    
                        external_dense = tf.keras.layers.Dense(units=self._single_embedding_dim, kernel_regularizer=tf.keras.regularizers.l2(0.01), bias_regularizer=tf.keras.regularizers.l2(0.01))(external_dense)
                    

                    elif self.external_method[0] == "multi":

                        classified_ST_feature_dim = self._classified_temporal_feature_dim + self._classified_spatial_feature_dim
                        ST_embedding_dim = self._temporal_embedding_dim + self._spatial_embedding_dim
                        print("**** Using classified embedding layers {} >> {} ****".format(classified_ST_feature_dim, ST_embedding_dim))
                        
                        external_dense = multiple_embedding_layer(external_dense, classified_ST_feature_dim, ST_embedding_dim, agg_axis=-1) # [T, N, D]
                        print("external_dense:",external_dense.get_shape())

                            
                    elif self.external_method[0] == "lstm":
                        if self.temporalFeatureFlag:
                            lstm_hidden_for_historial_temporal_context = 16
                            print("**** Using LSTM for temporal contextual features and their window size is {}. Temporal contextual features dims is {}. LSTM hidden state is {} ****".format(self._external_lstm_len, self._temporal_external_dim, lstm_hidden_for_historial_temporal_context))
                             # LSTM for temporal external features
                            cell = tf.keras.layers.LSTMCell(units=lstm_hidden_for_historial_temporal_context)
                            multi_layer_gru = tf.keras.layers.StackedRNNCells([cell] * 1)
                            external_dense = tf.keras.layers.RNN(multi_layer_gru)(tf.reshape(past_temporal_context_for_LSTM, [-1, self._external_lstm_len, self._temporal_external_dim]))
                            external_dense = tf.tile(tf.reshape(external_dense, [-1, 1, lstm_hidden_for_historial_temporal_context]),[1, self._num_node, 1])
                        
                        if self.spatialFeatureFlag:
                            # MLP for spatial external features
                            embedding_dim_for_spatial_context_in_LSTM = 16
                            spatial_context_embedding = MLP(embedding_dim_for_spatial_context_in_LSTM, spatial_external_input)
                            spatial_context_embedding = tf.tile(tf.reshape(spatial_context_embedding, [1, self._num_node, embedding_dim_for_spatial_context_in_LSTM]), [tf.shape(dense_inputs)[0], 1, 1])
                            external_dense = tf.concat([external_dense, spatial_context_embedding], axis = -1)


                    elif self.external_method[0] == "MGate":
                        classified_ST_feature_dim = self._classified_temporal_feature_dim + self._classified_spatial_feature_dim
                        print("**** Using multiple linear layers {}, which is prepared for multiple gating. ****".format(classified_ST_feature_dim))
                        
                        external_dense = multiple_embedding_layer(external_dense, classified_ST_feature_dim, [dense_inputs.get_shape()[-1].value]*len(classified_ST_feature_dim), new_axis=True) # [T, N, D, num_external_categories]
                        external_dense = tf.transpose(external_dense, [0, 1, 3, 2])   # [T, N, num_external_categories, D]
                    else:
                        raise ValueError("The first `external method` parameter is wrong.")

                    ##################
                    ## alignment stage
                    ##################
                    #external_dense = tf.tile(tf.reshape(external_dense, [-1, 1, 1, reshape_size]),[1, tf.shape(dense_inputs)[1], tf.shape(dense_inputs)[2], 1])
                    
                    if self.external_method[1] == "not":
                        print("**** This model doesn't have alignment stage.****")

                    elif self.external_method[1] == "linear":
                        external_dense = MLP(dense_inputs.get_shape()[-1], external_dense)
                    else:
                        raise ValueError("The second `external method` parameter is wrong.")
                    
                    ##############
                    ## fusion stage
                    ##############
                    if self.external_method[2] == "concat":
                        dense_inputs = tf.concat([dense_inputs, external_dense], axis=-1)

                    elif self.external_method[2] == "add":
                        dense_inputs = tf.add(dense_inputs, external_dense)

                    elif self.external_method[2] == "gating":
                        dense_inputs = tf.multiply(dense_inputs, external_dense)
                    
                    elif self.external_method[2] == "ResGate":
                        assert self.external_method[1] == "linear"
                        gating_output = tf.multiply(dense_inputs, external_dense)
                        dense_inputs = dense_inputs + gating_output
                    
                    elif self.external_method[2] == "GateConcat":
                        assert self.external_method[1] == "linear"
                        gating_output = tf.multiply(dense_inputs, external_dense)
                        dense_inputs = tf.concat([dense_inputs, gating_output], axis=-1)
                    
                    elif self.external_method[2] == "GateAttn":
                        assert self.external_method[1] == "linear"
                        gating_output = tf.multiply(dense_inputs, external_dense)

                        attn_input = tf.stack([dense_inputs, gating_output], axis=-2) # [T, N, 2, D]
                        attn_input = tf.reshape(attn_input, [-1, 2, attn_input.get_shape()[-1].value]) # [T*N, 2, D]
                        
                        attn_output = attention(attn_input, self._lstm_units//2) # [T*N, 2, D]

                        dense_inputs = tf.reshape(tf.reduce_mean(attn_output, axis=-2), [-1, self._num_node, attn_output.get_shape()[-1].value])

                    elif self.external_method[2] == "MGateConcat":
                        assert self.external_method[0] == "MGate"
                        
                        gating_output = tf.multiply(dense_inputs[:, :, tf.newaxis, :], external_dense) # [T, N, num_external_categories, D]                
                        gating_output = tf.reshape(gating_output, [-1, self._num_node, len(classified_ST_feature_dim) * dense_inputs.get_shape()[-1].value]) # [T, N, num_external_categories*D]
                        dense_inputs = tf.concat([dense_inputs, gating_output], axis=-1)

                    elif self.external_method[2] == "MGateConcatRes":
                        assert self.external_method[0] == "MGate"
                        
                        gating_output = tf.multiply(dense_inputs[:, :, tf.newaxis, :], external_dense) # [T, N, num_external_categories, D]                
                        gating_output = tf.reshape(gating_output, [-1, self._num_node, len(classified_ST_feature_dim) * dense_inputs.get_shape()[-1].value]) # [T, N, num_external_categories*D]
                        gating_output = MLP(dense_inputs.get_shape()[-1].value, gating_output)

                        dense_inputs = tf.add(dense_inputs, gating_output)


                    elif self.external_method[2] == "MGateAttn":
                        assert self.external_method[0] == "MGate"
                        
                        gating_output = tf.multiply(dense_inputs[:, :, tf.newaxis, :], external_dense) # [T, N, num_external_categories, D]
                        
                        attn_input = tf.concat([dense_inputs[:, :, tf.newaxis, :], gating_output], axis=-2) # [T, N, num_external_categories + 1, D]
                        attn_input = tf.reshape(attn_input, [-1, 1 + len(classified_ST_feature_dim), dense_inputs.get_shape()[-1].value]) # [T*N, num_external_categories + 1, D]
                        
                        attn_output = attention(attn_input, self._lstm_units//2) # [T*N, num_external_categories + 1, D]

                        dense_inputs = tf.reshape(tf.reduce_mean(attn_output, axis=-2), [-1, self._num_node, self._lstm_units//2])


                    elif self.external_method[2] == "MGateAttnRes":
                        assert self.external_method[0] == "MGate"
                      
                        gating_output = tf.multiply(dense_inputs[:, :, tf.newaxis, :], external_dense) # [T, N, num_external_categories, D]
                        
                        attn_input = tf.concat([dense_inputs[:, :, tf.newaxis, :], gating_output], axis=-2) # [T, N, 1 + num_external_categories, D]
                        attn_input = tf.reshape(attn_input, [-1, 1 + len(classified_ST_feature_dim), dense_inputs.get_shape()[-1].value]) # [T*N, 1 + num_external_categories, D]
                        attn_output = attention(attn_input, self._lstm_units//2) # [T*N, 1 + num_external_categories, D]

                        agg_output = MLP(dense_inputs.get_shape()[-1].value, tf.reshape(tf.reduce_mean(attn_output, axis=-2), [-1, self._num_node, self._lstm_units//2]))
                        
                        dense_inputs = tf.add(dense_inputs, agg_output)
                        
                
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
                       external_closeness=None,
                       external_period=None,
                       external_trend=None,
                       past_temporal_context_for_LSTM=None,
                       target=None, 
                       temporal_external_feature=None, 
                       spatial_external_feature=None):
        feed_dict = {
            'traffic_flow': traffic_flow,
            'laplace_matrix': laplace_matrix,
        }
        if target is not None:
            feed_dict['target'] = target
        # if external_feature is not None:
        #     feed_dict['external_feature'] = external_feature
        
        if self._temporal_external_dim is not None and self._temporal_external_dim > 0:
            feed_dict['temporal_external_feature'] = temporal_external_feature
        if self._spatial_external_dim is not None and self._spatial_external_dim > 0:
            feed_dict['spatial_external_feature'] = spatial_external_feature
        if self._external_lstm_len is not None and self._external_lstm_len > 0 and self._temporal_external_dim > 0:
            feed_dict['past_temporal_context_for_LSTM'] = past_temporal_context_for_LSTM
        if (self.earlyconcatFlag or self.earlyaddFlag) and self._temporal_external_dim > 0:
            feed_dict['external_closeness'] = external_closeness
            feed_dict['external_period'] = external_period
            feed_dict['external_trend'] = external_trend
        return feed_dict
