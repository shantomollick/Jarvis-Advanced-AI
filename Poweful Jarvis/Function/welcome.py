from HEAD.MOUTH import speak
from Data.dlg_data.dlg import welcome_dlg
import random

def welcome():
    welcome = random.choice(welcome_dlg)
    speak(welcome)


