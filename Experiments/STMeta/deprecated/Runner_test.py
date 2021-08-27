import os
import warnings
warnings.filterwarnings("ignore")


# ###############################################
# # BenchMark DiDi
# ###############################################
### Xian ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-not-not,graph:Distance-Correlation,mark:not_external')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:not-not-concat,graph:Distance-Correlation,mark:direct_concat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:emb-not-concat,graph:Distance-Correlation,mark:one_embedding')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:multi-not-concat,graph:Distance-Correlation,mark:multi_embedding')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:not-linear-add,graph:Distance-Correlation,mark:adding_fusion')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:not-linear-gating,graph:Distance-Correlation,mark:gating_fusion')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation,mark:lstm4')

## supplement
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:emb-linear-add,graph:Distance-Correlation,mark:embedding_add')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:emb-linear-gating,graph:Distance-Correlation,mark:embedding_gating')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation,mark:multiembedding_add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation,mark:multiembedding_gating')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:lstm-not-concat,graph:Distance-Correlation,mark:lstm_concat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p batch_size:8,external_method:lstm-linear-gating,graph:Distance-Correlation,mark:lstm_gating')
