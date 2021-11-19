import os
import warnings
warnings.filterwarnings("ignore")

# # ###############################################
# # BenchMark Metro
# ###############################################

metro_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset Metro '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation-Line '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays All '
                         '--threshold_correlation 0.7 '
                         '--threshold_distance 5000 '
                         '--threshold_interaction 30 '
                         '--Epoch 2000 '
                         '--Train True '
                         '--lr 1e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay sum '
                         )

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion emb_linear_gating')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion emb_linear_gating')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion emb_linear_gating')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion emb_linear_gating')


os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-not-concat '
                                      '  --MergeIndex 1 --CodeVersion multi_not_concat ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-not-concat '
                                      '  --MergeIndex 1 --CodeVersion multi_not_concat ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-not-concat '
                                      '  --MergeIndex 1 --CodeVersion multi_not_concat ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-not-concat '
                                      '  --MergeIndex 1 --CodeVersion multi_not_concat ')


