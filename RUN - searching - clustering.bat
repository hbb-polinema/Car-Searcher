ECHO OFF
CLS
ECHO Input your query image:

ECHO Content Based Image Retrieval System Starting ...

python search_clustering.py --index index_clustering_50.csv --query queries/q2.jpg --result-path datacars --cluster 10

ECHO execution completed.

PAUSE