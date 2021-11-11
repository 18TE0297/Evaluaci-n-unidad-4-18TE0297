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
                    if perfil == 2:
                        print("Biemvenido a", Empresa, "aspirante")
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
                    if eleccion == 2:
                        print("Bienvenido a su trabajo.", "\n","Sus pendientes son:")
                    if eleccion == 3:
                        print("Bienvenido Comenzaremos su entrevista")
                    if eleccion == 4:
                        print("Hasta pronto")
                        break
                else:
                    print("Ingrese su eleccion en el rango otorgado")

            except ValueError:
                print("Por favor, ingrese solo valores numerico")




