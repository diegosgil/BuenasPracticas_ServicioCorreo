from abc import ABC, abstractmethod
from typing import Collection

# Definición de la clase Correo
class Correo:
    def __init__(self, contenido: str):
        self.contenido = contenido

# Definición de la clase InfoCorreo
class InfoCorreo:
    def __init__(self, id: int):
        self.id = id

# Interfaz IServicioCorreo
class IServicioCorreo(ABC):

    @abstractmethod
    def enviarCorreo(self, correo: Correo) -> None:
        pass

    @abstractmethod
    def listarCorreos(self, inicio: int, fin: int) -> Collection[InfoCorreo]:
        pass

    @abstractmethod
    def descargarCorreo(self, info_correo: InfoCorreo) -> Correo:
        pass

# Implementación de la interfaz IServicioCorreo
class ServicioCorreo(IServicioCorreo):

    def __init__(self):
        self.correos = []  # Simulación de una lista de correos

    def enviarCorreo(self, correo: Correo) -> None:
        # Simulación de envío de correo
        self.correos.append(correo)
        print(f"Correo enviado: {correo.contenido}")

    def listarCorreos(self, inicio: int, fin: int) -> Collection[InfoCorreo]:
        # Simulación de listar correos
        return [InfoCorreo(i) for i in range(inicio, min(fin, len(self.correos)))]

    def descargarCorreo(self, info_correo: InfoCorreo) -> Correo:
        # Simulación de descarga de correo
        correo_id = info_correo.id
        if 0 <= correo_id < len(self.correos):
            return self.correos[correo_id]
        else:
            raise ValueError("Correo no encontrado")

# Ejemplo de uso
if __name__ == "__main__":
    servicio_correo = ServicioCorreo()

    correo1 = Correo("Hola, ¿cómo estás?")
    servicio_correo.enviarCorreo(correo1)

    correo2 = Correo("¡Hola! Estoy bien, gracias.")
    servicio_correo.enviarCorreo(correo2)

    lista_correos = servicio_correo.listarCorreos(0, 2)
    for info_correo in lista_correos:
        correo = servicio_correo.descargarCorreo(info_correo)
        print(f"Correo descargado: {correo.contenido}")