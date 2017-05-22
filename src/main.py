import time

from SpeechRecog import transcribe
from RecordSound import record
from Speech_Interpreter import Text_Interpreter
from GMailAuth import quickstart
from AlarmsAndReminders import Alarms

from WeatherApps import Accuweather
from TTS import PlaySounds,speech_rec
from DateTime import Present
from resources import *
from Academics import class_data

Rec = record
Rec.record_from_mic(5)
time.sleep(5.5)

TR = transcribe
Transcripted_Text = TR.transcribe_file("output.flac")

SIN = Text_Interpreter
sin_code = Text_Interpreter(Transcripted_Text)
sin_dialog = Transcripted_Text

def perform_action_with_code(sin_code,sin_dialog):
    if(sin_code==1):
        GM = quickstart
        gmail_dialog = GM.return_string_unread()
        return gmail_dialog

    if (sin_code == 2): #Weather Current
        WD  = Accuweather
        weather_current_dialog = WD.return_cuurent_weather()
        return weather_current_dialog


    if (sin_code == 3):
        WD = Accuweather
        weather_forecast_dialog =WD.return_forecast()
        return weather_forecast_dialog


    if (sin_code == 4):
        return "Feature Coming Soon."


    if (sin_code == 5):
        return "Feature Coming Soon."

    if (sin_code == 6):
        AL = Alarms
        return AL.setAlarm(sin_dialog)

    if (sin_code == 7):
        CL = class_data


    if (sin_code == 2):
    if (sin_code == 2):
    if (sin_code == 2):
    if (sin_code == 2):
    if (sin_code == 2):
    if (sin_code == 2):


'''