from ast import Num



def menuprincipal():

    salir = False
    opcion = 0
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
        print("")
        print("")
        print("")

        opcion = int(input("ingrese el numero"))

        if opcion == 1:
            print("1")
        elif opcion == 2:
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