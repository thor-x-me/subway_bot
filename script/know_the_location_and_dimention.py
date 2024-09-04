"""This part of the program will help you set up you environment
1. Place the window of emulator to desired location on the screen.
2. Run this piece of code, it will tell you about the location of it
3. use the dimensions in 1_put_window_to_fixed_location
4. Run that code everytime you want to use your model to fix the window.
5. You need to change the dimension in other files too where screen location and dimension is necessary. """


import pygetwindow as gw

# Find the window by its title
window_title = "MEmu"
window = gw.getWindowsWithTitle(window_title)

# Check if the window is found
if window:
    window = window[0]  # Assuming there's only one window with the given title
    print(window.size)
    print(window.topleft)