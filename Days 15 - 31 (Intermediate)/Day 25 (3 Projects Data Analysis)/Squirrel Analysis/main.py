import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

col = "Primary Fur Color"

grey_sq = len(data[data[col] == "Gray"])
cinnamon_sq = len(data[data[col] == "Cinnamon"])
black_sq = len(data[data[col] == "Black"])

data_dict = {
    "Colour": ["Gray", "Cinnamon", "Black"],
    "Total": [grey_sq, cinnamon_sq, black_sq]
}

df = pd.DataFrame(data = data_dict)
df.to_csv("new_data.csv")


