import logging

# Clase ServicioCorreoConLogging
class ServicioCorreoConLogging(IServicioCorreo):
    def __init__(self, servicio_correo, logger_name):
        self.servicio_correo = servicio_correo
        self.logger = logging.getLogger(logger_name)

    def enviarCorreo(self, correo):
        try:
            self.servicio_correo.enviarCorreo(correo)
            self.logger.info("Correo enviado con éxito.")
        except Exception as e:
            self.logger.error("Error al enviar correo: %s", str(e))

    def listarCorreos(self, inicio, fin):
        try:
            correos = self.servicio_correo.listarCorreos(inicio, fin)
            self.logger.info("Lista de correos obtenida con éxito.")
            return correos
        except Exception as e:
            self.logger.error("Error al listar correos: %s", str(e))
            return []

    def descargarCorreo(self, info_correo):
        try:
            correo = self.servicio_correo.descargarCorreo(info_correo)
            self.logger.info("Correo descargado con éxito.")
            return correo
        except Exception as e:
            self.logger.error("Error al descargar correo: %s", str(e))
            return None

# Uso de la clase ServicioCorreoConLogging
if __name__ == "__main__":
    # Configuración básica del registro de eventos
    logging.basicConfig(filename="correo.log", level=logging.INFO)

    # Crear una instancia del servicio de correo base
    servicio_correo_base = ServicioCorreo()

    # Crear una instancia del servicio de correo con registro de eventos
    servicio_correo_con_logging = ServicioCorreoConLogging(servicio_correo_base, "CorreoLogger")

    # Enviar un correo con registro de eventos
    correo = Correo("Ejemplo de correo", "Este es un correo de prueba")
    servicio_correo_con_logging.enviarCorreo(correo)

    # Listar correos con registro de eventos
    correos = servicio_correo_con_logging.listarCorreos(1, 10)

    # Descargar un correo con registro de eventos
    info_correo = InfoCorreo(123)
    correo_descargado = servicio_correo_con_logging.descargarCorreo(info_correo)