import asyncio
import os
from Function.make_voice import amain




def speak(TEXT, output_file = None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"

        asyncio.run(amain(TEXT, output_file))

        # print("done")


