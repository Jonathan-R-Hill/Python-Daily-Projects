import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "KEY HERE"
account_sid = "ACCOUNT SID HERE"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="TWILIO VIRTUAL NUMBER",
        to="TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)


"""
import requests

API_KEY = 'KEY'

lat = 54.568230
lon = -1.314430

location = "Middlesbrough"

api = f"http://api.openweathermap.org/data/2.5/weather?q={location},UK&appid={API_KEY}"

response = requests.get(api)
data = response.json()

current_weather = data['weather'][0]['main']
current_weather_disc = data['weather'][0]['description']
print(f"Current weather is: {current_weather}: {current_weather_disc}")
"""