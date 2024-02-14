# main.py
from core.proceso import Proceso
from core.ejecucion import mostrar_todos_los_procesos, crear_y_ejecutar_lotes
from utils.helpers import limpiar_pantalla
from ui.app import iniciar_gui

procesos = []
ids_usados = set()

def agregar_proceso(id_proceso, nombre, operacion, dato1, dato2, tiempo_max_estimado):
    if id_proceso in ids_usados:
        raise ValueError("El ID ya está en uso.")
    nuevo_proceso = Proceso(id_proceso, nombre, operacion, dato1, dato2, tiempo_max_estimado)
    procesos.append(nuevo_proceso)
    ids_usados.add(id_proceso)

# Iniciar la GUI y pasar agregar_proceso como la función de callback
iniciar_gui(agregar_proceso)

# Mostrar todos los procesos antes de agruparlos en lotes
mostrar_todos_los_procesos(procesos)
limpiar_pantalla()

# Crear y ejecutar lotes
crear_y_ejecutar_lotes(procesos)