import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import numpy as np
import csv
import json

with open('meteorite-landings.csv', 'rb') as file:
    reader = csv.reader(file)
    X = list(reader)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def feature_scale(nparray):
    return (nparray - np.amin(nparray))/(np.amax(nparray) - np.amin(nparray))

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

mass = X[1:,4].astype(np.float)
new_mass = np.log(np.log(np.sort(mass)+1)+1)
new_mass = (new_mass - np.amin(new_mass))/(np.amax(new_mass) - np.amin(new_mass))

indices = feature_scale(np.arange(mass.shape[0]).astype(float))

plt.plot(new_mass, color="red")
plt.plot(indices, color="blue")
plt.plot(feature_scale(np.log(np.sort(mass).astype(float) + 1)), color="purple")
plt.plot(feature_scale(np.sort(mass).astype(float)), color='green')

plt.ylabel('Mass')
plt.xlabel('Index')
plt.show()
