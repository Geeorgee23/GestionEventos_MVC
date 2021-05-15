from evento import Evento
from random import randint

class Controlador:
    def __init__(self):
        self.listaEventos={}

    def numEventos(self):
        return len(self.listaEventos)


    def añadirEvento(self,evento):
        if evento.getNombreEvento() not in self.listaEventos:
            self.listaEventos[evento.getNombreEvento()]=evento
            return True

        return False


    def estaEvento(self,nomEvento):
        if nomEvento in self.listaEventos:
            return True
        return False

    def addParticipante(self,nomEvento,dni,nombre,edad):
        if self.listaEventos[nomEvento].addParticipante(dni,nombre,edad):
            return True

        return False

    
    def mostrarEventos(self):
        lista=[]
        for clave,valor in self.listaEventos.items():
            if valor.getFinalizado()==False:
                lista.append("Nombre del evento: "+clave+"\n\tFecha: "+valor.getFecha()+"\n\tLocalidad: "+valor.getLocalidad()+"\n\tProvincia: "+valor.getProvincia()+"\n\tPrecio Inscripción: "+valor.precioInscipcion())
                
        return lista


    def mostrarEventosConParticipantes(self):
        lista=[]
        for clave,valor in self.listaEventos.items():
            if valor.getFinalizado()==False:
                lista.append("Nombre del evento: "+clave+"\n\tFecha: "+valor.getFecha()+"\n\tLocalidad: "+valor.getLocalidad()+"\n\tProvincia: "+valor.getProvincia()+"\n\tPrecio Inscripción: "+valor.precioInscipcion()+"\n\tParticipantes: "+valor.mostrarParticipantes())
                
        return lista


    def mostrarEventosAcabados(self):
        lista=[]
        for clave,valor in self.listaEventos.items():
            if valor.getFinalizado()==True:
                lista.append("Nombre del evento: "+clave+"\n\tFecha: "+valor.getFecha()+"\n\tLocalidad: "+valor.getLocalidad()+"\n\tProvincia: "+valor.getProvincia()+"\n\tPrecio Inscripción: "+valor.precioInscipcion()+"\n\tParticipantes: "+valor.mostrarParticipantes()+"\n\tPodium: "+valor.mostrarPodium())
                
        return lista


    def finalizarEvento(self,nomEvento):
        if nomEvento in self.listaEventos:
            self.listaEventos[nomEvento].finalizarEvento()
            return True
            #randint(0,len(self.listaEventos[nomEvento].getListadoParticipantes())

        return False


