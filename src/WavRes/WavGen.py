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


def makemp3(words, mp3name, language='en'):
    tts = gTTS(text=words, lang=language)
    tts.save("%s.mp3" % mp3name)
    print("File %s.mp3 Successfully Saved" % mp3name)
    return mp3name


def play(wavname):
    pg.mixer.init(frequency=21050, size=-16, channels=1, buffer=4096)
    clock = pg.time.Clock()
    pg.mixer.music.load('D:\Learning\PYTHON\Tyara\src\WavRes\%s.mp3'%wavname)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
