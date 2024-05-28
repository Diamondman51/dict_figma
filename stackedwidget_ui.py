# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stacked_UIGgDIcn.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(390, 683)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(390, 683))
        Form.setMaximumSize(QSize(390, 683))
        Form.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 390, 683))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(14, 683))
        self.stackedWidget.setMaximumSize(QSize(16777215, 644))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 210, 160, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"pictures/Group 1.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"pictures/Dicty.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(0, 642))
        self.page_2.setStyleSheet(u"QLabel {\n"
"padding: 0 0 5 0;\n"
"}\n"
"\n"
"#lbl_search {\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"#page_2_line_edit{\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"border:rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"padding: 0 0 0 10\n"
"}\n"
"\n"
"#page_2_btn_voice {\n"
"border:rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"#widget_word {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"border-radius: 10px;\n"
"}\n"
"#page_2_plainTextEdit_definition {\n"
"background-color: rgba(171, 171, 171, 0);\n"
"border:rgba(255, 255, 255, 0);\n"
"}")
        self.page_2_btn_voice = QToolButton(self.page_2)
        self.page_2_btn_voice.setObjectName(u"page_2_btn_voice")
        self.page_2_btn_voice.setGeometry(QRect(320, 100, 30, 22))
        icon = QIcon()
        icon.addFile(u"pictures/voice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_2_btn_voice.setIcon(icon)
        self.horizontalLayoutWidget_2 = QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-10, -10, 411, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_search = QLabel(self.horizontalLayoutWidget_2)
        self.lbl_search.setObjectName(u"lbl_search")
        self.lbl_search.setMaximumSize(QSize(410, 16777215))
        self.lbl_search.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.lbl_search)

        self.widget_word = QWidget(self.page_2)
        self.widget_word.setObjectName(u"widget_word")
        self.widget_word.setGeometry(QRect(20, 160, 348, 242))
        self.page_2_label_title = QLabel(self.widget_word)
        self.page_2_label_title.setObjectName(u"page_2_label_title")
        self.page_2_label_title.setGeometry(QRect(80, 25, 190, 51))
        font = QFont()
        font.setPointSize(25)
        self.page_2_label_title.setFont(font)
        self.page_2_label_title.setAlignment(Qt.AlignCenter)
        self.page_2_plainTextEdit_definition = QPlainTextEdit(self.widget_word)
        self.page_2_plainTextEdit_definition.setObjectName(u"page_2_plainTextEdit_definition")
        self.page_2_plainTextEdit_definition.setGeometry(QRect(20, 90, 311, 141))
        font1 = QFont()
        font1.setPointSize(9)
        self.page_2_plainTextEdit_definition.setFont(font1)
        self.page_2_plainTextEdit_definition.setReadOnly(True)
        self.page_2_line_edit = QLineEdit(self.page_2)
        self.page_2_line_edit.setObjectName(u"page_2_line_edit")
        self.page_2_line_edit.setGeometry(QRect(20, 90, 348, 42))
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 605, 389, 78))
        self.widget.setStyleSheet(u"QPushButton {\n"
"  background-color: black;\n"
"  selection-color: yellow;\n"
"  selection-background-color: black;\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"  color:white;\n"
"  font-weight: 700;\n"
"  margin: 0 0 0 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: rgba(255, 255, 255, 0);\n"
"padding: 0 0 10 0;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"  margin: 0 1 0 1;\n"
"}\n"
"")
        self.horizontalLayoutWidget_3 = QWidget(self.widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(-1, 0, 391, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_2_btn_home = QPushButton(self.horizontalLayoutWidget_3)
        self.page_2_btn_home.setObjectName(u"page_2_btn_home")
        self.page_2_btn_home.setMaximumSize(QSize(16777215, 80))
        icon1 = QIcon()
        icon1.addFile(u"pictures/home_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_2_btn_home.setIcon(icon1)
        self.page_2_btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.page_2_btn_home)

        self.page_2_btn_saved = QPushButton(self.horizontalLayoutWidget_3)
        self.page_2_btn_saved.setObjectName(u"page_2_btn_saved")
        self.page_2_btn_saved.setMaximumSize(QSize(16777215, 80))
        icon2 = QIcon()
        icon2.addFile(u"pictures/saved.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_2_btn_saved.setIcon(icon2)
        self.page_2_btn_saved.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.page_2_btn_saved)

        self.page_2_btn_settings = QPushButton(self.horizontalLayoutWidget_3)
        self.page_2_btn_settings.setObjectName(u"page_2_btn_settings")
        self.page_2_btn_settings.setMaximumSize(QSize(16777215, 80))
        icon3 = QIcon()
        icon3.addFile(u"pictures/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_2_btn_settings.setIcon(icon3)
        self.page_2_btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.page_2_btn_settings)

        self.stackedWidget.addWidget(self.page_2)
        self.page_2_line_edit.raise_()
        self.page_2_btn_voice.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.widget_word.raise_()
        self.widget.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QLabel {\n"
"padding: 0 0 5 0;\n"
"}\n"
"\n"
"#lbl_search_5 {\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: rgba(255, 255, 255, 0);\n"
"padding: 0 0 10 0;\n"
"}\n"
"\n"
"#page_3_line_edit{\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"border:rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"padding: 0 0 0 10\n"
"}\n"
"\n"
"#page_3_btn_voice {\n"
"border:rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"#widget_word_3 {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QListView {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: rgba(255, 255, 255, 0);\n"
"}")
        self.page_3_btn_voice = QToolButton(self.page_3)
        self.page_3_btn_voice.setObjectName(u"page_3_btn_voice")
        self.page_3_btn_voice.setGeometry(QRect(320, 100, 30, 22))
        self.page_3_btn_voice.setIcon(icon)
        self.horizontalLayoutWidget_9 = QWidget(self.page_3)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(-10, -10, 411, 81))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_search_5 = QLabel(self.horizontalLayoutWidget_9)
        self.lbl_search_5.setObjectName(u"lbl_search_5")
        self.lbl_search_5.setMaximumSize(QSize(410, 16777215))
        self.lbl_search_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_11.addWidget(self.lbl_search_5)

        self.listWidget = QListWidget(self.page_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 160, 352, 461))
        self.widget_3 = QWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 605, 390, 78))
        self.widget_3.setStyleSheet(u"QPushButton {\n"
"  background-color: black;\n"
"  selection-color: yellow;\n"
"  selection-background-color: black;\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"  color:white;\n"
"  font-weight: 700;\n"
"  margin: 0 0 0 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: rgba(255, 255, 255, 0);\n"
"padding: 0 0 10 0;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"  margin: 0 1 0 1;\n"
"}\n"
"\n"
"")
        self.horizontalLayoutWidget_8 = QWidget(self.widget_3)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(-1, 0, 391, 80))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.page_3_btn_home = QPushButton(self.horizontalLayoutWidget_8)
        self.page_3_btn_home.setObjectName(u"page_3_btn_home")
        self.page_3_btn_home.setMaximumSize(QSize(16777215, 80))
        icon4 = QIcon()
        icon4.addFile(u"pictures/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_3_btn_home.setIcon(icon4)
        self.page_3_btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.page_3_btn_home)

        self.page_3_btn_saved = QPushButton(self.horizontalLayoutWidget_8)
        self.page_3_btn_saved.setObjectName(u"page_3_btn_saved")
        self.page_3_btn_saved.setMaximumSize(QSize(16777215, 80))
        icon5 = QIcon()
        icon5.addFile(u"pictures/saved_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_3_btn_saved.setIcon(icon5)
        self.page_3_btn_saved.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.page_3_btn_saved)

        self.page_3_btn_settings = QPushButton(self.horizontalLayoutWidget_8)
        self.page_3_btn_settings.setObjectName(u"page_3_btn_settings")
        self.page_3_btn_settings.setMaximumSize(QSize(16777215, 80))
        self.page_3_btn_settings.setIcon(icon3)
        self.page_3_btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.page_3_btn_settings)

        self.page_3_line_edit = QLineEdit(self.page_3)
        self.page_3_line_edit.setObjectName(u"page_3_line_edit")
        self.page_3_line_edit.setGeometry(QRect(20, 90, 348, 42))
        self.stackedWidget.addWidget(self.page_3)
        self.page_3_line_edit.raise_()
        self.listWidget.raise_()
        self.page_3_btn_voice.raise_()
        self.horizontalLayoutWidget_9.raise_()
        self.widget_3.raise_()
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"#widget_4 {\n"
"background-color: rgba(206, 206, 206, 0.5);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#widget_5 {\n"
"background-color: rgba(206, 206, 206, 0.5);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#widget_6 {\n"
"background-color: rgba(206, 206, 206, 0.5);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#widget_7 {\n"
"background-color: rgba(206, 206, 206, 0.5);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"border: rgba(255, 255, 255, 0);\n"
"padding: 0 0 10 0;\n"
"}\n"
"\n"
"#page_4_btn_ads {\n"
"\n"
"  selection-color: yellow;\n"
"  selection-background-color: black;\n"
"  border-radius: 5px;\n"
"  color:white;\n"
"  font-weight: 700;\n"
"  margin: 0 0 0 0;\n"
"}\n"
"\n"
"#page_4_btn_ads:pressed { \n"
"  margin: 0 3 0 3;\n"
"}\n"
"\n"
"\n"
"#lbl_search_4 {\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"font-size: 20px;\n"
"padding: 0 0 5 0\n"
"}")
        self.horizontalLayoutWidget_6 = QWidget(self.page_4)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(-10, -10, 411, 81))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lbl_search_4 = QLabel(self.horizontalLayoutWidget_6)
        self.lbl_search_4.setObjectName(u"lbl_search_4")
        self.lbl_search_4.setMaximumSize(QSize(410, 16777215))
        self.lbl_search_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_10.addWidget(self.lbl_search_4)

        self.verticalLayoutWidget_2 = QWidget(self.page_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 90, 351, 251))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.verticalLayoutWidget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 12, 180, 30))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_3.setFont(font2)
        self.page_4_btn_show_suggestions = QPushButton(self.widget_7)
        self.page_4_btn_show_suggestions.setObjectName(u"page_4_btn_show_suggestions")
        self.page_4_btn_show_suggestions.setGeometry(QRect(284, 20, 61, 30))
        icon6 = QIcon()
        icon6.addFile(u"pictures/Toggle_Off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_4_btn_show_suggestions.setIcon(icon6)
        self.page_4_btn_show_suggestions.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.verticalLayoutWidget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(15, 12, 150, 30))
        self.label_4.setFont(font2)
        self.page_4_btn_show_keyboard = QPushButton(self.widget_6)
        self.page_4_btn_show_keyboard.setObjectName(u"page_4_btn_show_keyboard")
        self.page_4_btn_show_keyboard.setGeometry(QRect(284, 20, 61, 30))
        self.page_4_btn_show_keyboard.setIcon(icon6)
        self.page_4_btn_show_keyboard.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_4 = QWidget(self.verticalLayoutWidget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(15, 12, 150, 30))
        self.label_5.setFont(font2)
        self.page_4_btn_ads = QPushButton(self.widget_4)
        self.page_4_btn_ads.setObjectName(u"page_4_btn_ads")
        self.page_4_btn_ads.setGeometry(QRect(300, 20, 41, 31))
        icon7 = QIcon()
        icon7.addFile(u"pictures/union-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_4_btn_ads.setIcon(icon7)
        self.page_4_btn_ads.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.verticalLayoutWidget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(15, 12, 150, 30))
        self.label_6.setFont(font2)
        self.page_4_btn_terms_of_use = QPushButton(self.widget_5)
        self.page_4_btn_terms_of_use.setObjectName(u"page_4_btn_terms_of_use")
        self.page_4_btn_terms_of_use.setGeometry(QRect(300, 20, 41, 30))
        self.page_4_btn_terms_of_use.setIcon(icon7)
        self.page_4_btn_terms_of_use.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 605, 389, 78))
        self.widget_2.setStyleSheet(u"QPushButton {\n"
"  background-color: black;\n"
"  selection-color: yellow;\n"
"  selection-background-color: black;\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"  color:white;\n"
"  font-weight: 700;\n"
"  margin: 0 0 0 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: rgba(255, 255, 255, 0);\n"
"padding: 0 0 10 0;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"  margin: 0 1 0 1;\n"
"}")
        self.horizontalLayoutWidget_5 = QWidget(self.widget_2)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(-1, 0, 391, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.page_4_btn_home = QPushButton(self.horizontalLayoutWidget_5)
        self.page_4_btn_home.setObjectName(u"page_4_btn_home")
        self.page_4_btn_home.setMaximumSize(QSize(16777215, 80))
        self.page_4_btn_home.setIcon(icon4)
        self.page_4_btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.page_4_btn_home)

        self.page_4_btn_saved = QPushButton(self.horizontalLayoutWidget_5)
        self.page_4_btn_saved.setObjectName(u"page_4_btn_saved")
        self.page_4_btn_saved.setMaximumSize(QSize(16777215, 80))
        self.page_4_btn_saved.setIcon(icon2)
        self.page_4_btn_saved.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.page_4_btn_saved)

        self.page_4_btn_settings = QPushButton(self.horizontalLayoutWidget_5)
        self.page_4_btn_settings.setObjectName(u"page_4_btn_settings")
        self.page_4_btn_settings.setMaximumSize(QSize(16777215, 80))
        icon8 = QIcon()
        icon8.addFile(u"pictures/settings_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_4_btn_settings.setIcon(icon8)
        self.page_4_btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.page_4_btn_settings)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QLabel {\n"
"padding: 0 0 5 0;\n"
"}\n"
"\n"
"#lbl_search_2 {\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"#page_5_line_edit{\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"border:rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"padding: 0 0 0 10\n"
"}\n"
"\n"
"#page_5_btn_voice {\n"
"border:rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"#widget_word {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"border-radius: 10px;\n"
"}\n"
"#page_5_plainTextEdit_definition {\n"
"background-color: rgba(171, 171, 171, 0);\n"
"border:rgba(255, 255, 255, 0);\n"
"}")
        self.page_5_btn_voice = QToolButton(self.page_5)
        self.page_5_btn_voice.setObjectName(u"page_5_btn_voice")
        self.page_5_btn_voice.setGeometry(QRect(320, 100, 30, 22))
        self.page_5_btn_voice.setIcon(icon)
        self.page_5_line_edit = QLineEdit(self.page_5)
        self.page_5_line_edit.setObjectName(u"page_5_line_edit")
        self.page_5_line_edit.setGeometry(QRect(20, 90, 348, 42))
        self.widget_word_2 = QWidget(self.page_5)
        self.widget_word_2.setObjectName(u"widget_word_2")
        self.widget_word_2.setGeometry(QRect(20, 160, 351, 321))
        self.page_5_label_title = QLabel(self.widget_word_2)
        self.page_5_label_title.setObjectName(u"page_5_label_title")
        self.page_5_label_title.setGeometry(QRect(80, 25, 190, 51))
        self.page_5_label_title.setFont(font)
        self.page_5_label_title.setAlignment(Qt.AlignCenter)
        self.page_5_plainTextEdit_definition = QPlainTextEdit(self.widget_word_2)
        self.page_5_plainTextEdit_definition.setObjectName(u"page_5_plainTextEdit_definition")
        self.page_5_plainTextEdit_definition.setGeometry(QRect(20, 90, 311, 221))
        self.page_5_plainTextEdit_definition.setFont(font1)
        self.page_5_plainTextEdit_definition.setReadOnly(True)
        self.horizontalLayoutWidget_10 = QWidget(self.page_5)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(-10, -10, 411, 81))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_search_2 = QLabel(self.horizontalLayoutWidget_10)
        self.lbl_search_2.setObjectName(u"lbl_search_2")
        self.lbl_search_2.setMaximumSize(QSize(410, 16777215))
        self.lbl_search_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_6.addWidget(self.lbl_search_2)

        self.widget_8 = QWidget(self.page_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 605, 391, 78))
        self.widget_8.setStyleSheet(u"QPushButton {\n"
"  background-color: black;\n"
"  selection-color: yellow;\n"
"  selection-background-color: black;\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"  color:white;\n"
"  font-weight: 700;\n"
"  margin: 0 0 0 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"border: rgba(255, 255, 255, 0);\n"
"padding: 0 0 10 0;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"  margin: 0 1 0 1;\n"
"}\n"
"")
        self.horizontalLayoutWidget_12 = QWidget(self.widget_8)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(-1, 0, 391, 80))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.page_5_btn_home = QPushButton(self.horizontalLayoutWidget_12)
        self.page_5_btn_home.setObjectName(u"page_5_btn_home")
        self.page_5_btn_home.setMaximumSize(QSize(16777215, 80))
        self.page_5_btn_home.setIcon(icon4)
        self.page_5_btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.page_5_btn_home)

        self.page_5_btn_saved = QPushButton(self.horizontalLayoutWidget_12)
        self.page_5_btn_saved.setObjectName(u"page_5_btn_saved")
        self.page_5_btn_saved.setMaximumSize(QSize(16777215, 80))
        self.page_5_btn_saved.setIcon(icon2)
        self.page_5_btn_saved.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.page_5_btn_saved)

        self.page_5_btn_settings = QPushButton(self.horizontalLayoutWidget_12)
        self.page_5_btn_settings.setObjectName(u"page_5_btn_settings")
        self.page_5_btn_settings.setMaximumSize(QSize(16777215, 80))
        self.page_5_btn_settings.setIcon(icon3)
        self.page_5_btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.page_5_btn_settings)

        self.stackedWidget.addWidget(self.page_5)
        self.page_5_line_edit.raise_()
        self.page_5_btn_voice.raise_()
        self.widget_word_2.raise_()
        self.horizontalLayoutWidget_10.raise_()
        self.widget_8.raise_()

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.page_2_btn_voice.setText(QCoreApplication.translate("Form", u"...", None))
        self.lbl_search.setText(QCoreApplication.translate("Form", u"Search", None))
        self.page_2_label_title.setText("")
        self.page_2_plainTextEdit_definition.setPlainText("")
        self.page_2_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.page_2_btn_home.setText("")
        self.page_2_btn_saved.setText("")
        self.page_2_btn_settings.setText("")
        self.page_3_btn_voice.setText(QCoreApplication.translate("Form", u"...", None))
        self.lbl_search_5.setText(QCoreApplication.translate("Form", u"Bookmarks", None))
        self.page_3_btn_home.setText("")
        self.page_3_btn_saved.setText("")
        self.page_3_btn_settings.setText("")
        self.page_3_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.lbl_search_4.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Show suggestions", None))
        self.page_4_btn_show_suggestions.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Show keyboard", None))
        self.page_4_btn_show_keyboard.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Remove ads", None))
        self.page_4_btn_ads.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Terms of use", None))
        self.page_4_btn_terms_of_use.setText("")
        self.page_4_btn_home.setText("")
        self.page_4_btn_saved.setText("")
        self.page_4_btn_settings.setText("")
        self.page_5_btn_voice.setText(QCoreApplication.translate("Form", u"...", None))
        self.page_5_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.page_5_label_title.setText("")
        self.page_5_plainTextEdit_definition.setPlainText("")
        self.lbl_search_2.setText(QCoreApplication.translate("Form", u"Meanings", None))
        self.page_5_btn_home.setText("")
        self.page_5_btn_saved.setText("")
        self.page_5_btn_settings.setText("")
    # retranslateUi

