"""This program set the area for the emulator to run in.
It is important as our input neurons need pixels as input in a fixed
number.
number of pixels = width * height"""

import pygetwindow as gw

# Find the window by its title
window_title = "MEmu"
window = gw.getWindowsWithTitle(window_title)

# Check if the window is found
if window:
    window = window[0]  # Assuming there's only one window with the given title
    print(window.size)
    print(window.topleft)

    # Resize the window
    new_width = 600
    new_height = 1035
    window.resizeTo(new_width, new_height)

    # Move the window to a specific location (replace these coordinates with desired values)
    new_x = 1300
    new_y = 0
    window.moveTo(new_x, new_y)
else:
    print(f"Window with title '{window_title}' not found.")
