class Proceso:
    def __init__(self, id_proceso, nombre_programador, operacion, dato1, dato2, tiempo_max_estimado):
        self.id_proceso = id_proceso
        self.nombre_programador = nombre_programador
        self.operacion = operacion
        self.dato1 = float(dato1)
        self.dato2 = float(dato2)
        self.tiempo_max_estimado = int(tiempo_max_estimado)
        self.resultado = None
        self.estado = "TO DO"  # Estados posibles: TO DO, IN PROGRESS, COMPLETED
        self.tiempo_restante = self.tiempo_max_estimado
        self.tiempo_transcurrido = 0

    def actualizar_estado(self, segundos):
        if self.estado == "TO DO":
            self.estado = "IN PROGRESS"
        self.tiempo_transcurrido += segundos
        self.tiempo_restante = max(0, self.tiempo_max_estimado - self.tiempo_transcurrido)
        if self.tiempo_restante == 0:
            self.estado = "COMPLETED"
            self.ejecutar_operacion()
            
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
            self.resultado = f"Error: {str(e)}"

        return self.resultado

    def __str__(self):
            if self.estado == "COMPLETED":
                resultado_str = f" = {self.resultado}"
            else:
                resultado_str = ""
            
            estado = (f"{self.estado} - {self.tiempo_restante}SEC REMAINING / "
                    f"{self.tiempo_transcurrido}SEC PASSED{resultado_str}") if self.estado != "TO DO" else self.estado

            info_proceso = (f"ID: {self.id_proceso}\t"
                            f"NAME: {self.nombre_programador}\t"
                            f"PROCESS: {self.dato1}{self.operacion}{self.dato2}\t"
                            f"ET: {self.tiempo_max_estimado}SEC\t"
                            f"---- {estado}")

            return info_proceso.expandtabs(20)