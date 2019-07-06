import speech_recognition as sr

with open('google_credentials.json') as inp:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = inp.read()

LANG_ENG = 'en-US'
LANG_RUS = 'ru-RU'


def recognize(audio, language=LANG_ENG):
    text = None
    try:
        text = r.recognize_google_cloud(audio, language=language, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        # text = r.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text


r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print(r.energy_threshold)

    print('Say smth')

    audio = r.listen(source)

    a = recognize(audio, language=LANG_ENG)
    print(a)
