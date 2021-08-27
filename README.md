# STCFP Context

## Project

This repository provides the data and code for reproducing the experiment results of `Benchmarking Context Factor Generalizability in Spatiotemporal Crowd Flow Prediciton`.

## Data

We provide ride-sharing and corresponding POI data in the `data` directory. Move them into the UCTB package data directory to make the `dataloader` can find data files.

## Environment

**Urban Computing Tool Box (UCTB, https://github.com/uctb/UCTB)** is a package providing **spatial-temporal prediction models**. This project is developed based on the UCTB toolkit, so firstly install UCTB by the following command.

```bash
python3 build_install.py
```

Experiments require specific dependencies.

* tensorflow-gpu ==1.13.1
* keras ==2.2.4
* cuda toolkit==10.0



## Context Modeling Techniques Impact

To analyze context modeling techniques, run the following experiments.

#### Early Jointly Modeling vs. Late Fusion Modeling

```
python3 Runner_Early_Modelling.py
```

#### Late Fusion Modeling Variants

```bash
python3 Runner_60_External.py

python3 Runner_supplement_external_60.py
```

## Context Generalization Ability

To exploring the generalization ability of context , run the following experiments.

```bash
python3 Runner_ablation.py
```

