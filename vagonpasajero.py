from VagonCubico import VagonCubico

class VagonPasajeros(VagonCubico):
  __cantAsientos: int
  __asientosOcupados: int
  __tipo: str
  def __init__(self, num, alt, ancho, profundidad,cant=30, tipo=''):
    super().__init__(num, alt, ancho, profundidad)
    self.__cantAsientos=cant 
    self.__asientosOcupados=0
    self.__tipo=tipo
  def pasajeros(self,pas=10):
    self.__asientosOcupados+=pas
  def mostrarDatos(self):
    super().mostrarDatos()
    print(f'{self.__cantAsientos} {self.__asientosOcupados} {self.__tipo}')
  