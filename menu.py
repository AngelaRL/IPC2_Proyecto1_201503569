from ast import Num
from turtle import st
from listaPacientes import listaPaciente
from paciente import paciente
import xml.etree.ElementTree as AE

salir = False
ruta = None

def menuprincipal():
    global salir, ruta
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
                print('::::::::::::::: Seccion de Pacientes :::::::::::::::::')
                
                recibirPaciente = ruta.buscarPaciente(input('Escriba el nombre del paciente a Analizar:  '))

                if (recibirPaciente):
                    menuPaciente(recibirPaciente)
                else:
                    print('¿Desea seguir buscando?')
                    print('1. Si ')
                    print('2. No ')

                    subopcion = int(input("ingrese el numero de la opcion que desea:"))

                    if subopcion == 2:
                        salir = True
                    elif subopcion < 1 and subopcion >2:
                        print("opcion no valida")

                print("")
            salir = False
        elif opcion == 3:
            print("")
        elif opcion == 4:
            salir = True
            print("Cerrando programa")
        else:
            print("Opcion invalida")

def menuPaciente(pacienteE):
    global salir, ruta
    while not salir:
        print("")
        print("")
        print(":::::::::::  PACIENTE: "+pacienteE.paciente.nombre +" ::::::::::::")
        print("")
        print("1. Analizar Muestra Automaticamente")
        print("2. Analizar Muestra por Periodo ")
        print("3. Regresar al menu principal ")
        print("")
        print("")
        print("")
        print("")
        print("")

        subopcion = int(input("ingrese el numero de la opcion que desea: "))

        if subopcion == 1:
            print("Empezando a analizar Automaticamente:  ")
            contador = 1
            while pacienteE.paciente.periodos > 0:
                print(" Periodo numero: "+str(contador))
                pacienteE.paciente.celulasMuestra.analizar()
                pacienteE.paciente.periodos-=1 
                contador += 1
        elif subopcion == 2:
            if(pacienteE.paciente.periodos > 0 ): 
                print(" Periodo numero: "+str(contador))
                pacienteE.paciente.celulasMuestra.analizar()
                pacienteE.paciente.periodos-=1 
            else:
                print('Error: No se puede analizar nuevamente la muestra debido que llego al maximo de peridos permitidos.')     
        elif subopcion == 3: 
            salir=True
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menuprincipal()