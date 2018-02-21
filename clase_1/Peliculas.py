# -*- coding: utf-8 -*-
from Estructuras import Pila

class Pelicula(object):
    def __init__(self, nombre, genero,clasificacion,calificacion):
        self.nombre = nombre
        self.genero=genero
        self.clasificacion=clasificacion
        self.calificacion=calificacion
    def mostar(self):
        return self.nombre

def mostrarPila(pila):
    while not pila.es_vacia():
        auxPel=pila.desapilar()
        print auxPel.mostar()

pila=Pila()
peliculasList=[]
peliculasList.append(Pelicula('Thor','accion','Familiar',4.3))
peliculasList.append(Pelicula('Thor2','accion','Familiar',3.3))
peliculasList.append(Pelicula('Thor3','accion','Familiar',4.3))
peliculasList.append(Pelicula('Chuky','Terror','Adultos',3.7))
peliculasList.append(Pelicula('Chuky2','Terror','Adultos',4.8))
peliculasList.append(Pelicula('Chuky3','Terror','Adultos',3.2))
peliculasList.append(Pelicula('¿que paso ayer?','Comedia','Familiar',3.0))
peliculasList.append(Pelicula('Rapido y furioso','carros','Familiar',1.1))
peliculasList.append(Pelicula('Rapido y furioso 2','carros','Familiar',4.2))
peliculasList.append(Pelicula('Rapido y furioso 3','Terror','Familiar',4.3))
peliculasList.append(Pelicula('Rapido y furioso 4','carros','Familiar',4.5))

while True:
    opc=input("1 genero,2 clasificacion")
    if opc==1:
        for x in range(0, len(peliculasList)):#Recorremos la lista de peliculas
            if peliculasList[x].genero=="Terror":
                pila.apilar(peliculasList[x])#apilamos todas las peliculas de terror
        mostrarPila(pila)#imprimimos la pila 
    elif opc==2:
        for x in range(0, len(peliculasList)):
            if peliculasList[x].calificacion=="Familiar":
                pila.apilar(peliculasList[x])
        mostrarPila(pila)
    else:
        break
