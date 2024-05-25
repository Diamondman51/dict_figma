from PySide6.QtWidgets import QWidget

from stackedwidget_ui import Ui_Form


class Control(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)