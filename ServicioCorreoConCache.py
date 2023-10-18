import cachetools

class ServicioCorreoConCache(IServicioCorreo):
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo
        self.cache = cachetools.LRUCache(maxsize=100)  # Usamos una caché de 100 elementos como ejemplo

    def enviarCorreo(self, correo):
        # Verificar si el correo ya está en la caché
        key = f"enviar_{correo.id}"
        if key in self.cache:
            print("Enviando correo desde la caché...")
            return self.cache[key]
        else:
            # Si no está en la caché, enviar el correo utilizando el servicio subyacente
            result = self.servicio_correo.enviarCorreo(correo)
            # Almacenar el resultado en la caché
            self.cache[key] = result
            return result

    def listarCorreos(self, inicio, fin):
        # Verificar si la lista de correos ya está en la caché
        key = f"listar_{inicio}_{fin}"
        if key in self.cache:
            print("Listando correos desde la caché...")
            return self.cache[key]
        else:
            # Si no está en la caché, listar los correos utilizando el servicio subyacente
            result = self.servicio_correo.listarCorreos(inicio, fin)
            # Almacenar el resultado en la caché
            self.cache[key] = result
            return result

    def descargarCorreo(self, info_correo):
        # Verificar si el correo a descargar ya está en la caché
        key = f"descargar_{info_correo.id}"
        if key in self.cache:
            print("Descargando correo desde la caché...")
            return self.cache[key]
        else:
            # Si no está en la caché, descargar el correo utilizando el servicio subyacente
            result = self.servicio_correo.descargarCorreo(info_correo)
            # Almacenar el resultado en la caché
            self.cache[key] = result
            return result