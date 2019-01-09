from apixu.client import ApixuClient, ApixuException
from time import sleep
import schedule
import time


api_key = '99513eae83b24272ad625651190601'
client = ApixuClient(api_key)

def job():
    current = client.getCurrentWeather(q='45039')
    print(current['current']['last_updated']) #last time the record was updated (in local time)
    print(current['current']['last_updated_epoch']) #last time the record was updated (in Unix time)
    print(current['current']['temp_f'])  # show temprature in fahrenheit
    print(current['current']['condition']['text']) # summary description
    print(current['current']['feelslike_f']) #how hot/cold it really feels
    print(current['current']['cloud'])  # percentage cloud cover
    print(current['current']['humidity']) # percent rH
    print(current['current']['wind_mph']) # windspeed
    print(current['current']['precip_in']) # rainfall
    print(current['location']['country'])  # name of country
    print(current['location']['lat'])  # latitude value
    print(current['location']['lon'])  # longitude value

schedule.every(2).minutes.do.(job)

while True:
    schedule.run_pending()
    time.sleep(1)