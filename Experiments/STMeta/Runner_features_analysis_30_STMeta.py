import os

#############################################
# BenchMark Bike Chicago
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:weather,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:weather-holiday,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:wea_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:weather-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:wea_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:holiday-tp,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-weather,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-holiday,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-weather-holiday,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_wea_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-weather-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_wea_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-holiday-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:poi_wea_holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:sp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:sp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:holiday-tp-sp,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:holi_tp_sp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:road,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:holiday-tp-road,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:holi_tp_road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:demo,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:holiday-tp-demo,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:holi_tp_demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p data_range:0.5,train_data_length:183,MergeIndex:6,external_use:weather-holiday-tp-poi-road-sp-demo,poi_distance:5000,batch_size:16,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:wea_holi_tp_poi_road_sp_demo')




# #############################################
# # BenchMark Metro Shanghai
# #############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:weather,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:weather-holiday,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:wea_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:weather-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:wea_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:holiday-tp,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-weather,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-weather-holiday,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_wea_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-weather-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_wea_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:poi_wea_holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:sp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:sp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:holiday-tp-sp,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:holi_tp_sp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:road,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:holiday-tp-road,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:holi_tp_road')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:demo,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:holiday-tp-demo,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:holi_tp_demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p MergeIndex:6,external_use:weather-holiday-tp-poi-road-sp-demo,poi_distance:5000,batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:wea_holi_tp_poi_road_sp_demo')





# #############################################
# # BenchMark ChargeStation
# #############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:weather,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:mark:poi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:weather-holiday,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:wea_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:weather-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:wea_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:holiday-tp,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-weather,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_wea')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-weather-holiday,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_wea_holi')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-weather-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_wea_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:poi-weather-holiday-tp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:poi_wea_holi_tp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:sp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:sp')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:holiday-tp-sp,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:holi_tp_sp')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:road,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:road')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:holiday-tp-road,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:holi_tp_road')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:demo,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:demo')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:holiday-tp-demo,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:holi_tp_demo')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p MergeIndex:1,external_use:weather-holiday-tp-poi-road-sp-demo,poi_distance:5000,batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:wea_holi_tp_poi_road_sp_demo')

