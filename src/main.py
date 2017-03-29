from Authorizations import quickstart
from WeatherApps import Accuweather
from TTS import PlaySounds,speech_rec
from resources import *
from Academics import *


#Creating Objects for these classes :
G=quickstart
W=Accuweather
P=PlaySounds


#Start with collecting Data
##1. Collect the Weather Data :
weather_condition=W.wc
current_temp = W.ct

##2. Collect GMail Data:
gmail_unreads=G.doit()  #Integer Value of number of Unread Messages

#333333333333333333333333333333333333333333333333333333333333333333333

#Now, send the data for String formation:
speechtext=P.makewords(str(int(current_temp)),str(weather_condition),str(gmail_unreads))
#Create mp3 of the speech
wavname=P.makemp3(speechtext,"report")

#play the file
P.play(wavname)












