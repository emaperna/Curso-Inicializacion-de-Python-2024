import random

usuario = input ("Ingrese su nombre: ")
puntaje_total = 0
intentos = 6
palabras = ["manzana", "banana", "pera", "uva", "naranja"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []

print(f"¡Bienvenido al juego del ahorcado! {usuario} ")


def terminar():
    """Este procedimiento me va a permitir terminar el juego o seguir jugando"""
    continuar_juego = True
    while continuar_juego:
        pregunta = input("Quieres jugar de nuevo? (S/n): ").upper()
        if  pregunta == "S" or  pregunta == "SI" :
            continuar_juego = False
        elif  pregunta == "N" or   pregunta == "NO" :
                print(f"Gracias por jugar {usuario}, tu puntaje total es:{puntaje_total}")
                
                exit()
        else : print ("Respuesta no valida")
    return

def buscar_palabra():
    palabra_actual = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_actual += letra
        else:
            palabra_actual += "_"
    return palabra_actual


while True:
    intentos = 6
    palabras = ["manzana", "banana", "pera", "uva", "naranja"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    
    while intentos > 0:
        palabra_actual = buscar_palabra()
        
        print("Palabra:", palabra_actual)

        if "_" not in palabra_actual:
            print(f"¡Felicidades! {usuario} Has adivinado la palabra:", palabra_secreta)
            puntaje_total = puntaje_total + 10
            break

        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print(f"¡Has perdido {usuario}! La palabra era:", palabra_secreta)       
        puntaje_total = puntaje_total - 10

    terminar()