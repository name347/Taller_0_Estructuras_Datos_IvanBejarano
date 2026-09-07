# Ejercicio 4 — Calculadora

def sumar_dos_numeros(primer_numero, segundo_numero):
    resultado_de_la_suma = primer_numero + segundo_numero
    return resultado_de_la_suma

def restar_dos_numeros(primer_numero, segundo_numero):
    resultado_de_la_resta = primer_numero - segundo_numero
    return resultado_de_la_resta

def multiplicar_dos_numeros(primer_numero, segundo_numero):
    resultado_de_la_multiplicacion = primer_numero * segundo_numero
    return resultado_de_la_multiplicacion

def dividir_dos_numeros(primer_numero, segundo_numero):
    if segundo_numero == 0:
        return "Error: No se puede dividir entre cero."
    resultado_de_la_division = primer_numero / segundo_numero
    return resultado_de_la_division

while True:
    print("=========================")
    print("       CALCULADORA")
    print("=========================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion_seleccionada_por_el_usuario = input("Seleccione una opción (1-5): ")
    print("--------------------------------------------------------")
    
    if opcion_seleccionada_por_el_usuario == "5":
        print("Saliendo de la calculadora... ¡Hasta luego!")
        print("--------------------------------------------------------")
        break
        
    if opcion_seleccionada_por_el_usuario == "1" or opcion_seleccionada_por_el_usuario == "2" or opcion_seleccionada_por_el_usuario == "3" or opcion_seleccionada_por_el_usuario == "4":
        # Datos requeridos para las operaciones matematicas
        primer_numero_ingresado = float(input("Escribe tu primer número: "))
        segundo_numero_ingresado = float(input("Escribe tu segundo número: "))
        print("--------------------------------------------------------")
        
        print("Resultados de la operacion seleccionada:")
        if opcion_seleccionada_por_el_usuario == "1":
            print(f"Resultado: {sumar_dos_numeros(primer_numero_ingresado, segundo_numero_ingresado)}")
        elif opcion_seleccionada_por_el_usuario == "2":
            print(f"Resultado: {restar_dos_numeros(primer_numero_ingresado, segundo_numero_ingresado)}")
        elif opcion_seleccionada_por_el_usuario == "3":
            print(f"Resultado: {multiplicar_dos_numeros(primer_numero_ingresado, segundo_numero_ingresado)}")
        elif opcion_seleccionada_por_el_usuario == "4":
            print(f"Resultado: {dividir_dos_numeros(primer_numero_ingresado, segundo_numero_ingresado)}")
        print("=================================\n")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        print("=================================\n")
