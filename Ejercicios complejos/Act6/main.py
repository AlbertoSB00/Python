"""
Proyecto:           Cursos Online
Archivo:            main.py
Autor:              Alberto Sánchez Barona
Fecha:              10/11/2022
Descripción:
    Desarrollar un programa en Python que calcule y visualice por pantalla los cursos de formación online elegidos por los alumnos, junto con el precio de cada uno de ellos y el precio total:

        1.- Introducir de forma repetida los datos de un alumno y los cursos en los que se matricula hasta que en el nombre del alumno sea una cadena vacía. Por cada alumno hay que introducir:
            a) Nombre → Nombre del alumno que quiere matricularse en cursos de formación.

            b) Temática del curso → Los cursos están distribuidos en tres disciplinas: INFormática, ADMinistración de Empresas y DISeño gráfico.
                • En Informática tenemos los cursos de Ofimática (100€), Programación (200€) y Reparación de ordenadores (150€)
                • En Administración de Empresas tenemos los cursos de Contabilidad y Finanzas (300€), Recursos Humanos (250€) y Leyes Tributarias de Empresas (150€)
                • En Diseño gráfico tenemos los cursos de Retoque fotográfico (200€) y Creación de Logotipos Corporativos (250€)

            c) Porcentaje de incremento por clases presenciales → Existe la posibilidad de hacer alguna clase presencial por lo que se paga un incremento. Si son una el incremento es del 5%, si son dos el incremento es un 7,5% y si son 3 se incrementará un 10%. Las clases presenciales podrán ser de cualquier curso.

            d) Descuento → Se podrá hacer un descuento si se eligen más de un curso independientemente de la temática del curso. Por dos cursos el descuento es de un 10%, si se eligen tres cursos es un 15% y eligiendo cuatro o más cursos se tendrá un descuento del 20%.
        
         2.- Desarrollar un programa que visualiza por pantalla los datos de cada alumno, los cursos elegidos con su precio, el incremento por clases presenciales, el descuento por número de cursos y el importe total de todos los cursos.
"""

# Importamos el archivo de las funciones.
import funciones as f
precio_cursos = 0
contador_cursos = 0

# Pedimos nombres hasta que se introduzca una cadena vacía.
while True:

    try:

        nombre = input("Introduzca su nombre: ")
        
        if nombre == "":
            print("Has introducio una cadena vacía.")
            print("Saliendo del programa...")
            exit(1)

        # Mostramos la función del menú.
        menu = f.menu()
        print(menu)

        # Damos a elegir al cliente.
        eleccion_menu = f.eleccion_menu()
        print(f"Estos cursos son los que has elegido: {eleccion_menu}")

        # Convertimos y calculamos la variable cursos.
        if "OFI" in eleccion_menu:
            precio_cursos += 100
            contador_cursos += 1
        if "PRO" in eleccion_menu:
            precio_cursos += 200
            contador_cursos += 1
        if "REP" in eleccion_menu:
            precio_cursos += 150
            contador_cursos += 1
        if "CON" in eleccion_menu:
            precio_cursos += 300
            contador_cursos += 1
        if "REC" in eleccion_menu:
            precio_cursos += 300
            contador_cursos += 1
        if "LEY" in eleccion_menu:
            precio_cursos += 150
            contador_cursos += 1
        if "FOT" in eleccion_menu:
            precio_cursos += 200
            contador_cursos += 1
        if "CRE" in eleccion_menu:
            precio_cursos += 250
            contador_cursos += 1
        
        print(f"Has elegido {contador_cursos} cursos, el precio total es de {precio_cursos}€")

        incremento = f.clases_presenciales()

        print(f"El incremento de las clases presenciales es de {incremento}%")
        calculo_incremento = incremento * precio_cursos / 100
        precio_cursos += calculo_incremento

        print(f"El precio total es de {precio_cursos}€")

        if contador_cursos == 2:
            print("Se va a aplicar un descueto del 10%")
            descuento = 10
            calculo_descuento = descuento * precio_cursos / 100
            precio_total = precio_cursos - calculo_descuento
            print(f"El precio total aplicando el descuento es de {precio_total}€")

        elif contador_cursos == 3:
            print("Se va a aplicar un descueto del 15%")
            descuento = 15
            calculo_descuento = descuento * precio_cursos / 100
            precio_total = precio_cursos - calculo_descuento
            print(f"El precio total aplicando el descuento es de {precio_total}€")

        elif contador_cursos >= 4:
            print("Se va a aplicar un descueto del 20%")
            descuento = 20
            calculo_descuento = descuento * precio_cursos / 100
            precio_total = precio_cursos - calculo_descuento
            print(f"El precio total aplicando el descuento es de {precio_total}€")

        else:
            print("Ha escodigo 1 curso o menos, no se va a aplicar descuento.")
    
    except KeyboardInterrupt:
        print("Has solicitado salir del programa.")
        print("Finalizando el programa...")
        exit(2)