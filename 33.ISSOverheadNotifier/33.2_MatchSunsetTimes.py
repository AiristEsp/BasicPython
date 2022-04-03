import requests
from datetime import datetime

MY_LAT = '-0.789275'
MY_LONG = '113.921326'

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print("Sunrise:", sunrise)
print("Sunset:", sunset)

time_now = datetime.now()
