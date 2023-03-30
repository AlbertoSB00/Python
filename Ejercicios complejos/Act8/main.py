"""
Programa:       Paquete vacacional
Archivo:        main.py
Autor:          Alberto Sánchez Barona
Fecha:          25/11/2022
Descripción:


    Desarrollar un programa en Python que calcule y visualice por pantalla el coste de un paquete de vacaciones familiar a pagar por una familia.

        1.- Introducir de forma repetida los datos del paquete de vacaciones hasta que el nombre de introducido sea la cadena vacía. Por cada paquete vacacional hay que introducir:
            a) Nombre → Nombre de la persona que hace el presupuesto de las vacaciones.

            b) Fecha de inicio y fecha de fin → El periodo de tiempo de las vacaciones. De aquí se pueden extraer los días que componen las vacaciones.

            c) N.º de adultos → Número de personas adultas para las que hay que reservar.

            d) N.º de niños → Número de niños que se incluyen. La edad limite es de 15 años inclusive.

            e) N.º de niños menores de 5 años → Cuantos niños de los anteriores son menores de 5 años. Su límite será el dato anterior y el dato mínimo es 0.

            f) Límite de gasto → Cantidad de dinero máximo que la familia está dispuesta a pagar por el paquete vacacional. Hay que tener en cuenta que esta cantidad es orientativa a la hora de elegir destino y que se admite una oferta que se encuentra en una horquilla de un ±20%.

            g) Destino → El programa ofrece un destino vacacional en función de los días de vacaciones, los adultos incluidos y los niños mayores de 5 años, ya que los menores de 5 años van gratis con un tope de 2. Los posibles destinos son:
                • Imperio Austro - Hungaro → 12 días con estancias en Praga, Viena y Budapest. Se visitan los lugares más emblemáticos de la época imperial. El coste es de 120 € por adulto/dia y 50 € por niño mayor de 5 años/dia.
                
                • Fiordos noruegos → Crucero de 8 días con salida en Kristiansand y navegación por la costa noruega haciendo escala en Oslo, Bergen y Trodhein. El coste es de 150 € por adulto/dia y 55 € por niño mayor de 5 años/dia.
                
                • Repúblicas bálticas → 15 días de con estancias en Tallin, Riga y Vilnius. El coste es de 80 € por adulto/dia y 35 € por niño mayor de 5 años/dia.

            h) Hotel de estancia → En el paquete está incluido la estancia en un hotel de 3*. Si se quiere de 4* hay un incremento de un 20%. Si se quiere un hotel de 2* hay un descuento de un 10%. Solo se tiene en cuenta en los paquetes que incluyen estancia en el hotel.

            i) Camarote de barco → Para el paquete del crucero se incluye la estancia en un camarote de 3 anclas. Si se quire uno de 4 anclas hay un incremento del 15% y si se elige uno de 2 anclas hay un descuento del 10%. 

            j) Desayuno en hotel → Si se quiere incluir un desayuno buffet en el hotel se incrementará en un 10%. El crucero tiene incluido el desayuno.

            k) Excursiones → Según el paquete vacacional elegido hay posibilidad de ir a excursiones. Estas son:
                • Visitas guiada al castillo de Karlstein en Praga → Incremento de 35 € por persona y 20€ por niño mayor de 5 años ya que incluye el billete de entrada al castillo
                
                • Visita guiada a Oslo → Incremento de 15 € por persona y 10€ por niño mayor de 5 años.
                
                • Visita guiada a Tallin → Incremento de 10 € por persona y 5€ por niño mayor de 5 años.
            
            l) Si se quiere traslado al aeropuerto se aumenta el precio un 3%.

            m) Descuentos por arreglos de habitación/camarote → El paquete incluye que el servicio de habitaciones arregla la habitación/camarote cada día. Si se hace cada 2 días hay un descuento del 5% y si se hace cada 3 días hay un descuento del 10%.

            n) Coche de alquiler → Si se quiere coche de alquiler hay un incremento del precio. Se ofrecerán tres tipos de coche:
                • Segmento pequeño (VW Polo, Renault Clio, Seat Ibiza o similar) → El precio por día es de 45 €.
                
                • Segmento medio (VW Golf, Renault Megane, Opel Astra o similar) → El precio por día es de 65€.
                
                • Segmento grande o SUV (Renault Fluence, Opel Insignia, Nissan Qashqai o similar) → El precio por día es de 85€
                
                • Hay un descuento de un 10% si el coche se alquila por más de 10 días.

        2.- Desarrollar un programa que visualiza por pantalla los datos de cada usuario, los servicios elegidos con su precio, el número de temáticas de canales de TV con su precio, el incremento por conexiones simultáneas, el descuento por número de servicios contratados y por temáticas de canal, y el importe total de todo el paquete contratado. 
"""

from funciones import leer_numero, ninos_menores_5, destino, seleccion_estrellas

PORCENATJE_MINIMO = 0.2
PORCENATJE_MAXIMO = 0.2

# Comienza el programa.
def main():
    
    # Comienza bucle while
    while True:

        try:

            # a) Pedimos el nombre al cliente.
            nombre = input("Introduzca su nombre: ")
            if nombre == "":
                break

            # b) Pedimos el número de días que va a reservar.
            dias = int(input("Introduzca el número de días que desea reservar: "))

            # c) Pedimos el número de adultos para la reserva.
            numero_adultos = leer_numero("Introduzca el número de adultos para la reserva: ")

            # d) Pedimos el número de niños para la reserva.
            numero_ninos = leer_numero("Introduzca el número de niños para la reserva: ")
            
            # e) De esos x niños, ¿cuántos son menores de 5 años?
            numero_ninos_menores_5 = ninos_menores_5(numero_ninos)

            # f) Preguntamos al cliente cuánto dinero máximo está dispuesto a pagar por el paquete vacacional.
            coste_maximo_cliente = leer_numero("Introduzca el precio máximo que está dispuesto a pagar por el paquete vacacional: ")

            # f.1) Calculamos un máximo y mínimo del 20% del coste máximo que el cliente permite gastarse.
            coste_minimo = coste_maximo_cliente - coste_maximo_cliente * PORCENATJE_MINIMO
            coste_maximo = coste_maximo_cliente + coste_maximo_cliente * PORCENATJE_MAXIMO
            print("Se ha calculado un ±20% del precio que ha elegido: ")
            print(f"Presupuesto mínimo.....{coste_minimo}€")
            print(f"Presupuesto cliente....{coste_maximo_cliente}€")
            print(f"Presupuesto máximo.....{coste_maximo}€")

            # g) Ofrece y calculamos el preecio de un destino en función de los días, adultos y niños.
            print("Ofrecemos destinos en función de los días elegidos, número de adultos, números de niños mayores de 5 años y número de niños menores de 5 años. Sus datos son:")
            print(f"Número de días reservados: {dias}")
            print(f"Número de adultos: {numero_adultos}")
            print(f"Número de niños mayores de 5 años: {numero_ninos}")
            print(f"Número de niños menores de 5 años: {numero_ninos_menores_5}")
            print("Los destinos posibles segun sus datos son:")

            nombre_destino, precio_total = destino(dias, numero_adultos, numero_ninos, numero_ninos_menores_5)

            print(f"Ha elegido viajar al destino {nombre_destino} y el precio total de la reserva es de {precio_total}€")

            # h) El cliente elige número de estrellas.
            hotel_estrellas = seleccion_estrellas()

        except KeyboardInterrupt:
            print("El cliente ha solicitado cancelar el programa. Saliendo...")
            exit(1)
    
    # Termina bucle while.

# Terminar el programa.

if __name__ == "__main__":
    main()