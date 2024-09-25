#Cuenten cuantas veces se ingreso el texto.
contador = 0
seguir = True

while seguir == True: #cuando es booleano no hace falta poner ==
    valor_usuario = input(" Ingrese un valor o ingrese A para finalizar ")
    contador +=1
    valor_usuario = valor_usuario.upper()
    if valor_usuario == "A":
        seguir = False

print(f" Se ejecuto correctamente {contador} veces!")
