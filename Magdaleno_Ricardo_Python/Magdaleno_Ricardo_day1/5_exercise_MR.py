#Magdaleno Loaiza Ricardo Daniel
#11-07-23

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
# la <n> entre <m> da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

num1 = int(input('Ingrese un número entero: '))
num2 = int(input('Ingrese otro número entero: '))

cociente = int(num1/num2)
residuo = num1%num2

print(num1, 'entre', num2, 'da un cociente', cociente, 'y un resto', residuo)
