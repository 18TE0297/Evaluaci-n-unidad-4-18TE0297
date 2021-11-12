"""
Clase_Persona, Nombre, Sexo, Edad, Estatura, Cargo.
Clase_Vestirese, Casual, Formal, Uniforme.
"""

class Persona:
    def __init__(self, Nombre, Sexo, Edad, Estatura, Cargo=None, Calzado = None):
        self.__Nombre = Nombre
        self.__Sexo = Sexo
        self.__Edad = Edad
        self.__Estatura = Estatura
        self.__Cargo = Cargo
        self.__Calzado = Calzado
    def getNombre(self):
        return self.__Nombre
    def getSexo(self):
        return self.__Sexo
    def getEdad(self):
        return self.__Edad
    def getEstatura(self):
        return self.__Estatura
    def getCargo(self):
        return self.__Cargo
    def getCalzado(self):
        return self.__Calzado

    def setNombre(self, NewNombre):
        self.__Nombre = NewNombre
    def setSexo(self, NewSex):
        self.__Sexo = NewSex
    def setEdad(self, NewEdad):
        self.__Edad = NewEdad
    def setEstatura(self, NewEstatura):
        self.__Estatura = NewEstatura
    def setCargo(self, NewCargo):
        self.__Cargo = NewCargo
    def setCalzado(self, NewCalzado):
        self.__Calzado = NewCalzado



class VCasual(Persona):
    def __init__(self, Polera, Jeans, Calzado):
        Persona.__init__(self, Calzado)
        self.__Polera = Polera
        self.__Jeans = Jeans


    def getPolera(self):
        return self.__Polera
    def getJeans(self):
        return self.__Jeans

    def setPolera(self, NewPolera):
        self.__Polera = NewPolera
    def setJeans(self, NewJeans):
        self.__Jeans = NewJeans

class VFormal(Persona):
    def __init__(self, Camisa, Saco, Corbata, Pantalon_Vestir, Calzado):
        Persona.__init__(self, Calzado)
        self.__Camisa = Camisa
        self.__Saco = Saco
        self.__Corbata = Corbata
        self.__Pantalon_Vestir = Pantalon_Vestir

    def getCamisa(self):
        return self.__Camisa

    def getSaco(self):
        return self.__Saco

    def getCorbata(self):
        return self.__Corbata

    def getPantalon_Vestir(self):
        return self.__Pantalon_Vestir

    def setCamisa(self, NewCamisa):
        self.__Camisa = NewCamisa

    def setSaco(self, NewSaco):
        self.__Saco = NewSaco

    def setCorbata(self, NewCorbata):
        self.__Corbata = NewCorbata

    def setPantalon_Vestir(self, NewPantalon):
        self.__Pantalon_Vestir = NewPantalon

class VUniforme(Persona):
    def __init__(self, Uniforme, Calzado):
        Persona.__init__(self, Calzado)
        self.__Uniforme = Uniforme

    def getUniforme(self):
        return self.__Uniforme

    def setUniforme(self, NewUniforme):
        self.__Uniforme = NewUniforme

