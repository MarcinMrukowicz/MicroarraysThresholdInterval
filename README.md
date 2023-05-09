# MicroarraysThresholdInterval

## Overview

`dataset` folder contains 5 used dataset parsed from elvira format to csv files.

`aggregations.py` implementation of interval-value aggregation functions.

`algorithm.py` proposition of ensemble algorithm for microarrays

`colon.py`, `almall.py`, `dlbcl.py`, `ovarian.py`, `prostate.py` contains script generating results for each dataset. In each script the same hyperparameters for algotithm are considered.

`plots.py` plots diagram for each aggregation functions.

`filter_results.py` script used for pick result that fuffils condition where accuracy > x and coverage > y

## Prerequisite
1. install python 3.9 
   - Windows
     - download installer(https://www.python.org/downloads/release/python-390/)
   - Linux
     - `sudo apt install python3.9 `
2. install requiments.txt
```terminal
  $ pip install -r requirements.txt
```

## Reproduce results

Generating excel file with results for Colon dataset:
```terminal
python colon.py
```
Generating excel file with results for Leukemia (ALLAML) dataset:
```terminal
python AMLALL.py
```
Generating excel file with results for  Lymphoma(DLBCL) dataset:
```terminal
python dlbcl.py
```
Generating excel file with results for prostate dataset:
```terminal
python prostate.py
```
Generating excel file with results for ovarian dataset:
```terminal
python ovarian.py
```
