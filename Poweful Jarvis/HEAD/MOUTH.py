import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Function.print_animated_screen import print_animated_screen

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_driver_path = r"C:\Users\win11\Desktop\Poweful Jarvis\Data\driver\chromedriver.exe"

chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://tts.5e7en.me/")

def speak_base(text):
    element_to_click = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
    )

    element_to_click.click()

    text_to_input = text
    element_to_click.send_keys(text_to_input)

    sleep_duration = min(0.3 + len(text) // 150, 150)

    button_to_click = WebDriverWait(driver, 3,).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
    )

    button_to_click.click()
    time.sleep(sleep_duration)

    element_to_click.clear()



def speak(text):
    x = threading.Thread(target=speak_base, args=(text,))
    y = threading.Thread(target=print_animated_screen, args=(text,))
    x.start()
    y.start()
    x.join()
    y.join()




