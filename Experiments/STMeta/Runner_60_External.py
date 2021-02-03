import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike
#############################################
#### NYC
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1')

### Chicago ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1')

### DC ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1')


# ###############################################
# # BenchMark DiDi
# ###############################################
### Xian ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p batch_size:8,external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1')

## Chengdu ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1')

# ###############################################
# # BenchMark Metro
# ###############################################
### Shanghai ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Line,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Line,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1bs8')

### Chongqing ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation-Line,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation-Line,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1')



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


# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation,mark:not_external_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:not-not-concat,graph:Distance-Correlation,mark:direct_concat_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:emb-not-concat,graph:Distance-Correlation,mark:one_embedding_layer_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:multi-not-concat,graph:Distance-Correlation,mark:classified_embedding_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_fusion_V1')
