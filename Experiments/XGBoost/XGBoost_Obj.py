import numpy as np
import argparse
from UCTB.dataset import NodeTrafficLoader
from UCTB.model import XGBoost
from UCTB.evaluation import metric
from UCTB.preprocess import SplitData
from UCTB.preprocess.time_utils import is_work_day_china, is_work_day_america
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Argument Parser")
# data source
parser.add_argument('--dataset', default='Metro', type=str)
parser.add_argument('--city', default="Chongqing", type=str)

parser.add_argument('--closeness_len', default=12, type=int)
parser.add_argument('--period_len', default=6, type=int)
parser.add_argument('--trend_len', default=4, type=int)
parser.add_argument('--max_depth', default=8, type=int)
parser.add_argument('--num_boost_round', default=51, type=int)

parser.add_argument('--MergeIndex', default=1)
parser.add_argument('--MergeWay', default="sum")
parser.add_argument('--data_range', default="all")
parser.add_argument('--train_data_length', default="all")
parser.add_argument('--test_ratio', default=0.1, type=float)
parser.add_argument('--external_use', default="weather-holiday-tp", type=str)
parser.add_argument('--poi_distance', default=1000, type=int)


#use params and args to show its difference
args = vars(parser.parse_args())

print("dataset:",args['dataset'])
print("city:",args['city'])
print("external_use:",args['external_use'])

data_loader = NodeTrafficLoader(dataset=args['dataset'], city=args['city'],
                                data_range=args['data_range'], train_data_length=args['train_data_length'],
                                test_ratio=args['test_ratio'],
                                closeness_len=args['closeness_len'],
                                period_len=args['period_len'],
                                trend_len=args['trend_len'],
                                normalize=False,
                                workday_parser=is_work_day_america if args['dataset'] == 'Bike' else is_work_day_china,
                                external_use=args['external_use'],
                                poi_distance=args['poi_distance'],
                                MergeIndex=args['MergeIndex'],
                                MergeWay="max" if args["dataset"] == "ChargeStation" else "sum")


train_closeness, val_closeness = SplitData.split_data(
    data_loader.train_closeness, [0.9, 0.1])
train_period, val_period = SplitData.split_data(
    data_loader.train_period, [0.9, 0.1])
train_trend, val_trend = SplitData.split_data(
    data_loader.train_trend, [0.9, 0.1])
if data_loader.external_dim > 0:
    train_ef, val_ef = SplitData.split_data(data_loader.train_ef, [0.9, 0.1])
if data_loader.poi_dim is not None and data_loader.poi_dim > 0:
    train_poi,val_poi = SplitData.split_data(data_loader.poi_feature_train, [0.9, 0.1])

train_y, val_y = SplitData.split_data(data_loader.train_y, [0.9, 0.1])

prediction_test = []
prediction_val = []


#for i in tqdm(range(data_loader.station_number),desc="training model..."):
for i in range(data_loader.station_number):
    #print('Station', i)

    model = XGBoost(n_estimators=int(args['num_boost_round']), max_depth=int(args['max_depth']),verbosity=0)

    X_Train = []
    X_Val = []
    X_Test = []
    if int(args['closeness_len']) > 0:
        X_Train.append(train_closeness[:, i, :, 0])
        X_Val.append(val_closeness[:, i, :, 0])
        X_Test.append(data_loader.test_closeness[:, i, :, 0])
    if int(args['period_len']) > 0:
        X_Train.append(train_period[:, i, :, 0])
        X_Val.append(val_period[:, i, :, 0])
        X_Test.append(data_loader.test_period[:, i, :, 0])
    if int(args['trend_len']) > 0:
        X_Train.append(train_trend[:, i, :, 0])
        X_Val.append(val_trend[:, i, :, 0])
        X_Test.append(data_loader.test_trend[:, i, :, 0])
    
    # append external features
    if data_loader.external_dim > 0:
        X_Train.append(train_ef)
        X_Val.append(val_ef)
        X_Test.append(data_loader.test_ef)
    
    # append poi features
    if data_loader.poi_dim is not None and data_loader.poi_dim > 0:
        X_Train.append(train_poi[:,i,:])
        X_Val.append(val_poi[:,i,:])
        X_Test.append(data_loader.poi_feature_test[:,i,:])
    
    X_Train = np.concatenate(X_Train, axis=-1)
    X_Val = np.concatenate(X_Val, axis=-1)
    X_Test = np.concatenate(X_Test, axis=-1)

    model.fit(X_Train, train_y[:, i, 0])

    p_val = model.predict(X_Val)
    p_test = model.predict(X_Test)
    
    prediction_val.append(p_val.reshape([-1, 1, 1]))
    prediction_test.append(p_test.reshape([-1, 1, 1]))

print("X_Train:",X_Train.shape)

prediction_test = np.concatenate(prediction_test, axis=-2)
prediction_val = np.concatenate(prediction_val, axis=-2)

print('Val RMSE', metric.rmse(prediction_val, val_y, threshold=0))
print('Test RMSE', metric.rmse(prediction_test, data_loader.test_y, threshold=0))
print('Val MAE', metric.mae(prediction_val, val_y, threshold=0))
print('Test MAE', metric.mae(prediction_test, data_loader.test_y, threshold=0))
