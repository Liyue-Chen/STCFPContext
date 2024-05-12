import os
import warnings
warnings.filterwarnings("ignore")

# #############################################
# # BenchMark Bike
# #############################################
### Chicago ### 
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:NoContext')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:EarlyConcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:EarlyAdd')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:Raw_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:Raw_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Raw_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:Emb_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Interaction,mark:Emb_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Interaction,mark:Emb_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:MultiEmb_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Interaction,mark:MultiEmb_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Interaction,mark:MultiEmb_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Interaction,mark:LSTM_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:LSTM_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Interaction,mark:LSTM_Gating')



# ### Chicago  trial 2 ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation-Interaction,mark:NoContext_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation-Interaction,mark:EarlyConcat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation-Interaction,mark:EarlyAdd_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-not-concat,graph:Distance-Correlation-Interaction,mark:Raw_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation-Interaction,mark:Raw_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:not-linear-gating,graph:Distance-Correlation-Interaction,mark:Raw_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-not-concat,graph:Distance-Correlation-Interaction,mark:Emb_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Interaction,mark:Emb_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Interaction,mark:Emb_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-not-concat,graph:Distance-Correlation-Interaction,mark:MultiEmb_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Interaction,mark:MultiEmb_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Interaction,mark:MultiEmb_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Interaction,mark:LSTM_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Interaction,mark:LSTM_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d bike_chicago.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Interaction,mark:LSTM_Gating_T2')




# # ###############################################
# # # BenchMark Metro
# # ###############################################
### Shanghai ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation-Line,mark:NoContext')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation-Line,mark:EarlyConcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation-Line,mark:EarlyAdd')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-not-concat,graph:Distance-Correlation-Line,mark:Raw_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation-Line,mark:Raw_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Raw_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:Emb_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Line,mark:Emb_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Line,mark:Emb_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:MultiEmb_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Line,mark:MultiEmb_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Line,mark:MultiEmb_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Line,mark:LSTM_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Line,mark:LSTM_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Line,mark:LSTM_Gating')



# ### Shanghai Trial 2 ###
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation-Line,mark:NoContext_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation-Line,mark:EarlyConcat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation-Line,mark:EarlyAdd_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-not-concat,graph:Distance-Correlation-Line,mark:Raw_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation-Line,mark:Raw_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:not-linear-gating,graph:Distance-Correlation-Line,mark:Raw_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-not-concat,graph:Distance-Correlation-Line,mark:Emb_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation-Line,mark:Emb_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation-Line,mark:Emb_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-not-concat,graph:Distance-Correlation-Line,mark:MultiEmb_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation-Line,mark:MultiEmb_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation-Line,mark:MultiEmb_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation-Line,mark:LSTM_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation-Line,mark:LSTM_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d metro_shanghai.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation-Line,mark:LSTM_Gating_T2')






# # # ###############################################
# # # # BenchMark ChargeStation
# # # ###############################################

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation,mark:NoContext')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation,mark:EarlyConcat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation,mark:EarlyAdd')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:not-not-concat,graph:Distance-Correlation,mark:Raw_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation,mark:Raw_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Raw_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:emb-not-concat,graph:Distance-Correlation,mark:Emb_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation,mark:Emb_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation,mark:Emb_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:multi-not-concat,graph:Distance-Correlation,mark:MultiEmb_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation,mark:MultiEmb_Add')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation,mark:MultiEmb_Gating')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation,mark:LSTM_Concat')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation,mark:LSTM_Add')
          
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation,mark:LSTM_Gating')


###### Beijing Trial 2 ######
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:not-not-not,graph:Distance-Correlation,mark:NoContext_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:earlyconcat,graph:Distance-Correlation,mark:EarlyConcat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:earlyadd,graph:Distance-Correlation,mark:EarlyAdd_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:not-not-concat,graph:Distance-Correlation,mark:Raw_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:not-linear-add,graph:Distance-Correlation,mark:Raw_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:not-linear-gating,graph:Distance-Correlation,mark:Raw_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:emb-not-concat,graph:Distance-Correlation,mark:Emb_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:emb-linear-add,graph:Distance-Correlation,mark:Emb_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:emb-linear-gating,graph:Distance-Correlation,mark:Emb_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p batch_size:32,external_method:multi-not-concat,graph:Distance-Correlation,mark:MultiEmb_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:multi-linear-add,graph:Distance-Correlation,mark:MultiEmb_Add_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_method:multi-linear-gating,graph:Distance-Correlation,mark:MultiEmb_Gating_T2')


os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-not-concat,graph:Distance-Correlation,mark:LSTM_Concat_T2')

os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-add,graph:Distance-Correlation,mark:LSTM_Add_T2')
          
os.system('python STMeta_Obj.py -m STMeta_v1.model.yml -d chargestation_beijing.data.yml '
          '-p external_lstm_len:4,external_method:lstm-linear-gating,graph:Distance-Correlation,mark:LSTM_Gating_T2')

