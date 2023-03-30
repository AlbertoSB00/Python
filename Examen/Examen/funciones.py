"""
Proyecto:           Examen
Archivo:            funciones.py
Nombre:             Alberto Sánchez Barona
Fecha:              28/11/2022
"""


# Comienzan las excepciones.
class PinIncorrectoExcepcion(Exception):
    """
    Clase:      PinIncorrectoExcepcion
    Raise:      Cuando el PIN que ha introducido el usuario es incorrecto.
    """
    pass


class ErrorEleccionCategoriaExcepcion(Exception):
    """
    Clase:      ErrorEleccionCategoriaExcepcion
    Raise:      Cuando el usuario se equivoca al introducir una categoria.
    """
    pass


class SalarioMinimoMaximoIncorrectoExcepcion(Exception):
    """
    Clase:      SalarioMinimoMaximoIncorrectoExcepcion
    Raise:      Cuando el usuario excede por abajo o por arriba el salario.
    """
    pass


class NumeroHorasExtrasExcedeMaximoExcepcion(Exception):
    """
    Clase:      NumeroHorasExtrasExcedeMaximoExcepcion
    Raise:      Cuando el número de horas extra supera al número máximo de horas extras.
    """
    pass


class NumeroHorasNoValidoExcepcion(Exception):
    """
    Clase:      NumeroHorasNoValidoExcepcion
    Raise:      Cuando el número de horas es negativo.
    """
    pass


class NumeroAnosAntiguedadNoValidoExcepcion(Exception):
    """
    Clase:      NumeroAnosAntiguedadNoValidoExcepcion
    Raise:      Cuando el número de años de antigüeadd es negativo.
    """
    pass


class ImporteMaximoSalarioBaseExcepcion(Exception):
    """
    Clase:      ImporteMaximoSalarioBaseExcepcion
    Raise:      Cuando el importe es mayor al máximo permitido.
    """
    pass


# Comienzan las funciones
def seleccionar_categoria() -> str:
    """
    Función:        seleccionar_categoria()
    Descripción:    Imprime por  pantalla las categorias disponibles y el usuario selecciona una.
    Parámetros:     Ninguno.
    Return:         String con la categoria.
    """

    opcion_valida = False

    while not opcion_valida:

        try:
            print("   Categorias    ")
            print("[DIR].....Directivo")
            print("[MI]......Mando Intermedio")
            print("[EMP].....Empleado")

            opcion = input("Seleccione la categoria: ")
            opcion = opcion.upper()

            match opcion:

                case "DIR":
                    print("Ha elegido la categoria Directivo.")

                case "MI":
                    print("Ha elegido la categoria Mando Intermedio.")

                case "EMP":
                    print("Ha elegido la categoria Empleado.")

                case _:
                    raise ErrorEleccionCategoriaExcepcion(f"La categoria {opcion} no es válida.")

        except ErrorEleccionCategoriaExcepcion as eece:
            print(eece.__str__())
            print("Inténtelo de nuevo...")

        else:
            opcion_valida = True

    return opcion
# Fin funcion seleccionar_categoria()


