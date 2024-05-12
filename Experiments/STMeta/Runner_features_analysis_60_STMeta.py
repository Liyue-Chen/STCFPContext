import os

#############################################
# BenchMark Bike Chicago
#############################################
####### Bike Chicago

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:sp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:SP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp-sp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_SP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:road,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp-road,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_Road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:demo,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp-demo,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_Demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-holiday-tp-poi-sp-demo,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_TP_POI_SP_Demo')




####### Bike Chicago Trial 2

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:sp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:SP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp-sp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_SP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:road,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Road_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp-road,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_Road_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:demo,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Demo_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:holiday-tp-demo,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Holi_TP_Demo_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_use:weather-holiday-tp-poi-sp-demo,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Wea_Holi_TP_POI_SP_Demo_T2')


# #############################################
# # BenchMark Metro Shanghai
# #############################################
####### Metro Shanghai
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:sp,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:SP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp-sp,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_SP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:road,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp-road,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_Road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:demo,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp-demo,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_Demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-holiday-tp-poi-sp-demo,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_TP_POI_SP_Demo')


####### Metro Shanghai Trial 2
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:sp,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:SP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp-sp,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_SP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:road,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Road_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp-road,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_Road_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:demo,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Demo_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:holiday-tp-demo,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Holi_TP_Demo_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_use:weather-holiday-tp-poi-sp-demo,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Wea_Holi_TP_POI_SP_Demo_T2')



# #############################################
# # BenchMark ChargeStation Beijing
# #############################################
####### ChargeStation Beijing
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:mark:POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_TP_POIs')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:sp,external_method:not-linear-gating,graph:Distance-Correlation,mark:SP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp-sp,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_SP')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:road,external_method:not-linear-gating,graph:Distance-Correlation,mark:Road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp-road,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_Road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:demo,external_method:not-linear-gating,graph:Distance-Correlation,mark:Demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp-demo,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_Demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-holiday-tp-poi-sp-demo,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_TP_POI_SP_Demo')




####### ChargeStation Beijing Trial 2
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:mark:POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_TP_POIs_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:sp,external_method:not-linear-gating,graph:Distance-Correlation,mark:SP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp-sp,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_SP_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:road,external_method:not-linear-gating,graph:Distance-Correlation,mark:Road_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp-road,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_Road_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:demo,external_method:not-linear-gating,graph:Distance-Correlation,mark:Demo_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:holiday-tp-demo,external_method:not-linear-gating,graph:Distance-Correlation,mark:Holi_TP_Demo_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_use:weather-holiday-tp-poi-sp-demo,external_method:not-linear-gating,graph:Distance-Correlation,mark:Wea_Holi_TP_POI_SP_Demo_T2')


