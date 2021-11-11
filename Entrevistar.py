"""
Class Entrevista, Nombre, Sexo, Edad, Estatura, Cargo, justificacion.
Solicitud de informacion.-
1.- Hablame de ti
2.- ¿Porque te interesa el puesto?
3.- ¿Que sabes de nuestra empresa?
4.- ¿Que te gusta hacer en tu tiempo libre?
5.- ¿Cual es tu meta en la vida?
6.- ¿Tuviste un anterior empleo?
7.- ¿Porque dejaste tu arnterior empleo?
8.- Cuéntame de algún momento de tu vida laboral
    en el que hayas cometido un error, ¿cómo lo solucionaste?
"""
import csv
import Trabajar as Trabajador
Encuesta = []
lista_preguntas = []

with open('Preguntas.csv', newline='') as csvfile:
    mispreguntas = csv.DictReader(csvfile)
    for filas in mispreguntas:
        print(filas)
    csvfile.close()

class Entrevista:
     def __init__(self, Nombre, Sexo, Edad, Estatura, Area_de_experiencia, Tiempo_de_experiencia):
        Trabajador.Empleado.__init__(self, Nombre, Sexo, Edad, Estatura, Area_de_experiencia, Tiempo_de_experiencia)
