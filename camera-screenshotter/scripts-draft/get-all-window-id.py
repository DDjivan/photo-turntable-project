import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.show()

    # Get the window ID
    window_id = main_window.winId()
    print(f"Window ID: {window_id}")
