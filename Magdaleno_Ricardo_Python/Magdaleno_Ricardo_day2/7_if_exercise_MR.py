#Ricardo Daniel Magdaleno Loaiza
#12-07-23

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú 
# con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

Menu_Vegetariano = '''
Menú Vegetariano:
    Pimiento
    Tofu
'''
Menu_noVegetariano = '''
Menú no vegetariano:
    Peperoni
    Jamón
    Salmón
'''
eleccion = input('Ingrese vegetariana o no vegetariana: ')
Ingrediente = ''

if eleccion.lower() == 'vegetariana':
    print(Menu_Vegetariano)
else:
    print(Menu_noVegetariano)

Ingrediente = input('Ingrese el ingrediente que desea: ')
print(f'\nSe eligió una pizza {eleccion} que lleva tomate, mozzarella y {Ingrediente}')