# Ejercicio 8 - Búsqueda

# Lista de productos
print("Bienvenido busca tu producto")
print("Listado de productos disponibles: Teclado, Mouse, Monitor, Impresora, Memoria RAM, Disco SSD")

productos = ("Teclado", "Mouse", "Monitor", "Impresora", "Memoria RAM", "Disco SSD")

busqueda = input("Que producto desea comprar: ")

# Buscador
busqueda_limpia = busqueda.strip().lower()

encontrado = False

for prod in productos:
    if prod.lower() == busqueda_limpia:
        encontrado = True
        break 

# Resspuesta final a usario
if encontrado:
    print(f"Resultado: El producto {busqueda} Si esta disponible en el inventario.")
else:
    print(f"Resultado: El producto {busqueda} No esta disponible en el inventario.")

# Explicar brevemente cómo hizo el programa para recorrer la lista. 

# El programa utiliza el bucle for. Para cada elemento compara si el elemento coincide con la búsqueda. Si se encuentra una coincidencia, establece 'encontrado' como True y rompe el bucle.