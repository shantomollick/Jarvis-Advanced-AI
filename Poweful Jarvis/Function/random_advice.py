import random
import time
import requests
from HEAD.MOUTH import speak
from HEAD.EAR import listen


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def advice():
    # x = [13, 15, 18]
    x = [293, 9238, 23, 927, 232, 834, 298, 823, 723, 723, 623, 902]
    x = random.choice(x)
    time.sleep(x)
    speak("I have some suggestion for you, sir")
    text = listen().lower()
    if "yes tell me" in text or "yes" in text:
        advice = get_random_advice()
        speak(advice)

