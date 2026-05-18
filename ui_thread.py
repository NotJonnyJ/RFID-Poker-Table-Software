from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer
from BuildUI import Ui_Dialog
from enum import Enum, auto
from port_scanner import assign_port
import pathlib
from pathlib import Path



UI_SPEED = 200


images_path = "cards/"



class State(Enum):
    IDLE = auto()

class State(Enum):
    IDLE = auto()
    READ = auto()



class UIThread(QDialog):
    def __init__(self, context):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.incoming_data = context.incoming_data_queue
        self.outgoing_data = context.outgoing_data_queue

        self.setup_ui_state_machine()
        self.port = assign_port()



    def setup_ui_state_machine(self):
        self.state = State.IDLE
        self.next_state = None

        self.state_timer = QTimer(self)
        self.state_timer.timeout.connect(self.state_machine)
        self.state_timer.start(UI_SPEED)



    def state_machine(self):
        match self.state:
            case State.IDLE:
                self.state = State.READ

            case State.READ:
                update = self.get_update()
                if update:

                    #self.ui.p1_lineEdit.setText(str(update))

                    startByte = update[0]
                    packet_length = update[1]
                    print(f"Start Byte: {startByte}, packet_length: {packet_length}")

                    p1_suit, p1_card = update[2:4]
                    print(f"P1 suit: {hex(p1_suit)}, p1_card: {hex(p1_card)}")

                    p2_suit, p2_card = update[4:6]
                    print(f"P2 suit: {hex(p2_suit)}, p2_card: {hex(p2_card)}")

                    p3_suit, p3_card = update[6:8]
                    print(f"P3 suit: {hex(p3_suit)}, p3_card: {hex(p3_card)}")

                    p4_suit, p4_card = update[8:10]
                    p5_suit, p5_card = update[10:12]
                    p6_suit, p6_card = update[12:14]
                    p7_suit, p7_card = update[14:16]
                    p8_suit, p8_card = update[16:18]
                    p9_suit, p9_card = update[18:20]

                    players = [[p1_suit, p1_card],
                               [p2_suit, p2_card],
                               [p3_suit, p3_card],
                               [p4_suit, p4_card],
                               [p5_suit, p5_card],
                               [p6_suit, p6_card],
                               [p7_suit, p7_card],
                               [p8_suit, p8_card],
                               [p9_suit, p9_card]
                               ]


                    players_cards = []

                    for player in players:
                        if player[0] == 68:  suit_string = "diamonds"
                        elif player[0] == 72: suit_string = "hearts"
                        elif player[0] == 67: suit_string = "clubs"
                        elif player[0] == 83: suit_string = "spades"
                        else:
                            print("Unknown suit: ", hex(player[0]))

                        card_number_raw = player[1] & 0x0F
                        if card_number_raw == 1:
                            card_number_string = "ace"
                        elif card_number_raw == 10:
                            card_number_string = "jack"
                        elif card_number_raw == 11:
                            card_number_string = "queen"
                        elif card_number_raw == 12:
                            card_number_string = "king"
                        else:
                            card_number_string = str(card_number_raw)


                        #print(f"Card Number: {card_number_raw}, Hex: {hex(card_number_raw)}")



                        card_string = f"{card_number_string}_of_{suit_string}.svg"

                        print(f"Card String: {card_string}")
                        players_cards.append(card_string)



                    print(players_cards)
                    p1_map = QPixmap(images_path + players_cards[0])
                    p2_map = QPixmap(images_path + players_cards[1])
                    p3_map = QPixmap(images_path + players_cards[2])
                    p4_map = QPixmap(images_path + players_cards[3])
                    p5_map = QPixmap(images_path + players_cards[4])
                    p6_map = QPixmap(images_path + players_cards[5])
                    p7_map = QPixmap(images_path + players_cards[6])
                    p8_map = QPixmap(images_path + players_cards[7])
                    p9_map = QPixmap(images_path + players_cards[8])


                    self.ui.label_p1.setPixmap(p1_map)
                    self.ui.label_p2.setPixmap(p2_map)
                    self.ui.label_p3.setPixmap(p3_map)
                    self.ui.label_p4.setPixmap(p4_map)
                    self.ui.label_p5.setPixmap(p5_map)
                    self.ui.label_p6.setPixmap(p6_map)
                    self.ui.label_p7.setPixmap(p7_map)
                    self.ui.label_p8.setPixmap(p8_map)
                    self.ui.label_p9.setPixmap(p9_map)










                self.state = State.IDLE

    def get_update(self):

        while not self.incoming_data.empty():
            update = self.incoming_data.get()
            return update