import speech_recognition as sr
import os
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)


def Trans_Hindi_to_English(txt):
    english_txt = translate(txt, to_language="en-in")
    return english_txt


def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = 30000
    recognizer.dynamic_energy_adjustment_damping = 0.1
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.5
    recognizer.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.LIGHTGREEN_EX + "Microphone initialized and adjusted. Awaiting audio input...")

        while True:
            try:
                print(Fore.LIGHTGREEN_EX + "\rI am listening......", end="", flush=True)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("\r" + Fore.LIGHTYELLOW_EX + "Got it, Now Recognizing......", end="", flush=True)

                # Recognizing the audio
                recognized_txt = recognizer.recognize_google(audio).lower()
                print(Style.RESET_ALL, end="", flush=True)

                # Process recognized text
                if recognized_txt:
                    translated_txt = Trans_Hindi_to_English(recognized_txt)
                    print(Fore.BLUE + "Mr.Shanto: " + translated_txt)
                    return translated_txt
                else:
                    print(Fore.RED + "No speech detected, continuing to listen...")
            except sr.UnknownValueError:
                print(Fore.RED + "\rSorry, could not understand the audio. Listening again...", end="", flush=True)
            except sr.RequestError as e:
                print(Fore.RED + f"\rCould not request results; {e}")
            except Exception as e:
                print(Fore.RED + f"\rError occurred: {e}")
            finally:
                os.system("cls" if os.name == "nt" else "clear")


while True:
    listen()