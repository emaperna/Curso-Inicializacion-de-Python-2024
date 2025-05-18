#programa que solo ingrese palabras con solo 3 intentos

var = input("Ingrese una palabra")

if var.isdigit():
    print("Error: Este es tu primer error")
    continuar = True
else:
    continuar = False

if continuar:
    var = input("Ingrese por segunda vez una palabra:")
        
if var.isdigit():
    print("Error : Este es tu segundo error")
    continuar = True
else:
    continuar = False

if continuar:
    var = input("Ingrese por tercer vez una palabra:")
        
if var.isdigit():
    print("Error : Este es tu tercer error")
    continuar = True
else:
    continuar = False       
print(f"La palabra o letra que ingresaste es: {var}")

exit()