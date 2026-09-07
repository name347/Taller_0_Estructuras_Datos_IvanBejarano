# Ejercicio 7 - Notas

# Notas de los estudiantes
notas = [3.5, 4.2, 2.8, 4.5, 3.9, 2.5, 4.0, 4.7]

# Contador de Notas
contero_estudiantes = 0
for n in notas:
    contero_estudiantes += 1

# Sumador y promediador de las notas
suma_notas = 0
nota_mayor = notas[0]  
nota_menor = notas[0]  
aprobados = 0
reprobados = 0

for n in notas:

    suma_notas += n
    
    if n > nota_mayor:
        nota_mayor = n
        
    if n < nota_menor:
        nota_menor = n
        
    if n >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma_notas / contero_estudiantes

notas_mayores_promedio = []
for n in notas:
    if n > promedio:
        notas_mayores_promedio.append(n)

# Resultados finales
print("=========================================")
print("          RESULTADOS EJERCICIO 7")
print("=========================================")
print(f"Número de estudiantes total: {contero_estudiantes}")
print(f"Promedio final del grupo: {promedio:.2f}")
print(f"Mayor nota encontrada: {nota_mayor}")
print(f"Menor nota encontrada: {nota_menor}")
print(f"Numero de aprobados: {aprobados}")
print(f"Numero de reprobados: {reprobados}")
print(f"Notas superiores al promedio: {notas_mayores_promedio}")
print("=========================================")
