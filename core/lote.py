import time
import keyboard
from threading import Lock
from utils.helpers import limpiar_pantalla, mostrar_banner


class Lote:
    def __init__(self, numero_lote, lotes_restantes):
        self.procesos = []
        self.numero_lote = numero_lote
        self.lotes_restantes = lotes_restantes
        self.pausado = False
        self.interrupcion = False
        self.error = False

        self.pausa_lock = Lock()
        self.interrupcion_lock = Lock()
        self.error_lock = Lock()

        keyboard.on_press_key('P', self.pausar_ejecucion)
        keyboard.on_press_key('C', self.continuar_ejecucion)
        keyboard.on_press_key('I', self.interrumpir_proceso)
        keyboard.on_press_key('E', self.error_en_proceso)

    def pausar_ejecucion(self, event):
        if self.pausa_lock.acquire(blocking=False):
            try:
                if not self.pausado:
                    print("PAUSE DETECTED. EXECUTION HALTED.")
                    self.pausado = True
            finally:
                self.pausa_lock.release()

    def continuar_ejecucion(self, event):
        self.pausado = False

    def interrumpir_proceso(self, event):
        if self.interrupcion_lock.acquire(blocking=False):
            try:
                print("INTERRUPTION DETECTED. PROCESS MOVING TO THE END OF THE BATCH.")
                self.interrupcion = True
            finally:
                self.interrupcion_lock.release()

    def error_en_proceso(self, event):
        if self.error_lock.acquire(blocking=False):
            try:
                if not self.error:
                    print("ERROR DETECTED. PROCESS TERMINATING.")
                    self.error = True
            finally:
                self.error_lock.release()

    def agregar_proceso(self, proceso):
        if len(self.procesos) >= 3:
            raise ValueError("BATCH CANNOT HAVE MORE THAN 3 PROCESS.")
        self.procesos.append(proceso)

    def ejecutar_lote(self):

        self.pausado = False
        self.interrupcion = False
        self.error = False

        while True:
            if all(proceso.estado in ["COMPLETED", "ERROR"] for proceso in self.procesos):
                break

            proceso = self.procesos[0]

            if proceso.estado in ["COMPLETED", "ERROR"]:
                self.procesos.append(self.procesos.pop(0))
                continue

            if self.interrupcion:
                self.procesos.append(self.procesos.pop(0))
                self.interrupcion = False
                continue

            if self.error:
                proceso.estado = "ERROR"
                self.error = False
                continue

            if self.pausado:
                time.sleep(0.1)
                continue

            limpiar_pantalla()
            mostrar_banner()
            print(f"BATCH NO.{self.numero_lote} - BATCHS REMAINING {self.lotes_restantes}")
            proceso.actualizar_estado(1)
            self.mostrar_estado_actual()
            time.sleep(1)

            if proceso.estado == "COMPLETED":
                self.procesos.append(self.procesos.pop(0))

    def mostrar_estado_actual(self):
        for proceso in self.procesos:
            print(proceso)

    def __str__(self):
        lote_info = f"BATCH NO.{self.numero_lote} - BATCHS REMAINING {self.lotes_restantes}\n"
        procesos_info = '\n'.join(str(proceso) for proceso in self.procesos)
        return lote_info + procesos_info
