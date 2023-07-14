#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
# los números impares desde 1 hasta ese número separados por comas.

numero = int(input('Ingrese un número entero positivo: '))

for i in range(1,numero,2):
    print(i,end=', ')
    
