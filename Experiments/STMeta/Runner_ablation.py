import os
##########################
# ablation experiment
################# Bike
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:weather,batch_size:16,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:holiday,batch_size:16,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:tp,batch_size:16,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:weather-holiday,batch_size:16,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:weather-tp,batch_size:16,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:holiday-tp,batch_size:16,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_V1_hi_tp')


################# Shanghai
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1_we')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:tp,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_fusion_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-holiday,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-tp,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp,batch_size:8,external_method:gating,graph:Distance-Correlation-Line,mark:gating_V1_hi_tp')

################# Beijing
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather,batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_fusion_V1_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday,batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_fusion_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-pexternal_use:tp,batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_fusion_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-holiday,batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-tp,batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp,batch_size:32,external_method:gating,graph:Distance-Correlation,mark:gating_V1_hi_tp')

################# DiDi
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_use:weather,batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_use:holiday,batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_use:tp,batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_fusion_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_use:weather-holiday,batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_use:weather-tp,batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_use:holiday-tp,batch_size:8,external_method:gating,graph:Distance-Correlation-Interaction,mark:gating_V1_hi_tp')

