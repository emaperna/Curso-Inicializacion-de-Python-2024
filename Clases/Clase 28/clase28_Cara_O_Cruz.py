#hacer un juego de Cara o Cruz donde el usuario tenga
#2 opciones para elegir, si jugar contra la computadora
#o un amigo… si elige la segunda deberíamos preguntarle el nombre a ambos


nombre_jugador = input("Hola Jugador👋, escribe tu Nombre ::.. ")
jugador1 = input("Queres jugar con un Amigo 🤹 ingresa 1 , o contra la Computadora 🖥️  ingresa 2 ::.. ")

if not jugador1.isdigit():
    print ("Debes ingresar opcion 1 o 2 solamente 🫨🫨... vuelve a empezar 😥😥...")
    exit()

if jugador1 == 1:
    nombre_jugador1 = input(" {jugador1} Que tu amigo escriba su nombre")
    print (f" {jugador1} y {nombre_jugador}  Juguemos cara o cruz 🪙🪙...!")
elif jugador1 == 2:
    print (f"{nombre_jugador} Hola soy la computadora , jugaremos cara o cruz 🪙���...!")

#jugador2 = input("Jugador 2 escribe tu Nombre ::..")