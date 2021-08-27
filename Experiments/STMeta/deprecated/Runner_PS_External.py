import os
import warnings
warnings.filterwarnings("ignore")

# ###############################################
# # LSTM windos size
# ###############################################
##### didi_xian
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_lstm_len:4,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_lstm_len:6,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm6_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_lstm_len:8,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm8_V1')

## chargestation_beijing
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm,graph:Distance-Correlation,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:6,external_method:lstm,graph:Distance-Correlation,mark:lstm6_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:8,external_method:lstm,graph:Distance-Correlation,mark:lstm8_V1')



# ###############################################
# # Embedding layers 
# ###############################################

# # differnt emb-not-concat size
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p embedding_dim:6,lr:5e-5,batch_size:4,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1emb6')
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p embedding_dim:8,lr:5e-5,batch_size:4,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1emb8')
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p embedding_dim:10,lr:5e-5,batch_size:4,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1emb10')
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p embedding_dim:12,lr:5e-5,batch_size:4,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1emb12')
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p embedding_dim:14,lr:5e-5,batch_size:4,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1emb14')

# ## differnet multi-not-concat emb-not-concat size ##
# # time position
# os.system('python STMeta_Obj.py -m STMeta_v1.model_4.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1tpemb4')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_6.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1tpemb6')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_8.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1tpemb8')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_10.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1tpemb10')

# # weather
# os.system('python STMeta_Obj.py -m STMeta_v1.model_4_6.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1we4tpemb6')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_6_6.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1we6tpemb6')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_8_6.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1we8tpemb6')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_10_6.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1we10tpemb6')
# os.system('python STMeta_Obj.py -m STMeta_v1.model_12_6.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:multi_embedding_layer_V1we12tpemb6')
