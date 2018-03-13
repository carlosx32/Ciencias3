# -*- coding: utf-8 -*-
from Estructuras import *

listaOperadores=[]
"""
def crearArbol(cadena,pila):
	#Funcion que permite convertir una entrada en posfijo a un arbol de expresion
	for i in cadena:
		if i in "+-*/^=":
			der=pila.desapilar()
			izq=pila.desapilar()
			pila.apilar(Nodo(i,izq,der))
			#apila las operaciones asignando la variable a la izquierda y a la derecha
		else:
			pila.apilar(Nodo(i,None,None))#apila las variables
	return pila.desapilar() #retorna la cabeza del arbol
"""
def crearArbol(cadena,pila):
	#Funcion que permite convertir una entrada en posfijo a un arbol de expresion
	for i in range(0,len(cadena)):
		if cadena[i] in "+-*/^=":
			der=pila.desapilar()
			izq=pila.desapilar()
			pila.apilar(Nodo(cadena[i],izq,der))
			#apila las operaciones asignando la variable a la izquierda y a la derecha
		else:
			pila.apilar(Nodo(cadena[i],None,None))#apila las variables
	return pila.desapilar() #retorna la cabeza del arbol

class Tabla():
    variables = {}

def evaluar(arbol):
#evaluamos en pos orden
    if arbol.valor == '+':
        return int(evaluar(arbol.izq)) + int(evaluar(arbol.der))
    if arbol.valor == '-':
        return int(evaluar(arbol.izq)) - int(evaluar(arbol.der))
    if arbol.valor == '/':
        return int(evaluar(arbol.izq)) / int(evaluar(arbol.der))
    if arbol.valor == '*':
        return int(evaluar(arbol.izq)) * int(evaluar(arbol.der))
    if arbol.valor == '^':
        return int(evaluar(arbol.izq)) ** int(evaluar(arbol.der))
    if arbol.valor == '=':
        valor = evaluar(arbol.izq)
        Tabla.variables[arbol.der.valor] = valor
        return valor
    if Tabla.variables.has_key(arbol.valor) == True:
        return Tabla.variables[arbol.valor]
    elif Tabla.variables.has_key(arbol.valor) == False:
        return int(arbol.valor)
def entrada():
	#funcion que permite ingresar una expresion en postfijo, esta esntrada no esta validada
	#return raw_input("Ingrese una operacion en postfijo, separando cada entrada por espacios ").split(' ')
	#return [g.split(' ') for g in [x.strip('\n') for x in open("operaciones.txt", "r").readlines() ] ]
	return [g.split(' ') for g in [x.strip('\n') for x in open("operaciones.txt", "r").readlines() ]]

menu=True
while menu:
	cadena = entrada()
	pila = Pila()
	arbolesExpresion =[]
	#print cadena[0]
	for x in cadena:
		arbolesExpresion.append(crearArbol(x,pila))

	#print cadena
	for x in arbolesExpresion:
		print ("arbol ",x)
		print imprimirArbolPreOdn(x)
		print imprimirArbolInOdn(x)
		print imprimirArbolPosOdn(x)


	#print "Arbol de expresion en In orden"
	#imprimirArbolPreOdn(arbolExpresion)
	#print "Arbol de expresion en Pos orden"
	#imprimirArbolPreOdn(arbolExpresion)

#	print"		Resultado: ",evaluar(arbolExpresion)
	menuopc=raw_input("¿Desea Volver a intentarlo ? s/n ")
	if menuopc=='s' or menu=='S':
		menu=True
	else: menu=False
