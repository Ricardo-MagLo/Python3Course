#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre por pantalla si es un número primo o no.

numero = int(input('Ingrese un numero entero positivo mayor que 2: '))
ref = 2
primo = True

while ref < numero:
    if numero%ref == 0:
        primo = False
        break
    ref+=1
    
if primo:
    print('El número es primo')
else:
    print('El número no es primo')