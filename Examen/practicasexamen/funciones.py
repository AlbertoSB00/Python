"""
Proyecto:           practicasexamen
Archivo:            funciones.py
Autor:              Alberto Sánchez Barona
Fecha:              28/11/2022
"""
class EleccionCursoNoValidoExcepcion(Exception):
    pass


def pregunta_si_no(pregunta):

    opcion_valida = False

    respuesta = input(pregunta + "? Introduzca [S]i o [n]o: ")

    if respuesta == "" or respuesta.upper() == "S" or respuesta.upper() == "N":
        opcion_valida = True
    else:
        print("Introduzca una respuesta válida: [s]i o [n]o")
        print("Inténtelo de nuevo...")
    
    if respuesta == "" or respuesta.upper() == "S":
        return True
    else:
        return False


def elegir_cursos():
    """
    Función:            elegir_cursos()
    Descripción:        Pregunta los cursos que desea.
    Parámetros:         Ninguno.
    Return:             Devuelve el curso y su precio.
    """

    opcion_valida = False

    while not opcion_valida:

        try:

            precio_curso = 0
            opcion = input("Introduzca las tres primeras letras del cursos para añadirlo: ")

            match opcion:
                case "OFI":
                    curso = "OFI"
                    precio_curso = 100

                case "PRO":
                    curso = "PRO"
                    precio_curso = 200

                case "REP":
                    curso = "REP"
                    precio_curso = 150

                case "CON":
                    curso = "CON"
                    precio_curso = 300

                case "REC":
                    curso = "REC"
                    precio_curso = 250

                case "LEY":
                    curso = "LEY"
                    precio_curso = 150

                case "RET":
                    curso = "RET"
                    precio_curso = 200

                case "LOG":
                    curso = "LOG"
                    precio_curso = 250

                case _:
                    raise EleccionCursoNoValidoExcepcion("Compruebe lo que ha escrito e inténtelo de nuevo...")
        
        except EleccionCursoNoValidoExcepcion as ecnve:
            print(ecnve.__str__())
        
        else:
            opcion_valida = True
    
    return curso, precio_curso