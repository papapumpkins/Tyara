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


def makemp3(words, mp3name, language='hi'):
    tts = gTTS(text=words, lang=language)
    tts.save("%s.flac" % mp3name)
    print("File %s.flac Successfully Saved" % mp3name)
    return mp3name


def play(wavname):
    pg.mixer.init(frequency=21050, size=-16, channels=2, buffer=4096)
    clock = pg.time.Clock()
    pg.mixer.music.load('D:\Learning\PYTHON\Tyara\src\WavRes\%s.flac'%wavname)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

bol = ""
mpn =makemp3(bol,'111')
play(mpn)