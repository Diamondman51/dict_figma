import time

from PySide6.QtWidgets import QApplication

from control import Control

app = QApplicatiqon()
controller = Control()
controller.show()
app.exec()
