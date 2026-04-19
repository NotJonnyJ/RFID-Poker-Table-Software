from asyncio import Event

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

        self.stop = Event()
        self.stop.clear()

        self.incoming_data = context.incoming_data_queue
        self.outgoing_data = context.outgoing_data_queue

        self.port = assign_port()

        self.baudrate = 9600


        self.run()


    def run(self):

        state = State.IDLE      # Initial State

        ser = serial.Serial(
            port = self.port,
            baudrate = self.baudrate,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1,
        )

        while not self.stop.is_set():
            match state:
                case State.IDLE:
                    self.state = State.RX

                case State.RX:

                    if ser.in_waiting:
                        message = ser.read()
                        self.incoming_data.put(message)
                    

                    self.state = State.IDLE






    def stop(self):
        self.stop.set()