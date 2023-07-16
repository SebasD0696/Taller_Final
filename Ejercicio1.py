"""Desarrollo de un sistema de gestión de una biblioteca:
Crea un sistema de gestión de una biblioteca que incluya clases como "Libro", "Autor" y "Biblioteca". 
Implementa métodos para agregar libros, buscar libros por autor, prestar libros a usuarios y llevar un 
registro de los libros prestados."""

#--------------------------------- Diccionarios ----------------------------------------
autor_libro = {}
genero_libro = {}
libros_prestados = {}
usuarios = {}

class Biblioteca:
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
                self.agregar_libro()
            elif opcion == "2":
                self.buscar_libros_autor()
            elif opcion == "3":
                self.prestar_libros()
            elif opcion == "4":
                self.informe_libros_prestados()
            elif opcion == "5":
                self.buscar_libros_genero()
            elif opcion == "0":
                print("SALIENDO DEL PROGRAMA.....")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def agregar_libro(self):
        Libro_agregar = Libro()
        Libro_agregar.agregar_libro()

    def buscar_libros_autor(self):
        nom1 = input("INGRESE EL NOMBRE DEL AUTOR: ")
        if nom1 not in autor_libro.values():
            print("El autor ingresado no tiene libros en nuestra biblioteca.")
        else:
            print("====================================")
            print(f"    Libros del autor: {nom1} ")
            print("====================================")
            for key,value in autor_libro.items():
                if value == nom1:
                    print(f"- {key}")

    def prestar_libros(self):
        usuario = input("INGRESE EL NOMBRE DEL USUARIO: ")
        nom2 = input("INGRESE EL NOMBRE DEL LIBRO: ")
        if nom2 not in autor_libro:
            print("El autor ingresado no tiene libros en nuestra biblioteca.")
        else:
            for key,value in libros_prestados.items():
                if key == nom2:
                    if value == True:
                        print(f"EL Libro: {nom2} fue prestado a {usuario}")
                        libros_prestados[key] = False
                        usuarios[key] = usuario
                    else:
                        print("EL LIBRO YA FUE PRESTADO")

    def informe_libros_prestados(self):
        print("      INFORME DE LOS LIBROS PRESTADOS              ")
        print(" ")
        print("NOMBRE LIBRO                    USUARIO ")
        print("===================================================")
        for key,value in usuarios.items():
            print(f"{key}                       {value}")

#------------------------------------ Metodo adicional -------------------------------------------
    def buscar_libros_genero(self):
        gen = input("INGRESE EL GENERO A BUSCAR: ")
        if gen not in genero_libro.values():
            print("La biblioteca no posee libros de dicho genero.")
        else:
            print("====================================")
            print(f"    Libros del genero: {gen} ")
            print("====================================")
            for key,value in genero_libro.items():
                if value == gen:
                    print(f"- {key}")
#------------------------------------ Clases autor y libro ---------------------------------------------
class Autor:
    def _init_(self,nombre_autor):
        self.nombre_autor = nombre_autor

class Libro(Autor):
    def _init_(self, nombre_autor, nombre_libro, genero):
        super()._init_(nombre_autor)
        self.nombre_libro = nombre_libro
        self.genero = genero
    
    def agregar_libro(self):
        nombre = input("DIGITE EL NOMBRE DEL LIBRO: ")
        autor = input("DIGITE EL NOMBRE DEL AUTOR: ")
        genero = input("DIGITE EL GENERO DEL LIBRO: ")

        autor_libro[nombre] = autor
        genero_libro[nombre] = genero
        libros_prestados[nombre] = True
        
#----------------------------------------- Objetos de la clase biblioteca ------------------------------
Biblioteca1 = Biblioteca()
Biblioteca1.menu()
