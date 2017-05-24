import time
import os

from src.SpeechRecog import transcribe, SpeechLock
from src.RecordSound import record
from src.Speech_Interpreter import Text_Interpreter
from src.GMailAuth import gmailpick
from src.Calendars import calendar_data
import src.UberBook



from src.WeatherApps import Accuweather
from src.TTS import PlaySounds,speech_rec
from src.DateTime import Present
from src.resources import *
from src.Academics import class_data

lock_status = 0
audio_count = 0


def perform_action_with_code(sin_code,sin_dialog):
    #print(sin_code)
    first_command=0

    if(sin_code==0):
        return("Ok. See you later!")

    if(sin_code==1):
        GM = gmailpick
        gmail_dialog = GM.return_string_unread()
        return gmail_dialog

    if (sin_code == 2): #Weather Current
        WD  = Accuweather
        weather_current_dialog = WD.return_current_weather()
        return weather_current_dialog


    if (sin_code == 3):
        WD = Accuweather
        weather_forecast_dialog =WD.return_forecast()
        return weather_forecast_dialog


    if (sin_code == 4):
        UB = src.UberBook
        return UB.book_ride(1)


    if (sin_code == 5):
        return ("Feature Coming Soon.")

    if (sin_code == 6):
        AL = calendar_data
        return AL.setAlarm(sin_dialog)

    if (sin_code == 7):
        CL = class_data
        return (sin_dialog)

    if (sin_code == 8):
        DT = Present
        date_today_dialog=DT.returnTodayData()
        return date_today_dialog

    if (sin_code == 9):
        DT = Present
        time_now_dialog = DT.returnCurrentTime()
        return time_now_dialog

    if (sin_code == 10):
        #initiate SR lock
        #If command says " Lock Speech", then lock the function unless an unlock isn't initiated
        SL = SpeechLock
        lock_status=1
        return("Speech Recognition has been Locked.")
        #This will be used only for streaming speech.

    if (sin_code == 11):
        #Authenticate & unlock Device
        return("Speech Recognition has been unlocked. Welcome! ")
        #This will be used only for streaming speech.

    if (sin_code==12):
        return "exit"

    if (sin_code==-1):
        return "Oops! I didn't get that. Please try speaking clearer & louder."

Rec = record
TR = transcribe
SIN = Text_Interpreter


def listen_now():
    TSpeak = PlaySounds
    global audio_count
    prev_audio_filename = "speaker" + str(audio_count)+".mp3"

    if(audio_count==0):
        TSpeak.tyaraSpeaks("Hi ! What can I do for You?", "hello")
        audio_count = audio_count+1

    elif(audio_count>0):
        TSpeak.tyaraSpeaks("Can I do anything else for you ? ")
        audio_count = audio_count + 1
        os.remove(prev_audio_filename)
    else:
        TSpeak.tyaraSpeaks("Uff! I feel Sick. Bye. ")
        os.remove(prev_audio_filename)
        exit(0)


    Rec.record_from_mic(5)
    #time.sleep(5.5)

    Transcripted_Text = TR.transcribe_file("output.flac")

    sin_code = SIN.Interpret_Text(Transcripted_Text)

    if(sin_code==0|sin_code==-1):
        TSpeak.tyaraSpeaks("Goodbye!","bye")
        exit()

    else:
        sin_dialog = Transcripted_Text
        speech_string = perform_action_with_code(sin_code, sin_dialog)
        audio_filename = "speaker"+str(audio_count)
        TSpeak.tyaraSpeaks(speech_string,audio_filename)


    listen_now()


listen_now()
