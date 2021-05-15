class Evento:
    def __init__(self,nombreEvento,fecha,localidad,provincia,precioInscipcion):
        self.nombreEvento=nombreEvento
        self.fecha=fecha
        self.localidad=localidad
        self.provincia=provincia
        self.precioInscipcion=precioInscipcion
        self.totalAcumulado=0
        self.listadoParticipantes=[]
        self.finalizado=False
        self.podium={"PRIMERO":0,
                    "SEGUNDO":0,
                    "TERCERO":0}


    def getNombreEvento(self):
        return self.nombreEvento

    def getFecha(self):
        return self.fecha

    def getLocalidad(self):
        return self.localidad

    def getProvincia(self):
        return self.provincia

    def getPrecioInscripcion(self):
        return self.precioInscipcion

    def getTotalAcumulado(self):
        return self.totalAcumulado

    def getListadoParticipantes(self):
        return self.listadoParticipantes

    def getFinalizado(self):
        return self.finalizado

    def getPodium(self):
        return self.podium


    def addParticipante(self,dni,nombre,edad):
        self.listadoParticipantes.append((dni,nombre,edad))
        return True


    def mostrarParticipantes(self):
        lista=""
        for i in self.listadoParticipantes:
            lineas+="\tDni: "+str(i[0])+"\tNombre: "+str(i[1])+"\tEdad: "+str(i[2])+"\n\t\t\t"

        return lista


    def mostrarPodium(self):
        lista=""
        for clave,valor in self.podium.items():
            lineas+="\t"+clave+": "+valor+"\n\t\t\t"

        return lista


    def finalizarEvento(self):
        self.finalizado=True