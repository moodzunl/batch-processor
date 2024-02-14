import tkinter as tk
from tkinter import messagebox

def iniciar_gui(agregar_proceso_callback):
    root = tk.Tk()
    root.title("Añadir Proceso")
    root.geometry("600x400")  # Aumentar el tamaño de la ventana

    def agregar_placeholder(entry, text):
        entry.insert(0, text)
        entry.config(fg='grey')
        entry.bind("<FocusIn>", lambda args: [entry.delete('0', 'end'), entry.config(fg='black')] if entry.get() == text else None)
        entry.bind("<FocusOut>", lambda args: [entry.insert('0', text), entry.config(fg='grey')] if entry.get() == '' else None)

    # Crear y configurar los campos de entrada con placeholders
    entry_id = tk.Entry(root, font=('Helvetica', 14), width=35)
    agregar_placeholder(entry_id, "ID (e.g., 1)")
    entry_nombre = tk.Entry(root, font=('Helvetica', 14), width=35)
    agregar_placeholder(entry_nombre, "Nombre (e.g., Juan)")
    entry_operacion = tk.Entry(root, font=('Helvetica', 14), width=35)
    agregar_placeholder(entry_operacion, "Operación (e.g., +, *, /)")
    entry_dato1 = tk.Entry(root, font=('Helvetica', 14), width=35)
    agregar_placeholder(entry_dato1, "Primer dato (e.g., 5)")
    entry_dato2 = tk.Entry(root, font=('Helvetica', 14), width=35)
    agregar_placeholder(entry_dato2, "Segundo dato (e.g., 3)")
    entry_tiempo = tk.Entry(root, font=('Helvetica', 14), width=35)
    agregar_placeholder(entry_tiempo, "Tiempo máximo estimado (e.g., 10)")

    def agregar_proceso():
        try:
            # Obtener los valores de los campos de entrada
            id_proceso = int(entry_id.get())
            nombre = entry_nombre.get()
            operacion = entry_operacion.get()
            dato1 = float(entry_dato1.get())
            dato2 = float(entry_dato2.get())
            tiempo_max_estimado = float(entry_tiempo.get())

            # Usar la función de callback para agregar el proceso
            agregar_proceso_callback(id_proceso, nombre, operacion, dato1, dato2, tiempo_max_estimado)

            # Limpiar los campos de entrada
            entry_id.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_operacion.delete(0, tk.END)
            entry_dato1.delete(0, tk.END)
            entry_dato2.delete(0, tk.END)
            entry_tiempo.delete(0, tk.END)

            messagebox.showinfo("Éxito", "Proceso añadido correctamente.")

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    # Crear y configurar el botón de agregar
    boton_agregar = tk.Button(root, text="Añadir", command=agregar_proceso, font=('Helvetica', 14), width=20)
    
    # Organizar los widgets en la ventana con padding adicional
    entries = [entry_id, entry_nombre, entry_operacion, entry_dato1, entry_dato2, entry_tiempo, boton_agregar]
    for entry in entries:
        entry.pack(pady=5)  # Añadir padding vertical entre los widgets

    root.mainloop()
