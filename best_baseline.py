import csv
from datetime import datetime
import os.path
import sys
import plotly.express as px
import pandas as pd

file = 'painting.csv'

if not os.path.exists(file):
    w = csv.writer(open(file, "w"))

today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

painting = {}
# default values
min_value, max_value = sys.maxsize, -1
min_key, max_key = "", ""

painting['health'] = int(input("health: "))
painting['family'] = int(input("family: "))
painting['friends'] = int(input("friends: "))
painting['intimate relationship'] = int(input("intimate relationship: "))
painting['mission'] = int(input("mission: "))
painting['finances'] = int(input("finances: "))
painting['adventure'] = int(input("adventure: "))
painting['hobby'] = int(input("hobby: "))
painting['spirituality'] = int(input("spirituality: "))
painting['emotion'] = int(input("emotion: "))

# calculate key and values
for k,v in painting.items():
    if v < min_value:
        min_key, min_value = k, v
    elif v > max_value:
        max_key, max_value = k, v

# write to file
w = csv.writer(open(file, "a"))
w.writerow(["date", today])
w.writerow(["min_value", min_value])
w.writerow(["max_value", max_value])
w.writerow(["min_key", min_key])
w.writerow(["max_key", max_key])
for key, val in painting.items():
    w.writerow([key, val])

df = pd.DataFrame(dict(
    value=list(painting.values()),
    key=list(painting.keys())))
fig = px.line_polar(df, r='value', theta='key', line_close=True)
fig.show()

# REPR
print("Minimum is {} at {}.".format(min_key, min_value))
print("Maximum is {} at {}.".format(max_key, max_value))