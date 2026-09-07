# Ejercicio 9 - Notas de grupo

# Notas de los estudiantes
notas = [
 [4.0, 3.5, 4.2], # Estudiante 1
 [3.0, 4.1, 3.7], # Estudiante 2
 [4.5, 3.8, 4.0], # Estudiante 3
 [2.8, 3.2, 3.5], # Estudiante 4
 [3.9, 4.5, 4.2]  # Estudiante 5
]

# Asignaturas
asignaturas = ["Programación", "Matemáticas", "Inglés"]

# Organizador de notas
nota_mayor = notas[0][0]
nota_menor = notas[0][0]

sumas_asignaturas = [0.0, 0.0, 0.0]

# Interfaz de notas
print("=========================================")
print("Notas de los estudiantes")
print("=========================================")

for i in range(len(notas)):
    suma_estudiante = 0.0
    
    for j in range(len(notas[i])):
        nota_actual = notas[i][j]
        
        suma_estudiante += nota_actual
        
        sumas_asignaturas[j] += nota_actual
        
        if nota_actual > nota_mayor:
            nota_mayor = nota_actual
        if nota_actual < nota_menor:
            nota_menor = nota_actual
            
    promedio_estudiante = suma_estudiante / len(notas[i])
    print(f"Estudiante {i + 1}: Promedio = {promedio_estudiante:.2f}")

print("\n=========================================")
print("Promedio por asignatura")
print("=========================================")

for j in range(len(sumas_asignaturas)):
    promedio_asignatura = sumas_asignaturas[j] / len(notas)
    print(f"{asignaturas[j]}: Promedio = {promedio_asignatura:.2f}")

print("\n=========================================")
print(" Resumen de notas")
print("=========================================")
print(f"Nota mayor del grupo: {nota_mayor}")
print(f"Nota menor del grupo: {nota_menor}")
print("=========================================")