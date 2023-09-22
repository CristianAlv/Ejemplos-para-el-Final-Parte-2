class Maquina:
  __numserie: str
  __marca: str
  __tipoCombustible: str

  def __init__(self, numserie, marca, tipoCombustible):
    self.__numserie = numserie
    self.__marca = marca
    self.__tipoCombustible = tipoCombustible

  def __str__(self):
    return f"{self.__numserie} {self.__marca} {self.__tipoCombustible}"
