ECHO OFF
CLS

ECHO Indexing dataset System Starting ...

python index.py --dataset datacars --index indexcar.csv

ECHO execution completed.

PAUSE