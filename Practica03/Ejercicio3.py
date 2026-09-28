class Sensor:
    tipo = "Genérico"  # atributo de CLASE (compartido, cada subclase lo redefine)
    def __init__(self, id):
        self.id = id            # atributo de INSTANCIA
        self.encendido = False  # atributo de INSTANCIA
    def activar(self):
        self.encendido = True
        print(f"[{self.tipo}] Sensor {self.id} activado.")
    def desactivar(self):
        self.encendido = False
        print(f"[{self.tipo}] Sensor {self.id} desactivado.")


class Camara(Sensor):
    tipo = "Cámara"  # atributo de CLASE
    def __init__(self, id, resolucion):
        Sensor.__init__(self, id)
        self.resolucion = resolucion  # atributo de INSTANCIA

class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"  # atributo de CLASE
    def __init__(self, id, alcance):
        Sensor.__init__(self, id)
        self.alcance = alcance  # atributo de INSTANCIA

class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"  # atributo de CLASE
    def __init__(self, id, resolucion, alcance):
        Camara.__init__(self, id, resolucion)
        SensorLuzLaser.__init__(self, id, alcance)

vehiculo = VehiculoAutonomo("V001", "1080p", 50)
vehiculo.activar()
print(f"Tipo: {vehiculo.tipo}")
print(f"Resolución (de Camara): {vehiculo.resolucion}")
print(f"Alcance (de SensorLuzLaser): {vehiculo.alcance}")
vehiculo.desactivar()