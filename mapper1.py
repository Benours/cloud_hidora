#!/usr/bin/env python
"""mapper.py"""
import csv
import sys

# with open('dataw_fro03.csv', newline='') as csvfile:
csv_reader = csv.reader(sys.stdin)

next(csv_reader, None)


for row in csv_reader:
    nomcli, prenomcli, cpcli, villecli, datcde, timbrecli, qte = (
        row[2],
        row[3],
        row[4],
        row[5],
        row[7],
        row[9],
        row[15],
    )
    cpcli = int(cpcli) / 1000
    if cpcli in [53, 61, 28] and '2008' < datcde < '2016':
        client = nomcli + ' ' + prenomcli
        dep = cpcli

        print(str(timbrecli) + ';' + str(client) + ';' + str(villecli) + ';' + str(dep) + ';' + str(qte))

