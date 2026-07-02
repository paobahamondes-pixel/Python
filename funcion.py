def latidos_por_minuto(latidos, tiempo):
    """Calcula la cantidad de latidos por minuto.
    Args:
        latidos (int): Número de latidos registrados.
        tiempo (float): Tiempo en minutos durante el cual se registraron los latidos.
    Returns:
        float: Latidos por minuto.
    """
    if tiempo <= 0:
        raise ValueError("El tiempo debe ser mayor que cero.")
    return latidos / tiempo
registro_datos_pacientes = []
while True:
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    if nombre_paciente.lower() == 'salir':
        break
    try:
        latidos = int(input(f"Ingrese la cantidad de latidos registrados para {nombre_paciente}: "))
        tiempo = float(input(f"Ingrese el tiempo en minutos de la medición para {nombre_paciente}: "))
        bpm = latidos_por_minuto(latidos, tiempo)
        if bpm > 0:
            registro_datos_pacientes.append((nombre_paciente, bpm))
            print(f"-> Guardado con éxito. Paciente: {nombre_paciente}, Latidos por minuto: {bpm:.2f}\n")
        else:
            print("Error: Los latidos por minuto calculados deben ser mayores a 0.\n")
    except ValueError as e:
        print(f"Error de ingreso: {e}. Intente nuevamente con este paciente.\n")
buscar = float(input("Ingrese el valor de lpm a buscar: "))
encontrado = False
for nombre, bpm in registro_datos_pacientes:
    if bpm == buscar:
        print(f"-> Encontrado: El paciente {nombre} registró {bpm} latidos por minuto.")
        encontrado = True
if not encontrado:
    print("No se encontraron registros con ese valor exacto de LPM.")    
for i, (nombre, bpm) in enumerate(registro_datos_pacientes):
    print(f"[{i}] Paciente: {nombre}, LPM: {bpm:.2f}")
indice = int(input("Ingrese el número (índice) del registro que desea modificar: "))
if 0 <= indice < len(registro_datos_pacientes):
    nuevo_bpm = float(input("Ingrese el nuevo valor correcto de LPM: "))
    nombre_original = registro_datos_pacientes[indice][0]
    registro_datos_pacientes[indice] = (nombre_original, nuevo_bpm)
    print("Registro modificado con éxito.")
else:
    print("Índice inválido.")
indice = int(input("Ingrese el índice del registro que desea eliminar: "))
if 0 <= indice < len(registro_datos_pacientes):
    eliminado = registro_datos_pacientes.pop(indice)
    print(f"Registro de {eliminado[0]} con {eliminado[1]:.2f} lpm ha sido eliminado.")
else:
    print("Índice inválido.")
if len(registro_datos_pacientes) == 0:
    print("No hay mediciones registradas para calcular un promedio.")
else:
    suma_lpm = 0 
    for nombre, bpm in registro_datos_pacientes:
        suma_lpm += bpm
    promedio = suma_lpm / len(registro_datos_pacientes)
    print(f"\nEl promedio actual de frecuencia cardíaca es: {promedio:.2f} lpm")
    if promedio < 60:
        print("Resultado -> Alerta: Bradicardia")
    elif 60 <= promedio <= 100:
        print("Resultado -> Estado: Normal")
    else:
        print("Resultado -> Alerta: Taquicardia")   