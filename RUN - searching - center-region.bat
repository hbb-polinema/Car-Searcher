ECHO OFF
CLS
ECHO Input your query image:

ECHO Content Based Image Retrieval System Starting ...

python search_center_region.py --index index_center_region.csv --query queries/q8.jpg --result-path datacars

ECHO execution completed.

PAUSE