# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cartuiwSSwCQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(352, 63)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 10, 348, 42))
        self.widget.setStyleSheet(u"#lbl_title {\n"
"padding: 0 0 0 3\n"
"}\n"
"#widget {\n"
"border-radius: 10px;\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 361, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.horizontalLayoutWidget)
        self.lbl_title.setObjectName(u"lbl_title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.lbl_title.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_title)

        self.lbl_text_definition = QLabel(self.horizontalLayoutWidget)
        self.lbl_text_definition.setObjectName(u"lbl_text_definition")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_text_definition.sizePolicy().hasHeightForWidth())
        self.lbl_text_definition.setSizePolicy(sizePolicy1)
        self.lbl_text_definition.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lbl_text_definition)

        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(40, 0))
        self.checkBox.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout.addWidget(self.checkBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_title.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_text_definition.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checkBox.setText("")
    # retranslateUi

