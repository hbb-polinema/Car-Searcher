ECHO OFF
CLS

ECHO Indexing dataset System Starting ...

python index_center_region.py --dataset datacars --index index_center_region.csv

ECHO execution completed.

PAUSE