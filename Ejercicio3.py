"""Creación de un sistema de reservas de vuelos:
Desarrolla un sistema de reservas de vuelos que permita a los usuarios buscar vuelos, 
seleccionar asientos y realizar reservas. Crea clases como "Vuelo", "Pasajero" y "Reserva" 
para modelar el sistema y utiliza métodos para gestionar las reservas y los asientos disponibles."""

#--------------------------------- Diccionarios ----------------------------------------
Vuelo_asientos = {}
vuelo_destino = {}
libros_prestados = {}
usuarios = {}

class sistema:
    def _init_(self):
        self.menu()

    def menu(self):
        while True:
            print("\n--- Menú de Inventario ---")
            print("1. Agregar libro")
            print("2. Buscar libros por autor")
            print("3. Prestar libro")
            print("4. Generar informe de libros prestados")
            print("5. Buscar libros por genero")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                pass
                #self.agregar_libro()
            elif opcion == "2":
                pass
                #self.buscar_libros_autor()
            elif opcion == "3":
                pass
                #self.prestar_libros()
            elif opcion == "4":
                pass
                #self.informe_libros_prestados()
            elif opcion == "5":
                pass
                #self.buscar_libros_genero()
            elif opcion == "0":
                print("SALIENDO DEL PROGRAMA.....")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


#------------------------------------ Clases vuelo y pasajero ---------------------------------------------
class vuelo:
    def _init_(self,nombre_vuelo,destino,asientos):
        self.nombre_autor = nombre_vuelo
        self.destino = destino
        self.asientos = asientos

#------------------------------------ Metodo adicional -------------------------------------------
    def crear_vuelo(self):
        self.nombre_vuelo = input("DIGITE EL NOMBRE DEL VUELO: ")
        self.destino = input("DIGITE EL DESTINO DEL VUELO: ")
        self.asientos = int(input("DIGITE LA CANTIDAD DE ASIENTOS QUE POSEE EL VUELO: "))

        Vuelo_asientos[self.nombre_vuelo] = self.asientos
        vuelo_destino[self.nombre_vuelo]  =self.destino

        for i in range (1,self.asientos+1):
            pass
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
    def _init_(self,nombre_pasajero):
        self.nombre_pasajero = nombre_pasajero

class reserva(pasajero):
    def _init_(self, nombre_pasajero):
        super()._init_(nombre_pasajero)

    def asientos_disponibles():
        vuelo_nom = input("DIGITE EL NOMBRE DEL VUELO: ")
        if vuelo_nom not in Vuelo_asientos:
            print("La aerolinea no posee vuelos con dicho nombre.")
        else:
            print("======================================================")
            print(f" Asientos disponibles para el vuelo: {vuelo_nom} ")
            print("======================================================")
            for key,value in Vuelo_asientos.items():
                if key == vuelo_nom:
                    pass
                    
    def hacer_reserva(self):
        pass        
#----------------------------------------- Objetos de la clase biblioteca ------------------------------
sistema1 = sistema()
sistema1.menu()
