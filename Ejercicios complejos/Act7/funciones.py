"""
Nombre:         TV por Internet
Archivo:        funciones.py
Autor:          Alberto Sánchez Barona
Fecha:          17/11/2022 
"""
CONEXIONES_POR_DEFECTO = 1
CONEXIONES_MAXIMAS = 6

class NombreEnBlanco(Exception):
    pass


class OpcionMenuNoValida(Exception):
    pass


class OpcionRepetida(Exception):
    pass


class NumeroConexionesSimultaneas(Exception):
    pass


def pregunta(pregunta):
    """
    Función:        pregunta(pregunta)
    Descripción:    Pregunta al usuario lo que pasemos como argumento.
    Parámetros:
        pregunta:   Argumento para preguntar.
    Return:         Devuelve True o False.
    """

    respuesta_valida = False

    while not respuesta_valida:

        respuesta = input(pregunta + " (S/n)? ")

        if respuesta == "" or respuesta.upper() == "S" or respuesta.upper() == "N":
            respuesta_valida = True
        else:
            print("ERROR -> Debes introducir [S]i o [N]o")
            print("Inténtelo de nuevo...")

    if respuesta == "" or respuesta.upper() == "S":
        return True
    else:
        return False


def menu_servicios():
    """
    Función:        menu_servicios()
    Descripción:    Muestra el menú de los servicios.
    Parámetros:     Ninguno.
    Return:         No devuelve nada.
    """

    print("----------------------")
    print("|   Menú servicios   |")
    print("----------------------")
    print("| Series.........15€ |")
    print("| Películas......20€ |")
    print("| Documentales....5€ |")
    print("----------------------")


def opcion_menu_servicios():
    """
    Función:        opcion_menu_servicios()
    Descripción:    Pregunta al cliente que elija servicios.
    Parámetros:     Ninguno.
    Return:         Devuelve el servicio seleccionado y su precio.
    """

    opcion_servicios_valido = False

    while not opcion_servicios_valido:

        try:

            opcion_servicios = input("Introduzca el nombre del servicio que quiera contratar: ")

            if opcion_servicios.upper() == "SERIES":
                opcion_servicios = "Series"
                precio_servicio = 15
            
            elif opcion_servicios.upper() == "PELÍCULAS" or opcion_servicios.upper() == "PELICULAS":
                opcion_servicios = "Películas"
                precio_servicio = 20

            elif opcion_servicios.upper() == "DOCUMENTALES":
                opcion_servicios = "Documentales"
                precio_servicio = 5

            else:
                raise OpcionMenuNoValida("Compruebe lo que ha escrito e inténtelo de nuevo...")
        
        except OpcionMenuNoValida as omnv:
            print(omnv.__str__())

        else:
            opcion_servicios_valido = True
    
    return opcion_servicios, precio_servicio

def menu_canales():
    """
    Función:        menu_canales()
    Descripción:    Muestra el menú de los canales de TV.
    Parámetros:     Ninguno.
    Return:         No devuelve nada.
    """

    print("----------------------------------------------------------------------------------|")
    print("|                                 Canales de TV                                   |")
    print("----------------------------------------------------------------------------------|")
    print("| Temática del canal |                Programas incluidos                | Precio |")
    print("|----------------------------------------------------------------------------------")
    print("| Deportes           | Champions, Europa League, La liga, La premier     |  25 €  |")
    print("| Comedia            | Todo Monólogos, Comedy Movies                     |  10 €  |")
    print("| Niños              | La Fábrica de Chocolate, Kinder Shows, Toddler TV |  15 €  |")
    print("| Películas clásicas | Classics Movies, Golden Hollywood                 |   5 €  |")
    print("-----------------------------------------------------------------------------------")


def opcion_menu_canales():
    """
    Función:        opcion_menu_canales()
    Descripción:    Pregunta al cliente que elija canales.
    Parámetros:     Ninguno.
    Return:         Devuelve el canal seleccionado y su precio.
    """
    
    opcion_canales_valido = False

    while not opcion_canales_valido:
        
        try:
            opcion_canales = input("Introduzca el nombre del canal que quiera contratar: ")

            if opcion_canales.upper() == "DEPORTES":
                opcion_canales = "Deportes"
                precio_canal = 25
            
            elif opcion_canales.upper() == "COMEDIA":
                opcion_canales = "Comedia"
                precio_canal = 10
            
            elif opcion_canales.upper() == "NIÑOS" or opcion_canales.upper() == "NINOS":
                opcion_canales = "Niños"
                precio_canal = 15
                
            elif opcion_canales.upper() == "PELÍCULAS CLÁSICAS" or opcion_canales.upper() == "PELICULAS CLASICAS":
                opcion_canales = "Películas Clásicas"
                precio_canal = 5

            else:
                raise OpcionMenuNoValida("Compruebe lo que ha escrito e inténtelo de nuevo...")

        except OpcionMenuNoValida as omnv:
            print(omnv.__str__())

        else:
            opcion_canales_valido = True
    
    return opcion_canales, precio_canal


