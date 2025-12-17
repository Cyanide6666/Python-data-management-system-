#Módulo para gestión de datos de empleados

def cargar_desde_archivo(nombre_archivo):
    """Carga datos y los guarda en una LISTA de DICCIONARIOS."""
    empleados = []
    try:
        with open(nombre_archivo, "r") as archivo:
            next(archivo)  # Saltamos el encabezado del txt
            for linea in archivo:
                # Limpiamos y separamos los datos
                partes = linea.strip().split(",")
                if len(partes) == 4:
                    # Creamos el diccionario
                    emp = {
                        "id": int(partes[0]),
                        "nombre": partes[1],
                        "puesto": partes[2],
                        "salario": float(partes[3])
                    }
                    empleados.append(emp)
        return empleados
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return []

def calcular_nomina_recursiva(lista_empleados):
    """Implementación de FUNCIÓN RECURSIVA para sumar salarios."""
    if not lista_empleados:
        return 0
    # Suma el primer salario y llama a la función con el resto de la lista
    return lista_empleados[0]['salario'] + calcular_nomina_recursiva(lista_empleados[1:])

# --- Lógica de Ganancias ---

def cargar_ganancias(ruta_archivo):
    """Lee el archivo y devuelve una lista de diccionarios con mes y monto."""
    lista_ganancias = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            next(f) # Para saltar el encabezado jijiji
            for linea in f:
                # Separamos mes y monto, quitando espacios y saltos de línea
                if "," in linea:
                    mes, monto = linea.strip().split(",")
                    lista_ganancias.append({"mes": mes, "monto": float(monto)})
        return lista_ganancias
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return []

def suma_recursiva_ganancias(lista):
    """Función recursiva para sumar todas las ganancias del archivo."""
    if not lista: # Si la lista está vacía, la suma es 0
        return 0
    # Suma el monto del primer elemento + el resto de la lista
    return lista[0]['monto'] + suma_recursiva_ganancias(lista[1:])