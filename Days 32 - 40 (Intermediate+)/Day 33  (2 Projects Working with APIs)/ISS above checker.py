import requests
from datetime import datetime
from time import sleep

MY_LAT = 54.568230
MY_LNG = -1.314430
ISS_LOC = ''


# --------------------------- Functions ----------------------------- #


def iss_check_overhead():
    global ISS_LOC
    # ----------------------------- ISS Location -------------------------- #
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")

    response_iss.raise_for_status()
    pos_long = float(response_iss.json()['iss_position']['longitude'])
    pos_lat = float(response_iss.json()['iss_position']['latitude'])
    iss_loc = (pos_lat, pos_long)

    close_low_lat = MY_LAT - 5.00
    close_high_lat = MY_LAT + 5.00

    close_high_lng = MY_LNG - 5.00
    close_low_lng = MY_LNG + 5.00

    ISS_LOC = iss_loc

    if close_low_lat < iss_loc[0] < close_high_lat and close_low_lng < iss_loc[1] < close_high_lng:
        return True


def is_night():
    # ---------------------------Sunset/sunrise --------------------------- #
    api = "https://api.sunrise-sunset.org/json"

    param = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        'formatted': 0,
    }
    response = requests.get(api, params=param)
    response.raise_for_status()
    data = response.json()

    sunrise = data['results']['sunrise']
    sunrise_hour = int(sunrise.split('T')[1].split(':')[0])

    sunset = data['results']["sunset"]
    sunset_hour = int(sunset.split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if sunrise_hour > time_now > sunset_hour:
        return True


while True:
    print(f"My Location: ({MY_LAT}, {MY_LNG})")
    if is_night() and iss_check_overhead():
        print("The ISS is above and it's dark!")
        print(f"ISS Location: {ISS_LOC}")
    elif not is_night() and iss_check_overhead():
        print("The ISS is above but it's light :(")
        print(f"ISS Location: {ISS_LOC}")
    else:
        print(f'The ISS is not nearby. {ISS_LOC}')
    sleep(30)
