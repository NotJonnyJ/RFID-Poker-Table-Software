import threading
import time
from dataclasses import dataclass

import serial
from PySide6.QtCore import QThread
from enum import Enum, auto
from port_scanner import assign_port


class State(Enum):
    IDLE = auto()
    TX = auto()
    RX = auto()

class UART_Thread(QThread):
    def __init__(self, context):
        super().__init__()

        self._stop_event = threading.Event()

        self.incoming_data = context.incoming_data_queue
        self.outgoing_data = context.outgoing_data_queue

        self.port = assign_port()

        self.baudrate = 9600


    def run(self):

        state = State.IDLE      # Initial State

        ser = serial.Serial(
            port = self.port,
            baudrate = self.baudrate,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 0.3,
        )

        while not self._stop_event.is_set():


            match state:
                case State.IDLE:
                    self.state = State.RX

                case State.RX:
                    if ser.in_waiting:
                        # data = ser.read(ser.in_waiting)
                        data = ser.read(1)
                        if data[0] == 0xaa:
                            self.incoming_data.put(data)
                        # print(f"data {data}")


                    else:
                        time.sleep(0.01)
                    self.state = State.IDLE






    def stop(self):
        self._stop_event.set()