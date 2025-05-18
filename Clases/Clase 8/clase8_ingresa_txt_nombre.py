#INGRESA UN TEXTO EN MINUSCULA Y SE TRANSFORMA A MAYUSCULA, INGRESA NRO Y ARROJA ERROR

#texto = ""
#texto = input("Ingrese un texto en minuscula:")

#if texto.isalpha and texto.islower():
#    texto = texto.upper() 
#    print(f"el texto ingresado es: {texto}")
#else:
#    print("ERROR, Debe ingresar solo texto en minuscula")

#INGRESA UN NUMERO Y LO MUESTRA, INGRESA TEXTO Y TIENES DOS OPORTUNIDADES MAS
numero = ""
numero = input("Ingrese un numero:")

if not numero.isdigit():
    print(f"ERROR, has ingresado {numero}, tienes dos oportunidades mas")
    numero = input("Ingrese un numero:")
    
if not numero.isdigit():
    print(f"ERROR, es tu primer oportunidad y has ingresado: {numero}, ultimo intento")
    numero = input("Ingrese un numero:")
    
if not numero.isdigit():
    print(f"ERROR, fue tu segunda oportunidad y has ingresado: {numero}")
    print(f" El valor ingresado: {numero},no es un numero")
else:
    print(f" El valor ingresado: {numero}")