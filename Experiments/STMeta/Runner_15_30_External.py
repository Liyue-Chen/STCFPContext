import os
import warnings
warnings.filterwarnings("ignore")
#############################################
# BenchMark Bike
#############################################
#### NYC
## 15mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:3')

# ## 30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:6')

# ### Chicago ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:3')

# ## 30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:6')

### DC ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:3')

# ##30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:6')

# ###############################################
# # BenchMark DiDi
# ###############################################
### Xian ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:3')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p batch_size:8,external_method:add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1,MergeIndex:3')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:3')

##30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p batch_size:8,external_method:add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:6')

### Chengdu ### 
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:3')

# #30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Interaction,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Interaction,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Interaction,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Interaction,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:add,graph:Distance-Correlation-Interaction,mark:adding_fusion_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1,MergeIndex:6')

# # ###############################################
# # # BenchMark Metro
# # ###############################################
### Shanghai ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Line,mark:not_external_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Line,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:embedding,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Line,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1bs8,MergeIndex:3')

# ##30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Line,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Line,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:embedding,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Line,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p lr:5e-5,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1bs8,MergeIndex:6')


# ### Chongqing ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Line,mark:not_external_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Line,mark:direct_concat_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Line,mark:classified_embedding_V1,MergeIndex:3')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1,MergeIndex:3')

##30mins
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:not,graph:Distance-Correlation-Line,mark:not_external_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:direct,graph:Distance-Correlation-Line,mark:direct_concat_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:embedding,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:classified,graph:Distance-Correlation-Line,mark:classified_embedding_V1,MergeIndex:6')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1,MergeIndex:6')


# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:not,graph:Distance-Correlation,mark:not_external_V1,MergeIndex:1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:direct,graph:Distance-Correlation,mark:direct_concat_V1,MergeIndex:1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:embedding,graph:Distance-Correlation,mark:one_embedding_layer_V1,MergeIndex:1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:classified,graph:Distance-Correlation,mark:classified_embedding_V1,MergeIndex:1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_fusion_V1,MergeIndex:1')
