import pyttsx3

engine = pyttsx3.init()
hablar = input("Escribe lo que quieras que diga:")
engine.say(hablar)
rate = engine.getProperty('rate')
print(f"la velocidad actual es:{rate}")
engine.setProperty('rate', 300)
engine.say(hablar)

#Muestra las voces disponibles
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}. {voice.name} ({voice.languages})")
    
#Establecer voz en español
engine.setProperty('voice', voices[0].id)
engine.runAndWait()

