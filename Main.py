import os 
import eel
from Engine.feature import *
eel.init("WWW ")

playAssistantSound()

os.system('start msedge.exe --app="http://127.0.0.1:5500/WWW/indiax.html"')

eel.start('index.html', mode=None, host='localhost', block=True)