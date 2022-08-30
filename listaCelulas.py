from turtle import st
from arejilla import arejilla


class listaCelulas:

    def __init__(self, m):

        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0
        self.inicializandoMuestra(m)

    def insertarCelula(self, f, c): #para que se este insertando las celulas 

        nuevo = arejilla(f,c)
        self.tamaño += 1 #aqui es donde aumentamos el tamaño de la lista 
        
        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def inicializandoMuestra(self, m):

        for x in range(m):

            for y in range(m):

                self.insertarCelula(x,y)


    def celulaInfectada(self, x, y, m):
        temp = self.primerNodo
        posicion = y+x*m
        n = m*m

        for recorrido in range(n):
            if posicion == recorrido:
                temp.estado = False
                break
            temp = temp.siguiente

    def mostrarCelula(self,m):
        dibujo = ''
        temp = self.primerNodo
        cont = 1
        contador = 1
        while temp :
            if (cont<(contador*m)):
                if (cont == (1+((contador-1)*m))):
                    dibujo+='||'

                if (temp.estado): #decimos que es true
                    dibujo+=' ||'
                else:
                    dibujo+='x||'
            elif (cont == (contador*m)):
                if (temp.estado): #decimos que es true
                    dibujo+=' ||\n'
                else:
                    dibujo+='x||\n'
                contador+=1
            cont+=1

            temp = temp.siguiente #para recorrer
        print(dibujo)    