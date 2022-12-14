'''
import csv

day = []
temp = []
condition = []

with open("weather_data.csv") as f:
    data = csv.reader(f)

    for row in data:
        if row[0] != "day":
            day.append(row[0])
        if row[1] != "temp":
            temp.append(int(row[1]))
        if row[2] != "condition":
            condition.append(row[2])
'''

import pandas as pd
'''
# data in column = data["columnname"] or data.columnname
data = pd.read_csv("weather_data.csv")

data_dict = data.to_dict()

small = data["temp"].min()
average = data["temp"].mean()
biggest = data["temp"].max()
med = data["temp"].median()

# data by row  data[data.columnname == "what you want to pull"]
monday = data[data.day == 'Monday']

# get data that had max temp
max_row = data[data.temp == data.temp.max()]

monday = data[data.day == 'Monday']
faren = (monday.temp * 9/5) + 32
print(faren)
'''
# Create dataframe from scratch
data_dict = {
    "students": ["Jonathan", "Kane", "Julie"],
    "scores": [76, 82, 69]
}

data = pd.DataFrame(data = data_dict)
data.to_csv("new_data.csv")