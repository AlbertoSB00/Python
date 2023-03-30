"""
Programa:           main.py
Autor:              Alberto Sánchez Barona
Fecha:              07/11/2022
Descripción:        Este es el fichero principal.
"""

# Importamos el fichero funciones.py
import funciones as f

preciototal = 0

# Con este bucle while hacemos que el cliente introduzca datos hasta que el nombre sea cadena vacía.
while True:
    
    # Pedimos el nombre.
    print("----------------------------------------------------------------------------")
    nombre = input("Introduzca su nombre: ")
    print("----------------------------------------------------------------------------")
    if nombre == "":
        break
    
    # Pedimos la direccion.
    direccion = input("Introduzca su dirección de envío completa: ")
    print("----------------------------------------------------------------------------")

    # Pedimos el dinero máximo que el cliente se quiere gastar.
    dinero_max = int(input("Introduzca el presupuesto que tiene pensado para el equipo: "))
    print("----------------------------------------------------------------------------")

    # Guardamos el valor de la función f.eleccion_procesador().
    placabase = f.eleccion_placabase()

    if placabase == "Z790":
        preciototal += 400
    elif placabase == "H610M":
        preciototal += 350
    elif placabase == "B660M":
        preciototal += 325
    elif placabase == "H81M":
        preciototal += 300
    
    if preciototal > dinero_max:
        print(f"Su presupuesto era de {dinero_max}€ y se ha pasado. Total = {preciototal}€")
        print("Saliendo del programa...")
        print("----------------------------------------------------------------------------")
        exit(3)
    else:
        print(f"Por ahora lleva {preciototal}€ gastados, su presupuesto es de {dinero_max}€")
        print("----------------------------------------------------------------------------")

    # Procesador.
    procesador = f.eleccion_procesador(placabase)

    if procesador == "z9":
        preciototal += 700
    elif procesador == "z7":
        preciototal += 450
    elif procesador == "z5":
        preciototal += 250
    elif procesador == "g9":
        preciototal += 670
    elif procesador == "g7":
        preciototal += 420
    elif procesador == "g5":
        preciototal += 275

    if preciototal > dinero_max:
        print(f"Su presupuesto era de {dinero_max}€ y se ha pasado. Total = {preciototal}€")
        print("Saliendo del programa...")
        print("----------------------------------------------------------------------------")
        exit(3)
    else:
        print(f"Por ahora lleva {preciototal}€ gastados, su presupuesto es de {dinero_max}€")
        print("----------------------------------------------------------------------------")
        

    # Se pregunta el tamaño total de memoria que desea el cliente.
    memoria4, memoria8, memoria16 = f.eleccion_memoria()
    print(f"El equipo tiene {memoria16} módulos de 16 GB, {memoria8} módulos de 8 GB y {memoria4} módulos de 4 GB de memoria RAM.")

    preciototal += memoria4 * 40
    preciototal += memoria8 * 60
    preciototal += memoria16 * 100

    if preciototal > dinero_max:
        print(f"Su presupuesto era de {dinero_max}€ y se ha pasado. Total = {preciototal}€")
        print("Saliendo del programa...")
        print("----------------------------------------------------------------------------")
        exit(3)
    else:
        print(f"Por ahora lleva {preciototal}€ gastados, su presupuesto es de {dinero_max}€")
        print("----------------------------------------------------------------------------")
    
    # Se pregunta que disco duro quiere.
    discoduro = f.eleccion_discoduro()
    if discoduro == 1:
        print("Ha elegido el disco duro SSD SATA3 de 1 TB")
        preciototal += 100
    else:
        print("Ha elegido el disco duro SSD NVMe de 512 GB")
        preciototal += 150

    if preciototal > dinero_max:
        print(f"Su presupuesto era de {dinero_max}€ y se ha pasado. Total = {preciototal}€")
        print("Saliendo del programa...")
        print("----------------------------------------------------------------------------")
        exit(3)
    else:
        print(f"Por ahora lleva {preciototal}€ gastados, su presupuesto es de {dinero_max}€")
        print("----------------------------------------------------------------------------")

    # Se pregunta la caja y cableado.
    caja = f.eleccion_caja()
    if caja == 1:
        print("Ha elegido caja con fuente de alimentación de 450w.")
        preciototal += 45
    elif caja == 2:
        print("Ha elegido caja con fuente de alimentación de 500w.")
        preciototal += 55
    else:
        print("Ha elegido caja con fuente de alimentación de 600w.")
        preciototal += 60

    if preciototal > dinero_max:
        print(f"Su presupuesto era de {dinero_max}€ y se ha pasado. Total = {preciototal}€")
        print("Saliendo del programa...")
        print("----------------------------------------------------------------------------")
        exit(3)
    else:
        print(f"Por ahora lleva {preciototal}€ gastados, su presupuesto es de {dinero_max}€")
        print("----------------------------------------------------------------------------")

    # Calculamos el porcentaje de incremento por envío.
    print("Se va a calcular el porcentaje de incremento por envío.")
    print("1.- España.")
    print("2.- Islas Canarias o Baleares.")
    print("3.- Otro pais de la UE.")
    envio = int(input("Indique con 1, 2 o 3: "))
    match envio:
        case 1:
            print("Ha elegido España, el incremento es de 0.5 por ciento del total.")
            preciototal += preciototal * 0.05
        case 2:
            print("Ha elegido Islas Canarias o Baleares, el incremento es de 0.75 por ciento del total.")
            preciototal += preciototal * 0.075
        case 3:
            print("Ha elegido otro pais de la UE, el incremento es de 1 por ciento del total.")
            preciototal += preciototal * 0.1
        case _:
            print("No contemplamos envíos fuera de la UE.")
            print("Saliendo del programa...")
            exit(4)
    
    if preciototal > dinero_max:
        print(f"Su presupuesto era de {dinero_max}€ y se ha pasado. Total = {preciototal}€")
        print("Saliendo del programa...")
        print("----------------------------------------------------------------------------")
        exit(3)
    else:
        print(f"Por ahora lleva {preciototal}€ gastados, su presupuesto es de {dinero_max}€")
        print("----------------------------------------------------------------------------")

    # Aplicamos el descuento.
    print("Se le va a aplicar un descuento dependiendo de su precio total.")
    if preciototal < 1000:
        print("En este caso se le va a aplicar un 5 por ciento de descuento.")
        descuento = (5 * preciototal) / 100
        preciofinal = preciototal - descuento
    elif preciototal >= 1000 and preciototal < 1250:
        print("En este caso se le va a aplicar un 10 por ciento de descuento.")
        descuento = (10 * preciototal) / 100
        preciofinal = preciototal - descuento
    elif preciototal > 1250:
        print("En este caso se le va a aplicar un 15 por ciento de descuento.")
        descuento = (15 * preciototal) / 100
        preciofinal = preciototal - descuento
    
    print(f"El montaje ya está terminado, el precio total del equipo es de {preciofinal}€, tenía un presupuesto de {dinero_max} y le ha sobrado {dinero_max - preciofinal}€")
    preciototal = 0
    preciofinal = 0