"""
Clase Gerente, Nombre, Edad, Sexo, Antiguedad
Clase Empleado, Nombre, Edad, Sexo, Estatura, Area de experiencia, Tiempo de experiencia
"""
import Vestirse
class Gerente:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Cargo, Antiguedad):
        self.__Antiguedad = Antiguedad
        Vestirse.Persona.__init__(self, Nombre, Sexo, Edad, Estatura, Cargo)

    def Formato(self):
        print("Favor de llenar el formato", type(self).__name__)

   # def Entrevista_de_trabajo(self):

