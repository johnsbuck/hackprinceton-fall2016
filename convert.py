import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import numpy as np
import csv
import json

def feature_scale(nparray):
    return (nparray - np.amin(nparray))/(np.amax(nparray) - np.amin(nparray))

with open('meteorite-landings.csv', 'rb') as file:
    reader = csv.reader(file)
    X = list(reader)

i = 0
while i < len(X):
    try:
        float(X[i][4])
        float(X[i][7])
        float(X[i][8])
        i = i + 1
    except ValueError:
        del X[i]

X = np.asarray(X)

X[1:,4] = feature_scale(np.log(X[1:,4].astype(np.float) + 1))

y = []
for i in range(1, X.shape[0]):
    y.append(float(X[i,7]))
    y.append(float(X[i,8]))
    y.append(float(X[i,4]))

with open('output.json', 'wb') as file:
    json.dump(y, file)
