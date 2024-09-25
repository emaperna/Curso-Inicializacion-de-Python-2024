import random


print("¡Bienvenido al juego del ahorcado!")

def juego():
    palabras = ["manzana", "banana", "pera", "uva", "naranja"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6
    gano = False
    while intentos > 0:
        palabra_actual = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_actual += letra
            else:
                palabra_actual += "_"
        print("Palabra:", palabra_actual)

        if "_" not in palabra_actual:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            gano = True
            break

        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")


    if intentos == 0:
        print("¡Has perdido! La palabra era:", palabra_secreta)
        
    return gano

usuario = input ("Ingrese su nombre: ")
while True:
    gano = juego()
    puntaje = 0 

    if gano :
        puntaje = puntaje + 100
    else :
        puntaje = puntaje - 100
        
    pregunta = input("desea volver a jugar?:").upper()
    
    if pregunta == "N":
        print(f"{ usuario} tu puntaje final es {puntaje}")
        exit()
        