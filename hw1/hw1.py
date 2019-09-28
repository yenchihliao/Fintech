import os
import sys
import numpy as np

class Tx:
    def __init__(self, args):#deal_date, product, due_month, deal_time, deal_price):
        self._deal_date = args[0].strip()#deal_date
        self._product = args[1].strip()#product
        self._due_month = args[2].strip()#due_month
        self._deal_time = int(args[3].strip())#deal_time
        self._deal_price = float(args[4].strip())#deal_price
    def show(self):
        print(self._deal_date, self._product, self._due_month, self._deal_time, self._deal_price)

class LegalTx():
    def __init__(self):
        self._list = []
        self._min_month = 10000000
    def tryAdd(self, tx):
        if tx._product != 'TX':
            return
        if tx._deal_time < 84500:
            return
        if tx._deal_time > 134500:
            return
        if len(tx._due_month) != 6:
            return
        if int(tx._due_month) > int(self._min_month):
            return
        if int(tx._due_month) < int(self._min_month):
            self._min_month = tx._due_month
            self._list = []
        self._list.append(tx)
    def show(self):
        for e in self._list:
            e.show()

f = open(sys.argv[1], 'r', encoding='big5')

count = 0
txList = LegalTx()
f.readline()
while True:
    line = f.readline()
    if not line:
        break
    txList.tryAdd(Tx(line.split(',')))
    count += 1

if len(txList._list) == 0:
    print("0 0 0 0")
else:
    first = txList._list[0]._deal_price
    last = txList._list[len(txList._list) - 1]._deal_price
    pMax = first
    for tx in txList._list:
        if tx._deal_price > pMax:
            pMax = tx._deal_price
    pMin = first
    for tx in txList._list:
        if tx._deal_price < pMin:
            pMin = tx._deal_price
    print(int(first), int(pMax), int(pMin), int(last))
