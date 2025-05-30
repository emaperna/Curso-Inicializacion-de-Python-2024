'''
Esto va en terminal
pip install pyaudio
pip install SpeechRecognition
pip install setuptools
'''
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r =sr.Recognizer()

with sr.Microphone() as source:
    print("Hable: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='es-ES')
        print(f"Dijiste: {text}")
        engine.say(text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Lo siento, no he podido entender lo que has dicho.")
    except sr.RequestError:
        print("Lo siento, no ha habido un problema al intentar comunicarme con el servicio de Google.")