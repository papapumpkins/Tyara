
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

    #print(daily_forecast_request.json())
    #print(weather_data_request.json())

    daily_forecast_request=daily_forecast_request.json()
    weather_data_request = weather_data_request.json()

    weather_condition = weather_data_request[0]['WeatherText']
    current_temp = weather_data_request[0]['Temperature']['Metric']['Value']
    today_min_temp=daily_forecast_request["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
    today_max_temp = daily_forecast_request["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
    hline=daily_forecast_request["Headline"]["Text"]
    #print((today_min_temp))
    return [weather_condition, current_temp, today_max_temp,today_min_temp,hline]

def return_current_weather():
    weather_array = extractValues()
    current_temp = weather_array[1]
    current_condition = weather_array[0]
    #print(" The temperature outside is "+str(current_temp) +", and the weather is "+current_condition)
    return " The temperature outside is "+str(current_temp) +", and the weather is "+current_condition


def return_forecast():
    WA = extractValues()
    weather_dialog = "The current temperature outside is "+ str(WA[1])+"and the weather is "+WA[0]+". The temperature will range from "
    weather_dialog = weather_dialog + str(WA[2]) + " to "+ str(WA[3])+". You can expect "+str(WA[4])+". That's all I have for now."
    return weather_dialog

return_current_weather()

