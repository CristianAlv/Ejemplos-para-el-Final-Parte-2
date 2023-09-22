from maquina import Maquina


class Maquinista:
  __dni: int
  __apellido: str
  __nombre: str
  __maquina: object

  def __init__(self, dni, apellido, nombre, maq):
    self.__dni = dni
    self.__apellido = apellido
    self.__nombre = nombre
    self.__maquina = maq

  def mostrarDatos(self):
    print(
        f'{self.__apellido + self.__nombre}, {self.__dni}, Maquina:{self.__maquina}'
    )


if __name__ == '__main__':
  maq = Maquina(1021, marc, combustible)
  x = Maquinista(11111111, ape, nom, maq)
  x.mostrarDatos()
