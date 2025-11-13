#!/usr/bin/env python

import pygetwindow as gw

if __name__ == "__main__":
    windows = gw.getAllWindows()

    for window in windows:
        print(f"Title: {window.title}, ID: {window._hWnd}")

