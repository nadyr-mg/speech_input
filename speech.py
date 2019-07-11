import sys
from urllib.error import URLError

import pyperclip
import speech_recognition as sr
from speech_recognition import RequestError, UnknownValueError
from PyQt5.QtWidgets import *
from pywinauto.keyboard import send_keys
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
import googleapiclient.errors
from uipyFiles.ui_speech_input import Ui_SpeechInput
import base64
import googleapiclient.http
import os
import json
from subprocess import run

with open('google_credentials.json', encoding='utf-8') as inp:
    api_credentials = GoogleCredentials.from_stream(inp.name)

LANG_ENG = 'en-US'
LANG_RUS = 'ru-RU'

cmd = 'nircmd.exe setsysvolume {} default_record'

config_dir = r'C:\Users\Andrew\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

with open(os.path.join(config_dir, 'voice.json'), encoding='utf-8') as inp:
    config = json.load(inp)

MAX_VOLUME = 65536


def set_volume(cur_volume):
    val = int((MAX_VOLUME * cur_volume) / 100)

    cmd1 = cmd.format(val)
    run(cmd1, shell=True)


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

        googleapiclient.http.DEFAULT_HTTP_TIMEOUT_SEC = 10
        self.speech_service = build("speech", "v1", credentials=api_credentials, cache_discovery=False)

        self.show()

    def btn_start_clicked(self):
        lang = LANG_RUS if self.uiautomat.rus_enabled.isChecked() else LANG_ENG

        with sr.Microphone() as source:
            self.uiautomat.btn_start.setText('Listening...')
            self.uiautomat.btn_start.repaint()

            set_volume(config['google'])
            audio = self.recognizer.listen(source, timeout=15)

        # self.uiautomat.btn_start.setText('Analyzing...')
        # self.uiautomat.btn_start.repaint()

        self.showMinimized()

        res = self.recognize(audio, lang)
        if res:
            pyperclip.copy(res)
            send_keys('^v')

        set_volume(config['voice'])

        res = "Couldn't recognize" if not res else res
        self.uiautomat.text_output.setPlainText(res)

        self.uiautomat.btn_start.setText('Record')
        self.uiautomat.btn_start.repaint()

    def recognize(self, audio_data, language):
        flac_data = audio_data.get_flac_data(
            convert_rate=None if 8000 <= audio_data.sample_rate <= 48000 else max(8000,
                                                                                  min(audio_data.sample_rate, 48000)),
            # audio sample rate must be between 8 kHz and 48 kHz inclusive - clamp sample rate into this range
            convert_width=2  # audio samples must be 16-bit
        )

        speech_config = {"encoding": "FLAC", "sampleRateHertz": audio_data.sample_rate, "languageCode": language}
        request = self.speech_service.speech().recognize(
            body={"audio": {"content": base64.b64encode(flac_data).decode("utf8")}, "config": speech_config})

        try:
            response = request.execute()
        except googleapiclient.errors.HttpError as e:
            raise RequestError(e)
        except URLError as e:
            raise RequestError("recognition connection failed: {0}".format(e.reason))

        if "results" not in response or len(response["results"]) == 0:
            raise UnknownValueError()
        transcript = ""
        for result in response["results"]:
            transcript += result["alternatives"][0]["transcript"].strip() + " "

        return transcript

    def closeEvent(self, evnt):
        buttonReply = QMessageBox.question(self, 'Confirmation', "Do you want to Exit?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            evnt.accept()
        else:
            evnt.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpeechInput()

    sys.exit(app.exec_())
