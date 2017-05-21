import pygame as pg
from gtts import gTTS


# w1=Current Temperature
# w2=Current Weather Conditions
# w3=MAx Temperature of Today
# w4=Min Temperature of Today
# w5=Headline Forecast of Today
# g1=Current Unread Messages
# g2=Total Unread Messages
#
spfs="."
sp01 = "Hello There!"
sp02 = "Welcome!"
sp03 = "Good Morning Neel! "
sp04 = "Good Evening!"
sp05 = "Good Night!"
sp06 = "Namastey"
#
sp11 = "It's time to wakeup!"
sp12 = "How was your Day?"
sp13 = ""
#
spdate01="The calendar reads "
spdate02=" "
sptimenow01="The clock ticks "
sptimenow02="hours and "
sptimenow03 = "minutes. "
spgmailunread01="You have "
spgmailunread02="unread messages in your primary inbox."
spgmailtotal03="The total number of Unread messages is"
#

spcurrtemp01="Accuweather dotcom reports the current temperature around you as: "
spcurrtemp02="degrees Celsius, and the weather as "
sprangetoday01=". The temperature will range from "
sprangetoday02=" to "
sprangetoday03=" degree Celsius. "
spheadlinetoday="You can expect "
def makewords(w1,w2,w3,w4,w5,g1,t0,t1,t2,t3,t4):
    final_string = sp03+sp11+spdate01+t0+":"+t1+spdate02+t2+spfs+sptimenow01+t3+sptimenow02+t4+sptimenow03+spgmailunread01+g1+spgmailunread02+spfs+spcurrtemp01+w1+spcurrtemp02+w2+\
                   spfs+sprangetoday01+w3+sprangetoday02+w4+sprangetoday03+spheadlinetoday+w5+spfs
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

