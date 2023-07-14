#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input('Ingrese su correo electrónico: ')
i = correo.find('@')
print(correo[:i+1]+'ceu.es')