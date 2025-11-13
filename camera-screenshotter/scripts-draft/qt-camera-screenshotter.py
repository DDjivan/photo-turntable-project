#!/usr/bin/env python

# pip install Pillow PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QScreen
from PyQt5.QtCore import QRect

def take_screenshot(window_id):
    app = QApplication(sys.argv)
    screen = app.primaryScreen()

    # Get the geometry of the window
    window = app.findChild(QMainWindow, window_id)
    if window:
        geometry = window.geometry()
        screenshot = screen.grabWindow(window.winId(), geometry.x(), geometry.y(), geometry.width(), geometry.height())
        screenshot.save('screenshot.png', 'png')
    else:
        print("Window not found.")

if __name__ == "__main__":
    take_screenshot("0x05800004")