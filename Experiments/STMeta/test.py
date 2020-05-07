import os

os.system('python STMeta_Obj.py -m STMeta_v1.model_4.yml -d metro_shanghai.data.yml '
          '-p lr:5e-5,batch_size:4,external_method:classified,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1tpemb4')
os.system('python STMeta_Obj.py -m STMeta_v1.model_6.yml -d metro_shanghai.data.yml '
          '-p lr:5e-5,batch_size:4,external_method:classified,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1tpemb6')
os.system('python STMeta_Obj.py -m STMeta_v1.model_8.yml -d metro_shanghai.data.yml '
          '-p lr:5e-5,batch_size:4,external_method:classified,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1tpemb8')
os.system('python STMeta_Obj.py -m STMeta_v1.model_10.yml -d metro_shanghai.data.yml '
          '-p lr:5e-5,batch_size:4,external_method:classified,graph:Distance-Correlation-Line,mark:one_embedding_layer_V1tpemb10')
        