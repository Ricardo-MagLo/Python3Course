#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')

largo = len(frase)
i = 0
contador = 0

while i < largo:
    if frase[i].lower() == letra.lower():
        contador += 1
    i += 1
print(f'La letra {letra} aparece {contador} veces en la frase.')