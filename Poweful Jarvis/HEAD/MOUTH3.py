import pyttsx3




def speak(text):
    engine = pyttsx3.init('sapi5')
    # pitch = 150
    rate = 200
    volume = 2
    voice_id = engine.getProperty("voices")

    if voice_id:
        voices = engine.getProperty("voices")
        print(voices)
        try:
            engine.setProperty('voice', voices[1].id)
        except IndexError:
            print("voice id not found")


    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    # engine.setProperty('pitch', pitch)

    engine.say(text)
    engine.runAndWait()


# while True:
#     x = listen()
#     speak(x)

# speak("hello sir, how are you can you tell me")