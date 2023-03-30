"""
Proyecto:           Examen
Archivo:            main.py
Nombre:             Alberto Sánchez Barona
Fecha:              28/11/2022
"""

# Importamos las excepciones.
from funciones import PinIncorrectoExcepcion
# Importamos las funciones.
from funciones import seleccionar_categoria, seleccionar_salio_base, seleccionar_horas_extras, seleccionar_antiguedad, calcular_importe_horas_extras, calcular_sexenio_trienio, \
    importe_sexenio_trienio, calcular_porcentaje_reduccion


# 1) Comienza el programa principal.
def main():
    # Variable global con el PIN.
    PIN = 1234

    # Números de intentos.
    intentos = 3
    intento_actual = 1

    # Mientras el nñumero de intentos actual sea menor o igual al de intentos permitidos...
    while intento_actual <= intentos:
        try:

            pin_usuario = int(input(f"Introduzca el número PIN({intento_actual}/{intentos}): "))

            if pin_usuario == PIN:

                # Una vez autenticado, comienza el programa.
                while True:

                    # 2a) Nombre.
                    nombre = input("Introduzca su nombre: ")
                    if nombre == "":
                        exit(2)
                    # 2b) Categoría personal.
                    categoria = seleccionar_categoria()

                    # 2c) Salario base.
                    salario_base = seleccionar_salio_base(categoria)
                    print(f"Su salario es de {salario_base}€")

                    # 2d) Horas extra.
                    horas_extras = seleccionar_horas_extras()
                    print(f"Este mes ha trabajado {horas_extras} horas extras.")

                    # 2e) Antigüedad.
                    antiguedad = seleccionar_antiguedad()
                    print(f"Tiene {antiguedad} años de antigüedad.")

                    # 3a) Calcular importe horas extras.
                    importe_horas_extras = int(calcular_importe_horas_extras(categoria, horas_extras, salario_base))
                    print(f"El importe de las horas extras es de {importe_horas_extras}€")

                    # 3b) Calcular sexenios y trienios.
                    sexenio, trienio = calcular_sexenio_trienio(antiguedad)
                    print(f"LLeva en la empresa {sexenio} sexenios y {trienio} trienios.")

                    # 3b2) Calcular importe antigüedad.
                    importe_antiguedad = importe_sexenio_trienio(categoria, sexenio, trienio)
                    print(f"El importe de antigüedad es de {importe_antiguedad}€")

                    # 3c) Sueldo bruto.
                    sueldo_bruto = salario_base + (horas_extras * importe_horas_extras) + importe_antiguedad
                    print(f"Tu sueldo bruto es de {sueldo_bruto}€")

                    # 3d) Porcentaje de reducción.
                    reduccion_irpf, reduccion_ss = calcular_porcentaje_reduccion(sueldo_bruto)
                    print(f"La reducción de IRPF es de {reduccion_irpf}€ y la reducción de SS es de {reduccion_ss}€")

                    # 3e) Sueldo neto.
                    sueldo_neto = sueldo_bruto - reduccion_irpf - reduccion_ss
                    print(f"Tu sueldo neto es de {sueldo_neto}€")

            else:
                raise PinIncorrectoExcepcion("El PIN no es correcto.")

        except PinIncorrectoExcepcion as pie:
            print(pie.__str__())
            intento_actual += 1
            print("Inténtelo de nuevo...")

        except ValueError:
            print("Compruebe lo que ha escrito e inténtelo de nuevo...")
            intento_actual += 1

        except KeyboardInterrupt:
            print("El usuario ha solicitado salir del programa...")
            exit(3)

    if intento_actual > intentos:
        print("Has superado el número máximo de intentos. Saliendo del programa...")
        exit(1)


if __name__ == "__main__":
    main()