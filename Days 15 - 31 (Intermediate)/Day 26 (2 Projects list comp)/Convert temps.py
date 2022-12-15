weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def convert_F(value):
    faren = (value * 9 / 5) + 32
    return faren

weather_f = {day:convert_F(val) for day, val in weather_c.items()}
print(weather_f)