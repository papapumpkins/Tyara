import time

from SpeechRecog import transcribe, SpeechLock
from RecordSound import record
from Speech_Interpreter import Text_Interpreter
from GMailAuth import gmailpick
from AlarmsAndReminders import Alarms


from WeatherApps import Accuweather
from TTS import PlaySounds,speech_rec
from DateTime import Present
from resources import *
from Academics import class_data

lock_status = 0
first_command =1




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



    if (sin_code == 11):
        #Authenticate & unlock Device
        return("Speech Recognition has been unlocked. Welcome! ")

    if (sin_code==-1):
        listen_now()
        return "Oops! I didn't get that. Please try speaking clearer & louder."


        '''
    if (sin_code == 12): 
    #For Emergency
'''

def listen_now():
    TSpeak = PlaySounds
    if(first_command==1):
        TSpeak.tyaraSpeaks("Hi Neel! What can I do for You?", "hello")

    else:
        TSpeak.tyaraSpeaks("Can I do anything else for you ? ")

    Rec = record
    Rec.record_from_mic(5)
    #time.sleep(5.5)

    TR = transcribe
    Transcripted_Text = TR.transcribe_file("output.flac")

    SIN = Text_Interpreter
    sin_code = SIN.Interpret_Text(Transcripted_Text)

    if(sin_code==0):
        TSpeak.tyaraSpeaks("Goodbye!","bye")
        exit()

    else:
        sin_dialog = Transcripted_Text
        speech_string = perform_action_with_code(sin_code, sin_dialog)
        TSpeak.tyaraSpeaks(speech_string)

    listen_now()



listen_now()
