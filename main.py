import os
import speech_recognition
from google.cloud import translate_v2 as translate


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jose/Downloads/massive-catfish-411714-89ecb4eed938.json"
# To create your own credentials follow: https://developers.google.com/workspace/guides/create-credentials


def translate_text(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    translated_text = result["translatedText"]
    return translated_text


def speech_to_text():
    recognizer = speech_recognition.Recognizer()

    while True:
        try: 
            with speech_recognition.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="es-PE")
                text = text.lower()

                translated_text = translate_text(text, target_language="qu")
                print(translated_text)


        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue


# === MAIN === 
speech_to_text()
