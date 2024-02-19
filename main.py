from tkinter import *
from core.proceso import Proceso
from core.ejecucion import mostrar_todos_los_procesos, crear_y_ejecutar_lotes
from utils.helpers import limpiar_pantalla

# Lista de procesos inicial
procesos = [
    Proceso(1,"Oscar","+",1,2,3),
]

# Una vez cerrada la ventana, puedes continuar con el resto de tu flujo
limpiar_pantalla()
mostrar_todos_los_procesos(procesos)
crear_y_ejecutar_lotes(procesos)    