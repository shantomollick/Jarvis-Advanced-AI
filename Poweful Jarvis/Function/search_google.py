import pywhatkit

def search_on_google(text):
    text = text.replace("search on google", "")
    text = text.replace("search in google", "")
    pywhatkit.search(text)


