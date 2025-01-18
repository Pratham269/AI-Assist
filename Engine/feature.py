import os
import re
import eel
import pywhatkit as kit
from playsound import playsound
from Engine.command import speak
from Engine.config import ASSISTANT_NAME



@eel.expose
def playAssistantSound():
    music_dir = "WWW\\assets\\Audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Invalis command ")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None