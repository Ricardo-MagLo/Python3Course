#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero = int(input('Introduzca un número entero positivo: '))

for i in range(1,numero+1,2):
    j = i
    for j in  range(j,0,-2):
        print(j,end= ' ')
    print('')