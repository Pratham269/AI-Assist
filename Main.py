import eel
import os
import pandas 


from Engine.feature import *
from Engine.command import *


eel.init("WWW")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)