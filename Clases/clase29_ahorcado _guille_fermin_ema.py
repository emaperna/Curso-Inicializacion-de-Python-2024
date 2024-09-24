import random


print("¡Bienvenido al juego del ahorcado!")

def palabra_para_adivinar(letra, secreta, actual, adivinadas):
        for letra in secreta:
            if letra in adivinadas:
                actual += letra
            else:
                actual += "_"
        return actual

def verifica(letra, secreta, adivinada, intento):
    if letra in secreta:
        adivinada.append(letra)
        print("¡Correcto!")
    else:
        intento -= 1
        print("Incorrecto. Te quedan", intento, "intentos.")
    return [adivinada, intento]

def una_letra():
    while True:
        letra = input("Introduce una sola letra: ").lower()
        if len(letra)>1 :
            print("Debe introducir solo una letra")
        else:
            if letra.isdigit():
                print("No debe ingresar numeros")
            else:
                break
    return letra

def ahoracado():
    palabras = ["manzana", "banana", "pera", "uva", "naranja"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        letra = una_letra()
        palabra_actual = ""

        verificada = verifica(letra, palabra_secreta, letras_adivinadas, intentos)
        intentos = verificada[1]
        letras_adivinadas = verificada[0]

        palabra_actual = palabra_para_adivinar(letra, palabra_secreta, palabra_actual, letras_adivinadas)
        print("Palabra:", palabra_actual)

        if "_" not in palabra_actual:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break

    if intentos == 0:
        print("¡Has perdido! La palabra era:", palabra_secreta)
    return intentos

def nombre():
    nombre_usuario = input("Bienvenido , Ingrese su nombre: ")
    return nombre_usuario
saludar = nombre()
print(saludar)

puntaje = 0
ganadas = 0
perdidas = 0

while True:
    resto = ahoracado()
    continuar = input("Desea seguir jugando (S/N): ")
    puntaje += int(resto)
    if resto == 0:
        perdidas +=1
    else:
        ganadas +=1
    if continuar.upper() == "N":
        exit(f"{saludar}, tu puntaje final es {puntaje}, ganaste {ganadas} veces y perdiste {perdidas} veces ! ")
