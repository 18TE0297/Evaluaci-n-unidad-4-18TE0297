"""
------------------------- MODELAR GERENTE-------------------------
Escriba una aplicación que modele en el paradigma orientado a objetos el siguiente escenario:
“El gerente de la empresa es un empleado que mide 1.80 m, se llama <nombre> y tiene puesto un
saco con tres botones. En este momento el gerente está entrevistando a una persona para su
contratación.”

Deberás generar múltiples archivos que representen la situación de la vida real en términos
de programación. Así tendrás varias clases como son: gerente, persona, empleado, empresa,
vestimenta, saco, etc. Debes establecer en ellas comportamientos como vestirse, trabajar
y entrevistar que hagan que el escenario cobre vida.
"""
import Vestirse, Trabajar, Entrevistar
import csv
import pprint
def Usuario():
    print(Datos)
def Entrevistado():
    print(Datos1)

Empresa = input(print("Ingrese el nombre de la empresa"))
print("Bienvenido a", Empresa, "favor de seleccionar su perfil","\n",
      "1.-Gerente", "\n",
      "2.-Persona_Entrevistada")
while True:
            try:
                perfil = float(input("Ingrese la eleccion de su perfil: "))
                if ((perfil >= 1) & (perfil <= 2)):
                    if perfil == 1:
                        print("Bienvenido a", Empresa, "Gerente")
                        print("Para seguir su proceso es necesario ingresar sus datos en el siguiente formato", "\n",
                              "Nombre, Sexo, Edad_años, Estatura_m, Cargo, Antiguedad")
                        Datos = input(Trabajar.Gerente)
                        print(Datos)
                        break
                    if perfil == 2:
                        print("Biemvenido a", Empresa, "aspirante")
                        print("Para seguir su proceso es necesario ingresar sus datos en el siguiente formato", "\n",
                              "Nombre, Sexo, Edad, Estatura, Area_de_experiencia, Tiempo_de_experiencia")
                        Datos = input(Entrevistar.Persona_Entrevistada)
                        print(Datos)
                        break

                else:
                    print("Ingrese su eleccion en el rango otorgado")

            except ValueError:
                print("Por favor, ingrese solo valores numerico")

print("¿Que desea Realizar hoy?,", "\n"
      "Favor de verificar las opciones disponibles")
print(" 1.-Vestirse", "\n",
      "2.-Trabajar", "\n",
      "3.-Entrevistar", "\n",
      "4.-Salir")
