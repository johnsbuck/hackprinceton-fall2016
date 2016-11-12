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
new_mass = np.log(np.sort(mass)+1)
mass_indices = np.indices(new_mass.shape)[0]
new_mass = new_mass.reshape(new_mass.shape[0],1)
mass_indices = mass_indices.reshape(mass_indices.shape[0],1)

linear = linear_model.LinearRegression().fit(new_mass[:new_mass.shape[0]/2], mass_indices[:mass_indices.shape[0]/2])
plt.scatter(new_mass[new_mass.shape[0]/2:], mass_indices[mass_indices.shape[0]/2:], color="red")

plt.plot(new_mass[new_mass.shape[0]/2:], linear.predict(new_mass[new_mass.shape[0]/2:]), color="blue", linewidth=3)

plt.ylabel('Mass')
plt.xlabel('Index')
plt.show()
