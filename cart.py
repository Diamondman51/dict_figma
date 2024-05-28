from PySide6.QtWidgets import QWidget

from cart_ui import Ui_Form


class Cart(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)