def seleccionar_salio_base(categoria: str) -> int:
    """
    Función:            seleccionar_salio_base()
    Descripción:        Dependiendo de la categoria le preguntamos al usuario su salario.
    Parámetros:
        categoria:      La categoria elegida anteriormente.
    Return:             El salario base.
    """

    salario_valido = False

    while not salario_valido:

        try:
            match categoria:

                case "DIR":
                    salario_minimo = 3000
                    salario_maximo = 4000
                    salario_base = int(input(f"Introduzca su salario, recuerda que está entre {salario_minimo}€ y {salario_maximo}€: "))
                    if salario_base < salario_minimo or salario_base > salario_maximo:
                        raise SalarioMinimoMaximoIncorrectoExcepcion(f"Compruebe el salario que ha introducido, no puede ser inferior a {salario_minimo}€ ni superior a {salario_maximo}€")
                case "MI":
                    salario_minimo = 2000
                    salario_maximo = 3000
                    salario_base = int(input(f"Introduzca su salario, recuerda que está entre {salario_minimo}€ y {salario_maximo}€: "))
                    if salario_base < salario_minimo or salario_base > salario_maximo:
                        raise SalarioMinimoMaximoIncorrectoExcepcion(f"Compruebe el salario que ha introducido, no puede ser inferior a {salario_minimo}€ ni superior a {salario_maximo}€")
                case "EMP":
                    salario_minimo = 1000
                    salario_maximo = 2000
                    salario_base = int(input(f"Introduzca su salario, recuerda que está entre {salario_minimo}€ y {salario_maximo}€: "))
                    if salario_base < salario_minimo or salario_base > salario_maximo:
                        raise SalarioMinimoMaximoIncorrectoExcepcion(f"Compruebe el salario que ha introducido, no puede ser inferior a {salario_minimo}€ ni superior a {salario_maximo}€")

        except SalarioMinimoMaximoIncorrectoExcepcion as smmie:
            print(smmie.__str__())
            print("Inténtelo de nuevo...")

        except ValueError:
            print("Compruebe lo que ha escrito he inténtelo de nuevo...")

        else:
            salario_valido = True

    return salario_base
# Fin función seleccionar_salio_base()


def seleccionar_horas_extras() -> float:
    """
    Función:            seleccionar_horas_extras
    Descripción:        Pregunta al usuario el número de horas extras de este mes.
    Parámetros:         Ninguno.
    Return:             Número de horas extras.
    """
    horas_validas = False
    while not horas_validas:
        try:
            horas_extras = float(input("Introduzca el número de horas extras de este mes: "))
            if horas_extras < 0:
                raise NumeroHorasNoValidoExcepcion("No puede introducir un número de horas negativo.")
            horas_extras /= 4
            horas_maximas = 40
            porcentaje_horas = horas_extras * 0.4
            horas_extras_totales = horas_extras + porcentaje_horas
            if horas_extras_totales > horas_maximas:
                raise NumeroHorasExtrasExcedeMaximoExcepcion(f"No pueden ser más de un 40% de la jornada laboral semanal de 40 horas. Ha introducido {horas_extras_totales} horas.")

        except NumeroHorasExtrasExcedeMaximoExcepcion as nheeme:
            print(nheeme.__str__())
            print("Inténtelo de nuevo...")

        except NumeroHorasNoValidoExcepcion as nhnve:
            print(nhnve.__str__())
            print("Inténtelo de nuevo...")

        except ValueError:
            print("Compruebe lo que ha escrito he inténtelo de nuevo...")

        else:
            horas_validas = True

    return horas_extras_totales
# Fin función seleccionar_horas_extras()


def seleccionar_antiguedad() -> int:
    """
    Función:            seleccionar_antiguedad()
    Descripción:        Pregunta al usuario el número de años de antigüedad.
    Parámetros:         Ninguno.
    Return:             Número de años de antigüedad.
    :return:
    """
    antiguedad_valida = False

    while not antiguedad_valida:
        try:
            antiguedad = int(input("Introduzca el número de años de antigüedad: "))
            if antiguedad < 0:
                raise NumeroAnosAntiguedadNoValidoExcepcion("El número de años no puede ser negativo.")

        except NumeroAnosAntiguedadNoValidoExcepcion as naanve:
            print(naanve.__str__())
            print("Inténtelo de nuevo...")

        except ValueError:
            print("Compruebe lo que ha escrito he inténtelo de nuevo...")

        else:
            antiguedad_valida = True

    return antiguedad
# Fin función seleccionar_antiguedad()


