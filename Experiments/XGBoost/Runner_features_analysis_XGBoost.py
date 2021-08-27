import os
import warnings
warnings.filterwarnings("ignore")

#############################################
# BenchMark Bike
#############################################
#### Chicago
bike_param = {
    "closeness_len": 11,
    "period_len": 8,
    "trend_len": 0,
    "max_depth": 4,
    "num_boost_round": 35
}

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use not '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use weather '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use holiday '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))


os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use weather-holiday '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use weather-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use holiday-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Bike --city Chicago --train_data_length 365 '
          '--MergeIndex 1 --external_use weather-holiday-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(bike_param["closeness_len"],bike_param["period_len"],bike_param["trend_len"],bike_param["max_depth"],bike_param["num_boost_round"]))


#############################################
# BenchMark Metro
#############################################
#### Shanghai
metro_param = {
    "closeness_len": 3,
    "period_len": 7,
    "trend_len": 0,
    "max_depth": 5,
    "num_boost_round": 50
}

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use not '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use holiday '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-holiday '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use holiday-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use holiday-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-holiday-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-holiday-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use holiday-tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset Metro --city Shanghai  '
          '--MergeIndex 1 --external_use weather-holiday-tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(metro_param["closeness_len"],metro_param["period_len"],metro_param["trend_len"],metro_param["max_depth"],metro_param["num_boost_round"]))



#############################################
# BenchMark ChargeStation
#############################################
#### Beijing
cs_param = {
    "closeness_len": 12,
    "period_len": 7,
    "trend_len": 0,
    "max_depth": 2,
    "num_boost_round": 20
}


os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use not '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use holiday '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-holiday '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use holiday-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use holiday-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-holiday-tp '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-holiday-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use holiday-tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))

os.system('python XGBoost_Obj.py --dataset ChargeStation --city Beijing  '
          '--MergeIndex 1 --MergeWay max --external_use weather-holiday-tp-poi --poi_distance 5000 '
          '--closeness_len {} --period_len {} --trend_len {} --max_depth {} --num_boost_round {}'.format(cs_param["closeness_len"],cs_param["period_len"],cs_param["trend_len"],cs_param["max_depth"],cs_param["num_boost_round"]))
