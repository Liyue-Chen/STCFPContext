import os
import warnings
warnings.filterwarnings("ignore")


# #############################################
# # BenchMark Bike NYC
# # #############################################
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

os.system(bike_shared_params_st_mgcn + ' --City NYC --external_method not-not-not '
                                      '  --MergeIndex 12 --CodeVersion bikeNYC_noContext ')

os.system(bike_shared_params_st_mgcn + ' --City NYC --external_method not-linear-gating '
                                      '  --MergeIndex 12 --CodeVersion bikeNYC_gating --external_use holiday-tp ')


# #############################################
# # BenchMark Bike NYC
# # #############################################
bike_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset Taxi '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation-Interaction '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange [0,365] '
                         '--TrainDays 330 '
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

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-not-not '
                                      '  --MergeIndex 1 --CodeVersion taxiChi_noContext ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion taxiChi_gating --external_use holiday-tp ')
