#Magdaleno Loaiza Ricardo Daniel
#11-07-23

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas 
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payasos = int(input('Ingrese la cantidad de payasos vendidos: '))
munecas = int(input('Ingrese la cantidad de muñecas vendidas: '))

pesoPayasos = payasos*112
pesoMunecas = munecas*75

pesoTotal = pesoPayasos + pesoMunecas

print('El peso total del paquete a enviar es de', pesoTotal,'gramos.')

