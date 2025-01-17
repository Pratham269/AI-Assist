from playsound import playsound
import eel

@eel.expose
def playAssistantSound():
    music_dir = "WWW\\assets\\Audio\\start_sound.mp3"
    playsound(music_dir)