ECHO OFF
CLS

ECHO Indexing dataset System Starting ...

python index_center_region_clustering.py --dataset datacars --index index_center_region_clustering_144.csv --cluster 144

ECHO execution completed.

PAUSE