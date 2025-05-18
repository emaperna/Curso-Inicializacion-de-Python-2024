'''
Ejercicio 4: Crear una Clase de Contador

Objetivo: Crear una clase llamada Contador que tenga un atributo en cuenta que empieza en 0. Y que posea 4 metodos, Incrementar(sumará 1),
Decrementar(restará 1, no admite negativos osea hasta maximo 0), Mostrar Contador(deberá devolver el valor actual de contador) y
Reiniciar(volverá a cero el contador)
'''
class Contador:
    def __init__(self)->None: #Init inicializa la clase (objeto)
        self.cuenta = 0 #Atributo global
        pass #No es obligatorio el pas

    def incrementar(self):
        self.cuenta = self.cuenta + 1 
        #Logica para incrementar el contador
        return

    def decrementar(self):
        verificar = self.cuenta - 1 #Varible auxiliar para ver si se puede restar
        if verificar < 0 :
            print("No se puede restar")
        else: 
            self.cuenta = self.cuenta - 1
        #Logica para decrementar el contador
        return
    
    def mostrar_contador(self):
        print(f"El valor de contador es : {self.cuenta}")
        #Logica para mostrar el contador
        return
    
    def reiniciar(self):
        self.cuenta = 0 
        #Logica para reiniciar el contador
        return 
    
cuenta = Contador()
cuenta.mostrar_contador()
cuenta.incrementar()
cuenta.incrementar()
cuenta.mostrar_contador()
cuenta.decrementar()
cuenta.decrementar()
cuenta.decrementar()
cuenta.mostrar_contador()
cuenta.reiniciar()