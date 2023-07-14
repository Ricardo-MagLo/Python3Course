#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input('Ingrese una palabra: ')

largo = len(palabra)
i = -1
while largo != 0:
    print(palabra[i])
    i -= 1
    largo -= 1

