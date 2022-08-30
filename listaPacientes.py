from paciente import paciente
from arejilla import arejilla
from nodoPaciente import nodoPaciente
import xml.etree.ElementTree as ET


class listaPaciente:
    
    def __init__(self):

        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insertar(self, paciente):

        nuevo = nodoPaciente(paciente) #Creamos el nuevo nodo, mandamos a llamar el nodo de la clase nodo 
        self.tamaño += 1 #aqui es donde aumentamos el tamaño de la lista 
        
        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def mostrarLista(self): #este metodo nos ayudara a mostrar la lista 
        actual = self.primerNodo

        while actual != None: #mientras sea diferente de vacio 
            print(actual.paciente.nombre,actual.paciente.m)
            actual.paciente.celulasMuestra.mostrarCelula(actual.paciente.m)
            print('-----------------------------------------------------------')
            actual = actual.siguiente #con esto indicamos que vamso a avanzar al siguiente nodo (recorrer la lista)
    
    def cargarPacientes(self, rutaArchivo):

        #para los datos de los pacientes 
        nombrePa = ''
        edad = 0
        peridos = 0
        m = 0
        

        #para las filas y columnas
        fila = ''
        columna = ''

        #metodo utilizado para recorrer la lista 

       
        #para la lectura del .xml 
        leer = ET.parse(rutaArchivo) #parra recorrer el archivo
        root = leer.getroot()  #raiz 

        #para extraer los elemetos 

        print(rutaArchivo)

        for elementoArchivo in root: #para etiqueta paciente
            nombrePa = ''
            edad =''
            peridos = ''
            m = ''
            auxpa = None

            if elementoArchivo.tag == 'paciente': 

                for subElemento in elementoArchivo: #subelemento para etiqueta datospersonales

                    if subElemento.tag == 'datospersonales':

                        for ssElement in subElemento:  #ssElement para etiquetas de nombre, edad, celda

                            if ssElement.tag == 'nombre':

                                nombrePa = ssElement.text

                                print(nombrePa)

                            elif ssElement.tag == 'edad':

                                edad = ssElement.text

                                print(edad)
                    elif subElemento.tag == 'periodos':

                        peridos = subElemento.text

                        print(peridos)

                    elif subElemento.tag == 'm':

                        m = subElemento.text

                        print(m)
                        auxpa = paciente(nombrePa, int(edad), int(peridos), int(m))
                    
                    elif subElemento.tag == 'rejilla':

                        for ssElement in subElemento: #para entrar a la etiqueta celta que esta dentro de etiqueta rejilla 

                            if ssElement.tag == 'celda':

                                fila = ssElement.get('f')
                                print(fila)
                                columna = ssElement.get('c')
                                print(columna)

                                auxpa.celulasMuestra.celulaInfectada(int(fila),int(columna),int(m))
            self.insertar(auxpa)
        self.mostrarLista()
            
        print('-------------------------------------------------')














        


