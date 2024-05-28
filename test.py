# from PySide6.QtCore import QPoint
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QToolTip
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         vbox = QVBoxLayout()
#
#         btn = QPushButton('Button')
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.clicked.connect(self.showToolTip)
#
#         vbox.addWidget(btn)
#         self.setLayout(vbox)
#
#         self.setWindowTitle('Tooltip')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#     def showToolTip(self):
#         QToolTip.showText(self.mapToGlobal(self.sender().pos() + QPoint(80, 30)), 'Copied to clipboard')
#         print(self.pos())
#
# if __name__ == '__main__':
#     app = QApplication([])
#     ex = Example()
#     app.exec()

