#Magdaleno Loaiza Ricardo Daniel
#11-07-23

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

Ahorro_inicial = float(input('Ingrese la cantidad a depositar: '))
year1 = Ahorro_inicial + (Ahorro_inicial*0.04)
year2 = year1 + (year1*0.04)
year3 = year2 + (year2*0.04)

print('Ahorro inicial:',round(Ahorro_inicial,2))
print('Ahorro después de 1 año:',round(year1,2))
print('Ahorro después de 2 años:',round(year2,2))
print('Ahorro después de 3 año:',round(year3,2))
