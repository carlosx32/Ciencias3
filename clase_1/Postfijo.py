# -*- coding: utf-8 -*-
from Estructuras import *

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
def entrada():
	#funcion que permite ingresar una expresion en postfijo, esta esntrada no esta validada
	return raw_input("Ingrese una operacion en postfijo, separando cada entrada por espacios ").split(' ')

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


menu=True
while menu:
	cadena = entrada()
	pila = Pila()
	arbolExpresion = crearArbol(cadena, pila)
	print "Arbol de expresion en Pre orden"
	imprimirArbolPreOdn(arbolExpresion)
	print "Arbol de expresion en In orden"
	imprimirArbolPreOdn(arbolExpresion)
	print "Arbol de expresion en Pos orden"
	imprimirArbolPreOdn(arbolExpresion)

	print"		Resultado: ",evaluar(arbolExpresion)
	menuopc=raw_input("¿Desea Volver a intentarlo ? s/n ")
	if menuopc=='s' or menu=='S':
		menu=True
	else: menu=False
