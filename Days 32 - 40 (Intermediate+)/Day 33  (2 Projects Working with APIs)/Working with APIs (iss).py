import requests
# 1xx wait   2xx success   3xx denied   4xx error/miss type
response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()
pos_long = response.json()['iss_position']['longitude']
pos_lat = response.json()['iss_position']['latitude']
iss_loc = (pos_lat, pos_long)

print(iss_loc)
