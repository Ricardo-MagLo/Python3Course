#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

numero = int(input('Introduzca un número entero positivo: '))

for i in range(1,numero+1):
    print('*'*i)
    