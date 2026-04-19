from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer
from BuildUI import Ui_Dialog
from enum import Enum, auto
from port_scanner import assign_port

UI_SPEED = 200

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
        self.ui.p4_lineEdit.setText(str(self.state))
        match self.state:
            case State.IDLE:
                self.state = State.READ

            case State.READ:
                update = self.get_update()
                if update:
                    print(f"update {update}")
                    self.ui.p1_lineEdit.setText(str(update))


                else:
                    print("No update")
                self.state = State.IDLE

    def get_update(self):

        while not self.incoming_data.empty():
            update = self.incoming_data.get()
            print(update)
            return update