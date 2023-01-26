import requests
from datetime import datetime

# https://pixe.la/@USER_NAME
TOKEN = "TOKEN HERE"
USER_NAME = "USER_NAME"
DATE = datetime.today().strftime('%Y%m%d')

pixela_EP = "https://pixe.la/v1/users"
graph_EP = f"{pixela_EP}/{USER_NAME}/graphs"
addpixel_EP = f"{pixela_EP}/{USER_NAME}/graphs/graph1"
updatepixel_EP = f"{pixela_EP}/{USER_NAME}/graphs/graph1/{DATE}"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": "graph1",
    "name": "Coding Project",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",
}

add_params = {
    "date": DATE,
    "quantity": "10"
}

update_params = {
    "quantity": input("Enter Minutes spent coding: "),
}

# response = requests.post(url=pixela_EP, json=user_params)  # Create user

# response = requests.post(url=graph_EP, json=graph_config, headers=headers) # Create graph

# response = requests.post(url=addpixel_EP, json=add_params, headers=headers) # Add Pixel to graph

response = requests.put(url=updatepixel_EP, json=update_params, headers=headers)  # Update Pixel
print(response.text)
