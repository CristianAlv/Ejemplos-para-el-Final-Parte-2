from VagonCubico import VagonCubico


class VagonCarga(VagonCubico):
  __tnCarga: float
  __numRemito: str

  def __init__(self, num, alt, ancho, profundidad, tnCarga, numRemito):
    super().__init__(num, alt, ancho, profundidad)
    self.__tnCarga = tnCarga
    self.__numRemito = numRemito

  def mostrarDatos(self):
    super().mostrarDatos()
    print("{}".format(self.__tnCarga))
    print("{}".format(self.__numRemito))
