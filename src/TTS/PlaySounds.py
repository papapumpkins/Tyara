import pygame as pg
from gtts import gTTS


# w1=Current Temperature
# w2=Current Weather Conditions
# g1=Current Unread Messages
# g2=Total Unread Messages
#
spfs="."
sp01 = "Hello There!"
sp02 = "Welcome!"
sp03 = "Good Morning!"
sp04 = "Good Evening!"
sp05 = "Good Night!"
sp06 = "Namastey"
#
sp11 = "It's time to wake up!"
sp12 = "How was your Day?"
sp13 = ""
#
spgmailunread01="You have "
spgmailunread02="unread messages in your primary mail inbox."
spgmailtotal03="The total number of Unread messages is "
#
spcurrtemp01="Accuweather dotcom reports the current temperature around you as "
spcurrtemp02="degrees Celsius, and the weather as "

def makewords(w1,w2,g1):
    final_string = sp03+sp11+spgmailunread01+g1+spgmailunread02+spfs+spcurrtemp01+w1+spcurrtemp02+w2+spfs
    return final_string

def makemp3(words, mp3name, language='en'):
    tts = gTTS(text=words, lang=language)
    tts.save("%s.mp3" % mp3name)
    print("File %s.mp3 Successfully Saved" % mp3name)
    return mp3name


def play(wavname):
    pg.mixer.init(frequency=27050, size=-16, channels=2, buffer=4096)
    clock = pg.time.Clock()
    pg.mixer.music.load('D:\Learning\PYTHON\Tyara\src\%s.mp3'%wavname)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

