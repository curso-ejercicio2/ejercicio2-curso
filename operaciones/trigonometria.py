import math


class FuncionesTrigonometricas:
    """Calcula funciones trigonometricas usando angulos en grados."""
    #Mantener estaticos para mejor manejo en estos casos 
    
    @staticmethod
    def seno(angulo):
        return math.sin(math.radians(angulo))
    
    @staticmethod
    def coseno(angulo):
        return math.cos(math.radians(angulo))

    @staticmethod
    def tangente(angulo):
        coseno = math.cos(math.radians(angulo))
        if math.isclose(coseno, 0, abs_tol=1e-12):
            raise ValueError("La tangente no esta definida para este angulo")
        return math.tan(math.radians(angulo))

    @staticmethod
    def arco_tangente(valor):
        return math.degrees(math.atan(valor))