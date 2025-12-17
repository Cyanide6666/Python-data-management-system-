import gestion  # Importación del módulo de los empleados

def imprimir_tabla(lista):
    """Formateo de salida con f-strings."""
    print(f"\n{'ID':<4} | {'NOMBRE':<15} | {'PUESTO':<12} | {'SALARIO':<10}")
    print("-" * 50)
    for e in lista:
        # Uso de f-strings para alinear columnas y redondear decimales
        print(f"{e['id']:<4} | {e['nombre']:<15} | {e['puesto']:<12} | ${e['salario']:>9.2f}")

def main():
    #Carga inicial de datos
    datos = gestion.cargar_desde_archivo("datos.txt")
    
    if not datos:
        return

    while True: # Bucle para iteraciones eficientes
        print("\n--- MENÚ DE GESTIÓN DE DATOS ---")
        print("1. Visualizar todos los empleados")
        print("2. Calcular nómina total de sueldos")
        print("3. Gestión de ganancias del año")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            imprimir_tabla(datos)
        
        elif opcion == "2":
            total = gestion.calcular_nomina_recursiva(datos)
            print(f"\n>>> El total de salarios procesado es: ${total:,.2f}")

        elif opcion == "3":
            # Cargamos los datos del las ganancias de la empresa durante el año
            ganancias = gestion.cargar_ganancias("ganancias.txt")
            
            if not ganancias:
                print("Error: No se encontró el archivo de ganancias.")
                continue

            print("\n--- SUB-MENÚ DE GANANCIAS ---")
            print("a. Ver lista entera de ganancias")
            print("b. Ver ganancia total del año (Suma)")
            print("c. Buscar ganancia de un mes específico")
            sub_opcion = input("Seleccione una opción: ").lower()

            if sub_opcion == "a":
                print("\n{:<15} | {:>12}".format("MES", "GANANCIA"))
                print("-" * 30)
                for g in ganancias:
                    print(f"{g['mes']:<15} | ${g['monto']:>12,.2f}")

            elif sub_opcion == "b":
                total = gestion.suma_recursiva_ganancias(ganancias)
                print(f"\nLa ganancia total de los 11 meses es: ${total:,.2f}")

            elif sub_opcion == "c":
                mes_buscado = input("Escriba el mes que desea consultar: ").capitalize()
                encontrado = False
                for g in ganancias:
                    if g['mes'] == mes_buscado:
                        print(f"La ganancia de {mes_buscado} fue: ${g['monto']:,.2f}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Mes no encontrado en el registro.")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo!")

if __name__ == "__main__":
    main()