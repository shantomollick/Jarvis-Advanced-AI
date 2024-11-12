import random
from HEAD.brain import *
from AUTOMATION.command import cmd
from Function.check_online_offline import is_online
from Data.dlg_data.dlg import *
from Function.random_advice import advice
from Function.battery import battery_alert, check_plugin_status
from FRIDAY.FSpeak import fspeak




def jarvis():
    cmd_thread = threading.Thread(target=cmd)
    advice_thread = threading.Thread(target=advice)
    # battery_thread = threading.Thread(target=battery_alert)
    plugin_thread = threading.Thread(target=check_plugin_status)
    cmd_thread.start()
    advice_thread.start()
    # battery_thread.start()
    plugin_thread.start()
    cmd_thread.join()
    advice_thread.join()
    # battery_thread.join()
    plugin_thread.join()

def check_jarvis():
    if is_online():
        # x = random.choice(online_dlg)
        # fspeak(x)
        jarvis()
    else:
        x = random.choice(ofline_dlg)
        fspeak(x)

check_jarvis()