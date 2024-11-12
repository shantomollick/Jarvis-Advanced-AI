import psutil
import time
from HEAD.MOUTH import speak
from Data.dlg_data.dlg import lower_b, lower_10, battery_100, plugged_in_dlg, plugged_out_dlg
import random

def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_dlg = random.choice(lower_b)
            speak(random_dlg)

        elif percent < 10:
            random_dlg = random.choice(lower_10)
            speak(random_dlg)

        elif percent == 100:
            random_dlg = random.choice(battery_100)
            speak(random_dlg)

        else:
            battery_percentage()

        time.sleep(1500)

def battery_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    speak(f"Your device is running on {percent} percent power, Sir.")

def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                random_dlg = random.choice(plugged_in_dlg)
                speak(random_dlg)
            else:
                random_dlg = random.choice(plugged_out_dlg)
                speak(random_dlg)

            previous_state = battery.power_plugged

        time.sleep(1)

