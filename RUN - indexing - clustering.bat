ECHO OFF
CLS

ECHO Indexing dataset System Starting ...

python index_clustering.py --dataset datacars --index index_clustering_250.csv --cluster 50

ECHO execution completed.

PAUSE