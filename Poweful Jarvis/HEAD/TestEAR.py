
# import speech_recognition as sr
# import os
# import threading
# from mtranslate import translate
# from colorama import Fore, Style, init
#
# init(autoreset=True)
#
#
# def print_loop():
#     while True:
#         print(Fore.LIGHTGREEN_EX + "I am listening......", end="", flush=True)
#         print(Style.RESET_ALL, end="", flush=True)
#         print("", end="", flush=True)
#
#
# def Trans_Hindi_to_English(txt):
#     english_txt = translate(txt, to_language="en-in")
#     return english_txt
#
#
# def listen():
#     recognizer = sr.Recognizer()
#
#     # Suggested adjustments
#     recognizer.dynamic_energy_threshold = True  # Adaptive to background noise
#     recognizer.energy_threshold = 30000  # More sensitive to normal speech
#     recognizer.dynamic_energy_adjustment_damping = 0.1  # Faster adaptation to noise
#     recognizer.pause_threshold = 0.8  # Suitable for natural pauses in conversation
#     recognizer.non_speaking_duration = 0.5  # Allows for natural pauses between words
#
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         while True:
#             print(Fore.LIGHTGREEN_EX + "I am listening......", end="", flush=True)
#             try:
#                 audio = recognizer.listen(source)
#                 print("\r" + Fore.LIGHTYELLOW_EX + "Got it, Now Recognizing......")
#                 recognized_txt = recognizer.recognize_google(audio).lower()
#                 if recognized_txt:
#                     translated_txt = Trans_Hindi_to_English(recognized_txt)
#                     print("\r" + Fore.BLUE + "Mr.Shanto: " + translated_txt)
#                     return translated_txt
#                 else:
#                     return ""
#             except sr.UnknownValueError:
#                 recognized_txt = ""
#             finally:
#                 print("\r", end="", flush=True)
#             os.system("cls" if os.name == "nt" else "clear")
#
#             listen_thread = threading.Thread(target=listen)
#             print_thread = threading.Thread(target=print_loop)
#             listen_thread.start()
#             print_thread.start()
#             listen_thread.join()
#             print_thread.join()
#
#
# while True:
#     listen()
