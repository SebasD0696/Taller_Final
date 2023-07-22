"""Creación de un sistema de reservas de vuelos:
Desarrolla un sistema de reservas de vuelos que permita a los usuarios buscar vuelos, 
seleccionar asientos y realizar reservas. Crea clases como "Vuelo", "Pasajero" y "Reserva" 
para modelar el sistema y utiliza métodos para gestionar las reservas y los asientos disponibles."""

#--------------------------------- Diccionarios ----------------------------------------
Vuelo_asientos = {}
vuelo_destino = {}

vuelo_lista_pasajeros = {}
asientos_ocupados = {}

class sistema:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\n--- Menú de Inventario ---")
            print("1. Crear vuelo")
            print("2. Buscar vuelos")
            print("3. Realizar reserva")
            print("4. Observar reservas realizadas ")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                vuelo_nuevo = vuelo(None,None,None)
                vuelo_nuevo.crear_vuelo()
            elif opcion == "2":
                vuelo_nuevo = vuelo(None,None,None)
                vuelo_nuevo.buscar_vuelo_destino()
            elif opcion == "3":
                reserva_nuevo = reserva(None)
                reserva_nuevo.hacer_reserva()
            elif opcion == "4":
                reserva_nuevo = reserva(None)
                reserva_nuevo.observar_reservas()
            elif opcion == "0":
                print("SALIENDO DEL PROGRAMA.....")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

#------------------------------------ Clases vuelo y pasajero ---------------------------------------------
class vuelo:
    def __init__(self,nombre_vuelo,destino,asientos):
        self.nombre_autor = nombre_vuelo
        self.destino = destino
        self.asientos = asientos

#------------------------------------ Metodo adicional -------------------------------------------
    def crear_vuelo(self):
        self.nombre_vuelo = input("DIGITE EL NOMBRE DEL VUELO: ")
        self.destino = input("DIGITE EL DESTINO DEL VUELO: ")
        self.asientos = int(input("DIGITE LA CANTIDAD DE ASIENTOS QUE POSEE EL VUELO: "))

        Vuelo_asientos[self.nombre_vuelo] = self.asientos
        vuelo_destino[self.nombre_vuelo]  = self.destino
        asientos_ocupados[self.nombre_vuelo] = []
            
#--------------------------------------------------------------------------------------------------

    def buscar_vuelo_destino(self):
        des = input("INGRESE SU DESTINO: ")
        if des not in vuelo_destino.values():
            print("La aerolinea no posee vuelos para dicho destino.")
        else:
            print("====================================")
            print(f" Vuelos con destino a: {des} ")
            print("====================================")
            for key,value in vuelo_destino.items():
                if value == des:
                    print(f"- {key}")

class pasajero:
    def __init__(self,nombre_pasajero):
        self.nombre_pasajero = nombre_pasajero

class reserva(pasajero):
    def __init__(self, nombre_pasajero):
        super().__init__(nombre_pasajero)

    def hacer_reserva(self):
            vuelo_nom = input("DIGITE EL NOMBRE DEL VUELO: ")
            if vuelo_nom not in Vuelo_asientos:
                print("La aerolinea no posee vuelos con dicho nombre.")
            else:
                asientos_disponibles = set(range(1, Vuelo_asientos[vuelo_nom] + 1))
                asientos_reservados = asientos_ocupados[vuelo_nom]  

                for asiento in asientos_reservados:
                    asientos_disponibles.remove(asiento)

                if not asientos_disponibles:
                    print("Lo sentimos, no hay asientos disponibles para este vuelo.")
                    return
                
                print("======================================================")
                print(f" Asientos disponibles para el vuelo: {vuelo_nom} ")
                print("======================================================")
                for i in asientos_disponibles:
                    print(f"- Asiento: {i}")

                asiento_seleccionado = int(input("Seleccione un asiento disponible: "))

                if asiento_seleccionado not in asientos_disponibles:
                    print("El asiento seleccionado no está disponible.")
                else:
                    asientos_ocupados[vuelo_nom].append(asiento_seleccionado)
                    vuelo_lista_pasajeros.setdefault(vuelo_nom, []).append(asiento_seleccionado - 1) 

                    print(f"¡Reserva exitosa! Asiento {asiento_seleccionado} reservado para el vuelo {vuelo_nom}.")

    def observar_reservas(self):
        vuelo_nom = input("DIGITE EL NOMBRE DEL VUELO: ")
        if vuelo_nom not in Vuelo_asientos:
            print("La aerolinea no posee vuelos con dicho nombre.")
        elif vuelo_nom not in vuelo_lista_pasajeros:
            print("No se han realizado reservas para este vuelo.")
        else:
            print("=======================================")
            print(f" Reservas para el vuelo: {vuelo_nom} ")
            print("=======================================")
            for asiento in vuelo_lista_pasajeros[vuelo_nom]:
                print(f" - Asiento: {asiento + 1} reservado")

#----------------------------------------- Objetos de la clase Sistema ------------------------------
sistema1 = sistema()