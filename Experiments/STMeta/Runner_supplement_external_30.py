import os
import warnings
warnings.filterwarnings("ignore")
#############################################
# BenchMark emb-linear-add
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Interaction,mark:emb_linear_add,MergeIndex:6')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Interaction,mark:emb_linear_add,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Line,mark:emb_linear_add,MergeIndex:6')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation,mark:emb_linear_add,MergeIndex:1')


#############################################
# BenchMark emb-linear-gating
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Interaction,mark:emb_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Interaction,mark:emb_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Line,mark:emb_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation,mark:emb_linear_gating,MergeIndex:1')


#############################################
# BenchMark multi-linear-add
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Interaction,mark:multi_linear_add,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Interaction,mark:multi_linear_add,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Line,mark:multi_linear_add,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation,mark:multi_linear_add,MergeIndex:1')


#############################################
# BenchMark multi-linear-gating
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Interaction,mark:multi_linear_gating,MergeIndex:6')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Interaction,mark:multi_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Line,mark:multi_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation,mark:multi_linear_gating,MergeIndex:1')


#############################################
# BenchMark lstm-not-concat
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Interaction,mark:lstm4_not_concat,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Interaction,mark:lstm4_not_concat,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Line,mark:lstm4_not_concat,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation,mark:lstm4_not_concat,MergeIndex:1')


#############################################
# BenchMark lstm-linear-gating
#############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Interaction,mark:lstm4_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Interaction,mark:lstm4_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Line,mark:lstm4_linear_gating,MergeIndex:6')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation,mark:lstm4_linear_gating,MergeIndex:1')
