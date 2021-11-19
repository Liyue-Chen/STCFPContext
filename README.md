# STCFP Context

## Project

This repository provides the data and code for reproducing the experiment results of `Benchmarking Context Factor Generalizability in Spatiotemporal Crowd Flow Prediciton`.

## Data

We provide crowd flow and corresponding POI data in the `dataset` directory. Move them into the UCTB package `data` directory to make the `dataloader` could find the data files. Weather data is stored in 'External' key of the `*.pkl` files.

## Environment

**Urban Computing Tool Box (UCTB, https://github.com/uctb/UCTB)** is a package providing **spatial-temporal prediction models**. This project is developed based on the UCTB toolkit, so firstly install UCTB by the following command.

```bash
python3 build_install.py
```

Experiments require specific dependencies.

* tensorflow-gpu ==1.13.1
* keras ==2.2.4
* cuda toolkit==10.0

## Exploring the generalizability of different modeling techniques

To analyze context modeling techniques, run the following experiments.

#### Experiments based on STMGCN

In `STCFP_External\Experiments\STMGCN` directory, run the following commands.

```
python3 Runner_techniques_analysis_30_STMGCN.py

python3 Runner_techniques_analysis_60_STMGCN.py

python3 Runner_techniques_analysis_120_STMGCN.py
```

#### Experiments based on STMeta

In `STCFP_External\Experiments\STMeta` directory, run the following commands.

```bash
python3 Runner_features_analysis_30_STMeta.py

python3 Runner_features_analysis_60_STMeta.py

python3 Runner_features_analysis_120_STMeta.py
```

## Exploring the generalizability of context features

To exploring the generalizability of context features, run the following experiments.

#### Experiments based on XGBoost

In `STCFP_External\Experiments\XGBoost` directory, run the following commands.

```bash
python3 Runner_features_analysis_XGBoost_30.py

python3 Runner_features_analysis_XGBoost_60.py

python3 Runner_features_analysis_XGBoost_120.py
```

#### Experiments based on STMGCN

In `STCFP_External\Experiments\ST_MGCN` directory, run the following commands.

```
python3 Runner_features_analysis_30_STMGCN.py

python3 Runner_features_analysis_60_STMGCN.py

python3 Runner_features_analysis_120_STMGCN.py
```

#### Experiments based on STMeta

In `STCFP_External\Experiments\STMeta` directory, run the following commands.

```
python3 Runner_features_analysis_30_STMeta.py

python3 Runner_features_analysis_60_STMeta.py

python3 Runner_features_analysis_120_STMeta.py
```