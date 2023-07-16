class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad
        self.asientos = {i: None for i in range(1, capacidad + 1)}

    def __str__(self):
        return f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino} el {self.fecha}. Asientos disponibles: {self.asientos_disponibles}"

    def mostrar_asientos_disponibles(self):
        print("Asientos disponibles:")
        for numero_asiento, pasajero in self.asientos.items():
            if pasajero is None:
                print(f"Asiento {numero_asiento}")

    def reservar_asiento(self, numero_asiento, pasajero):
        if numero_asiento in self.asientos and self.asientos[numero_asiento] is None:
            self.asientos[numero_asiento] = pasajero
            self.asientos_disponibles -= 1
            print(f"Reserva realizada: Asiento {numero_asiento} reservado para {pasajero.nombre} {pasajero.apellido}.")
            return True
        else:
            print("El asiento no está disponible o no existe.")
            return False


class Pasajero:
    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento


class Reserva:
    def __init__(self):
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def buscar_vuelo(self, origen, destino, fecha):
        vuelos_encontrados = [vuelo for vuelo in self.vuelos if vuelo.origen == origen and vuelo.destino == destino and vuelo.fecha == fecha]
        return vuelos_encontrados

# Ejemplo de uso:
if __name__ == "__main__":
    vuelo1 = Vuelo("V001", "Ciudad A", "Ciudad B", "2023-07-20", 100)
    vuelo2 = Vuelo("V002", "Ciudad B", "Ciudad C", "2023-07-22", 120)

    pasajero1 = Pasajero("Juan", "Pérez", "12345678")
    pasajero2 = Pasajero("María", "Gómez", "87654321")

    reserva = Reserva()
    reserva.agregar_vuelo(vuelo1)
    reserva.agregar_vuelo(vuelo2)

    vuelos_encontrados = reserva.buscar_vuelo("Ciudad B", "Ciudad C", "2023-07-22")
    for vuelo in vuelos_encontrados:
        print(vuelo)

    vuelo_seleccionado = vuelos_encontrados[0]
    vuelo_seleccionado.mostrar_asientos_disponibles()

    vuelo_seleccionado.reservar_asiento(1, pasajero1)
    vuelo_seleccionado.reservar_asiento(2, pasajero2)
    vuelo_seleccionado.mostrar_asientos_disponibles()
