"""
Nombre:         TV por Internet
Archivo:        main.py
Autor:          Alberto Sánchez Barona
Fecha:          17/11/2022
Descripción:
    Desarrollar un programa en Python que calcule y visualice por pantalla la cuota a pagar por un conjunto de usuarios que una plataforma de TV por Internet.
        1.- Introducir de forma repetida los datos de un usuario y los datos de personalización de los productos elegidos hasta que en el nombre del usuario sea una cadena vacía. Por cada usuario hay que introducir:

            a) Nombre → Nombre del usuario que quiere matricularse en cursos de formación.

            b) Login → Nombre de usuario empleado para conectarse a los servicios de la plataforma.

            c) Servicios → Los servicios y sus precios mensuales son:
                • Series → 15€
                • Películas → 20 €
                • Documentales → 5 €

            d) Canales de TV → Además de los servicios anteriores, es posible suscribirse a los canales de TV que elija el usuario. Estos canales están agrupados en temática para facilitar la búsqueda y la suscripción es por todos los canales de un grupo. Tenemos los siguientes:
                • Deportes (incluye Champions, Europa League, La Liga, La Premier), → 25 €
                • Comedy Channels (incluye Todo Monólogos y Comedy Movies) → 10 €
                • Kids (La Fábrica de Chocolate +, Kinder Shows, Toddler TV) → 15 €
                • Películas clásicas (incluye Classics Movies y Golden Hollywood) → 5 €. Este paquete ya va incluido en el servicio Películas.

            e) N.º de conexiones simultáneas → Cuantos dispositivos pueden conectarse simultáneamente para ver los contenidos de la plataforma. Por defecto es una, pero por una segunda se aumenta un 2.5% y por una tercera o siguientes se aumenta un 1%. En ningún caso podrán ser más de 6 por dirección IP.

            f) Porcentaje de descuento → Por cada servicio contratado se concede un 5% de descuento siempre que se contrate más de uno. Por cada grupo de canales de TV hay un descuento de un 5%, si son más de dos (Películas clásicas no se tiene en cuentra si se incluyo en el paquete el servicio de Pelícuas).

        2. Desarrollar un programa que visualiza por pantalla los datos de cada usuario, los servicios elegidos con su precio, el número de temáticas de canales de TV con su precio, el incremento por conexiones simultáneas, el descuento por número de servicios contratados y por temáticas de canal, y el importe total de todo el paquete contratado.
"""

from funciones import NombreEnBlanco, OpcionRepetida
from funciones import pregunta, menu_servicios, opcion_menu_servicios, menu_canales, opcion_menu_canales, conexiones_simultaneas, porcentaje_conexiones_simultaneas, calcular_descuento

