#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input('Ingresa tu nombre: ')
repeticiones = int(input('Ingresa un número entero: '))

for i in range(0,repeticiones):
    print(nombre)