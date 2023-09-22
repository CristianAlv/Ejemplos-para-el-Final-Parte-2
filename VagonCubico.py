from vagon import Vagon


class VagonCubico(Vagon):
  __ancho: float
  __profundidad: float

  def __init__(self,
               num,
               alt,
               ancho,
               profundidad):
    super().__init__(num, alt)
    self.__ancho = ancho
    self.__profundidad = profundidad

  def mostrarDatos(self):
    super().mostrarDatos()
    print("{}".format(self.__ancho))
    print("{}".format(self.__profundidad))
    pass
