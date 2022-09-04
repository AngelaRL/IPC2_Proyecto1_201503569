from arejilla import arejilla
from listaMuestras import listaMuestra
from muestra import Muestra

class paciente:

    def __init__(self, nombre, edad, periodos, m):
        
        #para almencenar los datos que contendra el archivo xml 
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.m = m
        self.celulasMuestra = listaMuestra(m)


    

