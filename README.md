# STCFP Context

## Project

This repository provides the data and code for reproducing the experiment results of `Exploring Context Modeling Techniques on the Spatiotemporal Crowd Flow Prediction`.

## Data

We provide ride-sharing and corresponding POI data in the `data` directory. Move them into the UCTB package data directory to make the `dataloader` can find data files.

## Environment

This project is based on the UCTB toolkit, so firstly install UCTB by the following command.

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

#### Context Modeling Techniques Impact

```bash
python3 Runner_60_External.py

python3 Runner_supplement_external_60.py
```

## Context Generalization Ability

To exploring the generalization ability of context , run the following experiments.

```bash
python3 Runner_ablation.py
```

