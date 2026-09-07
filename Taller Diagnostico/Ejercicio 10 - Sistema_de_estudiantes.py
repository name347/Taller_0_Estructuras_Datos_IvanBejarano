# Ejercicio 10 - Sistema de estudiantes

# Lista inicial de estudiantes en formato de matriz
base_de_datos_estudiantes = [
    ["Carlos", 20, 4.2],
    ["María", 19, 3.8],
    ["Juan", 21, 2.7]
]

# Definiciones de las funciones para el control de los datos
def registrar_nuevo_estudiante():
    print("--------------------------------------------------------")
    print("      Registrar nuevo estudiante")
    print("--------------------------------------------------------")
    nombre_del_estudiante = input("Escribe el nombre del estudiante: ")
    edad_del_estudiante = int(input("Escribe la edad del estudiante: "))
    
    while True:
        nota_del_estudiante = float(input("Escribe la nota definitiva (0.0 a 5.0): "))
        if nota_del_estudiante >= 0.0 and nota_del_estudiante <= 5.0:
            break
        print("Error: la nota ingresada no es válida. Debe estar entre 0.0 y 5.0.")
        
    base_de_datos_estudiantes.append([nombre_del_estudiante, edad_del_estudiante, nota_del_estudiante])
    print(f"¡Estudiante {nombre_del_estudiante} registrado con éxito!")
    print("=================================\n")

def mostrar_lista_de_estudiantes():
    print("--------------------------------------------------------")
    print("      Lista completa de estudiantes")
    print("--------------------------------------------------------")
    if not base_de_datos_estudiantes:
        print("No existen estudiantes registrados en el sistema.")
        print("=================================\n")
        return
    
    contero_de_posicion = 1
    for est in base_de_datos_estudiantes:
        print(f"{contero_de_posicion}. Nombre: {est[0]} | Edad: {est[1]} años | Nota: {est[2]}")
        contero_de_posicion += 1
    print("=================================\n")

def buscar_un_estudiante():
    print("--------------------------------------------------------")
    print("      Buscar un estudiante")
    print("--------------------------------------------------------")
    nombre_a_buscar = input("Escribe el nombre del estudiante que deseas buscar: ")
    nombre_buscado_limpio = nombre_a_buscar.strip().lower()
    estudiante_encontrado = False
    
    for est in base_de_datos_estudiantes:
        if est[0].lower() == nombre_buscado_limpio:
            print(f"\n¡Estudiante encontrado con éxito!")
            print(f"Nombre: {est[0]} | Edad: {est[1]} años | Nota: {est[2]}")
            estudiante_encontrado = True
            break
            
    if estudiante_encontrado == False:
        print("El estudiante ingresado no se encuentra en el sistema.")
    print("=================================\n")

def mostrar_promedio_general():
    print("--------------------------------------------------------")
    print("      Promedio general del grupo")
    print("--------------------------------------------------------")
    if not base_de_datos_estudiantes:
        print("No hay notas registradas para calcular un promedio.")
        print("=================================\n")
        return
        
    suma_total_de_notas = 0.0
    cantidad_de_estudiantes = 0
    for est in base_de_datos_estudiantes:
        suma_total_de_notas += est[2]
        cantidad_de_estudiantes += 1
        
    promedio_final_del_grupo = suma_total_de_notas / cantidad_de_estudiantes
    print(f"El promedio de notas de todo el grupo es: {promedio_final_del_grupo:.2f}")
    print("=================================\n")

def mostrar_nota_extrema_del_grupo(tipo_de_busqueda):
    if not base_de_datos_estudiantes:
        print("--------------------------------------------------------")
        print("No hay estudiantes registrados en el sistema.")
        print("=================================\n")
        return
        
    nota_extrema_encontrada = base_de_datos_estudiantes[0][2]
    nombre_del_estudiante_extremo = base_de_datos_estudiantes[0][0]
    
    for est in base_de_datos_estudiantes:
        if tipo_de_busqueda == "mayor" and est[2] > nota_extrema_encontrada:
            nota_extrema_encontrada = est[2]
            nombre_del_estudiante_extremo = est[0]
        elif tipo_de_busqueda == "menor" and est[2] < nota_extrema_encontrada:
            nota_extrema_encontrada = est[2]
            nombre_del_estudiante_extremo = est[0]
            
    print("--------------------------------------------------------")
    print(f"Resultados de nota extrema ({tipo_de_busqueda}):")
    print("--------------------------------------------------------")
    print(f"La nota más {tipo_de_busqueda} es de {nombre_del_estudiante_extremo} con: {nota_extrema_encontrada}")
    print("=================================\n")

def mostrar_estudiantes_aprobados():
    print("--------------------------------------------------------")
    print("      Lista de estudiantes aprobados (nota >= 3.0)")
    print("--------------------------------------------------------")
    contero_de_aprobados = 0
    cantidad_total_alumnos = 0
    
    for est in base_de_datos_estudiantes:
        cantidad_total_alumnos += 1
        if est[2] >= 3.0:
            print(f"• {est[0]} (Nota obtenida: {est[2]})")
            contero_de_aprobados += 1
            
    print(f"\nTotal de estudiantes aprobados: {contero_de_aprobados} de {cantidad_total_alumnos}")
    print("=================================\n")


# Programa principal
while True:
    print("========================================")
    print("         SISTEMA DE ESTUDIANTES")
    print("========================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio")
    print("5. Mostrar mayor nota")
    print("6. Mostrar menor nota")
    print("7. Mostrar aprobados")
    print("8. Salir")
    print("========================================")
    
    opcion_seleccionada_por_el_usuario = input("Seleccione una opción (1-8): ")
    print("--------------------------------------------------------")
    
    if opcion_seleccionada_por_el_usuario == "8":
        print("Cerrando el sistema de administración...")
        print("--------------------------------------------------------")
        break
        
    if opcion_seleccionada_por_el_usuario == "1":
        registrar_nuevo_estudiante()
    elif opcion_seleccionada_por_el_usuario == "2":
        mostrar_lista_de_estudiantes()
    elif opcion_seleccionada_por_el_usuario == "3":
        buscar_un_estudiante()
    elif opcion_seleccionada_por_el_usuario == "4":
        mostrar_promedio_general()
    elif opcion_seleccionada_por_el_usuario == "5":
        mostrar_nota_extrema_del_grupo("mayor")
    elif opcion_seleccionada_por_el_usuario == "6":
        mostrar_nota_extrema_del_grupo("menor")
    elif opcion_seleccionada_por_el_usuario == "7":
        mostrar_estudiantes_aprobados()
    else:
        print("Opción inválida. Digite un número válido entre 1 y 8.")
        print("=================================\n")