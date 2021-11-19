import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike
#############################################
### Chicago ### 
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:emb-linear-add,graph:Distance-Correlation-Interaction,mark:emb_linear_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:emb-linear-gating,graph:Distance-Correlation-Interaction,mark:emb_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:multi-linear-add,graph:Distance-Correlation-Interaction,mark:multi_linear_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:multi-linear-gating,graph:Distance-Correlation-Interaction,mark:multi_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Interaction,mark:lstm4_not_concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Interaction,mark:lstm4_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:earlyconcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:earlyadd')


# ###############################################
# # BenchMark Metro
# ###############################################
### Shanghai ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:not-not-not,graph:Distance-Correlation-Line,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:not-not-concat,graph:Distance-Correlation-Line,mark:direct_concat_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,batch_size:8,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:classified_embedding_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,lr:5e-5,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1bs8')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Line,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:not-linear-add,graph:Distance-Correlation-Line,mark:add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:emb-linear-add,graph:Distance-Correlation-Line,mark:emb_linear_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:emb-linear-gating,graph:Distance-Correlation-Line,mark:emb_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:multi-linear-add,graph:Distance-Correlation-Line,mark:multi_linear_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:multi-linear-gating,graph:Distance-Correlation-Line,mark:multi_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Line,mark:lstm4_not_concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Line,mark:lstm4_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:earlyconcat,graph:Distance-Correlation-Line,mark:earlyconcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_method:earlyadd,graph:Distance-Correlation-Line,mark:earlyadd')


# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:not-not-not,graph:Distance-Correlation,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,batch_size:32,external_method:not-not-concat,graph:Distance-Correlation,mark:direct_concat_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,batch_size:32,external_method:emb-not-concat,graph:Distance-Correlation,mark:one_embedding_layer_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,batch_size:32,external_method:multi-not-concat,graph:Distance-Correlation,mark:classified_embedding_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_fusion_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation,mark:lstm4_V1')
          
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:not-linear-add,graph:Distance-Correlation,mark:add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:emb-linear-add,graph:Distance-Correlation,mark:emb_linear_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:emb-linear-gating,graph:Distance-Correlation,mark:emb_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:multi-linear-add,graph:Distance-Correlation,mark:multi_linear_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:multi-linear-gating,graph:Distance-Correlation,mark:multi_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation,mark:lstm4_not_concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation,mark:lstm4_linear_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:earlyconcat,graph:Distance-Correlation,mark:earlyconcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_method:earlyadd,graph:Distance-Correlation,mark:earlyadd')
