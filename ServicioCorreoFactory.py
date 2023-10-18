class ServicioCorreoFactory:
    def createServicioCorreo(self, thread_safe=False, with_logging=False, with_cache=False):
        servicio_correo = ServicioCorreo()  # Crea una instancia básica de ServicioCorreo

        if thread_safe:
            # Si se solicita que sea thread-safe, envuelve el servicio en un decorador thread-safe
            servicio_correo = ServicioCorreoConReintentos(servicio_correo)

        if with_logging:
            # Si se solicita registro de eventos, envuelve el servicio en un decorador de registro
            logger = logging.getLogger(__name__)  # Configura un logger
            servicio_correo = ServicioCorreoConLogging(servicio_correo, logger)

        if with_cache:
            # Si se solicita caché, envuelve el servicio en un proxy con caché
            cache = CacheManager()  # Instancia de la caché
            servicio_correo = ServicioCorreoConCache(servicio_correo, cache)

        return servicio_correo