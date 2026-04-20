import threading
import time
from array import array
from collections import deque
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

        self.rx_buffer = bytearray()
        self.start_byte_found = False
        self.packet_size = 9



    def run(self):

        self.state = State.IDLE      # Initial State

        ser = serial.Serial(
            port = self.port,
            baudrate = self.baudrate,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 0.3,
        )

        while not self._stop_event.is_set():


            match self.state:
                case State.IDLE:
                    self.state = State.RX

                case State.RX:

                    if ser.in_waiting:
                        # data = ser.read(ser.in_waiting)
                        byte = ser.read(1)
                        if byte == b"\x01":
                            self.start_byte_found = True

                        if self.start_byte_found:
                            self.rx_buffer += byte

                            if len(self.rx_buffer) >= self.packet_size:
                                packet = self.rx_buffer[:self.packet_size]
                                self.rx_buffer = self.rx_buffer[self.packet_size:]

                                self.handle_packet(packet)

                    else:
                        time.sleep(0.01)
                    self.state = State.IDLE

    def handle_packet(self, packet: bytes):


        self.incoming_data.put(packet)
        self.start_byte_found = False



    def stop(self):
        self._stop_event.set()