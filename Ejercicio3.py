"""Creación de un sistema de reservas de vuelos:
Desarrolla un sistema de reservas de vuelos que permita a los usuarios buscar vuelos, 
seleccionar asientos y realizar reservas. Crea clases como "Vuelo", "Pasajero" y "Reserva" 
para modelar el sistema y utiliza métodos para gestionar las reservas y los asientos disponibles."""

"""Crear diccionarios anidados"""



#--------------------------------- Diccionarios ----------------------------------------
Vuelo_asientos = {}
vuelo_destino = {}
libros_prestados = {}

vuelo_lista_pasajeros = {}
pasajeros = {}


diccionario_1 = {}


class sistema:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\n--- Menú de Inventario ---")
            print("1. Crear vuelo")
            print("2. Buscar vuelos")
            print("3. Asientos disponibles")
            print("4. Generar informe de libros prestados")
            print("5. Buscar libros por genero")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                vuelo_nuevo = vuelo()
                vuelo_nuevo.crear_vuelo()
            elif opcion == "2":
                vuelo_nuevo = vuelo()
                vuelo_nuevo.buscar_vuelo_destino()
            elif opcion == "3":
                reserva_nuevo = reserva()
                reserva_nuevo.asientos_disponibles()
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
        vuelo_destino[self.nombre_vuelo]  = self.destino
        
        nuevo_diccionario = {}
        for i in range(1,self.asientos+1):
            n = True
            nuevo_diccionario[i] = n
        diccionario_1[self.nombre_vuelo]  = nuevo_diccionario 
            
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

    def asientos_disponibles(self):
        vuelo_nom = input("DIGITE EL NOMBRE DEL VUELO: ")
        if vuelo_nom not in Vuelo_asientos:
            print("La aerolinea no posee vuelos con dicho nombre.")
        else:
            print("======================================================")
            print(f" Asientos disponibles para el vuelo: {vuelo_nom} ")
            print("======================================================")
            for key,value in vuelo_lista_pasajeros.items():
                if key == vuelo_nom:
                    for i in value:
                        print(f" - Asiento: {i+1} ")
                    print("")
                    decision = int(input("SELECCIONE EL ASIENTO: "))
                    
                    if decision in value:
                        for i in value:
                            if decision == i+1:
                                self.nombre_pasajero = input("DIGITE El NOMBRE DEL PASAJERO")
                                value.remove(decision-1)
                                
                                pasajeros[self.nombre_pasajero] = decision
                                print(f"El pasajero: {self.nombre_pasajero} reservo el asiento {decision}")
                    else:
                        print("EL ASIENTO NO EXISTE O NO ESTA DISPONIBLE")
        
    def hacer_reserva(self):
        pass        
#----------------------------------------- Objetos de la clase biblioteca ------------------------------
sistema1 = sistema()
sistema1.menu()
