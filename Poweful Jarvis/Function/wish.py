from datetime import date
import datetime
import random

from Data.dlg_data.dlg import *
from HEAD.MOUTH import speak
from HEAD.brain import print_animated_screen

today = date.today()
formated_time = today.strftime("%d %b %y")
nowx = datetime.datetime.now()


def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gm_dlg = random.choice(good_morning_dlg)
        speak(gm_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoon_dlg)
        speak(ga_dlg)
    elif 17 <= current_hour < 22:
        ge_dlg = random.choice(good_evening_dlg)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_night_dlg)
        speak(gn_dlg)

















