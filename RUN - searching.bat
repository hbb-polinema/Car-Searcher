ECHO OFF
CLS
ECHO Input your query image:

ECHO Content Based Image Retrieval System Starting ...

python search.py --index indexcar.csv --query queries/q4.jpg --result-path datacars

ECHO execution completed.

PAUSE