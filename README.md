# SBUResearch487-GCP-Functions

#### We used Google Cloud Platform Scheduler and Functions to collect realtime weather and forecasting data from OpenWeatherApi. And, we stored them into Google Cloud Platform Firestore (Firebase) using Python Scripts.

#### This is Forecasting Data Collector

    for item in json_data['list']:
        stt = item['dt']
        time = datetime.fromtimestamp(stt)
        strTime = str(time)
        print(strTime)
        next_date, hour = strTime.split(' ')
        
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
       
#### Dictionary called "data" includes weather data and sends all data into Google Cloud Platform.
#### 
#### 
#### This is Realtime Weather Data Collector

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

#### Dictionary called "data" includes weather data and sends all data into Google Cloud Platform.
#### We need some Library for using this function in GCP functions
#### Requirements we need are below:

###### requests==2.20.0
###### numpy
###### google-cloud-storage
###### datetime
###### google
###### google-api-core
###### google-auth
###### google-cloud-core
###### google-cloud-firestore

