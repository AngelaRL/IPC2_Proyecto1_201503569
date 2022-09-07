from textwrap import indent
from muestra import Muestra
from paciente import paciente
from nodoPaciente import nodoPaciente
import xml.etree.ElementTree as ET
from xml.dom import minidom


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
            actual.paciente.celulasMuestra.primerNodo.muestra.mostrarCelula(actual.paciente.m)
            print('-----------------------------------------------------------')
            actual = actual.siguiente #con esto indicamos que vamso a avanzar al siguiente nodo (recorrer la lista)

    def mostrarPacientes(self): #este metodo nos ayudara a mostrar la lista 
        actual = self.primerNodo

        while actual != None: #mientras sea diferente de vacio 
            print('Paciente: ',actual.paciente.nombre)
            actual = actual.siguiente #con esto indicamos que vamso a avanzar al siguiente nodo (recorrer la lista)
        print('-----------------------------------------------------------')
    
    def cargarPacientes(self, rutaArchivo):
        print('Empezando a anlizar el archivo...')
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
            auxmuestra = None

            if elementoArchivo.tag == 'paciente': 
                print('Obteniendo paciente...')

                for subElemento in elementoArchivo: #subelemento para etiqueta datospersonales

                    if subElemento.tag == 'datospersonales':
                        print('Registrando los datos del paciente... ')

                        for ssElement in subElemento:  #ssElement para etiquetas de nombre, edad, celda

                            if ssElement.tag == 'nombre':

                                nombrePa = ssElement.text

                                print('Nombre: ',nombrePa)

                            elif ssElement.tag == 'edad':

                                edad = ssElement.text

                                print('Edad: ',edad)
                    elif subElemento.tag == 'periodos':

                        peridos = subElemento.text
                       
                    elif subElemento.tag == 'm':

                        m = subElemento.text
                        auxmuestra = Muestra(int(m))

                        print('La muestra es de tamaño: ',m)
                        auxpa = paciente(nombrePa, int(edad), int(peridos), int(m))
                    
                    elif subElemento.tag == 'rejilla':

                        for ssElement in subElemento: #para entrar a la etiqueta celta que esta dentro de etiqueta rejilla 

                            if ssElement.tag == 'celda':
                                print('Registrando los datos de la muestra... ')
                                fila = ssElement.get('f')                                
                                columna = ssElement.get('c')
                               
                                auxmuestra.celulaInfectada(int(fila),int(columna),int(m)) #inserta las celulas infectadas 
                        auxpa.celulasMuestra.insertarMuestra(auxmuestra)    

            self.insertar(auxpa)
                           
        print('-------------------------------------------------')


    def buscarPaciente(self, nombre):
        temp = self.primerNodo
        while temp:
            if temp.paciente.nombre == nombre:
                return temp        
            temp = temp.siguiente
        return None
        
    def resultados(self):
        temp = self.primerNodo

        raiz = ET.Element('pacientes')

        while temp:
            paciente = ET.SubElement(raiz, 'paciente')
            dp = ET.SubElement(paciente,'datospersonales')
            ET.SubElement(dp,'nombre').text= temp.paciente.nombre
            ET.SubElement(dp,'edad').text= str(temp.paciente.edad)
            ET.SubElement(paciente,'periodos').text= str(temp.paciente.periodos)
            ET.SubElement(paciente,'m').text= str(temp.paciente.m)
            
            if temp.paciente.celulasMuestra.n == 0 and temp.paciente.celulasMuestra.n1 == 0:
                ET.SubElement(paciente, 'resultado').text = 'leve'
            else:
                if  (temp.paciente.celulasMuestra.n == 1 or temp.paciente.celulasMuestra.n1 == 1) or (temp.paciente.celulasMuestra.n == 1 and temp.paciente.celulasMuestra.n1 == 1):
                    ET.SubElement(paciente, 'resultado').text = 'mortal'
                else: 
                    ET.SubElement(paciente, 'resultado').text = 'grave'
            if temp.paciente.celulasMuestra.n != 0 :
                ET.SubElement(paciente, 'n').text = str(temp.paciente.celulasMuestra.n)
            if temp.paciente.celulasMuestra.n1 != 0 :
                ET.SubElement(paciente, 'n1').text = str(temp.paciente.celulasMuestra.n1)
                
            temp = temp.siguiente

        archivo = open('resultados.xml', 'a')
        archivo.write(minidom.parseString(ET.tostring(raiz, encoding='utf-8').decode('utf-8')).toprettyxml(indent=" "))
        archivo.close()
    








        


