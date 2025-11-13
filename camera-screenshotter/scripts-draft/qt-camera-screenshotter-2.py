#!/usr/bin/env python

# chmod +x *.py

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QScreen, QPixmap
import subprocess

def get_window_id(title):
    # Use wmctrl to find the window ID by its title
    result = subprocess.run(['wmctrl', '-l'], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if title in line:
            return line.split()[0]  # Return the first element (the ID)
    return None

def take_screenshot(window_id):
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    # Use window ID to grab the window
    xwin_id = int(window_id, 16)
    screenshot = screen.grabWindow(xwin_id)

    print(screenshot.isNull())

    if screenshot.isNull():
        print("Failed to capture the screenshot.")
        return

    saved = screenshot.save('screenshot.png', 'PNG')
    print(saved)
    if saved:
        print("Screenshot saved as 'screenshot.png'.")
    else:
        print("Failed to save the screenshot.")

if __name__ == "__main__":
    window_title = "Obsidian" # !!!
    window_id = get_window_id(window_title)

    if not window_id:
        print("Window not found.")
    else:
        take_screenshot(window_id)


