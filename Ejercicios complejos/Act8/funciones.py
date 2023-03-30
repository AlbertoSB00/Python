"""
Programa:       Paquete vacacional
Archivo:        funciones.py
Autor:          Alberto Sánchez Barona
Fecha:          25/11/2022
"""


class ErrorNumeroNegativoExepcion(Exception):
    pass


class NumeroDeNinosSuperiorExcepcion(Exception):
    pass


class DestinoVacacionalNoExisteExepcion(Exception):
    pass


def pregunta_si_no(pregunta):

    respuesta_valida = False

    while not respuesta_valida:

        respuesta = input(pregunta + "? Introduzca [S]i/[n]o: ")

        if respuesta == "" or respuesta.upper() == "S" or respuesta.upper() == "N":
            respuesta_valida = True

        else:
            print("Debes introducir una respuesta válida, [s] o [n]")
            print("Inténtelo de nuevo...")
    
    if respuesta == "" or respuesta.upper() == "S":
        return True
    else:
        return False


def leer_numero(caption: str) -> int:
    """
    Función:            leer_numero
    Descripción:        Pide al usuario un número mediante un caption.
    Parametros:
        caption:        Pregunta que se le hace al usuario.
    Return:             Devuelve un número entero.
    """
    numero_valido = False

    while not numero_valido:

        try:

            numero = int(input(caption))

            if numero < 0:
                raise ErrorNumeroNegativoExepcion("El número introducido no puede ser negativo")
        
        except ErrorNumeroNegativoExepcion as enne:
            print(enne.__str__())
            print("Inténtelo de nuevo...")
        
        except ValueError:
            print("Compruebe lo que ha introducido e inténtelo de nuevo...")
        
        else:
            numero_valido = True
    
    return numero


def ninos_menores_5(numero_ninos: int) -> int:
    """
    Función:            ninos_menores_5
    Descripción:        De un número de niños pregunta cuántos son menores de 5 años.
    Parámetros:
        numero_ninos:   El número de niños que ha introducido.
    Return:             Devuelve el número de niños menores de 5 años.
    """

    numero_valido = False

    while not numero_valido:

        try: 

            numero_ninos_menores_5 = int(input(f"De los {numero_ninos} niños que ha introducido, ¿cuántos son menores de 5 años? "))

            if numero_ninos_menores_5 < 0:
                raise ErrorNumeroNegativoExepcion("El número introducido no puede ser negativo")
            
            if numero_ninos_menores_5 > numero_ninos:
                raise NumeroDeNinosSuperiorExcepcion(f"El número de niños no puede superar los {numero_ninos} que ha introducido.")

        except ErrorNumeroNegativoExepcion as enne:
            print(enne.__str__())
            print("Inténtelo de nuevo...")
            
        except NumeroDeNinosSuperiorExcepcion as ndnse:
            print(ndnse.__str__())
            print("Inténtelo de nuevo...")
            
        except ValueError:
                print("Compruebe lo que ha introducido e inténtelo de nuevo...")
            
        else:
            numero_valido = True
    
    return numero_ninos_menores_5


def destino(dias: int, numero_adultos: int, numero_ninos: int, numero_ninos_menores_5: int):
    """
    Función:            destino()
    Descripción:        En función de unos datos muestra destinos turísticos.
    Parámetros:
        dias:                   Número de días.
        numero_adultos:         Número de adultos.
        numero_ninos:           Número de niños.
        numero_ninos_menores_5: Número de niños menores de 5 años.
    Return:                     Devuelve los posibles destinos.
    """
    if dias < 8:
        print(f"En estos momentos no disponemos de paquetes vacacionales de menos de {dias} días. Saliendo del programa...")
        exit(2)

    if dias >= 8:
        print("Fiordos noruegos → Crucero de 8 días con salida en Kristiansand y navegación por la costa noruega haciendo escala en Oslo, Bergen y Trodhein. El coste es de 150 € por adulto/dia y 55 € por niño mayor de 5 años/dia.")

    if dias >= 12:
        print("Imperio Austro → 12 días con estancias en Praga, Viena y Budapest. Se visitan los lugares más emblemáticos de la época imperial. El coste es de 120 € por adulto/dia y 50 € por niño mayor de 5 años/dia.")

    if dias >= 15:
        print("Repúblicas bálticas → 15 días de con estancias en Tallin, Riga y Vilnius. El coste es de 80 € por adulto/dia y 35 € por niño mayor de 5 años/dia.")
    
    opcion_valida = False
    coste = 0

    while not opcion_valida:

        try:

            opcion = input("Introduzca el nombre del destino que desea ir: ")

            if opcion.upper() == "FIORDOS NORUEGOS":
                destino = "Fiordos noruegos"
                adulto_paga = 150
                nino_paga = 55
                dias_destino = 8
                precio_adulto = numero_adultos * adulto_paga
                precio_nino = numero_ninos * nino_paga
                precio_total_adulto = precio_adulto * dias_destino
                precio_total_nino = precio_nino * dias_destino
                precio_total = precio_total_adulto + precio_total_nino
                
                

            elif opcion.upper() == "IMPERIO AUSTRO":
                destino = "Imperio Austro"
                adulto_paga = 120
                nino_paga = 50
                dias_destino = 12
                precio_adulto = numero_adultos * adulto_paga
                precio_nino = numero_ninos * nino_paga
                precio_total_adulto = precio_adulto * dias_destino
                precio_total_nino = precio_nino * dias_destino
                precio_total = precio_total_adulto + precio_total_nino
                

            elif opcion.upper() == "REPÚBLICAS BÁLTICAS" or opcion.upper == "REPUBLICAS BÁLTICAS" or opcion.upper() == "REPÚBLICAS BALTICAS" or opcion.upper() == "REPUBLICAS BALTICAS":
                destino = "Repúblicas Bálticas"
                adulto_paga = 80
                nino_paga = 35
                dias_destino = 15
                precio_adulto = numero_adultos * adulto_paga
                precio_nino = numero_ninos * nino_paga
                precio_total_adulto = precio_adulto * dias_destino
                precio_total_nino = precio_nino * dias_destino
                precio_total = precio_total_adulto + precio_total_nino
            
            else:
                raise DestinoVacacionalNoExisteExepcion()
        
        except DestinoVacacionalNoExisteExepcion as dvnee:
            print(dvnee.__str__())
        
        else:
            opcion_valida = True
    
    return destino, precio_total


def seleccion_estrellas():
    
    print("En el paquete vacacional está incluido la estancia en un hotel de 3*")
    estrellas_defecto = 3

    opcion = pregunta_si_no("¿Quiéres aumentar la calidad del hotel")

    if opcion:
        estrellas = estrellas_defecto + 1
        print(f"Las estrellas del hotel han aumentado a {estrellas}")
    else:
        opcion_reducirla = pregunta_si_no("¿Quieres reducirla")
        if opcion:
            estrellas = estrellas_defecto - 1
            print(f"Las estrellas del hotel han disminuido a {estrellas}")
        
    return estrellas