#Operaciones/logaritmos.py
#Responsable: Herlan Ibañez Condori (eq04)
import math
class Logaritmo:
  def __init__(self, base):
    self.base = base
  def calcular(self, x):
    if x <= 0 or self.base <= 0 or self.base == 1:
      raise ValueError("El argumento debe ser > 0 y la base > 0 (distinta de 1)")
    return math.log(x) / math.log(self.base)