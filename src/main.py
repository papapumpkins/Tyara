from GMailAuth import quickstart
from WeatherApps import Accuweather
from TTS import PlaySounds,speech_rec
from DateTime import Present
from resources import *
from Academics import *


#Creating Objects for these classes :
G=quickstart
W=Accuweather
P=PlaySounds
D=Present



#Start with collecting Data
##1. Collect the Weather Data :

weather_condition=W.wc
current_temp = W.ct
max_temp=W.Mt
min_temp=W.mt
headline=W.hl

date = D.returnTodayData()
d1=date[0]
d2=date[1]
d3=date[2]

time=D.returnCurrentTime()
t1=time[0]
t2=time[1]
t3=time[2]

##2. Collect GMail Data:
gmail_unreads=G.doit()  #Integer Value of number of Unread Messages

#33333333333333333333333333333333333333333333333333333333333333333

#Now, send the data for String formation:
speechtext=P.makewords(str(int(current_temp)),str(weather_condition),str(int(max_temp)),str(int(min_temp)),headline,str(gmail_unreads)
                   ,d3,d1,d2,t1,t2)

#Create mp3 of the speech
wavname=P.makemp3(speechtext,"report")

#play the file
P.play(wavname)




#https://accounts.google.com/o/oauth2/token






