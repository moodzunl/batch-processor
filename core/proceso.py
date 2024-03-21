import time


class Proceso:
    def __init__(self, id_proceso, operacion, dato1, dato2, tiempo_max_estimado):
        """Clase proceso que genera una tarea dentro de un batch de procesos.

        Args:
            id_proceso (int): Identificador único del proceso.
            operacion (str): Operación a realizar. Puede ser: '+', '-', '*', '/', '%', '**'.
            dato1 (int): Primer número a operar.
            dato2 (int): Segundo número a operar.
            tiempo_max_estimado (int): Tiempo máximo estimado para la ejecución del proceso.
        """

        # Validaciones de tipo
        assert isinstance(id_proceso, int), "ID PROCESS HAS TO BE AN INTEGER."
        assert operacion in ['+', '-', '*', '/', '%', '**'], f"OPERATION '{operacion}' NOT SUPPORTED."
        assert isinstance(tiempo_max_estimado, (int, float)) and tiempo_max_estimado > 0, "MAX TIME CANNOT BE NON-NEGATIVE."

        # Conversión y asignación segura de valores
        try:
            self.dato1 = float(dato1)
            self.dato2 = float(dato2)
        except ValueError:
            raise ValueError("DATA HAS TO BE NUMERIC.")

        self.id_proceso = id_proceso
        self.operacion = operacion
        self.tiempo_max_estimado = int(tiempo_max_estimado)
        self.resultado = None
        self.estado = "TO DO"  # Estados posibles: TO DO, IN PROGRESS, COMPLETED
        self.tiempo_restante = self.tiempo_max_estimado
        self.tiempo_transcurrido = 0
        self.tiempo_llegada = time.time()  # Tiempo actual como tiempo de llegada
        self.tiempo_finalizacion = None
        self.tiempo_respuesta = None
        self.tiempo_espera = None

    def actualizar_estado(self, segundos):
        if self.estado == "TO DO":
            self.estado = "IN PROGRESS"
        self.tiempo_transcurrido += segundos
        self.tiempo_restante = max(0, self.tiempo_max_estimado - self.tiempo_transcurrido)
        if self.tiempo_restante == 0:
            self.estado = "COMPLETED"
            self.ejecutar_operacion()

        # Definir el tiempo de respuesta la primera vez que el proceso pasa a "IN PROGRESS"
        if self.estado == "IN PROGRESS" and self.tiempo_respuesta is None:
            self.tiempo_respuesta = time.time() - self.tiempo_llegada

        # Definir el tiempo de finalización cuando el proceso se completa
        if self.estado == "COMPLETED":
            self.tiempo_finalizacion = time.time()
            self.tiempo_espera = self.tiempo_respuesta  # El tiempo de espera es hasta que el proceso inicia

    def calcular_tiempo_retorno(self):
        if self.tiempo_finalizacion:
            return self.tiempo_finalizacion - self.tiempo_llegada
        return None  # El tiempo de retorno no se puede calcular hasta que el proceso no se complete

    def calcular_tiempo_servicio(self):
        return self.tiempo_transcurrido  # El tiempo de servicio es el tiempo transcurrido mientras estaba "IN PROGRESS"

    def ejecutar_operacion(self):
        try:
            if self.operacion == '+':
                self.resultado = self.dato1 + self.dato2
            elif self.operacion == '-':
                self.resultado = self.dato1 - self.dato2
            elif self.operacion == '*':
                self.resultado = self.dato1 * self.dato2
            elif self.operacion == '/':
                if self.dato2 == 0:
                    raise ValueError("CANNOT DIVIDE BY ZERO.")
                self.resultado = self.dato1 / self.dato2
            elif self.operacion == '%':
                self.resultado = self.dato1 % self.dato2
            elif self.operacion == '**':
                self.resultado = self.dato1 ** self.dato2
            else:
                raise ValueError(f"OPERATION '{self.operacion}' NOT SUPPORTED.")
        except Exception as e:
            self.resultado = f"ERROR: {str(e)}"

        return self.resultado

    def __str__(self):
        # Cálculo del tiempo de retorno y servicio solo si el proceso ha sido completado
        tiempo_retorno_str = f" / RT: {self.calcular_tiempo_retorno():.2f}SEC" if self.tiempo_finalizacion else ""
        tiempo_servicio_str = f" / ST: {self.calcular_tiempo_servicio():.2f}SEC" if self.estado == "COMPLETED" else ""

        # Cálculo del tiempo de respuesta y espera si están disponibles
        tiempo_respuesta_str = f" / RSP: {self.tiempo_respuesta:.2f}SEC" if self.tiempo_respuesta is not None else ""
        tiempo_espera_str = f" / WT: {self.tiempo_espera:.2f}SEC" if self.tiempo_espera is not None else ""

        # Información sobre el estado del proceso y el resultado si está completado
        if self.estado == "COMPLETED":
            resultado_str = f" = {self.resultado}"
        else:
            resultado_str = ""

        estado = (f"{self.estado} - {self.tiempo_restante}SEC REMAINING / "
                  f"{self.tiempo_transcurrido}SEC PASSED{resultado_str}") if self.estado != "TO DO" else self.estado

        # Información general del proceso
        info_proceso = (f"ID: {self.id_proceso}\t"
                        f"PROCESS: {self.dato1}{self.operacion}{self.dato2}\t"
                        f"ET: {self.tiempo_max_estimado}SEC\t"
                        f"---- {estado}"
                        f"{tiempo_retorno_str}{tiempo_servicio_str}"
                        f"{tiempo_respuesta_str}{tiempo_espera_str}")

        return info_proceso.expandtabs(20)
