import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike
#############################################
#### NYC
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1,MergeIndex:2')

# ## Chicago ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:2')



# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add,MergeIndex:2')


# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1,MergeIndex:2')

# ## DC ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1,MergeIndex:2')


# ###############################################
# # BenchMark DiDi
# ###############################################
# ## Xian ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p batch_size:8,external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1,MergeIndex:2')


# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1,MergeIndex:2')

# # Chengdu ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1,MergeIndex:2')

# ###############################################
# # BenchMark Metro
# ###############################################
# ## Shanghai ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Line,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Line,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Line,mark:lstm4_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Line,mark:add,MergeIndex:2')


# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1bs8,MergeIndex:2')

# ## Chongqing ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Line,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Line,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1,MergeIndex:2')

# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation,mark:not_external_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:not-not-concat,graph:Distance-Correlation,mark:direct_concat_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:emb-not-concat,graph:Distance-Correlation,mark:one_embedding_layer_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:multi-not-concat,graph:Distance-Correlation,mark:classified_embedding_V1,MergeIndex:2')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation,mark:lstm4_V1,MergeIndex:2')
          
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation,mark:add,MergeIndex:2')


# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1,MergeIndex:2')
