"""Implementación de un sistema de gestión de inventario:
Crea un sistema de gestión de inventario para una tienda, donde se puedan agregar productos, controlar el stock,
realizar ventas y generar informes de ventas. Utiliza clases como "Producto", "Inventario" y "Venta" 
para representar el sistema y utiliza métodos para gestionar las operaciones."""
#--------------------------------- Diccionarios ----------------------------------------
Valor_Producto = {}
Cantidad_Producto = {}
Dinero_Recibido_Ventas = {}
Producto_Vendido = {}

class Inventario:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\n--- Menú de Inventario ---")
            print("1. Agregar producto")
            print("2. Vender producto")
            print("3. Generar informe de ventas")
            print("4. Generar informe de stock")
            print("5. Actualizar informacion del producto")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.nuevo_Producto()
            elif opcion == "2":
                self.vender_producto()
            elif opcion == "3":
                self.informe_ventas()
            elif opcion == "4":
                self.informe_stock()
            elif opcion == "5":
                self.actualizar_producto()
            elif opcion == "0":
                print("SALIENDO DEL PROGRAMA.....")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def nuevo_Producto(self):
        nom = input("DIGITE EL NOMBRE DEL PRODUCTO: ")
        valor = int(input("DIGITE EL VALOR DEL PRODUCTO: "))
        cantidad = int(input("DIGITE LA CANTIDAD EN STOCK: "))

        Valor_Producto[nom] = valor
        Cantidad_Producto[nom] = cantidad

    def vender_producto(self):
        producto_vender = Venta(None,None,None)
        producto_vender.vender()

    def informe_ventas(self):
        TotalVenta = 0
        print("                              INFORME DE VENTAS")
        print(" ")
        print("NOMBRE PRODUCTO               CANTIDAD VENDIDA              VALOR DE VENTA")
        print("================================================================================")
        for key,value in Producto_Vendido.items():

            Valor_venta = Dinero_Recibido_Ventas[key]
            TotalVenta += Valor_venta

            print(f"{key}                         {value}                   {Valor_venta:,.2f}  ")
        print(f"                                              TOTAL VALOR VENDIDO: {TotalVenta:,.2f}")

    def informe_stock(self):
        print("              INFORME DEL STOCK")
        print(" ")
        print("NOMBRE PRODUCTO               CANTIDAD EN STOCK              ")
        print("===================================================")
        for key,value in Cantidad_Producto.items():
            print(f"{key}                         {value}")

#------------------------------------ Metodo adicional -------------------------------------------
    def actualizar_producto(self):
        nom3 = input("INGRESE EL NOMBRE DEL PRODUCTO AL QUE SE LE QUIERE ACTUALIZAR LA INFORMACION: ")
        if nom3 not in Cantidad_Producto:
            print("El producto ingresado no está en el inventario.")
        else:
            for key in Cantidad_Producto:
                if key == nom3:
                        actualizar_stock = int(input("DIGITE EL NUEVO STOCK DEL PRODUCTO: "))
                        actualizar_valor = int(input("DIGITE EL NUEVO VALOR DEL PRODUCTO: "))

                        Cantidad_Producto[key] = actualizar_stock
                        Valor_Producto[key] = actualizar_valor 
#------------------------------------ Clases producto y venta ---------------------------------------------
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Venta(Producto):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre, precio, stock)

    def vender(self):
        nom2 = input("INGRESE EL NOMBRE DEL PRODUCTO A VENDER: ")

        if nom2 not in Cantidad_Producto:
            print("El producto ingresado no está en el inventario.")
        else:
            for key,value in Cantidad_Producto.items():
                if key == nom2:
                    stock2 = int(input("INGRESE LA CANTIDAD A VENDER: "))
                    if value >= stock2:
                        nuevo_stock = value - stock2
                        Cantidad_Producto[key] = nuevo_stock

                        costo_producto = Valor_Producto[key]
                        valor_venta = stock2 * costo_producto

                        Dinero_Recibido_Ventas[key] = valor_venta
                        Producto_Vendido[key] = stock2
                    elif value < stock2:
                        print("No es posible realizar la venta puesto que la cantida excede al stock")
            
#----------------------------------------- Objetos de la clase inventario ------------------------------
inventario1 = Inventario()