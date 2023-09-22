class Formacion:
  __maquinas: object
  __vagones: list
  __tipoFormacion: str

  def __init__(self, maquinas, tipoFormacion):
    self.__maquinas = maquinas
    self.__vagones = []
    self.__tipoFormacion = tipoFormacion

  def __str__(self):
    return f"{self.__maquinas} {self.__vagones} {self.__tipoFormacion}"
