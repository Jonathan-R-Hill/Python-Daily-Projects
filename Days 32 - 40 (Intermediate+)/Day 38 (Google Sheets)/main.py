from datetime import datetime
import requests

# Nutritionix Stuff
APP_ID = "YOUR_NUTR_APPID"
APP_KEY = "YOUR_NUTR_APIKEY"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
DATE = datetime.today().strftime('%d/%m/%Y')
TIME = datetime.now().strftime("%X")

HEIGHT_CM = 185
WEIGHT_KG = 80
AGE = 28
GENDER = "male"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=data)
result = response.json()

data_to_input = {
    "workout": {
        "date": DATE,
        "time": TIME,
    }
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Google Sheets/Sheety
SHEETY_ENDPOINT = "YOUR_SHEETY_ENDPOINT"
response = requests.post(url=EXERCISE_ENDPOINT, json=sheet_inputs)
print(response.text)

