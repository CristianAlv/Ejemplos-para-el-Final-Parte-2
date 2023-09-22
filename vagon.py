from abc import ABC, abstractmethod


class Vagon(ABC):
  __num: str
  __alto: float

  def __init__(self, num, alt):
    self.__num = num
    self.__alto = alt

  @abstractmethod
  def mostrarDatos(self):
    print("{}".format(self.__num))
    print("{}".format(self.__alto))
    pass

  def volumen(self) -> float:
    pass
