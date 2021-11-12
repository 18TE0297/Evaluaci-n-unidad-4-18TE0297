"""
Clase Gerente, Nombre, Edad, Sexo, Antiguedad
Clase Empleado, Nombre, Edad, Sexo, Estatura, Area de experiencia, Tiempo de experiencia
"""
import Vestirse
class Gerente:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Cargo, Antiguedad):
        self.__Antiguedad = Antiguedad
        Vestirse.Persona.__init__(self, Nombre, Sexo, Edad, Estatura, Cargo)

class Supervicion_planta:
    def __init__(self, Nombre, Cargo, Fecha, Hora):
        self.__Fecha = Fecha
        self.__Hora = Hora
        Vestirse.Persona.__init__(self, Nombre, Cargo)

