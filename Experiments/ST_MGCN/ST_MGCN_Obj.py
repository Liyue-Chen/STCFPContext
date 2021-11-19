import os
import nni
import GPUtil
import numpy as np

from UCTB.dataset import NodeTrafficLoader
from UCTB.model import ST_MGCN
from UCTB.evaluation import metric
from UCTB.preprocess import SplitData
from UCTB.preprocess.time_utils import is_work_day_china, is_work_day_america

def stmeta_param_parser():
    import argparse
    parser = argparse.ArgumentParser(description="Argument Parser")
    # data source
    parser.add_argument('--Dataset', default='Metro')
    parser.add_argument('--City', default='Shanghai')
    # network parameter
    parser.add_argument('--CT', default='6', type=int)
    parser.add_argument('--PT', default='7', type=int)
    parser.add_argument('--TT', default='4', type=int)
    parser.add_argument('--K', default='1', type=int)
    parser.add_argument('--L', default='1', type=int)
    parser.add_argument('--Graph', default='Distance-Correlation-Line')
    parser.add_argument('--LSTMUnits', default='128', type=int)
    parser.add_argument('--LSTMLayers', default='3', type=int)
    # Training data parameters
    parser.add_argument('--DataRange', default='All')
    parser.add_argument('--TrainDays', default='365')
    parser.add_argument('--test_ratio', default=0.1, type=float)
    # Graph parameter
    parser.add_argument('--TC', default='0', type=float)
    parser.add_argument('--TD', default='1000', type=float)
    parser.add_argument('--TI', default='500', type=float)
    # training parameters
    parser.add_argument('--Epoch', default='20000', type=int)
    parser.add_argument('--Train', default='True')
    parser.add_argument('--lr', default='5e-4', type=float)
    parser.add_argument('--ESlength', default='50', type=int)
    parser.add_argument('--patience', default='0.1', type=float)
    parser.add_argument('--BatchSize', default='32', type=int)
    # graph parameter
    parser.add_argument('--threshold_distance', default=5000, type=float)
    parser.add_argument('--threshold_correlation', default=0.7, type=float)
    parser.add_argument('--threshold_interaction', default=30, type=float)
    # version control
    parser.add_argument('--CodeVersion', default='V')
    # Merge parameter
    parser.add_argument('--MergeIndex', default=1, type=int)
    parser.add_argument('--MergeWay', default='sum', type=str)
    # external features
    parser.add_argument('--external_method', default="not-not-not", type=str)
    parser.add_argument('--external_use', default="weather-holiday-tp", type=str)
    parser.add_argument('--external_lstm_len', default=5, type=int)
    parser.add_argument('--embedding_dim', default=[8,1,8,8], type=str)
    parser.add_argument('--poi_distance', default=5000, type=int)
    return parser

parser = stmeta_param_parser()
args = vars(parser.parse_args())

model_dir = os.path.join('model_dir', args['City'])
code_version = 'ST_MMGCN_{}_K{}L{}_{}_F{}'.format(''.join([e[0] for e in args['Graph'].split('-')]),
                                              args['K'], args['L'], args['CodeVersion'],int(args['MergeIndex']))

if isinstance(args["embedding_dim"],str):
    args["embedding_dim"] = [int(item) for item in args["embedding_dim"].replace("[","").replace("]","").split(",")]
print(args["embedding_dim"],type(args["embedding_dim"]))

print("external_method:",args["external_method"])
print("external_use:",args["external_use"])

# Config data loader
data_loader = NodeTrafficLoader(dataset=args['Dataset'], city=args['City'],
                                test_ratio=float(args['test_ratio']),
                                data_range=args['DataRange'], 
                                train_data_length=args['TrainDays'],
                                closeness_len=int(args['CT']), 
                                period_len=int(args['PT']), 
                                trend_len=int(args['TT']),
                                external_method=args['external_method'],
                                external_lstm_len=args['external_lstm_len'],
                                threshold_distance=args['threshold_distance'],
                                threshold_correlation=args['threshold_correlation'],
                                threshold_interaction=args['threshold_interaction'],
                                normalize=True, 
                                graph=args['Graph'],
                                with_lm=True,
                                workday_parser=is_work_day_america if args['Dataset'] == 'Bike' else is_work_day_china,
                                external_use=args['external_use'],
                                poi_distance=args['poi_distance'],
                                MergeIndex=args['MergeIndex'],
                                MergeWay=args["MergeWay"])

