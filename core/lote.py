import time
import keyboard
from utils.helpers import limpiar_pantalla, mostrar_banner


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
        if len(self.procesos) >= 3:
            raise ValueError("BATCH CANNOT HAVE MORE THAN 3 PROCESS.")
        self.procesos.append(proceso)

    def ejecutar_lote(self):
        for proceso in self.procesos:
            while proceso.estado != "COMPLETED":
                if keyboard.is_pressed('I'):  # Interrupción
                    print("INTERRUPTION DETECTED. PROCESS MOVING TO THE END OF THE BATCH.")
                    self.procesos.append(self.procesos.pop(0))  # Mover el proceso al final
                    continue

                if keyboard.is_pressed('E'):  # Error
                    print("ERROR DETECTED. PROCESS TERMINATING.")
                    proceso.estado = "ERROR"  # Actualizar el estado a ERROR
                    break  # Terminar el proceso actual

                if keyboard.is_pressed('P'):  # Pausa
                    print("PAUSE DETECTED. EXECUTION HALTED.")
                    self.pausado = True

                while self.pausado:  # Bucle de pausa
                    if keyboard.is_pressed('C'):  # Continuar
                        print("CONTINUE DETECTED. RESUMING EXECUTION.")
                        self.pausado = False

                limpiar_pantalla()
                mostrar_banner()
                print(f"BATCH NO.{self.numero_lote} - BATCHS REMAINING {self.lotes_restantes}")
                proceso.actualizar_estado(1)
                self.mostrar_estado_actual()
                time.sleep(1)  # Delay por simulación

    def mostrar_estado_actual(self):
        for proceso in self.procesos:
            print(proceso)

    def __str__(self):
        lote_info = f"BATCH NO.{self.numero_lote} - BATCHS REMAINING {self.lotes_restantes}\n"
        procesos_info = '\n'.join(str(proceso) for proceso in self.procesos)
        return lote_info + procesos_info
