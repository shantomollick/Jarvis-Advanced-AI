import threading
import edge_tts
from Function.remove_file import remove_file
from Function.play_file import play_audio
from Function.print_animated_screen import print_animated_screen

VOICE = "en-AU-WilliamNeural"
BUFFERSIZE = 1024


async def amain(TEXT, output_file) -> None:
    try:
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread2 = threading.Thread(target=print_animated_screen, args=(TEXT,))
        thread.start()
        thread2.start()
        thread.join()
        thread2.join()
    except Exception as e:
        print(f"voice exception error: {e}")
    finally:
        remove_file(output_file)