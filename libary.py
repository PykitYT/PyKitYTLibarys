from random import *

class Paint:
    def __init__(self):
        # Default state of the paint object
        self.now = """
mmmmmmmmmmmmmmmmmmmmmmm
mmmmmmmmmmmmmmmmmmmmmmm
mmmmmmmmmmmmmmmmmmmmmmm
mmmmmmmmmmmmmmmmmmmmmmm
"""

    def text(self, text):
        """
        Replaces spaces in the input text with '=' and ensures
        the text fits within the max_length constraint.
        """
        text = text.replace(" ", "=")
        max_length = 16
        if len(text) > max_length:
            raise ValueError("Text too long. Maximum length is 16.")
        # Pad the text with '=' if it's shorter
        padded_text = text.ljust(max_length, "=")
        self.now = f"""
================
{padded_text}
================
"""

    def paint(self, image):
        """
        Updates the `self.now` attribute with a custom image.
        The image must not exceed 52 characters in length.
        """
        if len(image) > 52:
            raise ValueError("Image too large. Maximum length is 52.")
        # Overwrite the `now` content
        self.now = image
    def clear(self):
        self.now = "\n"
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
        return "\n" * 100 + t
        #print("\n" * 100 + t)
        #print(x, y)
    def map(self, x, y):
        while True:
            # Split `self.now` into lines
            lines = self.now.strip().splitlines()

            # Check if the coordinates are valid
            if 0 <= y < len(lines) and 0 <= x < len(lines[0]):
                # Modify the character at the specified position
                lines[y] = lines[y][:x] + "p" + lines[y][x + 1:]
                
                # Rejoin lines
                self.now = "\n".join(lines)
                break  # Exit the loop if the coordinates are valid
            else:
                #print(f"Error in {(x, y)}: Invalid coordinates.")
                # Stay in place without modifying the grid, asking again for valid coordinates
                # Optionally, you can ask for new input or just exit the loop to retry
                return  # Or continue the loop for retry



    def show(self):
        """Returns the current state of the paint object."""
        return self.now

    def pshow(self):
        """Prints the current state of the paint object."""
        print(self.now)
    def start_loop(self, name):
        while True:
            # Use globals() to fetch the function name and call it
            if name in globals() and callable(globals()[name]):
                globals()[name]()  # Call the function dynamically
            else:
                print(f"Function {name} not found.")
                break
