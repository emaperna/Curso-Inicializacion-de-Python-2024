#APIKEY: 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

import pyttsx3
import speech_recognition as sr
from groq import Groq

engine = pyttsx3.init()
engine.say("¡Hola! ¿en que puedo ayudarte?")
engine.runAndWait()

engine = pyttsx3.init()
r = sr.Recognizer()

hablar_escribir = input("Desea escribir la pregunta? (S/n):").lower()
desea_escuchar = input("Desea escuchar la respusta de la IA? (S/n):").lower()

while True:
    
    if hablar_escribir == "n":
            
        with sr.Microphone() as source:
            print("Hable (tiene 10 segundos): ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            
            try:
                prompt = r.recognize_google(audio, language='es-ES').lower()
                print(f"Escuche esto: {text}")
                engine.say(text)
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Lo siento, no he podido entender lo que has dicho.")
            except sr.RequestError:
                print("Lo siento, no ha habido un problema al intentar comunicarme con el servicio de Google.")
    else:
        text = input("Escriba la pregunta")
        
    if text == "no" or text == "termina" :
        break
    else:
        cliente = Groq(
        api_key= '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',)



    interaccion_chat = cliente.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
    ],
    model="llama3-8b-8192",    
)

    
    
    if desea_escuchar != "n":  
        engine.say(interaccion_chat.choices[0].message.content)
        engine.runAndWait()