def main():
    
    while True:

        try:
            
            # Pedimos el nombre del cliente.
            nombre = input("Introduzca su nombre: ")

            if nombre == "":
                raise NombreEnBlanco
            
            # Pedimos el usuario del cliente.
            usuario = input("Introduzca su nombre de usuario: ")

            # Preguntamos al cliente si se quiere suscribir a algún servicio.
            servicio_valido = False

            precio_total = 0
            contador_servicios = 0
            contador_canales = 0

            while not servicio_valido:
                
                print("")
                menu_servicios()
                print("")

                precio_servicio = 0
                eleccion_servicio_1 = ""
                eleccion_servicio_2 = ""
                eleccion_servicio_3 = ""

                try:

                    respuesta_servicios_1 = pregunta("Estos son los servicios que tenemos disponibles ¿desea contratar alguno?")
                    if respuesta_servicios_1:
                        eleccion_servicio_1, precio_servicio_1 = opcion_menu_servicios()
                        precio_servicio += precio_servicio_1
                        contador_servicios += 1

                        respuesta_servicios_2 = pregunta("¿Desea contratar algún otro servicio")
                        if respuesta_servicios_2:
                            eleccion_servicio_2, precio_servicio_2 = opcion_menu_servicios()

                            if eleccion_servicio_1 == eleccion_servicio_2:
                                raise OpcionRepetida("Has introducido un servicio duplicado. Comenzando de nuevo la elección del servicio...")

                            precio_servicio += precio_servicio_2
                            contador_servicios += 1

                            respuesta_servicios_3 = pregunta("¿Desea contratar algún otro servicio")
                            if respuesta_servicios_3:
                                eleccion_servicio_3, precio_servicio_3 = opcion_menu_servicios()

                                if eleccion_servicio_1 == eleccion_servicio_2 or eleccion_servicio_1 == eleccion_servicio_3 or eleccion_servicio_2 == eleccion_servicio_3:
                                    raise OpcionRepetida("Has introducido un servicio duplicado. Comenzando de nuevo la elección del servicio...")

                                precio_servicio += precio_servicio_3
                                contador_servicios += 1
                                print(f"Ha elegido los servicios: {eleccion_servicio_1}, {eleccion_servicio_2} y {eleccion_servicio_3}.")
                                print(f"El precio total de todos los servicios es de {precio_servicio}€")
                            
                            else:
                                print(f"Ha elegido los servicios: {eleccion_servicio_1} y {eleccion_servicio_2}.")
                                print(f"El precio total de todos los servicios es de {precio_servicio}€")
                        
                        else:
                            print(f"Ha elegido el servicio: {eleccion_servicio_1}")
                            print(f"El precio es de {precio_servicio}€")
                    
                    else:
                        print("No ha elegido ningun servicio, continuando con el programa...")  

                except OpcionRepetida as opre:
                    print(opre.__str__())
                
                else:
                    servicio_valido = True
            # Fin bucle while.

            # Preguntamos al cliente si quiere comprar algún canal de TV extra.
            canal_valido = False

            while not canal_valido:

                print("")
                menu_canales()
                print("")

                precio_canal = 0
                eleccion_canal_1 = ""
                eleccion_canal_2 = ""
                eleccion_canal_3 = ""
                eleccion_canal_4 = ""

                try:

                    respuesta_canales_1 = pregunta("Estos son los canales de TV que tenemos disponibles, ¿desea contratar alguno?")
                    if respuesta_canales_1:
                        eleccion_canal_1, precio_canal_1 = opcion_menu_canales()
                        precio_canal += precio_canal_1
                        contador_canales += 1

                        respuesta_canales_2 = pregunta("¿Desea contratar algún otro canal")
                        if respuesta_canales_2:
                            eleccion_canal_2, precio_canal_2 = opcion_menu_canales()

                            if eleccion_canal_1 == eleccion_canal_2:
                                raise OpcionRepetida("Has introducido un canal duplicado. Comenzando de nuevo la elección del canal...")

                            precio_canal += precio_canal_2
                            contador_canales += 1

                            respuesta_canales_3 = pregunta("¿Desea contratar algún otro canal")
                            if respuesta_canales_3:
                                eleccion_canal_3, precio_canal_3 = opcion_menu_canales()

                                if eleccion_canal_1 == eleccion_canal_2 or eleccion_canal_1 == eleccion_canal_3 or eleccion_canal_2 == eleccion_canal_3:
                                    raise OpcionRepetida("Has introducido un canal duplicado. Comenzando de nuevo la elección del canal...")

                                precio_canal += precio_canal_3
                                contador_canales += 1

                                respuesta_canales_4 = pregunta("¿Desea contratar algún otro canal")
                                if respuesta_canales_4:
                                    eleccion_canal_4, precio_canal_4 = opcion_menu_canales()

                                    if eleccion_canal_1 == eleccion_canal_2 or eleccion_canal_1 == eleccion_canal_3 or eleccion_canal_4 or eleccion_canal_2 == eleccion_canal_3 or eleccion_canal_2 == eleccion_canal_4 or eleccion_canal_3 == eleccion_canal_4:
                                        raise OpcionRepetida("Has introducido un canal duplicado. Comenzando de nuevo la elección del canal...")

                                    precio_canal += precio_canal_4
                                    contador_canales += 1
                                    print(f"Ha elegido los canales: {eleccion_canal_1}, {eleccion_canal_2}, {eleccion_canal_3} y {eleccion_canal_4}")
                                    print(f"El precio total es de {precio_canal}€")
                                
                                else:
                                    print(f"Ha elegido los canales: {eleccion_canal_1}, {eleccion_canal_2} y {eleccion_canal_3}")
                                    print(f"El precio total es de {precio_canal}€")

                            else:
                                print(f"Ha elegido los canales: {eleccion_canal_1} y {eleccion_canal_2}")
                                print(f"El precio total es de {precio_canal}€")

                        else:
                            print(f"Ha elegido el canal: {eleccion_canal_1}")
                            print(f"El precio es de {precio_canal}€")
                        
                    else:
                        print("No ha elegido ningun canal, continuando con el programa...")
                
                except OpcionRepetida as opre:
                    print(opre.__str__())
                
                else:
                    canal_valido = True
            
            # Fin bucle while
            if eleccion_servicio_1 == "Películas" or eleccion_servicio_2 == "Películas" or eleccion_servicio_3 == "Películas" and eleccion_canal_1 == "Películas Clásicas" or eleccion_canal_2 == "Películas Clásicas" or eleccion_canal_3 == "Películas Clásicas" or eleccion_canal_4 == "Películas Clásicas":
                print("El canal Películas Clásicas va incluido en el servicio Películas, al haber comprado los dos, se le descuenta los 5€ del precio del canal.")
                contador_canales -= 1

            precio_sin_incremento = precio_servicio + precio_canal
            print(f"Por ahora el precio que lleva es de {precio_sin_incremento}€")

            # Preguntamos el número de conexiones simultáneas.
            conexiones = conexiones_simultaneas()
            print(f"Ha elegido {conexiones} conexiones simultáneas.")

            # Calculamos el porcentaje por las conexiones simultáneas.
            porcenataje_conexiones = porcentaje_conexiones_simultaneas(conexiones, precio_sin_incremento)
            if conexiones > 1:
                print(f"Ha elegido tener {conexiones} conexiones simultáneas, por lo que el incremento es de {porcenataje_conexiones} €")
            
            incremento = porcenataje_conexiones
            precio_con_incremento = precio_sin_incremento + incremento

            print(f"Por ahora el precio total es de {precio_con_incremento}€")

            # Calculamos el porcentaje de descuento.
            descuento_canal = calcular_descuento(precio_con_incremento, contador_servicios, contador_canales)

            print(f"El precio total con el descuento aplicado es de {descuento_canal}€")

        except KeyboardInterrupt:
            print("Has interrumpido el programa.")
            print("Saliendo...")
            exit(1)
        
        except NombreEnBlanco:
            print("Has introducido el nombre en blanco, vas a salir del programa.")
            print("Saliendo...")
            exit(2)

if __name__ == "__main__":
    main()