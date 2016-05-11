ECHO OFF
CLS

ECHO Indexing dataset System Starting ...

python index_center_region_clustering.py --dataset datacars --index index_center_region_clustering_50.csv --cluster 50

ECHO execution completed.

PAUSE