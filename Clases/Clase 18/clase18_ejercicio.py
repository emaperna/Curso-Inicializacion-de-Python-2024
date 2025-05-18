

import pyttsx3
import speech_recognition as sr
from groq import Groq

engine = pyttsx3.init()
engine.say("¡Hola! ¿en que puedo ayudarte?")
engine.runAndWait()
habla = input("Desea escuchar la respuesta? S/N").upper()
escrito = input("Desea escribir la pregunta? S/N").upper()


r = sr.Recognizer
engine = pyttsx3.init()

while True:
    if escrito == "N":
            
        with sr.Microphone() as source:
            print("Hable (tiene 10 segundos): ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            
            try:
                prompt = r.recognize_google(audio, language='es-ES').lower()
                print(f"Escuche esto: {prompt}")
                engine.say(prompt)
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Lo siento, no he podido entender lo que has dicho.")
            except sr.RequestError:
                print("Lo siento, no ha habido un problema al intentar comunicarme con el servicio de Google.")
    else:
        prompt = input("¿Que desea preguntar?")
        
    if prompt == "no" or prompt == "termina" :
        break
    else:
        continue
    
    cliente = Groq()



    interaccion_chat = cliente.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
    ],
    model="llama3-8b-8192",    
)

    
    
    if habla == "S":  
    engine.say(interaccion_chat.choices[0].message.content)
    engine.runAndWait()

    print(interaccion_chat.choices[0].message.content)
    seguir = input("Continuar ? S/N: ").upper()
    if seguir == "N":
        break
print("Gracias, hasta la proxima")


