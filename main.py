import time

from PySide6.QtWidgets import QApplication

from control import Control

app = QApplication()
controller = Control()
controller.show()
app.exec()
