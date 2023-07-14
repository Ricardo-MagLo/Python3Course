#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta
# atrás desde ese número hasta cero separados por comas.

numero = int(input('Ingrese un número entero positivo: '))

for i in range(numero, 0, -1):
    print(i, end=',')
print('0')
    

