import difflib
import json

from PySide6 import QtCore
from PySide6.QtCore import QTimer
from PySide6.QtGui import QKeyEvent, QIcon, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem

from Read_word_thread import Read_word_thread
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
        self.page_5_btn_home.clicked.connect(self.swap_to_1)
        self.page_5_btn_saved.clicked.connect(self.swap_to_2)
        self.page_5_btn_settings.clicked.connect(self.swap_to_3)
        self.page_4_btn_show_suggestions.clicked.connect(self.activate_disactivate_suggestions)
        self.page_4_btn_show_keyboard.clicked.connect(self.activate_disactivate_keyboard)
        self.page_2_btn_voice.clicked.connect(self.speech_recognition_thread)
        self.page_3_btn_voice.clicked.connect(self.speech_recognition_thread)
        self.page_5_btn_read.clicked.connect(self.define_page)
        self.page_2_btn_read.clicked.connect(self.define_page)
        self.page_3_btn_read.clicked.connect(self.define_page)
        self.speech_recognition = Speech_recognition_thread()
        self.number_of_carts(50)
        self.read_word_thread = Read_word_thread(word='Nothing to read')
        # make double click -> move to page 5
        self.listWidget.itemDoubleClicked.connect(self.swap_to_4)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def define_page(self):
        page = self.stackedWidget.currentIndex()
        # print(page)
        self.read_the_word(page)

    def read_the_word(self, page_num):

        if page_num == 1:
            text = self.page_2_label_title.text()
            text2 = self.page_2_line_edit.text()
            if text:
                self.read_word_thread.word = text
                print(self.read_word_thread.word)
            elif text2:
                self.read_word_thread.word = text2
            else:
                pass

        elif page_num == 2:
            if self.listWidget.currentItem():
                title, widget = self.make_widget_from_item()
                if title:
                    self.read_word_thread.word = title
                else:
                    self.read_word_thread.word = self.page_2_line_edit.text()
        elif page_num == 4:
            self.read_word_thread.word = self.page_5_label_title.text()
        if not self.read_word_thread.isRunning():
            self.read_word_thread.start()
    def make_widget_from_item(self):
        item = self.listWidget.currentItem()
        if item:
            widget = self.listWidget.itemWidget(item)
            title = widget.lbl_title.text()
            define = widget.lbl_text_definition.text()
            return title, define
    def swap_to_4(self):
        self.stackedWidget.setCurrentIndex(4)
        title, define = self.make_widget_from_item()
        self.page_5_label_title.setText(title)
        self.page_5_plainTextEdit_definition.setPlainText(define)

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
        num = self.stackedWidget.currentIndex()

        if not self.speech_recognition.isRunning():
            self.speech_recognition.start()
            if num == 1:
                self.page_2_line_edit.clear()
                self.speech_recognition.begin.connect(lambda: self.page_2_line_edit.setPlaceholderText('Speak to microphone'))
                self.speech_recognition.begin.connect(lambda: self.page_2_btn_voice.setDisabled(True))
                self.speech_recognition.finish.connect(lambda: self.page_2_line_edit.setPlaceholderText('Speech recognized'))
                self.speech_recognition.finish.connect(lambda: self.page_2_line_edit.setPlaceholderText('Search'))
                self.speech_recognition.signal.connect(lambda word: self.page_2_line_edit.setText(word))
                self.speech_recognition.finish.connect(self.search_btn_clicked)
                self.speech_recognition.finish.connect(lambda: self.page_2_btn_voice.setEnabled(True))
            elif num == 2:
                self.page_3_line_edit.clear()
                self.speech_recognition.begin.connect(lambda: self.page_3_btn_voice.setDisabled(True))
                self.speech_recognition.begin.connect(
                    lambda: self.page_3_line_edit.setPlaceholderText('Speak to microphone'))
                self.speech_recognition.finish.connect(
                    lambda: self.page_3_line_edit.setPlaceholderText('Speech recognized'))
                self.speech_recognition.finish.connect(lambda: self.page_3_line_edit.setPlaceholderText('Search'))
                self.speech_recognition.signal.connect(lambda word: self.page_3_line_edit.setText(word))
                self.speech_recognition.finish.connect(self.search_btn_clicked)
                self.speech_recognition.finish.connect(lambda: self.page_3_btn_voice.setEnabled(True))

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
        if event.key() == QtCore.Qt.Key_Enter and ((self.page_2_line_edit.text() or self.page_3_line_edit.text()) or (self.page_2_line_edit.text() and self.page_3_line_edit.text())):
            self.search_btn_clicked()

    def swap_to_1(self):
        self.timer.stop()
        self.stackedWidget.setCurrentIndex(1)

    def search_btn_clicked(self):
        num = self.stackedWidget.currentIndex()
        if num == 1:
            word = self.page_2_line_edit.text()
            if word in self.data.keys():
                self.page_2_label_title.setText(word)
                self.page_2_plainTextEdit_definition.setPlainText(self.data[word])
        elif num == 2:
            self.listWidget.clear()
            word1 = self.page_3_line_edit.text()
            if word1 in self.data.keys():
                words = difflib.get_close_matches(word1, self.data, 5)
                for word2 in words:
                    self.create_cart(word2, self.data[word2])

    def load_file(self):
        file = open("data.json", 'r')
        self.data = json.load(file)