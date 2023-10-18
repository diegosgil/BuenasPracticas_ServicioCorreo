import logging

class ObservadorEventos:
    def __init__(self, nombre_archivo_log):
        # Configuramos el sistema de registro de eventos
        logging.basicConfig(filename=nombre_archivo_log, level=logging.INFO)

    def notificarEvento(self, evento):
        # Registramos el evento en el archivo de registro
        logging.info(f"Evento: {evento}")

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia del ObservadorEventos con un archivo de registro llamado "eventos.log"
    observador = ObservadorEventos("eventos.log")

    # Simulamos notificar un evento
    evento = "Correo enviado con éxito"
    observador.notificarEvento(evento)

    # También puedes notificar otros eventos
    otro_evento = "Error al descargar correo"
    observador.notificarEvento(otro_evento)