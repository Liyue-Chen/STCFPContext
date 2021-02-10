
import os
import warnings
warnings.filterwarnings("ignore")

# #############################################
# # BenchMark Bike
# #############################################
# # NYC
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:earlyconcat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_nyc.data.yml '
#           '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:earlyadd')


# ## Chicago ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:earlyconcat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
#           '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:earlyadd')


# ## DC ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:earlyconcat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_dc.data.yml '
#           '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:earlyadd')

# # ###############################################
# # # BenchMark DiDi
# # ###############################################
# ## Xian ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:earlyconcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_xian.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:earlyadd')


# # Chengdu ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:earlyconcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d didi_chengdu.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:earlyadd')



# ###############################################
# # BenchMark Metro
# ###############################################
# ## Shanghai ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:earlyconcat,graph:Distance-Correlation-Line,mark:earlyconcat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
#           '-p external_method:earlyadd,graph:Distance-Correlation-Line,mark:earlyadd')


# ## Chongqing ###
# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:earlyconcat,graph:Distance-Correlation-Line,mark:earlyconcat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_chongqing.data.yml '
#           '-p external_method:earlyadd,graph:Distance-Correlation-Line,mark:earlyadd')


# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:earlyconcat,graph:Distance-Correlation,mark:earlyconcat')

# os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
#           '-p external_method:earlyadd,graph:Distance-Correlation,mark:earlyadd')

