# Ejercicio 6 - Estudiantes

# Lista de estudiantes
estudiantes = ("Brenda", "Jasmine", "Jhonny", "Jeison", "Kevin", "Ivan", "Alejandra", "Lina", "Victor", "Sofia")

# Informaciones sobre los estudiantes
print("Todos los estudiantes:", ", ".join(estudiantes))

print("Primer estudiante:", estudiantes[0])

print("Último estudiante:", estudiantes[-1])

print("Cantidad total de estudiantes:", len(estudiantes))

# Estados finales de lista de estudiantes
estudiantes = list(estudiantes)
estudiantes.append("Santiago")
print("La lista tras agregar a Santiago es:", ", ".join(estudiantes))

estudiantes.remove("Jasmine")
print("La lista despues de eliminar a Jasmine es:", ", ".join(estudiantes))

buscado = "Gallego"
if buscado in estudiantes:
    print(f"Buscando... {buscado} Si esta en la lista.")
else:
    print(f"Buscando... {buscado} NO esta en la lista.")

# ¿qué diferencia existe entre tener estudiante1, estudiante2, estudiante3... y tener una sola lista estudiantes?

#  Las variables individuales son estaticas y llevando a necesitar escribir líneas de código repetidas para cada una de ellas. en cambio una lista agrupa todos los datos con solo un nombre pudiendo hacer todo tipo de acciones con estos con menos instrucciones de control dinamico para tales es rebundante decir estudiante1, estudiante2, estudiante3 hasta estudiante 10 para 10 estudiantes envez de poner solamente los 10 nombres en una lista y poder trabajar de manera ,as directa con ellos.