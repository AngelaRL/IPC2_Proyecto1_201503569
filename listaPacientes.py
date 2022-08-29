from tkinter.tix import Tree
from nodoPaciente import nodoPaciente
import xml.etree.ElementTree as ET


class listaPaciente:
    
    def __init__(self):

        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insertarNodo(self, dato):
        nuevo = nodoPaciente(dato) #Creamos el nuevo nodo, mandamos a llamar el nodo de la clase nodo 
        self.size += 1 #aqui es donde aumentamos el tamaño de la lista 
        
        if(self.primerNodo == None): # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def mostrarLista(self): #este metodo nos ayudara a mostrar la lista 
        actual = self.primerNodo

        while(actual != None): #mientras sea diferente de vacio 
            print(actual.dato)

            actual = actual.siguiente #con esto indicamos que vamso a avanzar al siguiente nodo (recorrer la lista)
    
    def cargarPacientes(self):

        actual = self.primerNodo

        #para los datos de los pacientes 
        nombrePa = ''
        edad = 0
        peridos = 0
        m = 0
        rejilla = listaPaciente

        #para las filas y columnas
        fila = ''
        columna = ''

        #metodo utilizado para recorrer la lista 

        while actual != None:

            #para la lectura del .xml 
            leer = ET.parse(actual.dato) #parra recorrer el archivo
            root = leer.getroot  #raiz 

            #para extraer los elemetos 

            for elementoArchivo in root: #para etiqueta paciente
                    
                if elementoArchivo.tag == 'paciente': 

                    for subElemento in elementoArchivo: #subelemento para etiqueta datospersonales

                        if subElemento.tag == 'datospersonales':

                            for ssElement in subElemento:  #ssElement para etiquetas de nombre, edad, celda

                                if ssElement.tag == 'nombre':

                                    print(ssElement.text)

                                elif ssElement.tag == 'edad':

                                    print(ssElement.text)










            actual = actual.siguiente    




        


