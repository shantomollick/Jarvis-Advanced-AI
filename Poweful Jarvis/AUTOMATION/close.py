import random
import pyautogui as ui
from Data.dlg_data.dlg import closedlg
from HEAD.MOUTH import speak

def close():
    randon_close_dlg = random.choice(closedlg)
    speak(randon_close_dlg)
    ui.hotkey("alt","f4")