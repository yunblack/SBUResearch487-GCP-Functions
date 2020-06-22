import requests
import json
import datetime
from google.cloud import firestore
db = firestore.Client()

def hello_world(request):
    request_json = request.get_json()
    sendDataToGCP()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'

def sendDataToGCP():
    now = datetime.datetime.now()
    apikey = "474d59dd890c4108f62f192e0c6fce01"
    cities = ["Seoul,KR"]  ##
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

    k2c = lambda k: k - 273.15

    for name in cities:
        url = api.format(city=name, key=apikey)
        r = requests.get(url)
        data = json.loads(r.text)
        data = {
            u'City': data["name"],
            u'Date': now,
            u'Low_Temp': k2c(data["main"]["temp_min"]),
            u'High_Temp': k2c(data["main"]["temp_max"]),
            u'Avg_Temp': round(k2c(data["main"]["temp"])),
            u'Humidity': data["main"]["humidity"],
            u'Pressure': data["main"]["pressure"],
            u'Wind': data["wind"]["speed"]
        }
        print("Done")
    print(str(now).split(".")[0])
    DataName = str(now).split(".")[0]
    db.collection(u'RealTimeData_Test').document(DataName).set(data)
