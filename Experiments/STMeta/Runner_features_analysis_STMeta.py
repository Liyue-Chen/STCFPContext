import os

#############################################
# BenchMark Bike Chicago
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:gating_V1_hi_tp')



#############################################
# BenchMark Metro Shanghai
#############################################
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_we')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi,poi_distance:1000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_poi1000')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_poi5000')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_V1_hi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_hi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:gating_poi_wa_hi_tp')






#############################################
# BenchMark ChargeStation
#############################################
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi,poi_distance:1000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:mark:gating_V1_poi1000')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:mark:gating_V1_poi5000')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_V1_hi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_wa')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_wa_hi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_wa_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_hi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_poi_wa_hi_tp')



