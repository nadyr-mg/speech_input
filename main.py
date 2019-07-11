import sys
import os

import pyperclip
import speech_recognition as sr
from PyQt5.QtWidgets import *
from pywinauto.keyboard import send_keys
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from uipyFiles.ui_speech_input import Ui_SpeechInput

with open('google_credentials.json', encoding='utf-8') as inp:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = inp.read()

LANG_ENG = 'en-US'
LANG_RUS = 'ru-RU'

file_path = os.path.join(os.getcwd(), 'google_credentials.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = file_path


class SpeechInput(QWidget):
    def __init__(self):
        super(SpeechInput, self).__init__()

        self.recognizer = sr.Recognizer()

        # with sr.Microphone() as source:
        #    self.recognizer.adjust_for_ambient_noise(source)

        self.uiautomat = Ui_SpeechInput()
        self.uiautomat.setupUi(self)

        self.uiautomat.btn_start.clicked.connect(self.btn_start_clicked)
        self.uiautomat.eng_enabled.setChecked(True)

        self.client = speech.SpeechClient()

        self.show()

    def btn_start_clicked(self):
        self.uiautomat.btn_start.setText('Listening...')
        self.uiautomat.btn_start.repaint()
        # self.showNormal()
        # self.showMinimized()

        lang = LANG_RUS if self.uiautomat.rus_enabled.isChecked() else LANG_ENG
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        self.uiautomat.btn_start.setText('Analyzing...')
        self.uiautomat.btn_start.repaint()
        flag = True
        if flag:
            res = self.recognize2(audio, lang)
        else:
            res = self.recognize(audio, lang)
        if res:
            pyperclip.copy(res)
            send_keys('^v')

        res = "Couldn't recognize" if not res else res
        self.uiautomat.text_output.setPlainText(res)

        self.uiautomat.btn_start.setText('Record')
        self.uiautomat.btn_start.repaint()

    def recognize(self, audio, lang):
        text = None
        try:
            text = self.recognizer.recognize_google_cloud(audio, language=lang,
                                                          credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            # text = self.recognizer.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return text

    def recognize2(self, content, lang):
        audio = types.RecognitionAudio(content=content.get_flac_data())

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            language_code=lang)

        # response = self.client.recognize(config, audio, timeout=15)
        operation = self.client.long_running_recognize(config, audio)
        response = operation.result(timeout=15)

        res = []
        for result in response.results:
            res.append(result.alternatives[0].transcript)

        return ' '.join(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpeechInput()

    sys.exit(app.exec_())
