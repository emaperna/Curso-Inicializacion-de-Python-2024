# Forma 1 de detectar si es solo texto 

#variable = ""
#variable = input("Ingrese solo texto: ")

#if variable.isdigit():
#    print("Era solo texto")
#    exit()
#else:
#    print(f"El valor de la variable es {variable}")



#Forma 2 de detectar si es solo texto (Negando el if)

variable = ""
variable = input("Ingrese solo texto: ")

if not variable.isdigit():
    print(f"El valor de la variable es {variable}")
else:
    print("Era solo texto")