def calcular_importe_horas_extras(categoria: str, horas_extras_totales: float, salario_base: int) -> float:
    """
    Función:                    calcular_importe_horas_extras()
    Descripción:                Calcula el importe total de las horas extras.
    Parámetros:
        categoria:              La categoria del usuario.
        horas_extras_totales:   Número de horas extras totales.
        salario_base:           El salario base del usuario.
    Return:                     Devuelve el cálculo completo de las horas extras.
    """

    try:
        match categoria:

            case "DIR":
                hora_extra = 40
                maximo_importe_salario_base = 0.25 * salario_base
                importe_horas_extras = horas_extras_totales * hora_extra
                if importe_horas_extras > maximo_importe_salario_base:
                    importe_horas_extras = maximo_importe_salario_base
                    raise ImporteMaximoSalarioBaseExcepcion(f"Se ha superado el importe máximo de horas extras del salario base. El importe actual es {importe_horas_extras}€.")

            case "MI":
                hora_extra = 30
                maximo_importe_salario_base = 0.25 * salario_base
                importe_horas_extras = horas_extras_totales * hora_extra
                if importe_horas_extras > maximo_importe_salario_base:
                    importe_horas_extras = maximo_importe_salario_base
                    raise ImporteMaximoSalarioBaseExcepcion(f"Se ha superado el importe máximo de horas extras del salario base. El importe actual es {importe_horas_extras}€.")

            case "EMP":
                hora_extra = 20
                maximo_importe_salario_base = 0.25 * salario_base
                importe_horas_extras = horas_extras_totales * hora_extra
                if importe_horas_extras > maximo_importe_salario_base:
                    importe_horas_extras = maximo_importe_salario_base
                    raise ImporteMaximoSalarioBaseExcepcion(f"Se ha superado el importe máximo de horas extras del salario base. El importe actual es {importe_horas_extras}€.")

    except ImporteMaximoSalarioBaseExcepcion as imsbe:
        print(imsbe.__str__())

    finally:
        return importe_horas_extras
# Fin función calcular_importe_horas_extras()


def calcular_sexenio_trienio(antiguedad: int) -> (int, int):
    """
    Función:            calcular_sexenio_trienio()
    Descripción:        Calcula los sexenios y trienios.
    Parámetros:
        antiguedad:     El número de años que lleva en la empresa.
    Return:             El número de sexenios y trienios.
    """

    sexenio = 0
    trienio = 0
    for i in range(1, antiguedad):
        if i % 6 == 0:
            sexenio += 1
            if sexenio >= 6:
                break
        if i % 3 == 0:
            trienio += 1
            if trienio >= 12:
                break

    return sexenio, trienio
# Fin función calcular_sexenio_trienio()


def importe_sexenio_trienio(categoria: str, sexenio: int, trienio: int) -> float:
    """
    Función:            importe_sexenio_trienio()
    Descripción:        Calcula el importe total de antigüedad.
    Parámetros:
        categoria:      Categoría del usuario.
        sexenio:        Número de sexenios.
        trienio:        Número de trienios.
    Return:             Devuelve el importe total de antigüedad.
    """
    match categoria:

        case "DIR":
            coste_sexenio = 100
            coste_trienio = 50
            importe_total = (coste_sexenio * sexenio) + (coste_trienio * trienio)
        case "MI":
            coste_sexenio = 90
            coste_trienio = 40
            importe_total = (coste_sexenio * sexenio) + (coste_trienio * trienio)
        case "EMP":
            coste_sexenio = 70
            coste_trienio = 30
            importe_total = (coste_sexenio * sexenio) + (coste_trienio * trienio)

    return importe_total
# Fin función importe_sexenio_trienio()


def calcular_porcentaje_reduccion(sueldo_bruto: float) -> (float, float):
    """
    Función:            calcular_porcentaje_reduccion()
    Descripción:        Calcula la reduccion de IRPF y SS
    Parámetros:
        sueldo_bruto:   Sueldo bruto.
    Return:             Devuelve la reduccion de IRPF y SS.
    """
    if sueldo_bruto < 3000:
        irpf = 0.2
        ss = 0.1
        reduccion_irpf = sueldo_bruto * irpf
        reduccion_ss = sueldo_bruto * ss

    if sueldo_bruto > 3000 and sueldo_bruto < 6000:
        irpf = 0.25
        ss = 0.15
        reduccion_irpf = sueldo_bruto * irpf
        reduccion_ss = sueldo_bruto * ss

    if sueldo_bruto > 6000:
        irpf = 0.3
        ss = 0.2
        reduccion_irpf = sueldo_bruto * irpf
        reduccion_ss = sueldo_bruto * ss

    return reduccion_irpf, reduccion_ss
# Fin función calcular_porcentaje_reduccion()