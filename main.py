from tkinter import *
from core.proceso import Proceso
from core.ejecucion import mostrar_todos_los_procesos, crear_y_ejecutar_lotes
from utils.helpers import limpiar_pantalla

# Lista de procesos inicial
procesos = []

ids_usados = set()

def actualizar_lista_procesos():
    # Limpia la lista actual para evitar duplicados
    lista_procesos.delete(0, END)
    # Añade los procesos actualizados a la lista
    for proceso in procesos:
        lista_procesos.insert(END, f"ID: {proceso.id_proceso}, Nombre: {proceso.nombre_programador}, Operación: {proceso.operacion}, Tiempo Máx Estimado: {proceso.tiempo_max_estimado}")


def agregar_proceso():
    try:
        # Obtener valores de los inputs
        id_proceso = int(id_entry.get())
        nombre = nombre_entry.get()
        operacion = operacion_entry.get()
        dato1 = int(dato1_entry.get())
        dato2 = int(dato2_entry.get())
        tiempo_max_estimado = int(tiempo_max_estimado_entry.get())

        if id_proceso in ids_usados:
            raise ValueError("El ID ya está en uso.")
        nuevo_proceso = Proceso(id_proceso, nombre, operacion, dato1, dato2, tiempo_max_estimado)
        procesos.append(nuevo_proceso)
        ids_usados.add(id_proceso)

        # Limpiar inputs
        id_entry.delete(0, END)
        nombre_entry.delete(0, END)
        operacion_entry.delete(0, END)
        dato1_entry.delete(0, END)
        dato2_entry.delete(0, END)
        tiempo_max_estimado_entry.delete(0, END)

        # Opcional: mostrar mensaje de éxito o actualizar alguna parte de la UI
        actualizar_lista_procesos()
    except ValueError as e:
        print(e)

# Configuración de la ventana Tkinter
root = Tk()
root.title("Gestión de Procesos")
root.geometry("800x600")  # Tamaño inicial de la ventana

# Configura las filas y columnas para que se expandan con la ventana
root.grid_columnconfigure(1, weight=1)
for i in range(8):  # Asumiendo que tienes 8 filas en total
    root.grid_rowconfigure(i, weight=1)

# Configuración de fuente grande para los widgets
fuente_grande = ('Verdana', 12)

# Creación y configuración de widgets
id_label = Label(root, text="ID Proceso:", font=fuente_grande)
id_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)
id_entry = Entry(root, font=fuente_grande)
id_entry.grid(row=0, column=1, sticky=EW, padx=10, pady=10)

nombre_label = Label(root, text="Nombre:", font=fuente_grande)
nombre_label.grid(row=1, column=0, sticky=W, padx=10, pady=10)
nombre_entry = Entry(root, font=fuente_grande)
nombre_entry.grid(row=1, column=1, sticky=EW, padx=10, pady=10)

operacion_label = Label(root, text="Operación:", font=fuente_grande)
operacion_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)
operacion_entry = Entry(root, font=fuente_grande)
operacion_entry.grid(row=2, column=1, sticky=EW, padx=10, pady=10)

dato1_label = Label(root, text="Dato 1:", font=fuente_grande)
dato1_label.grid(row=3, column=0, sticky=W, padx=10, pady=10)
dato1_entry = Entry(root, font=fuente_grande)
dato1_entry.grid(row=3, column=1, sticky=EW, padx=10, pady=10)

dato2_label = Label(root, text="Dato 2:", font=fuente_grande)
dato2_label.grid(row=4, column=0, sticky=W, padx=10, pady=10)
dato2_entry = Entry(root, font=fuente_grande)
dato2_entry.grid(row=4, column=1, sticky=EW, padx=10, pady=10)

tiempo_max_estimado_label = Label(root, text="Tiempo Máx Estimado:", font=fuente_grande)
tiempo_max_estimado_label.grid(row=5, column=0, sticky=W, padx=10, pady=10)
tiempo_max_estimado_entry = Entry(root, font=fuente_grande)
tiempo_max_estimado_entry.grid(row=5, column=1, sticky=EW, padx=10, pady=10)

agregar_btn = Button(root, text="Agregar Proceso", command=agregar_proceso, font=fuente_grande)
agregar_btn.grid(row=6, column=0, columnspan=2, sticky=EW, padx=10, pady=10)

lista_procesos = Listbox(root, font=fuente_grande, width=50, height=10)
lista_procesos.grid(row=7, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

root.mainloop()

# Una vez cerrada la ventana, puedes continuar con el resto de tu flujo
limpiar_pantalla()
mostrar_todos_los_procesos(procesos)
crear_y_ejecutar_lotes(procesos)    