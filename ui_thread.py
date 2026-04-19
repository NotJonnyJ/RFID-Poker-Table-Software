from PySide6.QtWidgets import QDialog
from BuildUI import Ui_Dialog


class UIThread(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
