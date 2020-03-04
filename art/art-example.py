#!/usr/bin/env python

import pandas as pd

from train import art_train
from test import art_test

train_data = pd.read_csv('sample-data/train-example.csv').values
test_data = pd.read_csv('sample-data/test-example.csv').values
x = train_data[:,1:3]
y = test_data[:,1:3]


r = 0.9
Tmatrix = art_train(x,rho=r) #,beta=0.000001,alpha=1.0,nep=1)
print(Tmatrix)
T = art_test(y,Tmatrix,rho=r) #,beta=0.000001,alpha=1.0,nep=1)
print(T)