# split data
train_closeness, val_closeness = SplitData.split_data(data_loader.train_closeness, [0.9, 0.1])
train_period, val_period = SplitData.split_data(data_loader.train_period, [0.9, 0.1])
train_trend, val_trend = SplitData.split_data(data_loader.train_trend, [0.9, 0.1])
if data_loader.external_dim > 0:
    train_ef_closeness, val_ef_closeness = SplitData.split_data(data_loader.train_ef_closeness, [0.9, 0.1])
    train_ef_period, val_ef_period= SplitData.split_data(data_loader.train_ef_period, [0.9, 0.1])
    train_ef_trend, val_ef_trend = SplitData.split_data(data_loader.train_ef_trend, [0.9, 0.1])
    train_ef, val_ef = SplitData.split_data(data_loader.train_ef, [0.9, 0.1])
    train_lstm_ef, val_lstm_ef = SplitData.split_data(data_loader.train_lstm_ef, [0.9, 0.1])
if data_loader.poi_dim is not None and data_loader.poi_dim > 0:
    train_poi,val_poi = SplitData.split_data(data_loader.poi_feature_train, [0.9, 0.1])

train_y, val_y = SplitData.split_data(data_loader.train_y, [0.9, 0.1])

de_normalizer =  data_loader.normalizer.min_max_denormal

# GPU device
deviceIDs = GPUtil.getAvailable(order='memory', limit=2, maxLoad=1, maxMemory=0.7,
                                includeNan=False, excludeID=[], excludeUUID=[])

if len(deviceIDs) == 0:
    current_device = '-1'
else:
    current_device = str(deviceIDs[0])

ST_MGCN_Obj = ST_MGCN(num_node=data_loader.station_number,
                      T=int(args['CT']) + int(args['PT']) + int(args['TT']),
                      input_dim=1,
                      external_dim=data_loader.external_dim,
                      closeness_len=int(args['CT']), 
                      period_len=int(args['PT']), 
                      trend_len=int(args['TT']),
                      external_lstm_len=args['external_lstm_len'],
                      num_graph=data_loader.LM.shape[0],
                      gcl_k=args['K'],
                      gcl_l=args['L'],
                      lstm_units=args['LSTMUnits'],
                      lstm_layers=args['LSTMLayers'],
                      lr=args['lr'],
                      code_version=code_version,
                      model_dir=model_dir,
                      gpu_device=current_device,
                      external_method=args['external_method'],
                      embedding_dim=args['embedding_dim'],
                      poi_dim=data_loader.poi_dim,
                      classified_external_feature_dim=data_loader.external_onehot_dim if "multi" in args['external_method'] or args['external_method'] == "lstm" else [])

ST_MGCN_Obj.build()

print(args['Dataset'], args['City'], code_version)
print(ST_MGCN_Obj.trainable_vars)

# Training
if args['Train'] == 'True':
    ST_MGCN_Obj.fit(traffic_flow=np.concatenate((np.transpose(data_loader.train_closeness, [0, 2, 1, 3]),
                                                 np.transpose(data_loader.train_period, [0, 2, 1, 3]),
                                                 np.transpose(data_loader.train_trend, [0, 2, 1, 3])), axis=1),
                    poi_feature = data_loader.poi_feature_train,
                    external_closeness=data_loader.train_ef_closeness,
                    external_period=data_loader.train_ef_period,
                    external_trend=data_loader.train_ef_trend,
                    external_lstm_hidden=data_loader.train_lstm_ef,
                    laplace_matrix=data_loader.LM,
                    target=data_loader.train_y,
                    external_feature=data_loader.train_ef,
                    output_names=('loss', ),
                    evaluate_loss_name='loss',
                    early_stop_method='t-test',
                    early_stop_length=int(args['ESlength']),
                    early_stop_patience=float(args['patience']),
                    sequence_length=data_loader.train_sequence_len,
                    save_model=True,
                    batch_size=int(args['BatchSize']),
                    max_epoch=int(args['Epoch']))

