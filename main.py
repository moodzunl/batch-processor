from core.proceso import Proceso
from core.ejecucion import mostrar_todos_los_procesos, crear_y_ejecutar_lotes
from utils.helpers import limpiar_pantalla, mostrar_banner

# Registro global de IDs de procesos utilizados
ids_procesos_utilizados = set()
procesos = []

def crear_proceso(id_proceso, nombre_programador, operacion, dato1, dato2, tiempo_max_estimado):
    if id_proceso in ids_procesos_utilizados:
        raise ValueError(f"ID {id_proceso} IS ALREADY IN USE.")
    nuevo_proceso = Proceso(id_proceso, nombre_programador, operacion, dato1, dato2, tiempo_max_estimado)
    ids_procesos_utilizados.add(id_proceso)
    procesos.append(nuevo_proceso)

def solicitar_datos_proceso():
    while True:  # Bucle infinito para permitir la entrada continua de procesos
        try:
            # Solicitar al usuario que ingrese 'salir' para terminar la adición de procesos
            comando = input("TYPE 'EXIT' TO STOP ADDING PROCEESS INTO BATCH SIM, ELSE PRESS ENTER: ").strip().lower()
            if comando == 'exit':
                break  # Salir del bucle si el usuario desea terminar

            id_proceso = int(input("TYPE THE PROCESS ID: "))
            if id_proceso in ids_procesos_utilizados:
                raise ValueError("THE ID IS ALREADY IN USE. PLEASE, TRY AGAIN.")

            nombre_programador = input("TYPE THE PROGRAMMER'S NAME: ")
            if nombre_programador.strip() == "":
                raise ValueError("THE PROGRAMMER'S NAME CANNOT BE EMPTY. PLEASE, TRY AGAIN.")

            operacion = input("TYPE THE OPERATION (+, -, *, /, %, **):")
            if operacion not in ['+', '-', '*', '/', '%', '**']:
                raise ValueError("NO VALID OPERATION. PLEASE, TRY AGAIN.")

            dato1 = float(input("TYPE THE FIRST NUMBER: "))
            dato2 = float(input("TYPE THE SECOND NUMBER: "))
            if operacion == '/' and dato2 == 0:
                raise ValueError("CANNOT DIVIDE BY ZERO. PLEASE, TRY AGAIN.")

            tiempo_max_estimado = int(input("TYPE THE MAX ESTIMATED TIME (IN SECONDS): "))
            if tiempo_max_estimado <= 0:
                raise ValueError("MAX STIMATED TIME MUST BE GREATER THAN 0.")

            # Crear y añadir el proceso
            crear_proceso(id_proceso, nombre_programador, operacion, dato1, dato2, tiempo_max_estimado)

            # Mostrar todos los procesos después de añadir el nuevo proceso
            limpiar_pantalla()
            mostrar_todos_los_procesos(procesos)

        except ValueError as e:
            print(f"ERROR: {e}. PLEASE, TRY AGAIN.")

# Ejemplo de uso: Solicitar al usuario que añada procesos continuamente
limpiar_pantalla()
mostrar_banner()
solicitar_datos_proceso()
crear_y_ejecutar_lotes(procesos)
input("PRESS ENTER TO EXIT...")