# -*- coding: utf-8 -*-
from Estructuras import Cola
from Estructuras import Pila

class Persona(object):
    """docstring for Personas."""
    def __init__(self, documento,nombre,especialidad):
        self.documento = str(documento)
        self.nombre = nombre
        self.especialidad = especialidad
    def getNombre(self):
        return self.nombre
    def getDocumento(self):
        return self.documento
    def getEspecialidad(self):
        return self.especialidad
    def getPersona(self):
        return "Doc: " + self.documento + " nombre: "+self.nombre +" Especialidad: "+self.especialidad
class Gestion(object):
    def __init__(self):
        self.pacientes=Cola()
        self.pacientesAtendidos=Pila()
        self.historialPacientes=Pila()
        self.cardiologia= Cola()
        self.neumologia= Cola()
        self.fisioterapia=Cola()
        self.otras=Cola()
    def espera(self,paciente):
        self.pacientes.encolar(paciente)
        self.historialPacientes.apilar(paciente)
        self.asignarEspecialidades()
    def asignarEspecialidades(self):
        while not self.pacientes.es_vacia():
            if(self.pacientes.ver_cola().getEspecialidad()=='cardiologia'):
                self.cardiologia.encolar(self.pacientes.desencolar())
            elif(self.pacientes.ver_cola().getEspecialidad()=='neumologia'):
                self.neumologia.encolar(self.pacientes.desencolar())
            elif(self.pacientes.ver_cola().getEspecialidad()=='fisioterapia'):
                self.fisioterapia.encolar(self.pacientes.desencolar())
            else:
                self.otras.encolar(self.pacientes.desencolar())
    def atender(self, nEspecialidad):
        if(nEspecialidad==1):
            if not self.cardiologia.es_vacia():
                self.pacientesAtendidos.apilar(self.cardiologia.ver_cola())
                return self.cardiologia.desencolar()
        elif(nEspecialidad==2):
            if not self.neumologia.es_vacia():
                self.pacientesAtendidos.apilar(self.neumologia.ver_cola())
                return self.neumologia.desencolar()
        elif(nEspecialidad==3):
            if not  self.neumologia.es_vacia():
                self.pacientesAtendidos.apilar(self.fisioterapia.ver_cola())
                return self.fisioterapia.desencolar()
        else:
            if not self.otras.es_vacia():
                self.pacientesAtendidos.apilar(self.otras.ver_cola())
                return self.otras.desencolar()
        return ""
    def getHistorial(self):
        return self.historialPacientes
    def getAtendidos(self):
        return self.pacientesAtendidos
    def getCardiologia(self):
        return self.cardiologia
    def getNeumologia(self):
        return self.neumologia
    def getFisioterapia(self):
        return self.fisioterapia
    def getOtras(self):
        return self.otras

#menu
hospital=Gestion();
##datos prueba
hospital.espera(Persona(1,'persona1','cardiologia'))
hospital.espera(Persona(2,'persona2','fisioterapia'))
hospital.espera(Persona(3,'persona3','cardiologia'))
hospital.espera(Persona(4,'persona4','medicina general'))
hospital.espera(Persona(5,'persona5','neumologia'))
hospital.espera(Persona(6,'persona6','medicina general'))

a=True
auxCola=Cola()

while a:
    print("Elija una opcion")
    print("1 nuevo paciente")
    print("2 atender")
    print("3 pacientes en espera")
    print("4 pacientes atendidos")
    print("5 historial")
    print("6 salir")
    opcion=input("Selecciones una opcion:")
    if(opcion==1):
        hospital.espera(Persona(raw_input("Ingrese el documento: "),raw_input("Ingrese el nombre: "), raw_input("Ingrese la especialidad: ")))
    elif(opcion==2):
        print("         atender pacientes:       ")
        opcAtender=input("      ingrese 1 para para cardiologia, 2 para neumologia 3 para fisioterapia, 4 para otras : ")
        auxPersona=hospital.atender(opcAtender)
        if not auxPersona=="":
            print("     Datos del paciente   "+ auxPersona.getPersona())
        else:
            print("     No hay pacientes")
    elif(opcion==3):
        print("         pacientes en espera:       ")
        print("     pacientes cardiologia")
        auxCola=hospital.getCardiologia()
        while not auxCola.es_vacia:
            print(auxCola.desencolar().getPersona())
        print("     pacientes neumologia")
        auxCola=hospital.getNeumologia()
        while not auxCola.es_vacia:
            print(auxCola.desencolar().getPersona())
        print("     pacientes fisioterapia")
        auxCola=hospital.getFisioterapia()
        while not auxCola.es_vacia:
            print(auxCola.desencolar().getPersona())
        print("     pacientes otras")
        auxCola=hospital.getOtras()
        while not auxCola.es_vacia:
            print(auxCola.desencolar().getPersona())
        print("fin")
    elif opcion==4:
        print("         Pacientes atendidos:       ")
        auxCola=hospital.getAtendidos()
        while not auxCola.es_vacia():
            print("             "+auxCola.desapilar().getPersona())

    elif(opcion==5):
        auxCola=hospital.getHistorial()
        print("         Historial:       ")
        while not auxCola.es_vacia():
            print("             "+auxCola.desapilar().getPersona())
    else:
        a=False
