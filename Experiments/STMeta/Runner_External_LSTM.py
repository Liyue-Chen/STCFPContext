import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike
#############################################
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p weather_len:6,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p weather_len:6,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p weather_len:6,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm_V1')

# ###############################################
# # BenchMark DiDi
# ###############################################
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p weather_len:6,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p weather_len:6,external_method:lstm,external_method:not,graph:Distance-Correlation-Interaction,mark:lstm_V1')


# ###############################################
# # BenchMark Metro
# ###############################################
### Shanghai ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p weather_len:6,external_method:lstm,graph:Distance-Correlation-Line,mark:lstm_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p weather_len:6,external_method:lstm,graph:Distance-Correlation-Line,mark:lstm_V1')

# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p weather_len:6,external_method:lstm,graph:Distance-Correlation,mark:lstm_V1')
