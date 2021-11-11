"""
Clase_Persona, Nombre, Sexo, Edad, Estatura, Cargo.
Clase_Vestirese, Casual, Formal, Uniforme.
"""
class Persona:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Cargo=None):
        self.__Nombre = Nombre
        self.__Sexo = Sexo
        self.__Edad = Edad
        self.__Estatura = Estatura
        self.__Cargo = Cargo
