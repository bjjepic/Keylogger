from pathlib import Path
from pynput import keyboard
from tkinter import *
import customtkinter

"""
I used, TTinkter Designer and FIGMA to create this GUI for this code, here is the link to the GUI (It may look different to the GUI on the program at the moment, this is due to the fact
I most likely will configure the GUI to be more end user usable :3).

https://www.figma.com/design/owR7KFdx95WTPTqCreb12p/Untitled?node-id=0-1&t=v6NcsSaT1jG9sqie-1

"""

# Explicit imports to satisfy Flake8
"""
Alot of this code unironically, is from the import. Im doing research to understand what frameworks are used and to see if I can add anything to this code using them.
"""

from tkinter import Tk, Canvas, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\bjjep\Downloads\New folder\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize main Tkinter window
window = Tk()
window.geometry("700x400")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=400,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Create the rectangles
canvas.create_rectangle(
    0.0, 4.0, 589.0, 335.0, fill="#303030", outline="")  # Main rectangle
canvas.create_rectangle(
    294.0, 4.0, 589.0, 335.0, fill="#282828", outline="")  # Rectangle 2
canvas.create_rectangle(
    302.0, 16.0, 581.0, 329.0, fill="#202020", outline="")
canvas.create_rectangle(
    0.0, 4.0, 294.0, 41.0, fill="#535353", outline="")  # Rectangle 1


canvas.create_rectangle(
    584.0, 16.0, 587.0, 37.0, fill="#D9D9D9", outline="")

# Text widget for displaying keystroke output
keystroke_output = Text(
    window,
    bg="#202020",
    fg="#FFFFFF",
    wrap=WORD,
    font=("Helvetica", 10),
    relief="flat"
)
keystroke_output.place(x=302, y=16, width=279, height=313)

# Scroll functionality using Rectangle 1
scrollbar = Scrollbar(window, orient=VERTICAL, command=keystroke_output.yview)
keystroke_output.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=581, y=16, height=313)

# Function to capture keystrokes and display them

def keyPressed(key):
    try:
        char = key.char  # Try to get the character of the key pressed
        keystroke_output.insert(END, char)  
        keystroke_output.see(END)  # Auto-scroll to the end
    except AttributeError:
        special_key = f"[{key}]"
        keystroke_output.insert(END, special_key)  # Handle special keys
        keystroke_output.see(END)

if __name__ == "__main__":
    logger = keyboard.Listener(on_press=keyPressed)
    logger.start()

window.resizable(False, False)
window.mainloop()
