import eel
import os
from Engine.feature import *
from Engine.command import *
from Engine.auth import recoganize

def start():

    eel.init("WWW")
    
    playAssistantSound()
    @eel.expose
    def init():
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            speak("Face Authentication Successful")
        else:
            speak("Face Authentication Fail")


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)