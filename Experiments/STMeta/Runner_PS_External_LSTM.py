import os
import warnings
warnings.filterwarnings("ignore")

# ###############################################
# # BenchMark DiDi
# ###############################################
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_lstm_len:4,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_lstm_len:6,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm6_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_lstm_len:8,external_method:lstm,graph:Distance-Correlation-Interaction,mark:lstm8_V1')


# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm,graph:Distance-Correlation,mark:lstm4_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:6,external_method:lstm,graph:Distance-Correlation,mark:lstm6_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:8,external_method:lstm,graph:Distance-Correlation,mark:lstm8_V1')
