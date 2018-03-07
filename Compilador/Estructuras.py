# -*- coding: utf-8 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
    verificar si está vacía. """
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]
    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)
    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    def ver_cola(self):
        try:
            return self.items[0]
        except IndexError:
            raise ValueError("La cola está vacía")
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]
    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)
    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    def ver_pila(self):
        try:
            return self.items[len(self.items)-1]
        except IndexError:
            raise ValueError("La lista esta vacia")
class Nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der=der
def imprimirArbolPosOdn(arbol):
        if arbol != None:
                imprimirArbolPosOdn(arbol.izq)
                imprimirArbolPosOdn(arbol.der)
                print arbol.valor
def imprimirArbolInOdn(arbol):
        if arbol != None:
                imprimirArbolInOdn(arbol.izq)
                print arbol.valor
                imprimirArbolInOdn(arbol.der)
def imprimirArbolPreOdn(arbol):
        if arbol != None:
                print arbol.valor
                imprimirArbolPreOdn(arbol.izq)
                imprimirArbolPreOdn(arbol.der)
