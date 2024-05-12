import os

#############################################
# BenchMark Bike Chicago
#############################################

bike_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset Bike '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation-Interaction '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays 365 '
                         '--threshold_correlation 0 '
                         '--threshold_distance 1000 '
                         '--threshold_interaction 500 '
                         '--Epoch 10000 '
                         '--Train True '
                         '--lr 5e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay sum '
                         )

# # Chicago
os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use weather --MergeIndex 1 --CodeVersion wea ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use holiday --MergeIndex 1 --CodeVersion holi ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use tp --MergeIndex 1 --CodeVersion tp ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi --poi_distance 5000 --MergeIndex 1 --CodeVersion poi ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use weather-holiday --MergeIndex 1 --CodeVersion wea_holi ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use weather-tp --MergeIndex 1 --CodeVersion wea_tp ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use holiday-tp --MergeIndex 1 --CodeVersion holi_tp ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-weather --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-holiday --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_holi ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_tp ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-weather-holiday --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_holi ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-weather-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_tp ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-holiday-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_holi_tp ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --external_use poi-weather-holiday-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_holi_tp ')



# #############################################
# # BenchMark Metro Shanghai
# #############################################

metro_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset Metro '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays All '
                         '--threshold_correlation 0.7 '
                         '--threshold_distance 5000 '
                         '--threshold_interaction 30 '
                         '--Epoch 10000 '
                         '--Train True '
                         '--lr 1e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay sum '
                         )

# Shanghai
os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use weather --MergeIndex 1 --CodeVersion wea ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use holiday --MergeIndex 1 --CodeVersion holi ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use tp --MergeIndex 1 --CodeVersion tp ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi --poi_distance 5000 --MergeIndex 1 --CodeVersion poi ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use weather-holiday --MergeIndex 1 --CodeVersion wea_holi ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use weather-tp --MergeIndex 1 --CodeVersion wea_tp ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use holiday-tp --MergeIndex 1 --CodeVersion holi_tp ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-weather --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-holiday --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_holi ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_tp ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-weather-holiday --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_holi ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-weather-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_tp ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-holiday-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_holi_tp ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      ' --external_use poi-weather-holiday-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_holi_tp ')






# #############################################
# # BenchMark ChargeStation
# #############################################

cs_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset ChargeStation '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays All '
                         '--threshold_correlation 0.1 '
                         '--threshold_distance 1000 '
                         '--threshold_interaction 500 '
                         '--Epoch 10000 '
                         '--Train True '
                         '--lr 5e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay max '
                         )

# Beijing
os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use weather --MergeIndex 1 --CodeVersion wea ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use holiday --MergeIndex 1 --CodeVersion holi ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use tp --MergeIndex 1 --CodeVersion tp ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi --poi_distance 5000 --MergeIndex 1 --CodeVersion poi ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use weather-holiday --MergeIndex 1 --CodeVersion wea_holi ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use weather-tp --MergeIndex 1 --CodeVersion wea_tp ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use holiday-tp --MergeIndex 1 --CodeVersion holi_tp ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-weather --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-holiday --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_holi ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_tp ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-weather-holiday --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_holi ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-weather-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_tp ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-holiday-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_holi_tp ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      ' --external_use poi-weather-holiday-tp --poi_distance 5000 --MergeIndex 1 --CodeVersion poi_wea_holi_tp ')



