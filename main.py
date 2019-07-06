import sys

import pyperclip
import speech_recognition as sr
from PyQt5.QtWidgets import *

from uipyFiles.ui_speech_input import Ui_SpeechInput

with open('google_credentials.json', encoding='utf-8') as inp:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = inp.read()
LANG_ENG = 'en-US'
LANG_RUS = 'ru-RU'


class SpeechInput(QWidget):
    def __init__(self):
        super(SpeechInput, self).__init__()

        self.recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)

        self.uiautomat = Ui_SpeechInput()
        self.uiautomat.setupUi(self)

        self.uiautomat.btn_start.clicked.connect(self.btn_start_clicked)
        self.uiautomat.eng_enabled.setChecked(True)

        self.show()

    def btn_start_clicked(self):
        self.uiautomat.btn_start.setText('Listening...')
        self.uiautomat.btn_start.repaint()

        lang = LANG_RUS if self.uiautomat.rus_enabled.isChecked() else LANG_ENG
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            res = self.recognize(audio, language=lang)

        if res:
            pyperclip.copy(res)

        res = "Couldn't recognize" if not res else res
        self.uiautomat.text_output.setPlainText(res)

        self.uiautomat.btn_start.setText('Record')
        self.uiautomat.btn_start.repaint()

    def recognize(self, audio, language=LANG_ENG):
        text = None
        try:
            text = self.recognizer.recognize_google_cloud(audio, language=language,
                                                          credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            # text = r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpeechInput()

    sys.exit(app.exec_())
