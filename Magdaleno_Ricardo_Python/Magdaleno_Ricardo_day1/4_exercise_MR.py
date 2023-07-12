#Magdaleno Loaiza Ricardo Daniel
#11-07-23

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
# la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input('Ingrese su peso en kilogramos: '))
estatura = float(input('Ingrse su estatura en metros: '))
IMC = peso/(estatura**2)
IMC = round(IMC,2)
print('Tu ínidice de masa corporal es', IMC)

