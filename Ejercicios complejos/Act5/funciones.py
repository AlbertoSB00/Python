def eleccion_placabase() -> str:

    # Mostramos al cliente las placas base que hay.
    print("Estos son las placas base disponibles:")
    print("Z790")
    print("H610M")
    print("B660M")
    print("H81M")

    # Le damos a elegir.
    opcion = input("Escriba el nombre completo de la placa base y en mayúsculas: ")

    # Con match, encasillamos su opción.
    match opcion:
        case "Z790":
            print("Ha elegido la placa base Z790")
        case "H610M":
            print("Ha elegido la placa base H610M")
        case "B660M":
            print("Ha elegido la placa base B660M")
        case "H81M":
            print("Ha elegido la placa base H81M")
        case _:
            print(f"ERROR -> Ese placa base no existe.")
            print("Saliendo del programa...")
            exit(1)
    
    # Devolvemos la opción.
    return opcion


def eleccion_procesador(placabase: str) -> str:

    # Damos a elegir entre zorin o goldfinger.
    marca = input("Indique si el procesador es zorin o goldfinger: ")

    if marca == "zorin" or marca == "goldfinger":
        
        # Si la marca es zorin...
        if marca == "zorin":
            print("Ha elegido la marca zorin.")
            print("z9")
            print("z7")
            print("z5")

            # Va a seleccionar procesadores hasta que uno sea válido.
            procesador_valido = False
            while not procesador_valido:
                procesador = input("Seleccione uno de sus productos: ")
                match procesador:
                    case "z9":
                        if placabase == "Z790":
                            print(f"Por ahora tenemos la placa base {placabase} con el procesador {procesador}")
                            procesador_valido = True
                        else:
                            print(f"El precesador {procesador} no es compatible con la placa base {placabase}")
                            print("Inténtelo de nuevo...")
                    case "z7":
                        if placabase != "Z790" or placabase != "H81M":
                            print(f"Por ahora tenemos la placa base {placabase} con el procesador {procesador}")
                            procesador_valido = True
                        else:
                            print(f"El precesador {procesador} no es compatible con la placa base {placabase}")
                            print("Inténtelo de nuevo...")
                    case "z5":
                        if placabase != "Z790" or placabase != "H81M":
                            print(f"Por ahora tenemos la placa base {placabase} con el procesador {procesador}")
                            procesador_valido = True
                        else:
                            print(f"El precesador {procesador} no es compatible con la placa base {placabase}")
                            print("Inténtelo de nuevo...")

        # Si la marca es goldfinger...
        elif marca == "goldfinger":
            print("Ha elegido la marca goldfinger.")
            print("g9")
            print("g7")
            print("g5")

            # Va a seleccionar procesadores hasta que uno sea válido.
            procesador_valido = False
            while not procesador_valido:
                procesador = input("Seleccione uno de sus productos: ")
                match procesador:
                    case "g9":
                        if placabase != "H81M" or placabase != "H81M":
                            print(f"Por ahora tenemos la placa base {placabase} con el procesador {procesador}")
                            procesador_valido = True
                        else:
                            print(f"El precesador {procesador} no es compatible con la placa base {placabase}")
                            print("Inténtelo de nuevo...")
                    case "g7":
                        if placabase != "H81M" or placabase != "H81M":
                            print(f"Por ahora tenemos la placa base {placabase} con el procesador {procesador}")
                            procesador_valido = True
                        else:
                            print(f"El precesador {procesador} no es compatible con la placa base {placabase}")
                            print("Inténtelo de nuevo...")
                    case "g5":
                        if placabase == "H81M":
                            print(f"Por ahora tenemos la placa base {placabase} con el procesador {procesador}")
                            procesador_valido = True
                        else:
                            print(f"El precesador {procesador} no es compatible con la placa base {placabase}")
                            print("Inténtelo de nuevo...")
    
        return procesador

    else:
        print(f"ERROR -> El procesador {marca} no existe.")
        print("Saliendo del programa...")
        exit(2)


def eleccion_memoria():
    
    memoria_valida = False
    while not memoria_valida:
        memoria_max = int(input("Introduzca el número máximo de memoria que necesita para el equipo: "))
        if memoria_max % 4 == 0 and memoria_max >= 4 and memoria_max <= 64:
            
            contador_4ram = 0
            contador_8ram = 0
            contador_16ram = 0

            if memoria_max == 4:
                contador_4ram += 1
            elif memoria_max == 8:
                contador_8ram += 1
            elif memoria_max == 12:
                contador_4ram += 1
                contador_8ram += 1
            elif memoria_max == 16:
                contador_16ram += 1
            elif memoria_max == 20:
                contador_16ram += 1
                contador_4ram += 1
            elif memoria_max == 24:
                contador_16ram += 1
                contador_8ram += 1
            elif memoria_max == 28:
                contador_16ram += 1
                contador_8ram += 1
                contador_4ram += 1
            elif memoria_max == 32:
                contador_16ram += 2
            elif memoria_max == 36:
                contador_16ram += 2
                contador_4ram += 1
            elif memoria_max == 40:
                contador_16ram += 2
                contador_8ram += 1
            elif memoria_max == 44:
                contador_16ram += 2
                contador_8ram += 2
                contador_4ram += 1
            elif memoria_max == 48:
                contador_16ram += 3
            elif memoria_max == 52:
                contador_16ram += 3
                contador_4ram += 1
            elif memoria_max == 56:
                contador_16ram += 3
                contador_8ram += 1
            elif memoria_max == 60:
                contador_16ram += 3
                contador_8ram += 1
                contador_4ram += 1
            elif memoria_max == 64:
                contador_16ram += 4

            memoria_valida = True
        else:
            print("La memoria RAM debe ser un múltiplo de 4. Por ejemplo: 4, 8, 12, 16... hasta 64.")
            print("Inténtelo de nuevo...")
    
    return contador_4ram, contador_8ram, contador_16ram


def eleccion_discoduro():

    print("Tenemos estos dos discos duros diponibles.")
    print("1.- SSD SATA3 de 1 TB.")
    print("2.- SSD NVMe de 512 GB")
    opcion_discoduro = int(input("Seleccione una opción con 1 o 2: "))
    match opcion_discoduro:
        case 1:
            discoduro = 1
        case 2:
            discoduro = 2
    
    return discoduro


def eleccion_caja():

    print("Tenemos estas cajas diponibles, cada una con una fuente de alimentación diferente.")
    print("1.- Caja con fuente de 450w")
    print("2.- Caja con fuente de 500w")
    print("3.- Caja con fuente de 600w")
    opcion_caja = int(input("Introduzca 1, 2 o 3 para elegir: "))
    match opcion_caja:
        case 1:
            caja = 1
        case 2:
            caja = 2
        case 3:
            caja = 3

    return caja