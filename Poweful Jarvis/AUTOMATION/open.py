import pyautogui as ui
import difflib
import random
import time
import webbrowser

from HEAD.MOUTH import speak
from Data.dlg_data.dlg import *



def appopen(text):
    text = text.replace("open", "")
    text = text.strip()
    random_open_dlg = random.choice(open_dlg)
    speak(random_open_dlg+ text)
    time.sleep(0.5)
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
    random_success = random.choice(success_open)
    speak(random_success)


def openweb(text):

    # Convert the input to lowercase for case-insensitive matching
    website_name_lower = text.lower()

    # Check if the exact website name exists in the dictionary
    if website_name_lower in websites:
        random_open_dlg = random.choice(open_dlg)
        speak(random_open_dlg + text)
        url = websites[website_name_lower]
        webbrowser.open(url)
        random_success = random.choice(success_open)
        speak(random_success)
    else:
        # Find the closest matching website using string similarity
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            print(matches)
            random_dlg = random.choice(open_dlg)
            randonopen2 = random.choice(open_maybe)
            closest_match = matches[0]
            speak(randonopen2 + random_dlg + text)
            url = websites[closest_match]
            webbrowser.open(url)
            randonsuccess = random.choice(success_open)
            speak(randonsuccess)
        else:
            randonsorry = random.choice(sorry_open)
            speak(randonsorry +" named " + text)


def open(text):
    if "website" in text or "site" in text:
        text = text.replace("open", "")
        text = text.replace("website", "")
        text = text.replace("site", "")
        text = text.strip()
        openweb(text)
    elif "app" in text or "application" in text:
        text = text.replace("open", "")
        text = text.replace("app", "")
        text = text.replace("application", "")
        text = text.strip()
        appopen(text)
    else:
        text = text.replace("open", "")
        # text = text.replace("app", "")
        # text = text.replace("application", "")
        text = text.strip()
        appopen(text)


# open("open settings")
