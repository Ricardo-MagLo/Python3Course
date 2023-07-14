#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = input('Ingrese la contraseña: ')

while contraseña != 'contraseña':
    contraseña = input('Ingrese la contraseña: ')
    