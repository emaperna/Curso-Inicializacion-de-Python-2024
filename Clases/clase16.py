#Hacer el punto 4: armar el programa con todos los módulos que fuimos haciendo clase a clase. ¡Sumado a eso, en los tres 
#puntos previos al que deben hacer ustedes, les deje parte del código que fuimos haciendo en clase por si 
#no les funciona lo hecho! Al final también encontrarán un pequeño repaso por las lineas de codigo nuevas, 
#como el Whit, Try except y el as.

#APIKEY: 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

from groq import Groq
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer

while True:
    with sr.Microphone() as source:
        print("Hable (tiene 10 segundos): ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
        
        try:
            text = r.recognize_google(audio, language='es-ES').lower()
            print(f"Escuche esto: {text}")
            engine.say(text)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Lo siento, no he podido entender lo que has dicho.")
        except sr.RequestError:
            print("Lo siento, no ha habido un problema al intentar comunicarme con el servicio de Google.")

    if text == "no" or text == "termina" :
        break
    else:
        continue
    
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

    print(interaccion_chat.choices[0].message.content)
    engine.say(interaccion_chat.choices[0].message.content)
    engine.runAndWait()
