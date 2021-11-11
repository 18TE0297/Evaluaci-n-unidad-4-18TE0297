"""
Clase Gerente, Nombre, Edad, Sexo, Antiguedad
Clase Empleado, Nombre, Edad, Sexo, Estatura, Area de experiencia, Tiempo de experiencia
"""
import Vestirse as Pers

class Gerente:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Cargo, Antiguedad):
        self.__Antiguedad = Antiguedad
        Pers.Persona.__init__(self, Nombre, Sexo, Edad, Estatura, Cargo)

    def Formato(self):
        print("Favor de llenar el formato", type(self).__name__)
    def Planificar(self):


    #def Organizar(self):

    #def Entrevista_de_trabajo(self):

