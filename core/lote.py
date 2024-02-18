import time
from utils.helpers import limpiar_pantalla

class Lote:
    def __init__(self, numero_lote, lotes_restantes):
        """Clase que genera un lote de procesos.

        Args:
            numero_lote (int): Identificador único del lote.
            lotes_restantes (int): Lotes restantes por ejecutar.
        """
        
        self.procesos = []
        self.numero_lote = numero_lote
        self.lotes_restantes = lotes_restantes

    def agregar_proceso(self, proceso):
        if len(self.procesos) >= 4:
            raise ValueError("BATCH CANNOT HAVE MORE THAN 4 PROCESS.")
        self.procesos.append(proceso)

    def ejecutar_lote(self):
        for proceso in self.procesos:
            while proceso.estado != "COMPLETED":
                limpiar_pantalla()  # Limpiar la pantalla antes de mostrar el estado actual
                print(f"BATCH NO.{self.numero_lote} - BATCHS REMAINING {self.lotes_restantes}")
                proceso.actualizar_estado(1)  # Simulando el paso de 1 segundo
                self.mostrar_estado_actual()
                time.sleep(1)  # Real delay for simulation

    def mostrar_estado_actual(self):
        for proceso in self.procesos:
            print(proceso)

    def __str__(self):
        lote_info = f"BATCH NO.{self.numero_lote} - BATCHS REMAINING {self.lotes_restantes}\n"
        procesos_info = '\n'.join(str(proceso) for proceso in self.procesos)
        return lote_info + procesos_info
