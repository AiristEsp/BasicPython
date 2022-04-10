import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = ""
auth_token = ""

weather_params = {
    "lat": 6.17511,
    "lon": 106.865,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
# 1 https://api.openweathermap.org/data/2.5/onecall?
# lat=6.175110&&lon=106.865036&&
# exclude=current,minutely,daily&
# appid=6e8bdf76c20254889e240ed4c2f75f47
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?"
#                             "lat=-6.175110&"
#                             "lon=106.865036&"
#                             "appid=6e8bdf76c20254889e240ed4c2f75f47")
#
# response.raise_for_status()
# data = response.json()

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) > 500:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_='+15',
            to='+62'
        )
print(message.sid)