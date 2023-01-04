from pygame import mixer
import time
import os

mixer.init() 

mixer.music.load('outro.mp3')

mixer.music.play() 

time.sleep(17)

os.system("shutdown -s -t 0")

mixer.music.stop()