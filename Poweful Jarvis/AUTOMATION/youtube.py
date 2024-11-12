import random
import time
import webbrowser
import pyautogui as gui
import pywhatkit as kt
from Data.dlg_data.dlg import yt_search_query, success_open, yt_query, playin_yt_dlg
from HEAD.MOUTH import speak


def youtube_search(text):
    dlg = random.choice(yt_search_query)
    speak(dlg)
    webbrowser.open("https://www.youtube.com/")
    time.sleep(3)
    gui.press("/")
    gui.write(text)
    dlg2 = random.choice(yt_query)
    speak(dlg2)
    time.sleep(0.5)
    gui.press("enter")
    dlg2 = random.choice(success_open)
    speak(dlg2)



def play_music_on_youtube(text):
    dlg = random.choice(playin_yt_dlg)
    speak(dlg)
    kt.playonyt(text)
    time.sleep(3)
    speak("playin.....")



