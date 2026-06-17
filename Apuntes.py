# Crear la lista con las mediciones de temperatura indicadas
temperaturas = [36.7, 37.2, 38.1] 
 
# Acceder a la primera (índice 0) y última medición (índice -1)
primera = temperaturas[0] 
ultima = temperaturas[-1] 
 
# Imprimir los resultados
print(f"Primera temperatura: {primera}°C") 
print(f"Última temperatura: {ultima}°C") 

# 1. Iniciar lista vacía
medicamentos = [] 
 
# 2. Agregar al final medicamentos menos urgentes (append) 
medicamentos.append("Paracetamol") 
medicamentos.append("Ibuprofeno") 
 
# 3. Insertar al inicio el insumo de máxima urgencia (insert) 
medicamentos.insert(0, "Suero fisiológico") 
 
# Imprimir la lista completa y la cantidad total usando len() 
print("Lista de medicamentos administrados:", medicamentos) 
print("Cantidad total de medicamentos:", len(medicamentos)) 

# Lista inicial de tratamientos dentales
tratamientos = ["Limpieza", "Radiografía", "Extracción"] 
 
# Modificar el índice 1 por el término correcto
tratamientos[1] = "Radiografía panorámica" 
 
# Eliminar el último elemento con pop() y guardarlo en una variable
tratamiento_eliminado = tratamientos.pop() 
 
# Eliminar "Limpieza" por su nombre usando remove() 
tratamientos.remove("Limpieza") 
 
# Mostrar resumen final d tratamientos y cantidad restante usando len()
print("Lista final de tratamientos:", tratamientos) 
print("Elemento eliminado por pop():", tratamiento_eliminado) 
print("Cantidad restante de tratamientos:", len(tratamientos)) 

# Lista de ejemplo de pacientes registrados
pacientes = ["Ana García", "Luis Martínez", "María Rojas", "Pedro Soto"] 
 
# Solicitar el nombre al usuario 
nombre_buscar = input("Ingrese el nombre del paciente a verificar: ") 
 
# Validación preventiva usando el operador 'in' [cite: 13, 15, 17] 
if nombre_buscar in pacientes: 
   # Si existe, obtenemos su ubicación exacta en la lista con index()
   posicion = pacientes.index(nombre_buscar) 
   print(f"El paciente '{nombre_buscar}' ya está registrado en la posición (índice): {posicion}.") 
else: 
   # Mensaje de error si no se encuentra en el registro 
   print("Error: El paciente no se encuentra registrado en el sistema.") 

# Datos de ejemplo de la semana del paciente
glucosas = [140, 180, 160, 180, 150] 
 
# Hallar el valor más alto con max() 
max_glucosa = max(glucosas) 
 
# Contar cuántas veces se repitió ese valor crítico usando count()
frecuencia = glucosas.count(max_glucosa) 
 
# Mostrar el resumen clínico interpretado 
print("--- RESUMEN CLÍNICO DE DIABETES ---") 
print(f"Valor máximo de glucosa registrado: {max_glucosa} mg/dL") 
print(f"Frecuencia (veces que se repitió en la semana): {frecuencia} veces") 

# Temperaturas tomadas en el triaje respiratorio 
temperaturas = [36.5, 38.2, 37.1, 39.0, 36.8] 
 
print("Lista original de temperaturas:", temperaturas)
 
# Ordenar de menor a mayor (ascendente) 
temperaturas.sort() 
print("Temperaturas ordenadas de menor a mayor:", temperaturas) 
 
# Reordenar de mayor a menor (descendente) para priorizar urgencias
temperaturas.sort(reverse=True) 
print("Priorización de urgencias (mayor a menor):", temperaturas) 
 
# Explicación clínica del orden descendente 
print("\nUtilidad en Urgencias: El orden descendente permite colocar de forma automática " 
     "a los pacientes con los cuadros febriles más altos en las primeras posiciones de la lista, " 
     "facilitando una atención médica inmediata según la gravedad.") 