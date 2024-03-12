import random
from core.proceso import Proceso
from core.ejecucion import mostrar_todos_los_procesos, crear_y_ejecutar_lotes
from utils.helpers import limpiar_pantalla, mostrar_banner

# Registro global de IDs de procesos utilizados
ids_procesos_utilizados = set()
procesos = []


def crear_proceso(id_proceso, operacion, dato1, dato2, tiempo_max_estimado):
    if id_proceso in ids_procesos_utilizados:
        raise ValueError(f"ID {id_proceso} IS ALREADY IN USE.")
    nuevo_proceso = Proceso(id_proceso, operacion, dato1, dato2, tiempo_max_estimado)
    ids_procesos_utilizados.add(id_proceso)
    procesos.append(nuevo_proceso)


def generar_datos_proceso():
    operaciones = ['+', '-', '*', '/', '%']  # Lista de operaciones válidas
    while True:
        id_proceso = random.randint(1, 1000)  # Genera un ID de proceso aleatorio
        if id_proceso not in ids_procesos_utilizados:
            break  # Sale del bucle si el ID del proceso es único

    operacion = random.choice(operaciones)  # Selecciona una operación aleatoria de la lista
    dato1 = random.randint(1, 100)  # Genera el primer número aleatorio
    dato2 = random.randint(1, 100)  # Genera el segundo número aleatorio
    if operacion == '/' and dato2 == 0:  # Asegura que no haya división por cero
        dato2 = 1  # Asigna 1 para evitar la división por cero

    tiempo_max_estimado = random.randint(7, 18)  # Genera un tiempo máximo estimado aleatorio dentro del rango

    return id_proceso, operacion, dato1, dato2, tiempo_max_estimado


def agregar_procesos_aleatorios(n):
    for _ in range(n):  # Repite 'n' veces para agregar 'n' procesos aleatorios
        id_proceso, operacion, dato1, dato2, tiempo_max_estimado = generar_datos_proceso()
        crear_proceso(id_proceso, operacion, dato1, dato2, tiempo_max_estimado)


# Ejemplo de uso: Solicitar al usuario que añada procesos continuamente
limpiar_pantalla()
mostrar_banner()
n = int(input("INTRODUCE THE AMOUNT OF PROCESS TO GENERATE: "))
agregar_procesos_aleatorios(n)
limpiar_pantalla()
mostrar_todos_los_procesos(procesos)
input("PRESS ENTER TO ORDER PROCESS BY ID...")
procesos.sort(key=lambda proceso: proceso.id_proceso)
mostrar_todos_los_procesos(procesos)
crear_y_ejecutar_lotes(procesos)
input("PRESS ENTER TO EXIT...")
