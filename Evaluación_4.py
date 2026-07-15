lista_de_pacientes = []

def menú_principal():
    while True:
        nombre = input("\nIngrese el nombre del paciente (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        peso = float(input("Ingrese el peso en kilogramos: "))
        estatura = float(input("Ingrese la estatura en metros (ejemplo: 1.65): "))
        
        
        lista_de_pacientes.append((nombre, peso, estatura))

    print("\nResultados de los Pacientes")
    for nombre, peso, estatura in lista_de_pacientes:
        imc = peso / (estatura ** 2)
        
        if imc < 18.5:
            print(f"Paciente: {nombre}, IMC: {imc:.2f} - Bajo peso")
        elif imc >= 18.5 and imc <= 24.9:
            print(f"Paciente: {nombre}, IMC: {imc:.2f} - Peso normal")
        else:
            print(f"Paciente: {nombre}, IMC: {imc:.2f} - Sobrepeso")


def buscar_paciente():
    buscar = input("\nIngrese el nombre del paciente que desea buscar: ")
    encontrado = False
    for paciente in lista_de_pacientes:
        if buscar.lower() == paciente[0].lower():
            imc_buscado = paciente[1] / (paciente[2] ** 2)
            print(f"Paciente encontrado: {paciente[0]}, IMC: {imc_buscado:.2f}")
            encontrado = True
            break
    if not encontrado:
        print("Paciente no encontrado.")


def actualizar_paciente():
    actualizar = input("\n¿Desea actualizar el IMC de algún paciente? (si/no): ")

    if actualizar.lower() == 'si':
        encontrado = False 
        nombre_a_actualizar = input("Ingrese el nombre del paciente que desea actualizar: ")
        
        for i, paciente in enumerate(lista_de_pacientes):
            if nombre_a_actualizar.lower() == paciente[0].lower():
                nuevo_peso = float(input("Ingrese el nuevo peso en kilogramos: "))
                nueva_estatura = float(input("Ingrese la nueva estatura en metros: "))
                nuevo_imc = nuevo_peso / (nueva_estatura ** 2)
                
                
                lista_de_pacientes[i] = (nombre_a_actualizar, nuevo_peso, nueva_estatura)
                encontrado = True
                break
                
        if not encontrado:
            print("Paciente no encontrado.")
        else:
            print(f"IMC actualizado para {nombre_a_actualizar}: {nuevo_imc:.2f}")


def eliminar_paciente():
    eliminar = input("\n¿Desea eliminar algún paciente? (si/no): ")
    
    if eliminar.lower() == 'si':
        encontrado = False
        nombre_a_eliminar = input("Ingrese el nombre del paciente que desea eliminar: ")
        
        for paciente in lista_de_pacientes:
            if nombre_a_eliminar.lower() == paciente[0].lower():
                lista_de_pacientes.remove(paciente)
                print(f"Paciente {nombre_a_eliminar} eliminado.")
                encontrado = True
                break
                
        if not encontrado:
            print("Paciente no encontrado.")


def salir_del_programa():
    salir = input("\n¿Desea salir del programa? (si/no): ")
    if salir.lower() == 'si':
        print("Gracias por usar el sistema. Hasta pronto.")
        return True
    else:
        print("Continuando con el programa...")
        return False






while True:
    menú_principal()       
    buscar_paciente()      
    actualizar_paciente()  
    eliminar_paciente()    
    
    
    if salir_del_programa() == True:
        break