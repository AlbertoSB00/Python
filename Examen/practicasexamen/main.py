"""
Proyecto:           practicasexamen
Archivo:            main.py
Autor:              Alberto Sánchez Barona
Fecha:              28/11/2022
"""

from funciones import elegir_cursos, pregunta_si_no

def main():
    
    while True:
        
        try:

            # Pedimos el nombre.
            nombre = input("Introduzca su nombre: ")

            if nombre == "":
                break
            
            # Mostramos los cursos y damos a elegir.
            curso_valido = False

            while not curso_valido:

                print("Informática -> [OFI]mática(100€), [PRO]gramación(200€), [REP]aración de Ordenadores(150€)")
                print("Administración de Empresas -> [CON]tabilidad y Finanzas(300€), [REC]ursos Humandos(250€), [LEY]es tributarias de Empresas(150€)")
                print("Diseño gráfico -> [RET]oque Fotográfico(200€), [LOG]os Corporativos(250€)")
                
                cursos = ""
                eleccion_curso, precio_curso = elegir_cursos()
                cursos = eleccion_curso + "-"

                pregunta = pregunta_si_no("¿Desea comprar algún otro curso")

                if pregunta:
                    eleccion_curso, precio_curso = elegir_cursos()
                    cursos = eleccion_curso + "-"
                else:
                    curso_valido = True
                
                print(cursos)
            
            
        
        except KeyboardInterrupt:
            print("Se ha solicitado salir del programa.")
            print("Saliendo...")
            exit(1)



if __name__ == "__main__":
    main()