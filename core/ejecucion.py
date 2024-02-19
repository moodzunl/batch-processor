from core.lote import Lote
from utils.helpers import limpiar_pantalla, mostrar_banner

def mostrar_todos_los_procesos(procesos):
    mostrar_banner()
    print("LISTED PROCESS:")
    for proceso in procesos:
        info_proceso = (f"ID: {proceso.id_proceso}\t"
                    f"NAME: {proceso.nombre_programador}\t"
                    f"PROCESS: {proceso.dato1} {proceso.operacion} {proceso.dato2}\t"
                    f"ET: {proceso.tiempo_max_estimado}sec")
        # Usa .expandtabs(tabsize) para definir el ancho de las tabulaciones
        print(info_proceso.expandtabs(25))

def crear_y_ejecutar_lotes(procesos):
    if not procesos:
        raise ValueError("NO PROCESSES TO CREATE BATCHES. PLEASE, ADD PROCESSES FIRST.")
    
    lotes = []  # Almacenará los lotes creados
    info_lotes_completados = []  # Almacenará la información de los lotes completados
    for i, proceso in enumerate(procesos, start=1):
        if i % 4 == 1:  # Cada 4 procesos, empezar un nuevo lote
            lotes.append(Lote(len(lotes) + 1, 0))  # Añadir un nuevo lote con el número correspondiente
        lotes[-1].agregar_proceso(proceso)  # Añadir el proceso al último lote

    # Actualizar la cantidad de lotes restantes para cada lote
    for i, lote in enumerate(lotes):
        lote.lotes_restantes = len(lotes) - i - 1

    # Mostrar los lotes formados
    limpiar_pantalla()
    mostrar_banner()
    for lote in lotes:
        print(f"\nBATCH {lote.numero_lote} GENERATED:")
        for proceso in lote.procesos:
            print(proceso)
    input("\nPRESS ENTER TO START BATCH EXECUTION...")

    # Ejecutar cada lote
    for lote in lotes:
        limpiar_pantalla()
        mostrar_banner()
        print(f"\nEXECUTING BATCH {lote.numero_lote}:")
        lote.ejecutar_lote()
        info_lotes_completados.append(str(lote))
        # if lote != lotes[-1]:   Si no es el último lote, pausar antes del siguiente
        #    input("PRESS ENTER TO CONTINUE NEXT BATCH...")

    # Mostrar la información de todos los lotes al final
    limpiar_pantalla()
    mostrar_banner()
    print("\nALL BATCHES EXECUTED, DISPLAYING PROCESSED BATCH INFORMATION:")
    for info_lote in info_lotes_completados:
        print(info_lote)
        print("-" * 80)  # Una línea separadora para mayor claridad
