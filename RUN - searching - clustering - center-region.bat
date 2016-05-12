ECHO OFF
CLS
ECHO Input your query image:

ECHO Content Based Image Retrieval System Starting ...

python search_clustering_center_region.py --index index_center_region_clustering_36.csv --query queries/q2.jpg --result-path datacars --cluster 36

ECHO execution completed.

PAUSE