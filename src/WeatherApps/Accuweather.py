
import requests

ac_api_key = "HKMGN5Ga619bSd0nqzY7D6CxrccdD54q"
#25-202396_1_AL #Delhi
def extractValues():
    location_request = requests.get(
        "http://apidev.accuweather.com/locations/v1/search?q=new delhi, in&apikey=hoArfRosT1215")
    location_request = location_request.json()
    city_key = location_request[0]['Key']
    weather_data_request = requests.get(
        "http://apidev.accuweather.com/currentconditions/v1/%s.json?language=en&apikey=hoArfRosT1215" % city_key)
    daily_forecast_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/%s?apikey=HKMGN5Ga619bSd0nqzY7D6CxrccdD54q&details=false&metric=true"%city_key)
    print(daily_forecast_request.json())
    print(weather_data_request.json())
    daily_forecast_request=daily_forecast_request.json()
    weather_data_request = weather_data_request.json()
    weather_condition = weather_data_request[0]['WeatherText']
    current_temp = weather_data_request[0]['Temperature']['Metric']['Value']
    today_min_temp=daily_forecast_request["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
    today_max_temp = daily_forecast_request["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
    hline=daily_forecast_request["Headline"]["Text"]
    #print((today_min_temp))
    return [weather_condition, current_temp, today_max_temp,today_min_temp,hline]

arr=extractValues()
wc=arr[0]
ct=arr[1]
Mt=arr[2]
mt=arr[3]
hl=arr[4]

