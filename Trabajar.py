"""
Clase Gerente, Nombre, Edad, Sexo, Antiguedad
Clase Empleado, Nombre, Edad, Sexo, Estatura, Area de experiencia, Tiempo de experiencia
"""
import Vestirse as Pers

class Gerente:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Cargo, Antiguedad):
        self.__Antiguedad = Antiguedad
        Pers.Persona.__init__(self, Nombre, Sexo, Edad, Estatura, Cargo)

class Empleado:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Area_de_experiencia, Tiempo_de_experiencia):
        self.__Area_de_trabajo = Area_de_experiencia
        self.__Tiempo_de_experiencia = Tiempo_de_experiencia
        Pers.Persona.__init__(self, Nombre, Sexo, Edad, Estatura, Cargo)
