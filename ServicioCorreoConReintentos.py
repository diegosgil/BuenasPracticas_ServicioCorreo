import time

class ServicioCorreoConReintentos(IServicioCorreo):
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo

    def enviarCorreo(self, correo):
        max_intentos = 3
        espera_entre_intentos = 2

        for intento in range(1, max_intentos + 1):
            try:
                self.servicio_correo.enviarCorreo(correo)
                print("Correo enviado con éxito en el intento", intento)
                return
            except Exception as e:
                print(f"Error en el intento {intento}: {str(e)}")
                if intento < max_intentos:
                    print(f"Reintentando en {espera_entre_intentos} segundos...")
                    time.sleep(espera_entre_intentos)
                else:
                    print("Se han agotado los intentos. No se pudo enviar el correo.")