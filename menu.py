from ast import Num
from turtle import st
from listaPacientes import listaPaciente
from paciente import paciente
import xml.etree.ElementTree as AE
import os 

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
            
            if os.path.exists(rutaArchivo):
                ruta.cargarPacientes(rutaArchivo)
            else:
                print('Verifique el nombre del archivo  ')
            
        elif opcion == 2:
            while not salir:
                print('::::::::::::::: Seccion de Pacientes :::::::::::::::::')
                ruta.mostrarPacientes()
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
            print('Generando archivo de salida...')
            ruta.resultados()
        elif opcion == 4:
            salir = True
            print("Cerrando programa")
        else:
            print("Opcion invalida")

def menuPaciente(pacienteE):
    global salir, ruta
    contador = 1
    while not salir:
        print("")
        print("")
        print(":::::::::::  PACIENTE: "+pacienteE.paciente.nombre +" ::::::::::::")
        print("")
        pacienteE.paciente.celulasMuestra.primerNodo.muestra.mostrarCelula(pacienteE.paciente.m)
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
            if(pacienteE.paciente.periodos == 0 ): 
                
                print('Se llego al maximo de peridos permitidos.') 
                print('Se mostrara los resultados que se hicieron previamente.')
                pacienteE.paciente.celulasMuestra.recorriendo()
                if pacienteE.paciente.celulasMuestra.n == 0 and pacienteE.paciente.celulasMuestra.n1 == 0:
                    print('El estado del paciente es: leve')
                else:
                    if  (pacienteE.paciente.celulasMuestra.n == 1 or pacienteE.paciente.celulasMuestra.n1 == 1) or (pacienteE.paciente.celulasMuestra.n == 1 and pacienteE.paciente.celulasMuestra.n1 == 1):
                        print('El estado del paciente es: mortal')
                    else: 
                        print('El estado del paciente es: grave')
                if pacienteE.paciente.celulasMuestra.n != 0 :
                   print('El valor de n es: '+str(pacienteE.paciente.celulasMuestra.n))
                if pacienteE.paciente.celulasMuestra.n1 != 0 :
                    print('El valor de n1 es: '+str(pacienteE.paciente.celulasMuestra.n1))
            while  pacienteE.paciente.periodos > 0:
                print(" Periodo numero: "+str(contador))
                pacienteE.paciente.celulasMuestra.analizar(contador)
                pacienteE.paciente.periodos-=1
                contador += 1
        elif subopcion == 2:
            if(pacienteE.paciente.periodos > 0 ): 
                print(" Periodo numero: "+str(contador))
                pacienteE.paciente.celulasMuestra.analizar(contador)
                pacienteE.paciente.periodos-=1
                contador += 1
            else:
                print('Se llego al maximo de peridos permitidos.') 
                print('Se mostrara los resultados que se hicieron previamente.')
                pacienteE.paciente.celulasMuestra.recorriendo()
                if pacienteE.paciente.celulasMuestra.n == 0 and pacienteE.paciente.celulasMuestra.n1 == 0:
                    print('El estado del paciente es: leve')
                else:
                    if  (pacienteE.paciente.celulasMuestra.n == 1 or pacienteE.paciente.celulasMuestra.n1 == 1) or (pacienteE.paciente.celulasMuestra.n == 1 and pacienteE.paciente.celulasMuestra.n1 == 1):
                        print('El estado del paciente es: mortal')
                    else: 
                        print('El estado del paciente es: grave')
                if pacienteE.paciente.celulasMuestra.n != 0 :
                   print('El valor de n es: '+str(pacienteE.paciente.celulasMuestra.n))
                if pacienteE.paciente.celulasMuestra.n1 != 0 :
                    print('El valor de n1 es: '+str(pacienteE.paciente.celulasMuestra.n1))
        
                    
        elif subopcion == 3: 
            salir=True
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menuprincipal()