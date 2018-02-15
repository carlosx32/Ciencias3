class Persona(object):
    """docstring for Personas."""
    def __init__(self, documento,nombre,especialidad):
        self.documento = documento
        self.nombre = nombre
        self.especialidad = especialidad
    def getNombre(self):
        return self.nombre
    def getDocumento(self):
        return self.documento
    def getEspecialidad(self):
        return self.especialidad
class ColaHop(object):
    """Cola segun la especialidad"""
    def __init__(self,especialidad):
        self.especialidad=especialidad
        self.pacientes=[]
    def nuevoPaciente(self, x):
        self.pacientes.append(x);
    def desencolarCliente(self):
        try:
            return self.pacientes.pop(0)
        except IndexError:
            raise ValueError("No hay clientes")
    def es_vacia(self):
        return self.items == []

ListPacientes=[]
ListPacientes.append(Persona(1,'persona1','esp1'))
ListPacientes.append(Persona(2,'persona2','esp2'))
ListPacientes.append(Persona(3,'persona3','esp1'))

esp={'cardiologia':ListPacientes[0] ,'cardiologia':ListPacientes[0] }


for x in ListPacientes:
    print(x.getNombre(), x.getEspecialidad())
"""Asignamos las personas a las colas"""
