lista_pacientes = []
rut = input("Favor, digitar rut de paciente: ")
nombre = input("Por favor, escribir nomnbre de paciente: ")
edad = float(input("Digitar edad de paciente: "))
ritmo = float(input("Favor, digitar ritmo cardiaco: "))
lista_paciente = [rut, nombre, edad, ritmo]
presion = float(input("Ingrese presion arterial: "))
lista_paciente.append(presion)
lista_general_pacientes = [lista_paciente]
indice_riesgo = abs(ritmo - 80) + abs(presion - 120)
if ritmo < 50 or ritmo > 120 or presion < 70 or presion > 160:
    print("Paciente crítico")
    print(f"Índice de riesgo: {indice_riesgo}")
elif ritmo < 60 or ritmo > 90 or presion < 90 or presion > 130:
    print("Paciente en observación")
    print(f"índice de riesgo: {indice_riesgo}")
else:
    print("Paciente normal")
buscar = input("¿Qué paciente quiere buscar? (rut o nombre): ")
encontrado = False
for paciente in lista_general_pacientes:
     if buscar.lower() == paciente[0].lower() or buscar.lower() == paciente[1].lower():
         print(f"Paciente encontrado: {paciente[0]}, {paciente[1]}")
         encontrado = True
         break
if encontrado == False:
    print("Paciente no encontrado")
eliminar = input("¿Qué paciente desea dar de alta? (rut o nombre): ")
for paciente in lista_pacientes:
    if eliminar.lower() == paciente[0].lower or eliminar.lower() == paciente[1].lower():
        lista_general_pacientes.remove(paciente)
        print(f"Paciente {paciente[1]} ha sido dado de alta")
        break
