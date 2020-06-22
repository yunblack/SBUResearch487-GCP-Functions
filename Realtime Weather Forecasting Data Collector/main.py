import requests
from datetime import datetime
import requests
import json

from google.cloud import firestore
db = firestore.Client()

def predictionWeather():
    api_call = 'https://api.openweathermap.org/data/2.5/forecast?&q=Seoul&appid=474d59dd890c4108f62f192e0c6fce01'
    json_data = requests.get(api_call).json()
    current_date = ''
    k2c = lambda k: k - 273.15

    for item in json_data['list']:
        stt = item['dt']
        time = datetime.fromtimestamp(stt)
        strTime = str(time)
        print(strTime)
        next_date, hour = strTime.split(' ')
        # print('City: ', 'Seoul')
        # print('Date: ', strTime)
        # print('Condition: %s' % item['weather'][0]['description'])
        # print('Temperature: ', item['main']['temp'])
        # print('High Temperature: ', item['main']['temp_max'])
        # print('Low Temperature: ', item['main']['temp_min'])
        # print('Pressure: ', item['main']['pressure'])
        # print('Humidity: ', item['main']['humidity'])
        # print('Wind: ', item['wind']['speed'])
        # print()
        data = {
            u'City': 'Seoul',
            u'Date': strTime,
            u'Condition': item['weather'][0]['description'],
            u'Low_Temp': k2c(item["main"]["temp_min"]),
            u'High_Temp': k2c(item["main"]["temp_max"]),
            u'Avg_Temp': k2c(item['main']['temp']),
            u'Humidity': item["main"]["humidity"],
            u'Pressure': item["main"]["pressure"],
            u'Wind': item["wind"]["speed"]
        }
        db.collection(u'RealTimeForecastingData').document(strTime).set(data)

def main():
    predictionWeather()

if __name__ == "__main__":
    main()