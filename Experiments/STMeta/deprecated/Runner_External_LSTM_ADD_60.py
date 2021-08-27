import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike
#############################################
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add')

# # ###############################################
# # # BenchMark DiDi
# # ###############################################
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:add')

# ###############################################
# # BenchMark Metro
# ###############################################
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Line,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Line,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation-Line,mark:add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation-Line,mark:add')

###############################################
# BenchMark ChargeStation
###############################################
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation,mark:lstm4_V1')
          
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:not-linear-add,graph:Distance-Correlation,mark:add')
