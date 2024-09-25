'''
Ejercicio 2: Crear una clase de Cuenta Bancaria

Objetivo: Implementar una clase CuentaBancaria que permita a los usuarios realizar operaciones bancarias 
básicas como depositar, retirar y consultar el saldo.
'''
import funciones as fp

class CuentaBancaria:
    def __init__(self,saldo: int | None = 0 ,titular:str | None = "")->None:
        self.saldo = saldo
        self.titular = titular

    def deposito(self)-> int:
        deposito = fp.ingresar_numero("Ingrese el valor a depositar:$ ")
        self.saldo += deposito
        print(f"Usted a depositado a su cuenta:$ {deposito} ")
        return deposito
    
    def retiro(self)-> int:
        retiro = fp.ingresar_numero("Ingrese el valor a retirar:$ ")
        if retiro <= self.saldo and retiro >0:
            self.saldo -= retiro
            print(f"Usted ha retirado de su cuenta:$ {retiro}")
        else:
            print("Saldo insuficiente para realizar esta operacion $$")
        return
    
    def consulta(self):
        self.actual = self.saldo
        print(f"Su saldo actual es:$ {self.saldo}")

nombre = input("Bienvenido, Ingrese su nombre: ")
cuenta = CuentaBancaria(0,nombre)

while True:
    menu = int(input("Que tarea desea realizar:  \n 1: _ Deposito de Efectivo $ \n 2: _ Retiro de Efectivo $ \n 3: _ Consulta de Saldo $$ \n 4: _ Salir \n:"))
    if menu == 1 :
        cuenta.deposito()
    elif menu == 2:
        cuenta.retiro()
    elif menu == 3:
        cuenta.consulta()
    elif menu == 4:
        break
    else:
        print("Ingreso una opcion invalida")
