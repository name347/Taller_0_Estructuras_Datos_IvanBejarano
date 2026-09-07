# Ejercicio 2 - Estado académico

# Pedir nota al usuario
nota = float(input("Ingrese su nota definitiva (0.0 a 5.0): "))

# Revisor de notas y mostrar resultado
if nota < 0.0 or nota > 5.0:
    print("=================================")
    print("Resultado: No valido. Ingresa un valor entre 0.0 y 5.0.")
    print("=================================")
elif nota >= 3.0:
    print("=================================")
    print("Resultado: Has aprobado el curso.")
    print("=================================")
else:
    print("=================================")
    print("Resultado: Has reprobado el curso.")
    print("=================================")