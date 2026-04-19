import sys
from PySide6.QtWidgets import QApplication
from ui_thread import UIThread

def main():
    app = QApplication(sys.argv)


    window = UIThread()
    window.setWindowTitle("RFID Poker Table Contoller")

    window.show()
    app.exec()


if __name__ == '__main__':
    print("Starting main.py")
    main()