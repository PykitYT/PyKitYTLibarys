# Max image size is 52
# Max text size is 16
import libary
import os
from time import sleep  # Importing the sleep function
from keyboard import add_hotkey, wait  # Importing keyboard functions
SystemExit = False
def kill():
    os.startfile("main.py")
    exit()
# Initialize the a object
a = libary.Paint()
def cler():
    global x, y
    a.map(0, 0)
    a.clear()
    t = a.show()
    t = t.replace("m", " ")
    #t = "Hello, World!"
    #t = "Hello, World!"
    print("\n" * 100 + t)
    print(x, y)
# Starting position
x, y = 0, 0
a.map(x, y)
a.pshow()

def move(dx, dy):
    #try:
    """
    Move the 'p' character on the grid.
    :param dx: Change in the x-coordinate
    :param dy: Change in the y-coordinate
    """
    global x, y
    x += dx
    y += dy
    a.map(x, y)
    t = a.show()
    t = t.replace("m", " ")
    #t = "Hello, World!"
    #t = "Hello, World!"
    print("\n" * 100 + t)
    print(x, y)


def sys():
    try:
        # Assign hotkeys for movement
        add_hotkey("w", lambda: move(0, -1))  # Move up
        add_hotkey("s", lambda: move(0, 1))   # Move down
        add_hotkey("a", lambda: move(-1, 0))  # Move left
        add_hotkey("d", lambda: move(1, 0))   # Move right
        add_hotkey("e", lambda: cler())   # Clear
        add_hotkey("q", lambda: kill())
            # Keep the program running to listen for keyboard inputs
        wait()
    except:
        exit()
sys()


