import queue
import sys
from dataclasses import dataclass, field
from queue import Queue

from PySide6.QtWidgets import QApplication
from ui_thread import UIThread
from uart_thread import UART_Thread

@dataclass
class SharedData:
    incoming_data_queue: Queue
    outgoing_data_queue: Queue

def main():

    shared_data = SharedData(
        incoming_data_queue=queue.Queue(),
        outgoing_data_queue=queue.Queue())

    app = QApplication(sys.argv)

    serial_thread = UART_Thread(context=shared_data)
    serial_thread.start()

    window = UIThread(context=shared_data)
    window.setWindowTitle("RFID Poker Table Contoller")

    window.show()
    app.exec()

    serial_thread.stop()


if __name__ == '__main__':
    print("Starting main.py")
    main()