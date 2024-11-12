import asyncio
import threading
import os, sys, time
import edge_tts
import pygame

VOICE = "en-US-JennyNeural"
BUFFERSIZE = 1024


def print_animated_screen(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print()


def remove_file(file_path):
    max_attemts = 3
    attemts = 0
    while attemts < max_attemts:
        try:
            with open(file_path, 'wb'):
                pass
            os.remove(file_path)
            break
        except Exception as e:
            print(f"error: {e}")
            attemts += 1

async def amain(TEXT, output_file) -> None:
    try:
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        print(f"error: {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        pygame.init()
        sound = pygame.mixer.Sound(file_path)
        pygame.mixer.init()
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
        pygame.quit()
    except Exception as e:
        print(f"error: {e}")

def speak1(TEXT, output_file = None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
        asyncio.run(amain(TEXT, output_file))
        # print("done")


def jspeak(text):
    t1 = threading.Thread(target=speak1, args=(text,))
    t2 = threading.Thread(target=print_animated_screen, args=(text,))
    t1.start()
    # time.sleep(1.3)
    t2.start()
    t1.join()
    t2.join()



jspeak("Hello sir i love you if you love me then say yes please then and i will be very happy")
