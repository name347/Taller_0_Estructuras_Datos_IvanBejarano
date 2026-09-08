# Ejercicio 5 - Calificador múltiple

# Notas de los estudiantes
nota1 = 3.5
nota2 = 4.2
nota3 = 2.8
nota4 = 4.5
nota5 = 3.9

# Sumador y promediador de notas
suma_notas = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma_notas / 5

# Organizador de resultados
mayor_nota = max(nota1, nota2, nota3, nota4, nota5)
menor_nota = min(nota1, nota2, nota3, nota4, nota5)

# Identificador de estudiantes aprobados
aprobados = 0
if nota1 >= 3.0: aprobados += 1
if nota2 >= 3.0: aprobados += 1
if nota3 >= 3.0: aprobados += 1
if nota4 >= 3.0: aprobados += 1
if nota5 >= 3.0: aprobados += 1

# Mostrar resultados finales
print("=================================")
print("Resultados de notas")
print("=================================")
print(f"Promedio notas: {promedio:.2f}")
print(f"La nota mas alta es: {mayor_nota}")
print(f"La nota mas baja es: {menor_nota}")
print(f"Numero de estudiantes aprobados: {aprobados}")