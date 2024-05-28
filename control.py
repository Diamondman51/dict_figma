import json

from PySide6 import QtCore
from PySide6.QtCore import QTimer
from PySide6.QtGui import QKeyEvent, QIcon, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem

from Speech_recognition_thread import Speech_recognition_thread
from cart import Cart
from stackedwidget_ui import Ui_Form


class Control(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_file()
        self.suggestion_flag = False
        self.keyboard_flag = False
        self.stackedWidget.setCurrentIndex(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.swap_to_1)
        self.timer.start(2000)
        self.page_2_btn_saved.clicked.connect(self.swap_to_2)
        self.page_2_btn_settings.clicked.connect(self.swap_to_3)
        self.page_2_btn_home.clicked.connect(self.swap_to_1)
        self.page_3_btn_home.clicked.connect(self.swap_to_1)
        self.page_3_btn_saved.clicked.connect(self.swap_to_2)
        self.page_3_btn_settings.clicked.connect(self.swap_to_3)
        self.page_4_btn_home.clicked.connect(self.swap_to_1)
        self.page_4_btn_saved.clicked.connect(self.swap_to_2)
        self.page_4_btn_settings.clicked.connect(self.swap_to_3)
        self.page_4_btn_show_suggestions.clicked.connect(self.activate_disactivate_suggestions)
        self.page_4_btn_show_keyboard.clicked.connect(self.activate_disactivate_keyboard)
        self.page_2_btn_voice.clicked.connect(self.speech_recognition_thread)
        self.speech_recognition = Speech_recognition_thread()
        self.number_of_carts(50)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def number_of_carts(self, num):
        i = 0
        for word, definition in self.data.items():
            if i == num:
                break
            self.create_cart(word, definition)
            i += 1

    def create_cart(self, word, definition):
        carta = Cart()
        item = QListWidgetItem()
        carta.lbl_title.setText(word)
        carta.lbl_text_definition.setText(definition)
        self.listWidget.addItem(item)
        item.setSizeHint(carta.size())
        self.listWidget.setItemWidget(item, carta)

    def speech_recognition_thread(self):
        if not self.speech_recognition.isRunning():
            self.speech_recognition.start()
        self.speech_recognition.begin.connect(lambda: self.page_2_line_edit.setPlaceholderText('Speak to microphone'))
        self.speech_recognition.finish.connect(lambda: self.page_2_line_edit.setPlaceholderText('Speech recognized'))
        self.speech_recognition.finish.connect(lambda: self.page_2_line_edit.setPlaceholderText('Search'))
        self.speech_recognition.signal.connect(lambda word: self.page_2_line_edit.setText(word))
        self.speech_recognition.finish.connect(self.search_btn_clicked)

    def activate_disactivate_keyboard(self):
        if not self.keyboard_flag:
            self.keyboard_flag = True
            self.page_4_btn_show_keyboard.setIcon(QIcon('pictures/Toggle_On.png'))
        else:
            self.keyboard_flag = False
            self.page_4_btn_show_keyboard.setIcon(QIcon('pictures/Toggle_Off.png'))

    def activate_disactivate_suggestions(self):
        if not self.suggestion_flag:
            self.suggestion_flag = True
            self.page_4_btn_show_suggestions.setIcon(QIcon('pictures/Toggle_On.png'))
        else:
            self.suggestion_flag = False
            self.page_4_btn_show_suggestions.setIcon(QIcon('pictures/Toggle_Off.png'))

    def swap_to_3(self):
        self.stackedWidget.setCurrentIndex(3)

    def swap_to_2(self):
        self.stackedWidget.setCurrentIndex(2)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == QtCore.Qt.Key_Enter and self.page_2_line_edit.text():
            print(2)
            self.search_btn_clicked()

    def swap_to_1(self):
        self.timer.stop()
        self.stackedWidget.setCurrentIndex(1)

    def search_btn_clicked(self):
        word = self.page_2_line_edit.text()
        if word in self.data.keys():
            self.page_2_label_title.setText(word)
            self.page_2_plainTextEdit_definition.setPlainText(self.data[word])


    def load_file(self):
        file = open("data.json", 'r')
        self.data = json.load(file)