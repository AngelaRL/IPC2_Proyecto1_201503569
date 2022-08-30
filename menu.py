from ast import Num
from listaPacientes import listaPaciente
from paciente import paciente
import xml.etree.ElementTree as AE


def menuprincipal():

    salir = False
    opcion = 0
    subopcion =0
    while not salir:
        print("::::::::::::::::::::::::::::::::::: MENU :::::::::::::::::::::::::::::::::::")
        print("")
        print("Ingrese el numero de la opcion que desea:")
        print("")
        print("")
        print("")
        print("1. Cargar datos ")
        print("2. Elegir paciente")
        print("3. Generar archivo de resultado ")
        print("4. Salir ")
        print("")
        print("")
        print("")
    

        opcion = int(input("ingrese el numero:    "))

        if opcion == 1:

            ruta = listaPaciente()

            print("ingrese la ruta del archivo")
            rutaArchivo = input('  ') 
            print("")
            print("")
            

            ruta.cargarPacientes(rutaArchivo)


            
        elif opcion == 2:
            while not salir:
                print("")
                print("")
                print(":::::::::::___PACIENTE___::::::::::::")
                print("")
                print("1. Analizar Muestra Automaticamente")
                print("2. Analizar Muestra por Periodo ")
                print("3. Regresar al menu principal ")
                print("")
                print("")
                print("")
                print("")
                print("")

                subopcion = int(input("ingrese el numero de la opcion que desea:"))

                if subopcion == 1:
                    print("")
                elif subopcion == 2:
                    print("2")
                elif subopcion == 3:
                    menuprincipal()
                else:
                    print("opcion no valida")

            print("")
        elif opcion == 3:
            print("")
        elif opcion == 4:
            salir = True
            print("Cerrando programa")
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menuprincipal()