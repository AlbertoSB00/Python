"""
Proyecto:           Cursos Online
Archivo:            funciones.py
Autor:              Alberto Sánchez Barona
Fecha:              10/11/2022
Descripción:        Contiene funciones usadas en el programa principal
"""

import generic_functions as gf


class OpcionNoValidaMatch(Exception):
    pass


class EleccionErronea(Exception):
    pass


def menu():
    """
    Función:            menu
    Descripción:        Muestra un menú.
    Return:             No devuelve nada.
    """

    # Comenzamos a crear el menú con las opciones con print.
    print("")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("|            Informática            ||       Administración de Empresas      ||               Diseño gráfico               |")
    print("|-----------------------------------||---------------------------------------||--------------------------------------------|")
    print("| OFImática -> 100€                 || CONtabilidad y Finanzas -> 300€       || FOTográfico -> 200€                        |")
    print("| PROgramación -> 200€              || RECursos Humanos -> 300€              || CREación de Logotipos Corporativos -> 250€ |")
    print("| REParación de ordenadores -> 150€ || LEYes Tributarias de Empresas -> 150€ ||                                            |")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("")

    return ""

def eleccion_menu():
    """
    Función:            eleccion_menu
    Descripción:        Pregunta al cliente una opción del menú anterior.
    Return:             La cadena cursos.
    """

    opcion_valida = True

    cursos = ""

    # Mientras el interruptor sea verdadero, preguntamos que curso quiere.
    while opcion_valida:

        opcion = (input("Estos son los cursos diponibles. Introduzca las tres primeras letras del curso para añadirlo a la cesta: "))

        # Concatemos la opción a la variable cursos y un guión para que aparezca separado en la variable. (OFI-FOT-PRO-)
        cursos = opcion + "-" + cursos

        # Preguntamos si quiere seguir comprando más cursos con las funciones genéricas.
        mas_cursos = gf.question_yes_no("¿Quiéres comprar más cursos")

        if mas_cursos:
            opcion_valida = True
        else:
            opcion_valida = False
    
    return cursos


def clases_presenciales():
    """
    Función:            clases_presenciales
    Descripción:        Pregunta al cliente si quiere clases presenciales, si es así, cuántas.
    Return:             El incremento y el número de clases presenciales.
    """

    print("Puede elegir hasta 3 clases presenciales con un incremento en el precio final de: 5% | 7.5% | 10%")
    cuantas_clases_presenciales = int(input("¿Cuántas clases presenciales quiere? "))

    interruptor = False

    while not interruptor:

        try:

            match cuantas_clases_presenciales:
                case 0:
                    incremento = 0
                case 1:
                    incremento = 5
                case 2:
                    incremento = 7.5
                case 3:
                    incremento = 10
                case _:
                    raise OpcionNoValidaMatch(f"{cuantas_clases_presenciales} no es una opción válida, introduzca una opción entre 0 y 3.")

        except OpcionNoValidaMatch as onvm:
            print(onvm.__str__())
            print("Inténtalo de nuevo...")
        
        else:
            interruptor = True

    return incremento