'''
Programa escrito con Python para jugar a: 

Piedra, Papel o Tijera
'''
#Mensaje de bienvenida.
print()
print("Juego de Piedra Papel o Tijeras")
print("¿Quiéres jugar? Vamos!")
print()

#Variables con uso de input.
nombre1 = input("Jugador Nº1, ingresa tu nombre: ")
print()
nombre2 = input("Jugador Nº2, ingresa tu nombre: ")
print()
jugador1 = input("¡Hola Jugador Nº1, ¿Qué eliges? ¿Piedra, Papel o Tijeras?: ")
print()
jugador2 = input("¡Hola Jugador Nº2, ¿Qué eliges? Piedra, Papel o Tijeras?: ")

#Condiciones a utilizar
condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 =="piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

#Bucle
if jugador1 == jugador2:
    print()
    print("Fue un empate!")
    print()
elif condicion1 or condicion2 or condicion3:
    print(f"Gano el jugador Nº1: {nombre1}")
    print()
else:
    print(f"Gano el jugador Nº2: {nombre2}")