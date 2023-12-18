class Cliente:

    def __init__(self, nombre_apellido, dni, tarjeta, efectivo):
        self.nombre_apellido = nombre_apellido
        self.dni = dni
        self.tarjeta = tarjeta          # Tarjeta de credito
        self.efectivo = efectivo        # Efectivo disponible
        self.productos = []             # Lista de productos comprados vacia
        self.preferencia = "tarjeta"    # Por defecto, prefiere pagar con tarjeta

    def pagar(self, producto):
        if self.preferencia == "tarjeta" and self.tarjeta.puede_pagar(producto.precio):
            self.tarjeta.pagar(producto.precio)
            return True
        elif self.efectivo.puede_pagar(producto.precio):
            self.efectivo.pagar(producto.precio)
            return True
        return False

    def comprar(self, producto):
        if self.pagar(producto):
            self.productos.append(producto)

class Producto:
    def __init__(self, precio):
        self.precio = precio

class FormaDePago:
    def __init__(self, disponible):
        self.disponible = disponible
    def pagar(self, plata):
        pass
    def puede_pagar(self, plata):
        pass

class Efectivo(FormaDePago):
    def pagar(self, plata):
        self.disponible -= plata

    def puede_pagar(self, plata):
        return self.disponible >= plata


class Tarjeta(FormaDePago):
    def __init__(self, disponible, limite_maximo, gastado):
        super().__init__(disponible)
        self.limite_maximo = limite_maximo
        self.gastado = gastado

    def pagar(self, plata):
        self.disponible -= plata
        self.gastado += plata

    def puede_pagar(self, plata):
        return self.disponible >= plata and self.limite_maximo >= self.gastado + plata


# Create a Tarjeta with a limit of 100 and no initial expenditure
tarjeta = Tarjeta(100, 100, 0)

# Create an Efectivo with 50 available
efectivo = Efectivo(50)

# Create a Cliente with the Tarjeta and Efectivo
cliente = Cliente("John Doe", "12345678", tarjeta, efectivo)

# Create a Producto with a price of 30
producto1 = Producto(30)

# The client buys the product
cliente.pagar(producto1)

# Print the remaining balance on the card and in cash
print(f"Remaining card balance: {cliente.tarjeta.disponible}")
print(f"Remaining cash: {cliente.efectivo.disponible}")

# Create another Producto with a price of 90
producto2 = Producto(90)

# The client attempts to buy the second product, not allow
cliente.pagar(producto2)

# Print the remaining balance on the card and in cash
print(f"Remaining card balance: {cliente.tarjeta.disponible}")
print(f"Remaining cash: {cliente.efectivo.disponible}")