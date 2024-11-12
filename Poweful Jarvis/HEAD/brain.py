import threading
import sys, time
import webbrowser
import wikipedia
from wikipedia import wikipedia
from HEAD.MOUTH import speak
from Training_Model.model import mind
from colorama import Fore, Style, init

init(autoreset=True)

def print_animated_screen(message, color=Fore.LIGHTMAGENTA_EX, speed=0.075):
    for char in message:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r"C:\Users\win11\Desktop\Poweful Jarvis\Data\brain_data\qna_data.txt"
qa_dict = load_qa_data(qa_file_path)


def save_qa_data(file_path, qa_dict):
    with open(file_path, 'w', encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")


def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "")
    search_prompt = search_prompt.replace("wikipedia", "")
    search_prompt = search_prompt.replace("who is", "")

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=1)
        animate_thread = threading.Thread(target=print_animated_screen, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))
        animate_thread.start()
        speak_thread.start()
        animate_thread.join()
        speak_thread.join()

        # assuring search_prompt is defined somewhere
        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qa_file_path, qa_dict)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is disambiguation page for that given query. Please provide specific information")
        print("There is disambiguation page for that given query. Please provide specific information")
        pass
    except wikipedia.exceptions.PageError as e:
        google_search(prompt)


def google_search(query):
    query = query.replace("who is", "")
    query = query.strip()

    if query:
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)
        speak("You can see search results for "+query+" in Google on your screen, sir")
        print("You can see search results for "+query+" in Google on your screen, sir")
    else:
        speak("I didn't catch what you said please say again, sir")
        print("I didn't catch what you said please say again, sir")

def brain(text):

    try:
        response = mind(text)
        if not response:
            wiki_search(text)
            return

        animate_thread = threading.Thread(target=print_animated_screen, args=(f"Jarvis: {response}",))
        speak_thread = threading.Thread(target=speak, args=(response,))
        animate_thread.start()
        speak_thread.start()
        animate_thread.join()
        speak_thread.join()

        qa_dict[text] = response
        save_qa_data(qa_file_path, qa_dict)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        wiki_search(text)

# speak("Hello sir I am here")
# while True:
#     x = input("enter: ")
#     brain(x)























