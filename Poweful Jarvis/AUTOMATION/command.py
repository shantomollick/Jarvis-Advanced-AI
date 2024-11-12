import random
from AUTOMATION.open import open
from AUTOMATION.close import close
from AUTOMATION.youtube import youtube_search, play_music_on_youtube
from Function.search_google import search_on_google
from HEAD.EAR import *
from HEAD.brain import *
from Function.welcome import welcome
from Function.wish import wish
from Function.battery import *
from Data.dlg_data.dlg import *
import pyautogui as gui
from Training_Model.test3 import mind


def cmd():
    wish()
    while True:
        text = listen().lower()
        if "hello jarvis" in text:
            welcome()
        elif text in bye_key_word:
            random_by_reply = random.choice(reply_bye)
            speak(random_by_reply)
            break
        elif text.startswith(("open", "khulo", "show me")):
            text.replace("kholo", "")
            text.replace("show me", "")
            text.strip()
            open(text)
        elif text in open_input:
            text.replace("kholo", "")
            text.replace("show me", "")
            text.strip()
            open(text)
        elif "play music on youtube" in text:
            dlg = random.choice(which_one_dlg)
            speak(dlg)
            txt = listen().lower()
            play_music_on_youtube(txt)
        elif "search on google" in text or "search in google" in text:
            search_on_google(text)
        elif "search on youtube" in text or "search in youtube" in text or "search on yt" in text:
            text = text.replace("search on youtube", "")
            text = text.replace("search in youtube", "")
            text = text.replace("search on yt", "")
            youtube_search(text)

        elif "check battery percentage" in text or "battery percentage" in text:
            battery_percentage()
        elif "minimise" in text or "minimise the window" in text:
            speak("minimizing, sir")
            gui.hotkey('win', 'down')
            gui.hotkey('win', 'down')
        elif "write" in text or "lekho" in text:
            speak("writing...")
            text = text.replace("write", "").replace("lekho", "")
            gui.write(text)
        elif "enter" in text or "press enter" in text or "send" in text:
            gui.press("enter")
        elif "select all" in text or "select all paragraph" in text:
            gui.hotkey("ctrl", "a")
        elif "copy" in text or "copy this" in text:
            gui.hotkey("ctrl", "c")
        elif "increase volume" in text:
            speak("Increasing the volume")
            for i in range(5):  # Adjust the range as needed
                gui.press("volumeup")
        elif "decrease volume" in text:
            speak("Decreasing the volume")
            for i in range(5):
                gui.press("volumedown")
        elif "mute" in text:
            speak("Muting the system")
            gui.press("volumemute")
        elif "unmute" in text:
            speak("Unmuting the system")
            gui.press("volumemute")
        elif "open task manager" in text:
            speak("Opening Task Manager, sir")
            gui.hotkey('ctrl', 'shift', 'esc')
        elif "lock the pc" in text:
            speak("Locking the system")
            gui.hotkey('win', 'l')
        elif "switch window" in text or "next window" in text:
            speak("Switching windows")
            gui.hotkey('alt', 'tab')
        elif "take screenshot" in text:
            speak("Taking a screenshot")
            gui.hotkey('win', 'prtsc')
        elif "scroll up" in text:
            gui.scroll(10)
        elif "scroll down" in text:
            gui.scroll(-10)
        elif "open new tab" in text:
            speak("Opening a new tab, sir")
            gui.hotkey('ctrl', 't')
        elif "close tab" in text:
            speak("Closing the current tab")
            gui.hotkey('ctrl', 'w')
        elif "next tab" in text or "switch tab" in text:
            speak("Switching to the next tab")
            gui.hotkey('ctrl', 'tab')
        elif "previous tab" in text:
            speak("Switching to the previous tab")
            gui.hotkey('ctrl', 'shift', 'tab')
        elif "reload tab" in text or "refresh tab" in text:
            speak("Refreshing the current tab")
            gui.hotkey('ctrl', 'r')
        elif "mute tab" in text:
            speak("Muting the current tab")
            gui.hotkey('ctrl', 'm')  # In most browsers, you need an extension for muting tabs
        elif "unmute tab" in text:
            speak("Unmuting the current tab")
            gui.hotkey('ctrl', 'm')
        elif "go to tab" in text:
            tab_number = [int(s) for s in text.split() if s.isdigit()]
            if tab_number:
                speak(f"Switching to tab {tab_number[0]}")
                gui.hotkey('ctrl', str(tab_number[0]))
        elif "scroll up" in text:
            speak("Scrolling up")
            gui.scroll(10)
        elif "scroll down" in text:
            speak("Scrolling down")
            gui.scroll(-10)
        elif "zoom in" in text:
            speak("Zooming in")
            gui.hotkey('ctrl', '+')
        elif "zoom out" in text:
            speak("Zooming out")
            gui.hotkey('ctrl', '-')
        elif "open history" in text:
            speak("Opening browser history")
            gui.hotkey('ctrl', 'h')
        elif "open downloads" in text:
            speak("Opening downloads")
            gui.hotkey('ctrl', 'j')
        elif "maximize window" in text or "maximize" in text:
            speak("Maximizing the window")
            gui.hotkey('win', 'up')
        elif "minimize all" in text or "show desktop" in text:
            speak("Minimizing all windows")
            gui.hotkey('win', 'd')
        elif "restore last window" in text:
            speak("Restoring last minimized window")
            gui.hotkey('win', 'shift', 'm')
        elif "open start menu" in text:
            speak("Opening the start menu")
            gui.press('win')
        elif "new desktop" in text:
            speak("Creating a new virtual desktop")
            gui.hotkey('ctrl', 'win', 'd')
        elif "next desktop" in text:
            speak("Switching to the next desktop")
            gui.hotkey('ctrl', 'win', 'right')
        elif "previous desktop" in text:
            speak("Switching to the previous desktop")
            gui.hotkey('ctrl', 'win', 'left')
        elif "close desktop" in text:
            speak("Closing the current virtual desktop")
            gui.hotkey('ctrl', 'win', 'f4')
        elif "increase brightness" in text:
            speak("Increasing brightness")
            for i in range(5):  # Adjust the range as needed
                gui.hotkey('fn', 'f3')  # Adjust keys based on your keyboard model
        elif "decrease brightness" in text:
            speak("Decreasing brightness")
            for i in range(5):
                gui.hotkey('fn', 'f2')  # Adjust keys based on your keyboard model
        elif "next song" in text or "next track" in text:
            speak("Skipping to the next track")
            gui.press('nexttrack')
        elif "previous song" in text or "previous track" in text:
            speak("Going to the previous track")
            gui.press('prevtrack')
        elif "take full screen screenshot" in text:
            speak("Taking a full-screen screenshot")
            gui.hotkey('win', 'shift', 's')
        elif "open command prompt" in text or "open cmd" in text:
            speak("Opening Command Prompt")
            gui.hotkey('win', 'r')
            gui.write('cmd')
            gui.press('enter')
        elif text.startswith("search"):
            gui.hotkey("/")
            text = text.replace("search", "")
            speak(f"searching {text}")
            gui.write(text)
            time.sleep(0.5)
            gui.press("enter")
        elif text in close_input:
            close()
        else:
            mind(text)