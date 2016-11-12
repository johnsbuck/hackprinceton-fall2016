import csv
import json

with open('meteorite-landings.csv', 'rb') as file:
    reader = csv.reader(file)
    X = list(reader)

y = []

miss_mass = 0
miss_latlng = 0

for i in xrange(1, len(X)):
    try:
        y.append(float(X[i][7]))
        y.append(float(X[i][8]))
    except ValueError:
        miss_latlng = miss_latlng + 1

    try:
        float(X[i][4])
        y.append(float(X[i][4]))
    except ValueError:
        miss_mass = miss_mass + 1

with open('output.json', 'wb') as file:
    json.dump(y, file)
