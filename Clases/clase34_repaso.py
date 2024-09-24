'''
Temas de examen:

1-Variables y tipos de datos
2-Operadores aritmetricos y de comparacion
3-Estructuras de control: If, For y While
4-Listas
5-Funciones
6-Programacion orientada a objetos
7-Imports basicos de Python



Tema 1- Variables y Tipos de Datos:

-Variables: Son espacios de memoria en la computadora.
-Nombre: en snake_case. 
-Tipos de datos simples: boolean, float, int, str, complex(j). 
-Tipos de datos complejos: [Listas], {Conjuntos}, (Tuplas), Diccionario > {"clave":valor}. 



Tema 2- Operadores aritmeticos y de comparacion:

-Operadores: +, -, *, /, Modulo (resto de la division): % Exponente: ** (Potencia)
-Operadores dobles: +=, -=, *=, /=
-Comparacion: ==, !=, <, >, <=, >=    (! es el simbolo para negar) 
-Operadores Logicos: AND(&), OR(|) Y NOT(!)

Contador: Cuenta + 1, contador +=1
Acumulador: Suma resultados


Tema 3- Estructuras de Control: If, Elif, Else, For y While (nos permiten controlar el flujo del codigo)


Tema 4- Listas

Metodos simples ( append- remove- pop - copy)


Tema 5- Funciones

¿Como declararlas y como llamarlas?


Tema 6- Programacion orientada a objetos

¿Como declararlas y como llamarlas?
Self
Metodos y atributos


Tema 7: Import basicos en Python

Random - Datetime- Funciones

'''

#Trivias:

#¿Que valor tendra la variable resultado?

#resultado = 0
#for i in range(1,5):
#    resultado +=1

'''
Resultados:

a: 10 (Opcion correcta)
b: 15
c: 5
d: 20

''' 

#¿Que dato se utiliza para almacenar True o False en Python?

'''
a: int
b: str
c: bool (Opcion correcta)
d: float 

'''

#¿Cual es la salida de este codigo? print(3*"2")

'''
a: 6
b: 222 (Opcion correcta)
c: 32
d: 2

'''

#¿Que operador se usa para comprar si dos valores son iguales en Python?

'''
a: =  (Asigna)
b: == (Igual Igual - Comparacion) (Opcion correcta)
c: != (No igual - Comparacion)
d: === (No existe en Python)

'''

#¿Que funcion se usa para obtener a longitud de una lista en Python?

'''
a: length()
b: len() (Opcion correcta) Tamaño de lista
c: size()
d: count()

'''

#¿Que imprime el siguiente codigo?
#nombre = 'Diego'
#print(nombre[1])

'''
a: D
b: i (Opcion correcta)
c: e
d: o

'''

#Encontrar el mayor de x numeros:

'''
import random
import funciones as fp

numero_min = 0
numero_max = 0
acumulador = 0
lista_numeros = []

cantidad_numeros = fp.ingresar_numero("Ingresa la cantidad de numeros:")
for i in range(cantidad_numeros):
    num = random.randit(0,100000)
    acumulador += num
    promedio = acumulador / cantidad_numeros
    lista_numeros.append(num)
    if num >= numero_max:
        numero_max = num
    if num <= numero_min:
        numero_min = num

print(f"Los numeros seleccionados aleatorios fueron: {lista_numeros}")
print(f"El numero maximo es: {numero_max}")
print(f"El numero minimo es: {numero_min}")
print(f"El promedio de los {cantidad_numeros} elegido es: {promedio}")

'''

#Trivias:

#¿Es lo mismo poner  variable +=1  que variable =+1?

'''
variable += 1 incrementa el valor actual de variable en 1.
variable =+ 1 simplemente asigna el valor 1 a variable.

'''

#Puedo nombrar una variable así?  case_snake = "snake_case"?

''''
Sí, puedes nombrar una variable así: case_snake = "snake_case"

'''

#Que imprime este algoritmo?

'''
a = 100
b = 10
elif a > b :
    print (" a es mayor a b)

'''

'''

El código que has proporcionado tiene un error de sintaxis y, por lo tanto, 
no se ejecutará correctamente.

errores: 

-elif sin un if previo
-sintaxis debido a la comilla de cierre que falta en print

'''
#Sabemos que las variables bool (boolean) son para definir una valor True o False , 
#podemos decir que son variables de tipo  complejos?

'''
No, las variables booleanas (bool) en Python no se consideran variables de tipo complejo. En Python, 
el tipo bool es un tipo de datos básico y simple, no complejo. Aquí te explico por qué:

Tipos de Datos Básicos y Compuestos en Python

Tipos de Datos Básicos:

int (entero): Representa números enteros.
float (punto flotante): Representa números decimales.
bool (booleano): Representa valores True o False.
str (cadena de texto): Representa secuencias de caracteres.
Los booleanos (bool) son un tipo de dato simple que puede tener solo dos valores: True o False. 
Son un subconjunto del tipo int en Python (donde True se trata como 1 y False como 0) y se utilizan principalmente 
para controlar el flujo de programas y tomar decisiones basadas en condiciones.

Tipos de Datos Compuestos:

list (lista): Una colección ordenada y mutable de elementos.
tuple (tupla): Una colección ordenada e inmutable de elementos.
dict (diccionario): Una colección desordenada de pares clave-valor.
set (conjunto): Una colección desordenada de elementos únicos.
Los tipos de datos compuestos pueden contener múltiples valores de diferentes tipos, 
mientras que los booleanos son simplemente una representación de una condición de verdad o falsedad 
y no contienen múltiples valores.

Conclusión:
En resumen, el tipo bool no es un tipo de datos complejo en Python; es un tipo de datos básico. 
Los tipos complejos se refieren a estructuras de datos que pueden almacenar colecciones de elementos 
o combinaciones de otros tipos de datos.

'''

#Seleccione la correcta :

'''
Class Hola: 
Method Hola:
Object Hola:


1- Class (Clase): En Python, una clase es una plantilla para crear objetos. 
Define un conjunto de atributos y métodos que el objeto creado a partir de la clase tendrá. 
La sintaxis para definir una clase es:

class Hola:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def saludar(self):
        print(self.mensaje)

2- Method (Método): Un método es una función definida dentro de una clase que opera sobre los objetos de esa clase. 
Los métodos suelen tomar self como primer parámetro, que se refiere al objeto mismo. 
Ejemplo:

def saludar(self):
    print(self.mensaje)

3- Object (Objeto): Un objeto es una instancia de una clase. Es una entidad creada a partir de una clase 
que tiene atributos y métodos definidos por esa clase. 
Ejemplo de creación de un objeto:

hola_objeto = Hola("¡Hola, mundo!")
hola_objeto.saludar()  # Imprime: ¡Hola, mundo!


Selección Correcta:

Class: Se refiere a la plantilla para crear objetos.
Method: Se refiere a las funciones definidas dentro de una clase que operan sobre los objetos.
Object: Se refiere a una instancia de una clase.
En la lista de términos que has proporcionado:

Class Hola: Es la definición de una clase en Python.
Method Hola: No es correcto, ya que Hola no es un método, sino el nombre de la clase. 
Un método sería algo como def metodo(self):.
Object Hola: No es una terminología estándar, pero si te refieres a un objeto creado a partir de la clase Hola, 
el término correcto sería simplemente "object" o "instancia de la clase Hola".
Si tienes que seleccionar cuál es el término correcto en el contexto de la programación orientada a objetos, 
el más adecuado sería Class para la definición de una clase.

'''
#Que imprime ? 

'''
a=100
b=a
a=a+10
print (b)

el código imprime: 100
'''
