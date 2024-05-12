import keras
import tensorflow as tf
import numpy as np

from ..model_unit import BaseModel
from ..model_unit import GAL, GCL
from ..model_unit import DCGRUCell
from ..model_unit import GCLSTMCell
from ..train import Optimizer

class STMeta(BaseModel):
    """
        Args:
            num_node(int): Number of nodes in the graph, e.g. number of stations in NYC-Bike dataset.
            external_dim(int): Dimension of the external feature, e.g. temperature and wind are two dimension.
            closeness_len(int): The length of closeness data history. The former consecutive ``closeness_len`` time slots
            of data will be used as closeness history.
            period_len(int): The length of period data history. The data of exact same time slots in former consecutive
            ``period_len`` days will be used as period history.
            trend_len(int): The length of trend data history. The data of exact same time slots in former consecutive
            ``trend_len`` weeks (every seven days) will be used as trend history.
            num_graph(int): Number of graphs used in STMeta.
            gcn_k(int): The highest order of Chebyshev Polynomial approximation in GCN.
            gcn_layers(int): Number of GCN layers.
            gclstm_layers(int): Number of STRNN layers, it works on all modes of STMeta such as GCLSTM and DCRNN.
            num_hidden_units(int): Number of hidden units of RNN.
            num_dense_units(int): Number of dense units.
            graph_merge_gal_units(int): Number of units in GAL for merging different graph features.
                Only works when graph_merge='gal'
            graph_merge_gal_num_heads(int): Number of heads in GAL for merging different graph features.
                Only works when graph_merge='gal'
            temporal_merge_gal_units(int): Number of units in GAL for merging different temporal features.
                Only works when temporal_merge='gal'
            temporal_merge_gal_num_heads(int): Number of heads in GAL for merging different temporal features.
                Only works when temporal_merge='gal'
            st_method(str): must in ['GCLSTM', 'DCRNN', 'GRU', 'LSTM'], which refers to different
                spatial-temporal modeling methods.
                'GCLSTM': GCN for modeling spatial feature, LSTM for modeling temporal feature.
                'DCRNN': Diffusion Convolution for modeling spatial feature, GRU for modeling temporam frature.
                'GRU': Ignore the spatial, and model the temporal feature using GRU
                'LSTM': Ignore the spatial, and model the temporal feature using LSTM
            temporal_merge(str): must in ['gal', 'concat'], refers to different temporal merging methods,
                'gal': merge using GAL,
                'concat': merge by concat and dense
            graph_merge(str): must in ['gal', 'concat'], refers to different graph merging methods,
                'gal': merge using GAL,
                'concat': merge by concat and dense
            output_activation(function): activation function, e.g. tf.nn.tanh
            lr(float): Learning rate. Default: 1e-5
            code_version(str): Current version of this model code, which will be used as filename for saving the model
            model_dir(str): The directory to store model files. Default:'model_dir'.
            gpu_device(str): To specify the GPU to use. Default: '0'.
            external_method(str): to decide how we model external features. Its values can be `not` `direct` `embedding` `classified` `gating`
            decay_param=(str): The file path of decay function parameter. If set `None`, using fixed lr. default: None.
        """

    def __init__(self,
                 num_node,
                 temporal_external_dim, # temporal external feature dimensions
                 spatial_external_dim, # spatial external feature dimensions
                 closeness_len,
                 period_len,
                 trend_len,
                 external_lstm_len,

                 # gcn parameters
                 num_graph=1,
                 gcn_k=1,
                 gcn_layers=1,
                 gclstm_layers=1,

                 # LSTM units
                 num_hidden_units=64,
                 # dense units
                 num_dense_units=32,

                 # merge parameters
                 graph_merge_gal_units=32,
                 graph_merge_gal_num_heads=2,
                 temporal_merge_gal_units=64,
                 temporal_merge_gal_num_heads=2,

                 # network structure parameters
                 st_method='GCLSTM',  # gclstm
                 temporal_merge='gal',  # gal
                 graph_merge='gal',  # concat

                 output_activation=tf.nn.sigmoid,

                 lr=1e-4,
                 code_version='STMeta-QuickStart',
                 model_dir='model_dir',
                 gpu_device='0',
                 external_method="not-not-not",
                 temporal_embedding_dim = [10, 1, 5], # dim of multiple embedding layer for temporal features
                 spatial_embedding_dim = [8, 32, 5, 8], # dim of multiple embedding layer for spatial features
                 single_embedding_dim = 16, # dim of single embedding layer
                 classified_temporal_feature_dim = [],
                 classified_spatial_feature_dim = [],
                 decay_param=None,**kwargs):
        # no direct one_layer classified
        super(STMeta, self).__init__(code_version=code_version, model_dir=model_dir, gpu_device=gpu_device)

        self._num_node = num_node
        self._gcn_k = gcn_k
        self._gcn_layer = gcn_layers
        self._graph_merge_gal_units = graph_merge_gal_units
        self._graph_merge_gal_num_heads = graph_merge_gal_num_heads
        self._temporal_merge_gal_units = temporal_merge_gal_units
        self._temporal_merge_gal_num_heads = temporal_merge_gal_num_heads
        self._gclstm_layers = gclstm_layers
        self._num_graph = num_graph
       
        self._temporal_external_dim = temporal_external_dim
        self._spatial_external_dim = spatial_external_dim


        self._output_activation = output_activation

        self._st_method = st_method
        self._temporal_merge = temporal_merge
        self._graph_merge = graph_merge

        self._closeness_len = int(closeness_len)
        self._period_len = int(period_len)
        self._trend_len = int(trend_len)
        if "lstm" in external_method:
            self._external_lstm_len = int(external_lstm_len)
        else:
            self._external_lstm_len = None

        self._num_hidden_unit = num_hidden_units
        self._num_dense_units = num_dense_units
        self._lr = lr

        # add decay func
        self._optimizer = Optimizer(decay_param=decay_param,lr=self._lr)
        
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
            
            def MLP(hidden_state, input_tensor, activation=None):
                return tf.keras.layers.Dense(units=hidden_state,kernel_regularizer=tf.keras.regularizers.l2(0.01),bias_regularizer=tf.keras.regularizers.l2(0.01), activation=activation)(input_tensor)
            
            def multiple_embedding_layer(input_tensor, feature_dim_list, embedding_dim_list, agg_axis=-1):
                '''
                input_tensor: input tensor with shape (batch_size, num_node, 1, feature_dim)
                feature_dim_list: feature length for each type of context (e.g., [26, 2, 24]), sum(feature_dim_list) = feature_dim
                embedding_dim_list: embedding dim for each type of context (e.g., [8, 1, 8])
                agg_axis: axis for concatenation (default: -1)
                '''
                output = []
                ind = 0
                for i,tmp in enumerate(feature_dim_list):
                    tensor_slice = tf.strided_slice(input_tensor,[0,0,0,ind],[tf.shape(input_tensor)[0],tf.shape(input_tensor)[1],tf.shape(input_tensor)[2],ind+tmp],[1,1,1,1])
                    tensor_slice = tf.reshape(tensor_slice,[tf.shape(input_tensor)[0],tf.shape(input_tensor)[1],tf.shape(input_tensor)[2], tmp])
                    extern_embedding = tf.keras.layers.Dense(units=embedding_dim_list[i],kernel_regularizer=tf.keras.regularizers.l2(0.01),bias_regularizer=tf.keras.regularizers.l2(0.01))(tensor_slice)
                    output.append(extern_embedding)
                    ind += tmp
                return tf.concat(output,axis=agg_axis)

            def attention(inputs, attention_units):    
                query = tf.keras.layers.Dense(units=attention_units, activation=tf.nn.tanh)(inputs)
                key = tf.keras.layers.Dense(units=attention_units, activation=tf.nn.tanh)(inputs)
                value = tf.keras.layers.Dense(units=attention_units, activation=tf.nn.tanh)(inputs)

                d_k = tf.cast(tf.shape(key)[-1], dtype=tf.float32)
                
                attention_weights = tf.nn.softmax(tf.divide(tf.matmul(query, key, transpose_b=True), tf.sqrt(d_k)))
                attention_output = tf.matmul(attention_weights, value)
                
                return attention_output

            if self.earlyconcatFlag or self.earlyaddFlag:
                # with shape (slots, feature_dim, C P T len, 1)
                external_closeness = tf.placeholder(tf.float32, [None, self._temporal_external_dim, self._closeness_len, 1], name='external_closeness')
                self._input['external_closeness'] = external_closeness.name
                external_period = tf.placeholder(tf.float32, [None, self._temporal_external_dim, self._period_len, 1], name='external_period')
                self._input['external_period'] = external_period.name
                external_trend = tf.placeholder(tf.float32, [None, self._temporal_external_dim, self._trend_len, 1], name='external_trend')
                self._input['external_trend'] = external_trend.name

            temporal_features = []
            external_temporal_features_for_earlyfusion = []

            if self._closeness_len is not None and self._closeness_len > 0:
                closeness_feature = tf.placeholder(tf.float32, [None, None, self._closeness_len, 1], name='closeness_feature')
                self._input['closeness_feature'] = closeness_feature.name
                temporal_features.append([self._closeness_len, closeness_feature, 'closeness_feature'])
                if self.earlyconcatFlag or self.earlyaddFlag:
                    external_temporal_features_for_earlyfusion.append(tf.transpose(external_closeness,[0,3,2,1]))  # with shape (time, 1, C/P/T len, feature_dim)

            if self._period_len is not None and self._period_len > 0:
                period_feature = tf.placeholder(tf.float32, [None, None, self._period_len, 1], name='period_feature')
                self._input['period_feature'] = period_feature.name
                temporal_features.append([self._period_len, period_feature, 'period_feature'])
                if self.earlyconcatFlag or self.earlyaddFlag:
                    external_temporal_features_for_earlyfusion.append(tf.transpose(external_period,[0,3,2,1]))

            if self._trend_len is not None and self._trend_len > 0:
                trend_feature = tf.placeholder(tf.float32, [None, None, self._trend_len, 1], name='trend_feature')
                self._input['trend_feature'] = trend_feature.name
                temporal_features.append([self._trend_len, trend_feature, 'trend_feature'])
                if self.earlyconcatFlag or self.earlyaddFlag:
                    external_temporal_features_for_earlyfusion.append(tf.transpose(external_trend,[0,3,2,1]))
            
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

            if len(temporal_features) > 0:
                target = tf.placeholder(tf.float32, [None, None, 1], name='target')
                laplace_matrix = tf.placeholder(tf.float32, [self._num_graph, None, None], name='laplace_matrix')
                self._input['target'] = target.name
                self._input['laplace_matrix'] = laplace_matrix.name
            else:
                raise ValueError('closeness_len, period_len, trend_len cannot all be zero')

            graph_outputs_list = []

            for graph_index in range(self._num_graph):

                if self._st_method in ['GCLSTM', 'DCRNN', 'GRU', 'LSTM']:

                    outputs_temporal = []

                    for t_ind, temporal_item in enumerate(temporal_features):
                        
                        time_step, target_tensor, given_name = temporal_item

                        ####### Early Fusion #######
                        if self.earlyconcatFlag:
                            after_earlyconcat_dims = 1
                            #  with shape (slots, 1, C P T len, feature_dim)
                            if self.temporalFeatureFlag:
                                early_concat_temporal_embedding_dim = 16
                                after_earlyconcat_dims += early_concat_temporal_embedding_dim
                                temporal_context_embedding = MLP(early_concat_temporal_embedding_dim, tf.reshape(external_temporal_features_for_earlyfusion[t_ind], [-1, 1, time_step, self._temporal_external_dim]))
                                temporal_external_tile = tf.tile(temporal_context_embedding, [1, self._num_node, 1, 1])
                                target_tensor = tf.concat([target_tensor, temporal_external_tile], axis = -1)
                            
                            if self.spatialFeatureFlag:
                                early_concat_spatial_embedding_dim = 16
                                after_earlyconcat_dims += early_concat_spatial_embedding_dim
                                spatial_context_embedding = MLP(early_concat_spatial_embedding_dim, tf.reshape(spatial_external_input, [1, self._num_node, 1, self._spatial_external_dim]))
                                spatial_external_tile = tf.tile(spatial_context_embedding, [tf.shape(target)[0], 1, time_step, 1])
                                target_tensor = tf.concat([target_tensor,spatial_external_tile], axis = -1)

                        if self.earlyaddFlag:
                            if self.temporalFeatureFlag:
                                temporal_context = tf.reshape(external_temporal_features_for_earlyfusion[t_ind], [-1, 1, time_step, self._temporal_external_dim])
                                temporal_context_embedding = MLP(1, temporal_context, activation=tf.nn.tanh)
                                target_tensor = tf.add(target_tensor, temporal_context_embedding)
                            
                            if self.spatialFeatureFlag:
                                spatial_context_embedding = MLP(1, spatial_external_input, activation=tf.nn.tanh)
                                spatial_context_embedding = tf.tile(tf.reshape(spatial_context_embedding, [1, self._num_node, 1, 1]), [1, 1, time_step, 1])
                                target_tensor = tf.add(target_tensor, spatial_context_embedding)

                        if self._st_method == 'GCLSTM':

                            multi_layer_cell = tf.keras.layers.StackedRNNCells(
                                [GCLSTMCell(units=self._num_hidden_unit, num_nodes=self._num_node,
                                            laplacian_matrix=laplace_matrix[graph_index],
                                            gcn_k=self._gcn_k, gcn_l=self._gcn_layer)
                                 for _ in range(self._gclstm_layers)])

                            if self.earlyconcatFlag:
                                outputs = tf.keras.layers.RNN(multi_layer_cell)(tf.reshape(target_tensor, [-1, time_step, after_earlyconcat_dims]))
                            else:
                                outputs = tf.keras.layers.RNN(multi_layer_cell)(tf.reshape(target_tensor, [-1, time_step, 1]))

                            st_outputs = tf.reshape(outputs, [-1, 1, self._num_hidden_unit])

                        elif self._st_method == 'DCRNN':

                            cell = DCGRUCell(self._num_hidden_unit, 1, self._num_graph,
                                             # laplace_matrix will be diffusion_matrix when self._st_method == 'DCRNN'
                                             laplace_matrix,
                                             max_diffusion_step=self._gcn_k,
                                             num_nodes=self._num_node, name=str(graph_index) + given_name)

                            encoding_cells = [cell] * self._gclstm_layers
                            encoding_cells = tf.contrib.rnn.MultiRNNCell(encoding_cells, state_is_tuple=True)

                            if self.earlyconcatFlag:
                                target_tensor = tf.transpose(target_tensor,[0,1,3,2])

                                inputs_unstack = tf.unstack(tf.reshape(target_tensor, [-1, self._num_node*after_earlyconcat_dims, time_step]),axis=-1)
                                
                            else:
                                inputs_unstack = tf.unstack(tf.reshape(target_tensor, [-1, self._num_node, time_step]),axis=-1)
                            
                            outputs, _ = \
                                tf.contrib.rnn.static_rnn(encoding_cells, inputs_unstack, dtype=tf.float32)

                            st_outputs = tf.reshape(outputs[-1], [-1, 1, self._num_hidden_unit])

                        elif self._st_method == 'GRU':

                            cell = tf.keras.layers.GRUCell(units=self._num_hidden_unit)
                            multi_layer_gru = tf.keras.layers.StackedRNNCells([cell] * self._gclstm_layers)
                            outputs = tf.keras.layers.RNN(multi_layer_gru)(
                                tf.reshape(target_tensor, [-1, time_step, 1]))
                            st_outputs = tf.reshape(outputs, [-1, 1, self._num_hidden_unit])

                        elif self._st_method == 'LSTM':

                            cell = tf.keras.layers.LSTMCell(units=self._num_hidden_unit)
                            multi_layer_gru = tf.keras.layers.StackedRNNCells([cell] * self._gclstm_layers)
                            outputs = tf.keras.layers.RNN(multi_layer_gru)(
                                tf.reshape(target_tensor, [-1, time_step, 1]))
                            st_outputs = tf.reshape(outputs, [-1, 1, self._num_hidden_unit])

                        outputs_temporal.append(st_outputs)

                    if self._temporal_merge == 'concat':
                        
                        graph_outputs_list.append(tf.concat(outputs_temporal, axis=-1))

                    elif self._temporal_merge == 'gal':

                        _, gal_output = GAL.add_ga_layer_matrix(inputs=tf.concat(outputs_temporal, axis=-2),
                                                                units=self._temporal_merge_gal_units,
                                                                num_head=self._temporal_merge_gal_num_heads)

                        graph_outputs_list.append(tf.reduce_mean(gal_output, axis=-2, keepdims=True))

            if self._num_graph > 1:

                if self._graph_merge == 'gal':
                    # (graph, inputs_name, units, num_head, activation=tf.nn.leaky_relu)
                    _, gal_output = GAL.add_ga_layer_matrix(inputs=tf.concat(graph_outputs_list, axis=-2),
                                                            units=self._graph_merge_gal_units,
                                                            num_head=self._graph_merge_gal_num_heads)
                    dense_inputs = tf.reduce_mean(gal_output, axis=-2, keepdims=True)

                elif self._graph_merge == 'concat':

                    dense_inputs = tf.concat(graph_outputs_list, axis=-1)

            else:

                dense_inputs = graph_outputs_list[-1]

            dense_inputs = tf.reshape(dense_inputs, [-1, self._num_node, 1, dense_inputs.get_shape()[-1].value])

            dense_inputs = tf.keras.layers.BatchNormalization(axis=-1, name='feature_map')(dense_inputs)
            
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
                        duplicated_temporal_features = tf.tile(tf.reshape(temporal_external_input, [-1, 1, 1, self._temporal_external_dim]), [1, self._num_node, 1, 1])
                        external_dense.append(duplicated_temporal_features)
                    if self.spatialFeatureFlag:
                        ### temporal duplication for spatial context
                        duplicated_spatial_features = tf.tile(tf.reshape(spatial_external_input, [1, self._num_node, 1, self._spatial_external_dim]), [tf.shape(dense_inputs)[0], 1, 1, 1])
                        external_dense.append(duplicated_spatial_features)

                    if len(external_dense) > 1:
                        external_dense = tf.concat(external_dense, axis=-1)
                    elif len(external_dense) == 1:
                        external_dense = external_dense[0]
                    else:
                        raise ValueError("No external features are used.")

                    self._external_dim = self._temporal_external_dim + self._spatial_external_dim
                   
                   # external_dense with shape (batch_size, num_node, 1, external_dim)
                    external_dense = tf.reshape(external_dense, [-1, self._num_node, 1, self._external_dim])


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
                        
                        external_dense = multiple_embedding_layer(external_dense, classified_ST_feature_dim, ST_embedding_dim, agg_axis=-1) # [T, N, 1, D]

                            
                    elif self.external_method[0] == "lstm":
                        if self.temporalFeatureFlag:
                            lstm_hidden_for_historial_temporal_context = 16
                            print("**** Using LSTM for temporal contextual features and their window size is {}. Temporal contextual features dims is {}. LSTM hidden state is {} ****".format(self._external_lstm_len, self._temporal_external_dim, lstm_hidden_for_historial_temporal_context))
                             # LSTM for temporal external features
                            cell = tf.keras.layers.LSTMCell(units=lstm_hidden_for_historial_temporal_context)
                            multi_layer_gru = tf.keras.layers.StackedRNNCells([cell] * 1)
                            external_dense = tf.keras.layers.RNN(multi_layer_gru)(tf.reshape(past_temporal_context_for_LSTM, [-1, self._external_lstm_len, self._temporal_external_dim]))
                            external_dense = tf.tile(tf.reshape(external_dense, [-1, 1, 1, lstm_hidden_for_historial_temporal_context]),[1, self._num_node, 1, 1])
                        
                        if self.spatialFeatureFlag:
                            # MLP for spatial external features
                            embedding_dim_for_spatial_context_in_LSTM = 16
                            spatial_context_embedding = MLP(embedding_dim_for_spatial_context_in_LSTM, spatial_external_input)
                            spatial_context_embedding = tf.tile(tf.reshape(spatial_context_embedding, [1, self._num_node, 1, embedding_dim_for_spatial_context_in_LSTM]), [tf.shape(dense_inputs)[0], 1, 1, 1])
                            external_dense = tf.concat([external_dense, spatial_context_embedding], axis = -1)


                    elif self.external_method[0] == "MGate":
                        classified_ST_feature_dim = self._classified_temporal_feature_dim + self._classified_spatial_feature_dim
                        print("**** Using multiple linear layers {}, which is prepared for multiple gating. ****".format(classified_ST_feature_dim))
                        
                        external_dense = multiple_embedding_layer(external_dense, classified_ST_feature_dim, [dense_inputs.get_shape()[-1].value]*len(classified_ST_feature_dim), agg_axis=-2) # [T, N, num_external_categories, D]
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

                        attn_input = tf.concat([dense_inputs, gating_output], axis=-2) # [T, N, 2, D]
                        attn_input = tf.reshape(attn_input, [-1, 2, attn_input.get_shape()[-1].value]) # [T*N, 2, D]
                        
                        attn_output = attention(attn_input, self._num_hidden_unit//2) # [T*N, 2, D]

                        dense_inputs = tf.reshape(tf.reduce_mean(attn_output, axis=-2, keepdims=True), [-1, self._num_node, 1, attn_output.get_shape()[-1].value])

                    elif self.external_method[2] == "MGateConcat":
                        assert self.external_method[0] == "MGate"
                        
                        gating_output = tf.multiply(dense_inputs, external_dense) # [T, N, num_external_categories, D]                
                        gating_output = tf.reshape(gating_output, [-1, self._num_node, 1, len(classified_ST_feature_dim) * dense_inputs.get_shape()[-1].value]) # [T, N, 1, num_external_categories*D]
                        dense_inputs = tf.concat([dense_inputs, gating_output], axis=-1)

                    elif self.external_method[2] == "MGateConcatRes":
                        assert self.external_method[0] == "MGate"
                        
                        gating_output = tf.multiply(dense_inputs, external_dense) # [T, N, num_external_categories, D]                
                        gating_output = tf.reshape(gating_output, [-1, self._num_node, 1, len(classified_ST_feature_dim) * dense_inputs.get_shape()[-1].value]) # [T, N, 1, num_external_categories*D]
                        gating_output = MLP(dense_inputs.get_shape()[-1].value, gating_output)

                        dense_inputs = tf.add(dense_inputs, gating_output)


                    elif self.external_method[2] == "MGateAttn":
                        assert self.external_method[0] == "MGate"
                        
                        gating_output = tf.multiply(dense_inputs, external_dense) # [T, N, num_external_categories, D]
                        
                        attn_input = tf.concat([dense_inputs, gating_output], axis=-2) # [T, N, num_external_categories + 1, D]
                        attn_input = tf.reshape(attn_input, [-1, 1 + len(classified_ST_feature_dim), dense_inputs.get_shape()[-1].value]) # [T*N, num_external_categories + 1, D]
                        
                        attn_output = attention(attn_input, self._num_hidden_unit//2) # [T*N, num_external_categories + 1, D]

                        dense_inputs = tf.reshape(tf.reduce_mean(attn_output, axis=-2, keepdims=True), [-1, self._num_node, 1, self._num_hidden_unit//2])


                    elif self.external_method[2] == "MGateAttnRes":
                        assert self.external_method[0] == "MGate"
                      
                        gating_output = tf.multiply(dense_inputs, external_dense) # [T, N, num_external_categories, D]
                        
                        attn_input = tf.concat([dense_inputs, gating_output], axis=-2) # [T, N, 1 + num_external_categories, D]
                        attn_input = tf.reshape(attn_input, [-1, 1 + len(classified_ST_feature_dim), dense_inputs.get_shape()[-1].value]) # [T*N, 1 + num_external_categories, D]
                        attn_output = attention(attn_input, self._num_hidden_unit//2) # [T*N, 1 + num_external_categories, D]

                        agg_output = MLP(dense_inputs.get_shape()[-1].value, tf.reshape(tf.reduce_mean(attn_output, axis=-2, keepdims=True), [-1, self._num_node, 1, self._num_hidden_unit//2]))
                        
                        dense_inputs = tf.add(dense_inputs, agg_output)
                        
                
                    else:
                        raise ValueError("The third `external method` parameter is wrong.")
                  

            dense_output0 = tf.keras.layers.Dense(units=self._num_dense_units,
                                                  activation=tf.nn.tanh,
                                                  use_bias=True,
                                                  kernel_initializer='glorot_uniform',
                                                  bias_initializer='zeros',
                                                  kernel_regularizer=tf.keras.regularizers.l2(0.01),
                                                  bias_regularizer=tf.keras.regularizers.l2(0.01)
                                                  )(dense_inputs)

            dense_output1 = tf.keras.layers.Dense(units=self._num_dense_units,
                                                  activation=tf.nn.tanh,
                                                  use_bias=True,
                                                  kernel_initializer='glorot_uniform',
                                                  bias_initializer='zeros',
                                                  kernel_regularizer=tf.keras.regularizers.l2(0.01),
                                                  bias_regularizer=tf.keras.regularizers.l2(0.01)
                                                  )(dense_output0)

            pre_output = tf.keras.layers.Dense(units=1,
                                               activation=tf.nn.tanh,
                                               use_bias=True,
                                               kernel_initializer='glorot_uniform',
                                               bias_initializer='zeros',
                                               kernel_regularizer=tf.keras.regularizers.l2(0.01),
                                               bias_regularizer=tf.keras.regularizers.l2(0.01)
                                               )(dense_output1)

            prediction = tf.reshape(pre_output, [-1, self._num_node, 1], name='prediction')

            loss_pre = tf.sqrt(tf.reduce_mean(tf.square(target - prediction)), name='loss')
            
            train_op, global_step_name, learning_rate_name = self._optimizer.build(loss_pre=loss_pre)
            self._input['global_step'] = global_step_name

            # record output
            self._output['prediction'] = prediction.name
            self._output['loss'] = loss_pre.name
            # record lr decay
            self._output['lr'] = learning_rate_name

            # record train operation
            self._op['train_op'] = train_op.name

        super(STMeta, self).build(init_vars, max_to_keep)
    
    # Define your '_get_feed_dict function‘, map your input to the tf-model
    def _get_feed_dict(self,
                       laplace_matrix,
                       closeness_feature=None,
                       period_feature=None,
                       trend_feature=None,
                       past_temporal_context_for_LSTM=None,
                       external_closeness=None,
                       external_period=None,
                       external_trend=None,
                       target=None,
                       temporal_external_feature=None,
                       spatial_external_feature=None):
        feed_dict = {
            'laplace_matrix': laplace_matrix,
        }
        if target is not None:
            feed_dict['target'] = target
        if self._temporal_external_dim is not None and self._temporal_external_dim > 0:
            feed_dict['temporal_external_feature'] = temporal_external_feature
        if self._spatial_external_dim is not None and self._spatial_external_dim > 0:
            feed_dict['spatial_external_feature'] = spatial_external_feature
        if self._closeness_len is not None and self._closeness_len > 0:
            feed_dict['closeness_feature'] = closeness_feature
        if self._period_len is not None and self._period_len > 0:
            feed_dict['period_feature'] = period_feature
        if self._trend_len is not None and self._trend_len > 0:
            feed_dict['trend_feature'] = trend_feature
        if self._external_lstm_len is not None and self._external_lstm_len > 0 and self._temporal_external_dim > 0:
            feed_dict['past_temporal_context_for_LSTM'] = past_temporal_context_for_LSTM
        if (self.earlyconcatFlag or self.earlyaddFlag) and self._temporal_external_dim > 0:
            feed_dict['external_closeness'] = external_closeness
            feed_dict['external_period'] = external_period
            feed_dict['external_trend'] = external_trend
        # print("fd:",feed_dict.keys())
        return feed_dict
