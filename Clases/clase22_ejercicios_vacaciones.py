#Realizar un login que permita ingresar con varios usuarios y  contraseñas.

credencial = {"emanuel":"qwerty","diego":"1234","gustavo":"admin","kokas":"java"}

oportunidad = 0
maximo_oportunidades = 3

while oportunidad < maximo_oportunidades:
    usuario = input("A continuación ingrese su Usuario Aqui 🧑:::... ").lower()
    contraseña = input("A continuación ingrese su Contraseña Aqui 🔑🔑:::...").lower()

    if usuario in credencial and credencial [usuario] == contraseña:
        print("¡Bienvenido 🪪, Acceso correcto al Sistema!🖥️..")
        break
    else:
        oportunidad += 1
        print(f"Datos ingresados incorrectos. Intento {oportunidad} de {maximo_oportunidades}❌")

if oportunidad == maximo_oportunidades:
    print("No tienes mas intentos, Acceso denegado.❌❌❌")