def conexiones_simultaneas():
    """
    Función:        conexiones_simulatenas()
    Descripción:    Pregunta al cliente cuantas conexiones simultáneas desea disponer, mínimo 1, máximo 6.
    Parámetros:     Ninguno
    Return:         Devuelve el número de conexiones simultáneas.
    """

    conexion_valida = False
    
    while not conexion_valida:

        try:

            conexiones = int(input("Introduzca el número de conexiones simultáneas que desea disponer: "))

            if conexiones < CONEXIONES_POR_DEFECTO or conexiones > CONEXIONES_MAXIMAS:
                raise NumeroConexionesSimultaneas(f"Ha elegido {conexiones} conexiones simultáneas, cuando el mínimo es de {CONEXIONES_POR_DEFECTO} y el máximo es de {CONEXIONES_MAXIMAS}")
        
        except NumeroConexionesSimultaneas as ncs:
            print(ncs.__str__())

        except ValueError:
            print(ncs.__str__())
        
        else:
            conexion_valida = True
    
    return conexiones


def porcentaje_conexiones_simultaneas(conexiones, precio_sin_incremento):
    """
    Función:        porcentaje_conexiones_simultaneas()
    Descripción:    Calcula el porcentaje de incremento según las conexiones.
    Parámetros:
        conexiones: Número de conexiones.
    Return:         Devuelve el porcentaje de incremento.
    """

    precio_con_incremento = 0

    for i in range(CONEXIONES_POR_DEFECTO, conexiones + 1):
        if i == 1:
            precio_con_incremento = 0
        elif i == 2:
            precio_con_incremento = precio_sin_incremento + (precio_sin_incremento * 0.025)
        elif i == 3:
            precio_con_incremento = precio_sin_incremento + (precio_sin_incremento * 0.035)
        elif i == 4:
            precio_con_incremento = precio_sin_incremento + (precio_sin_incremento * 0.045)
        elif i == 5:
            precio_con_incremento = precio_sin_incremento + (precio_sin_incremento * 0.055)
        elif i == 6:
            precio_con_incremento = precio_sin_incremento + (precio_sin_incremento * 0.065)
    
    return precio_con_incremento


def calcular_descuento(precio_con_incremento, contador_servicios, contador_canales):
    """
    Función:                    calcular_descuento()
    Descripción:                Calcula el descuento.
    Parámetros:
        precio_con_incremento:  Precio total.
        contador_servicios:     Número de servicios contratados.
        contador_canales:       Número de canales contratados.
    Return:                     Devuelve el descuento completo.
    """

    porcentaje_servicio = 0
    porcentaje_canal = 0

    match contador_servicios:
        
        case 0:
            porcentaje_servicio = precio_con_incremento * 0
            descuento_servicio = precio_con_incremento - porcentaje_servicio
        
        case 1:
            porcentaje_servicio = precio_con_incremento * 0
            descuento_servicio = precio_con_incremento - porcentaje_servicio

        case 2:
            porcentaje_servicio = precio_con_incremento * 0.05
            descuento_servicio = precio_con_incremento - porcentaje_servicio
        
        case 3:
            porcentaje_servicio = precio_con_incremento * 0.1
            descuento_servicio = precio_con_incremento - porcentaje_servicio

    descuento_canal = descuento_servicio

    match contador_canales:

        case 0:
            porcentaje_canal = precio_con_incremento * 0
            descuento_canal = precio_con_incremento - porcentaje_canal

        case 1:
            porcentaje_canal = precio_con_incremento * 0
            descuento_canal = precio_con_incremento - porcentaje_canal

        case 2:
            porcentaje_canal = precio_con_incremento * 0.05
            descuento_canal = precio_con_incremento - porcentaje_canal

        case 3:
            porcentaje_canal = precio_con_incremento * 0.1
            descuento_canal = precio_con_incremento - porcentaje_canal

        case 4:
            porcentaje_canal = precio_con_incremento * 0.15
            descuento_canal = precio_con_incremento - porcentaje_canal

    return descuento_canal