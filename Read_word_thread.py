import pyttsx3
from PySide6.QtCore import QThread


class Read_word_thread(QThread):
    def __init__(self, word):
        super().__init__()
        self.word = word

    def run(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume', 1)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(self.word)
        engine.runAndWait()