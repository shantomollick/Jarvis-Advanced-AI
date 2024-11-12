import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def print_animated_screen(message, color=Fore.LIGHTMAGENTA_EX, speed=0.075):
    for char in message:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(speed)
    print()
