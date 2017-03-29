
import requests

ac_api_key = "v2oX9AGDnThsQZa7f3h7mBxr2KItzBIE"
def extractValues():
    location_request = requests.get(
        "http://apidev.accuweather.com/locations/v1/search?q=new delhi, in&apikey=hoArfRosT1215")
    location_request = location_request.json()
    city_key = location_request[0]['Key']
    weather_data_request = requests.get(
        "http://apidev.accuweather.com/currentconditions/v1/%s.json?language=en&apikey=hoArfRosT1215" % city_key)
    #print(weather_data_request.json())
    weather_data_request = weather_data_request.json()
    weather_condition = weather_data_request[0]['WeatherText']
    current_temp = weather_data_request[0]['Temperature']['Metric']['Value']
    return [weather_condition, current_temp]

arr=extractValues()
wc=arr[0]
ct=arr[1]


