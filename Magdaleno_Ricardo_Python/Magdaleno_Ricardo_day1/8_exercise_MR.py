#Magdaleno Loaiza Ricardo Daniel
#11-07-23

# Una panadería vende barras de pan a 3.49 MXN cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

Barras_viejas = int(input('Ingrese la cantidad de barras vendidas que no son del dia: '))
costeBarra = 3.49
descuento = costeBarra*0.6
Total = Barras_viejas*(costeBarra-descuento)

print('Precio Habitual de las barras de pan: $', round(costeBarra,2), 'MXN', sep='')
print('Descuento: $', round(descuento,2), 'MXN', sep='')
print('Precio final de una barra de pan: $', round(costeBarra-descuento,2), 'MXN', sep='')
print('Precio final total de la venta: $', round(Total,2), 'MXN', sep='')
