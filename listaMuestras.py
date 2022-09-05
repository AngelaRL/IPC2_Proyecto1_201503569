from tempfile import tempdir
from turtle import pos, st
from arejilla import arejilla
from muestra import Muestra
from nodoMuestra import nodoMuestra


class listaMuestra:

    def __init__(self, m):
        self.m = m
        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0
        self.resultado = ''
        self.n = 0
        self.n1 = 0

    def insertarMuestra(self, muestra): #para que se este insertando las celulas 

        nuevo = nodoMuestra(muestra)
        self.tamaño += 1 #aqui es donde aumentamos el tamaño de la lista 
        
        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo

    def analizar(self):
        temp = self.ultimoNodo #obtenemos la ultima muestra
        auxMuestra = Muestra(self.m) #creando una nueva muestra 
        analizando = temp.muestra.primerNodo #obtenemos la matriz de las celulas 
        while analizando:
            if analizando.estado:
                if self.enfermandoCelulas(temp.muestra, analizando, 'enfermar'):                    
                    auxMuestra.celulaInfectada(analizando.f, analizando.c , self.m)
            else:
                if self.enfermandoCelulas(temp.muestra, analizando, 'seguirenferma'):                    
                    auxMuestra.celulaInfectada(analizando.f, analizando.c , self.m)
                
            analizando = analizando.siguiente
        self.insertarMuestra(auxMuestra)
        auxMuestra.mostrarCelula(self.m)
        del auxMuestra #del elimina lo que contiene 
        

    def enfermandoCelulas(self, muestra, celula, condicion):
        vecinosEnfermos = 0
        posVecinos = [] #para guardar las posiciones de los vecinos 
        posVecinos.append(arejilla(celula.f,(celula.c+1)))
        posVecinos.append(arejilla((celula.f+1),celula.c))
        posVecinos.append(arejilla(celula.f,(celula.c-1)))
        posVecinos.append(arejilla((celula.f-1),celula.c))
        posVecinos.append(arejilla((celula.f+1),(celula.c+1)))
        posVecinos.append(arejilla((celula.f+1),(celula.c-1)))
        posVecinos.append(arejilla((celula.f-1),(celula.c+1)))
        posVecinos.append(arejilla((celula.f-1),(celula.c-1)))
                
        temp = muestra.primerNodo
        
        for vecino in posVecinos:
                       
            if ((vecino.f >= 0 and vecino.f < self.m) and (vecino.c >= 0 and vecino.c < self.m) ):
                while temp:         
                    
                    if temp.posicion == (vecino.f*self.m + vecino.c) and temp.estado == False:
                        
                        vecinosEnfermos += 1
                        break
                    elif temp.posicion == (vecino.f*self.m + vecino.c) and temp.estado:
                        break                                                                            
                    temp = temp.siguiente
                temp = muestra.primerNodo 
        
        if condicion == 'enfermar':

            if vecinosEnfermos == 3:
                return True 
        else:
            if vecinosEnfermos == 2 or vecinosEnfermos == 3:
                return True
        

        return False
        
    def procesando(self):
        encontrado = False
        temp = self.primerNodo
        temp2 = self.primerNodo.siguiente 
        periodo = 0
        while temp2:            #para buscar si hay muestras igualaes a la original 
            periodo +=1 
            if self.verificandoRepeticion(temp.muestra, temp2.muestra):
                encontrado = True
                break                
            temp2 = temp2.siguiente
        if encontrado:            
            self.n = periodo
        else:
            repetidos = 0
            periodo = 0 
            temp = self.primerNodo.siguiente 
            while temp:         #para buscar si hay laguna muestra que se repita que no sea la muestra original
                temp2 = temp.siguiente
                repetidos = 0 
                periodo +=1                     
                while temp2:
                    repetidos += 1
                    if self.verificandoRepeticion(temp.muestra, temp2.muestra):
                        encontrado = True
                        break
                    temp2 = temp2.siguiente
                temp = temp.siguiente
            if encontrado:
                self.n = periodo
                self.n1 = repetidos   



    def verificandoRepeticion(self, muestra, muestra2):
        temp = muestra.primerNodo
        temp2 = muestra2.primerNodo
        while temp:
            
            if (temp.estado != temp2.estado):
                return False
            temp = temp.siguiente
            temp2 = temp2.siguiente
        return True 
