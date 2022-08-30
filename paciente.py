from arejilla import arejilla
from listaCelulas import listaCelulas

class paciente:

    def __init__(self, nombre, edad, periodos, m):
        
        #para almencenar los datos que contendra el archivo xml 
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.m = m
        self.celulasMuestra = listaCelulas(m)

    

