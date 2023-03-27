import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike NYC and Taxi Chicago
#############################################
# ### Bike NYC ### 
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,MergeIndex:12,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
          '-p external_use:holiday-tp,external_method:not-linear-gating,graph:Distance-Correlation-Interaction,MergeIndex:12,mark:Gating')


### Taxi Chicago ### 
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d taxi_chicago.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation,MergeIndex:1,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d taxi_chicago.data.yml '
          '-p external_use:holiday-tp,external_method:not-linear-gating,graph:Distance-Correlation,MergeIndex:1,mark:Gating')


### PEMS BAY ### 
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d pems_bay.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation,MergeIndex:12,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d pems_bay.data.yml '
          '-p external_use:holiday-tp,external_method:not-linear-gating,graph:Distance-Correlation,MergeIndex:12,mark:Gating')


### Pedestrian Melbourne ### 
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d pedestrian_melbourne.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation,MergeIndex:1,mark:not_external_V1')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d pedestrian_melbourne.data.yml '
          '-p external_use:holiday-tp,external_method:not-linear-gating,graph:Distance-Correlation,MergeIndex:1,mark:Gating')