while True:
            try:
                eleccion = float(input("Ingrese su eleccion en el rango [1,4]: "))
                if ((eleccion >= 1) & (eleccion <= 4)):
                    if eleccion == 1:
                        print("Bienvenido comenzaremos a seleccionar su Outfit")
                        print("Favor se seleccionar su el estilo que desea portar el dia de hoy", "\n",
                              "1.- Vestimenta Casual", "\n",
                              "2.- Vestimenta Formal", "\n",
                              "3.- Vestimenta Uniforme")
                        while True:
                                    try:
                                        Outfit = float(input("Ingrese la eleccion de su Outfit: "))
                                        if ((Outfit >= 1) & (Outfit <= 3)):
                                            if Outfit == 1:
                                                print("Exelente decision, favor de introducir sus prendas en el siguiente formato.","\n",
                                                      "Polera(Playera o Sudadera casual), Jeans(Short, Bermuda, pans, Pantalon), Calzado")
                                                VestCasual = input(Vestirse.VCasual)
                                                print(Datos)
                                                print(VestCasual)
                                                print("¿Que mas desea realizar hoy?,", "\n",
                                                      "Favor de verificar las opciones disponibles")
                                                print(" 1.-Vestirse", "\n",
                                                      "2.-Trabajar", "\n",
                                                      "3.-Entrevistar", "\n",
                                                      "4.-Salir")
                                                break
                                            if Outfit == 2:
                                                print("Exelente decision, favor de introducir sus prendas en el siguiente formato.","\n",
                                                        "Camisa, Saco, Corbata, Pantalon de vestir, Calzado")
                                                VestFormal = input(Vestirse.VFormal)
                                                print(Datos)
                                                print(VestFormal)
                                                print("¿Que mas desea realizar hoy?,", "\n",
                                                      "Favor de verificar las opciones disponibles")
                                                print(" 1.-Vestirse", "\n",
                                                      "2.-Trabajar", "\n",
                                                      "3.-Entrevistar", "\n",
                                                      "4.-Salir")
                                                break
                                            if Outfit == 3:
                                                print("Exelente decision, favor de introducir sus prendas en el siguiente formato.", "\n",
                                                    "Uniforme(Descripcion), Calzado")
                                                VestUniforme = input(Vestirse.VUniforme)
                                                print(Datos)
                                                print(VestUniforme)
                                                print("¿Que mas desea realizar hoy?,", "\n",
                                                      "Favor de verificar las opciones disponibles")
                                                print(" 1.-Vestirse", "\n",
                                                      "2.-Trabajar", "\n",
                                                      "3.-Entrevistar", "\n",
                                                      "4.-Salir")
                                                break

                                        else:
                                            print("Ingrese su eleccion en el rango otorgado")

                                    except ValueError:
                                        print("Por favor, ingrese solo valores numerico")
                    if eleccion == 2:
                        print("Bienvenido a su trabajo.", "\n","Sus pendientes son:")
                        print("Favor de seleccionar el pendiente que realizara el dia de hoy","\n",
                              "1.- Entreviar_Aspirantes","\n",
                              "2.- Supervicion_control")
                        while True:
                                    try:
                                        Trabajo = float(input("Ingrese la eleccion del trabajo a realizar:"))
                                        if ((Trabajo >= 1) & (Trabajo <= 2)):
                                            if Trabajo == 1:
                                                print("Bienvenivo aspirante soy", Datos, "Te precento el cuestionario que deberas llenar")
                                                print("Nombre, Sexo, Edad, Estatura, Area_de_experiencia, Tiempo_de_experiencia")
                                                Datos1 = input(Entrevistar.Persona_Entrevistada)
                                                print(Datos1)
                                                print("A continuacion se muestran las preguntas que debera contestar")

                                                listaPreguntas = []

                                                with open('Preguntas.csv', newline='') as csvfile:
                                                    mispreguntas = csv.DictReader(csvfile)
                                                    for filas in mispreguntas:
                                                        auxpreguntas = filas["Pregunta"], filas["Respuesta"]
                                                        listaPreguntas.append(auxpreguntas)
                                                    csvfile.close()
                                                    i = 1
                                                    for pregunta in listaPreguntas:
                                                        print(i, pregunta)
                                                        i = i + 1
                                                Misrespuestas = {
                                                    'Pregunta1': input("R1="),
                                                    'Pregunta2': input("R2="),
                                                    'Pregunta3': input("R3="),
                                                    'Pregunta4': input("R4="),
                                                    'Pregunta5': input("R5="),
                                                    'Pregunta6': input("R6="),
                                                    'Pregunta7': input("R7="),
                                                    'Pregunta8': input("R8=")
                                                }
                                                print("Sus respuestas fueron guardadas:")
                                                pprint.pprint(Misrespuestas)
                                                print("¿Que mas desea realizar hoy?,", "\n",
                                                      "Favor de verificar las opciones disponibles")
                                                print(" 1.-Vestirse", "\n",
                                                      "2.-Trabajar", "\n",
                                                      "3.-Entrevistar", "\n",
                                                      "4.-Salir")
                                                break
                                            if Trabajo == 2:
                                                print("Bienvenido a su trabajo, procederemos a realizar la supervicion de personal")
                                                print("Por favor introdusca los datos correspondientes de quien realiza el llenado del reporte", "\n",
                                                      " Nombre, Cargo, Fecha(__/__/__), Hora(0-24)")
                                                Supervicion = input(Trabajar.Supervicion_planta)
                                                print(Supervicion)
                                                listaPreguntas = []

                                                with open('ListaCotejo.csv', newline='') as csvfile:
                                                    mispreguntas = csv.DictReader(csvfile)
                                                    for filas in mispreguntas:
                                                        auxpreguntas = filas["ListaC"], filas["Respuesta"]
                                                        listaPreguntas.append(auxpreguntas)
                                                    csvfile.close()
                                                    i = 1
                                                    for pregunta in listaPreguntas:
                                                        print(i, pregunta)
                                                        i = i + 1
                                                print("Registre solo Si / No")
                                                Misrespuestas = {
                                                    'Punto1': input("R1="),
                                                    'Punto2': input("R2="),
                                                    'Punto3': input("R3="),
                                                    'Punto4': input("R4="),
                                                    'Punto5': input("R5="),
                                                }
                                                print("Sus respuestas fueron guardadas:")
                                                pprint.pprint(Misrespuestas)

                                                print("¿Que mas desea realizar hoy?,", "\n",
                                                      "Favor de verificar las opciones disponibles")
                                                print(" 1.-Vestirse", "\n",
                                                      "2.-Trabajar", "\n",
                                                      "3.-Entrevistar", "\n",
                                                      "4.-Salir")
                                                break

                                        else:
                                            print("Ingrese su eleccion en el rango otorgado")

                                    except ValueError:
                                        print("Por favor, ingrese solo valores numerico")
                    if eleccion == 3:
                        print("Bienvenido a la entrevista de trabajo.")
                        print("Porfavor introdusca los datos del Entrevistador", "\n",
                              "Nombre, Sexo, Edad_Años, Estatura_m, Cargo, Antiguedad")
                        Gerente1 = input(Trabajar.Gerente)
                        print(Gerente1)
                        print("Porfavor introdusca los datos del entrevistado", "\n",
                              "Nombre, Sexo, Edad_Años, Estatura_m, Area_de_experiencia, Tiempo_de_experiencia")
                        Entrevistado1 = input(Entrevistar.Persona_Entrevistada)
                        print(Entrevistado1)
                        print("Introdusca 1 cuando este listo para comenzar la entrevista", "\n",
                              "1.- Entreviar_Aspirantes")
                        while True:
                            try:
                                Trabajo = float(input("Todo esta listo para comenzar:"))
                                if Trabajo == 1:
                                    print("A continuacion se muestran las preguntas que debera contestar")

                                    listaPreguntas = []

                                    with open('Preguntas.csv', newline='') as csvfile:
                                        mispreguntas = csv.DictReader(csvfile)
                                        for filas in mispreguntas:
                                            auxpreguntas = filas["Pregunta"], filas["Respuesta"]
                                            listaPreguntas.append(auxpreguntas)
                                        csvfile.close()
                                        i = 1
                                        for pregunta in listaPreguntas:
                                            print(i, pregunta)
                                            i = i + 1
                                    Misrespuestas = {
                                        'Pregunta1': input("R1="),
                                        'Pregunta2': input("R2="),
                                        'Pregunta3': input("R3="),
                                        'Pregunta4': input("R4="),
                                        'Pregunta5': input("R5="),
                                        'Pregunta6': input("R6="),
                                        'Pregunta7': input("R7="),
                                        'Pregunta8': input("R8=")
                                    }
                                    print("Sus respuestas fueron guardadas:")
                                    pprint.pprint(Misrespuestas)
                                    print("¿Que mas desea realizar hoy?,", "\n",
                                          "Favor de verificar las opciones disponibles")
                                    print(" 1.-Vestirse", "\n",
                                          "2.-Trabajar", "\n",
                                          "3.-Entrevistar", "\n",
                                          "4.-Salir")
                                    break
                                else:
                                    print("Ingrese su eleccion en el rango otorgado")

                            except ValueError:
                                print("Por favor, ingrese solo valores numerico")


                    if eleccion == 4:
                        print("Hasta pronto, Que tenga un buen dia")
                        break
                else:
                    print("Ingrese su eleccion en el rango otorgado")

            except ValueError:
                print("Por favor, ingrese solo valores numerico")
