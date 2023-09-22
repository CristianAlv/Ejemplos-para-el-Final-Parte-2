from vagon import Vagon


class VagonCilindrico(Vagon):
  __radio = float
  __cubicos = float
  __tipoCarga = str

  def __init__(self, num, alt, radio, cubicos, tipoCarga):
    super().__init__(num, alt)
    self.__radio = radio
    self.__cubicos = cubicos
    self.__tipoCarga = tipoCarga

  def mostrarDatos(self):
    super().mostrarDatos()
    print("{}".format(self.__radio))
    print("{}".format(self.__cubicos))
    print("{}".format(self.__tipoCarga))
