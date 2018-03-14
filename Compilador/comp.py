# -*- coding: utf-8 -*-
from Estructuras import Pila
variablesind=[]
variablesdef=[]
pilaVar=Pila()
operadores=["+","-","*","/","^"]

def operacion(operador, num1, num2):
    if operador == "+":
        return int(num2) + int(num1)
	if operador == "^":
		return int(num2)**int(num1)
	if operador == "-":
            return int(num2) - int(num1)
    if operador == "*":
            return int(num2) * int(num1)
    if operador == "/":
		if int(num1)==0:
			return "nop"
		else:
			return int(num2) / int(num1)

def leer():
	return [g.split(' ') for g in [x.strip('\n') for x in open("Operaciones2.txt", "r").readlines() ]]
def verificarOperadores(ListaExpresiones):
	for x in range(0,len(ListaExpresiones)):
		for g in ListaExpresiones[x]:
			if(g.isdigit()):
				#print "numero", g
				pilaVar.apilar(g)
			elif( g in operadores):
				print("operador")
			elif(g.isalnum() and not g[0].isdigit()):
				print "variable",g,"en ",ListaExpresiones[x].index(g)
				variablesind.append(g)
			elif(g=="="):
				print("Igual")
			else:
				print ("error")
				return [x,g.index(g)]
	return [-1,-1]
def verificarSintaxis():
	pass



def verificar():
	fuente=leer()
	a=verificarOperadores(fuente)
	if (a==[-1,-1]):
		verificarSintaxis()
		#print("el archivo esta correcto")
		#print "variables no definidas", variablesind
	else:
		print("Error en " + str(a))

verificar()
