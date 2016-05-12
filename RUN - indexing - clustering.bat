ECHO OFF
CLS

ECHO Indexing dataset System Starting ...

python index_clustering.py --dataset datacars --index index_clustering_35.csv --cluster 7

ECHO execution completed.

PAUSE