import os

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
