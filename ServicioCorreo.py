class ServicioCorreo(IServicioCorreo):

    def enviarCorreo(self, correo):
        max_intentos = 3
        espera_entre_intentos = 2  # segundos
        intento = 1
        while intento <= max_intentos:
            try:
                self.servicio_correo.enviarCorreo(correo)
                return
            except Exception as e:
                print(f"Intento {intento} fallido: {str(e)}")
                sleep(espera_entre_intentos)
                intento += 1
        print(f"Se agotaron los intentos. No se pudo enviar el correo.")

    def listarCorreos(self, inicio, fin):
        return self.servicio_correo.listarCorreos(inicio, fin)
        print(f"Listando correos desde {inicio} hasta {fin}")

    def descargarCorreo(self, info_correo):
        return self.servicio_correo.descargarCorreo(info_correo)
        print("Descargando correo:", info_correo)