ST_MGCN_Obj.load(code_version)

# Evaluate
prediction = ST_MGCN_Obj.predict(traffic_flow=np.concatenate((np.transpose(data_loader.test_closeness, [0, 2, 1, 3]),
                                                              np.transpose(data_loader.test_period, [0, 2, 1, 3]),
                                                              np.transpose(data_loader.test_trend, [0, 2, 1, 3])), axis=1),
                                 poi_feature=data_loader.poi_feature_test,
                                 external_closeness=data_loader.test_ef_closeness if data_loader.external_dim > 0 else None,
                                 external_period=data_loader.test_ef_period if data_loader.external_dim > 0 else None,
                                 external_trend=data_loader.test_ef_trend if data_loader.external_dim > 0 else None,
                                 external_lstm_hidden=data_loader.test_lstm_ef if data_loader.external_dim > 0 else None,
                                 laplace_matrix=data_loader.LM,
                                 external_feature=data_loader.test_ef if data_loader.external_dim > 0 else None,
                                 sequence_length=data_loader.test_sequence_len,
                                 output_names=['prediction'],
                                 cache_volume=int(args['BatchSize']))

test_rmse = metric.rmse(prediction=data_loader.normalizer.min_max_denormal(prediction['prediction']),
                        target=data_loader.normalizer.min_max_denormal(data_loader.test_y),
                        threshold=0)

test_mae = metric.mae(prediction=data_loader.normalizer.min_max_denormal(prediction['prediction']),
                        target=data_loader.normalizer.min_max_denormal(data_loader.test_y),
                        threshold=0)

# Evaluate
prediction = ST_MGCN_Obj.predict(traffic_flow=np.concatenate((np.transpose(val_closeness, [0, 2, 1, 3]),
                                                             np.transpose(val_period, [0, 2, 1, 3]),
                                                             np.transpose(val_trend, [0, 2, 1, 3])), axis=1),
                                 poi_feature=val_poi if data_loader.poi_dim is not None and data_loader.poi_dim > 0 else None,
                                 external_closeness=val_ef_closeness if data_loader.external_dim > 0 else None,
                                 external_period=val_ef_period if data_loader.external_dim > 0 else None,
                                 external_trend=val_ef_trend if data_loader.external_dim > 0 else None,
                                 external_lstm_hidden=val_lstm_ef if data_loader.external_dim > 0 else None,
                                 laplace_matrix=data_loader.LM,
                                 external_feature=val_ef if data_loader.external_dim > 0 else None,
                                 sequence_length=max((len(val_closeness), len(val_period), len(val_trend))),
                                 output_names=['prediction'],
                                 cache_volume=int(args['BatchSize']))

val_rmse = metric.rmse(prediction=data_loader.normalizer.min_max_denormal(prediction['prediction']),
                        target=data_loader.normalizer.min_max_denormal(val_y),
                        threshold=0)
val_mae = metric.mae(prediction=data_loader.normalizer.min_max_denormal(prediction['prediction']),
                        target=data_loader.normalizer.min_max_denormal(val_y),
                        threshold=0)

print('Val RMSE', val_rmse)
print('Test RMSE', test_rmse)
print('Val MAE', val_mae)
print('Test MAE', test_mae)

val_loss = ST_MGCN_Obj.load_event_scalar('val_loss')

time_consumption = [val_loss[e][0] - val_loss[e-1][0] for e in range(1, len(val_loss))]
time_consumption = sum([e for e in time_consumption if e < (min(time_consumption) * 10)]) / 3600
print('Converged using %.2f hour / %s epochs' % (time_consumption, ST_MGCN_Obj._global_step))

