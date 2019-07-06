import sys
from PyQt5.QtWidgets import *
from uipyFiles.uiautomat import Ui_Automat
import speech_recognition as sr

with open('google_credentials.json') as inp:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = inp.read()
LANG_ENG = 'en-US'
LANG_RUS = 'ru-RU'


class SpeechInput(QWidget):
    def __init__(self):
        super(SpeechInput, self).__init__()

        self.recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)

        self.uiautomat = Ui_Automat()
        self.uiautomat.setupUi(self)

        self.uiautomat.btn_start.clicked.connect(self.btn_start_clicked)

        self.show()

    def btn_start_clicked(self):
        pass

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

"""
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print(r.energy_threshold)

    print('Say smth')

    audio = r.listen(source)

    a = recognize(audio, language=LANG_ENG)
    print(a)
"""