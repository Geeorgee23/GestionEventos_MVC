from evento import Evento
from controlador import Controlador


controlador = Controlador()


while True:

    print()
    print("********** MENU EVENTOS **********")
    print("Total eventos registrados: ",controlador.numEventos())
    print("1.- Añadir Evento")
    print("2.- Añadir Participante a Evento")
    print("3.- Listar eventos pendientes de realizar (sin participantes)")
    print("4.- Listar eventos pendientes de realizar (con participantes)")
    print("5.- Listar eventos acabados con podium")
    print("6.- Finalizar un Evento")
    print("7.- Salir")

    while True:
        try:
            op=int(input("Introduce Opción: "))

            if op<=6 and op>=1:
                break

            else:
                print("Introduce un numero del 1 al 6")

        except ValueError:
            print("Introduce un numero!")

    
    if op==7:
        print("Adiós!")
        break


    if op == 1:
        print("Registrando evento....")
        nombreEvento=input("Nombre del evento: ")
        fecha=input("Fecha del evento: ")
        localidad=input("Localidad del evento: ")
        provincia=input("Provincia del evento: ")
        precioInscipcion=input("Precio de inscripción del evento: ")

        evento = Evento(nombreEvento,fecha,localidad,provincia,precioInscipcion)

        if controlador.añadirEvento(evento):
            print("Evento añadido correctamente!")
        else:
            print("Error al añadir el evento!")


    if op == 2:
        while True:
            nomEvento = input("Introduce el nombre del evento:")
            if controlador.estaEvento(nomEvento):
                break
            else:
                print("Este evento no existe!")

        print()
        print("Añadiendo nuevo participante...")
        dni=input("Introduce el dni: ")
        nombre=input("Introduce el nombre: ")
        edad=input("Introduce la edad: ")

        if controlador.addParticipante(nomEvento,dni,nombre,edad):
            print("Participante añadido!")

        else:
            print("Error al añadir el participante!")


    if op == 3:
        for i in controlador.mostrarEventos():
            print(i)
        print()


    if op == 4:
        for i in controlador.mostrarEventosConParticipantes():
            print(i)
        print()


    if op == 5:
        for i in controlador.mostrarEventosAcabados():
            print(i)
        print()

    if op == 6:
        nomEvento=input("¿Que evento quieres finalizar? ")

        if controlador.finalizarEvento(nomEvento):
            print("Evento finalizado con exito!")

        else:
            print("Error al finalizar evento!")
    