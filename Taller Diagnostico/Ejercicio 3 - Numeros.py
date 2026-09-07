# Ejercicio 3 - Números

# Mostrar numeros del 1 al 100
print("Numeros del 1 al 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n") # Salto de línea para separar las secciones

# Mostrar numeros pares
print("Numeros pares:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# Mostrar numeros impares
print("Numeros impares:")
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")

# Mostrar numeros múltiplos de 5
print("Numeros múltiplos de 5:")
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")
print("\n")

# Mostrar suma de los números del 1 al 100
suma = 0
for i in range(1, 101):
    suma += i
print(f"Suma de numeros del 1 al 100:\nResultado: {suma}")