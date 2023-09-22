from maquina import Maquina
from maquinista import Maquinista
from vagon import Vagon
from VagonCilindrico import VagonCilindrico
from VagonCubico import VagonCubico
import gc
from vagonCarga import VagonCarga

if __name__ == '__main__':
  tren1 = VagonCilindrico(2, 4.5, 2.25, 4.33, "Comercial")
  tren1.mostrarDatos()
  tren2 = VagonCarga(5, 3.3, 4.4, 6, 22, "FDWAS-03")
  tren2.mostrarDatos()
  maq = Maquina(1021, 'Epson', 'AXION')
  x = Maquinista(11111111, "Albornoz", "Joaquin", "Impresora 3D")
  x.mostrarDatos()
