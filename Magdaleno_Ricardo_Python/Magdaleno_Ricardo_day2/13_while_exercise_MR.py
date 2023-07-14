#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    frase = input('Introduzca una palabra o frase: ')
    if frase.lower() == 'salir':
        break
    print(f'¡{frase}!')
    