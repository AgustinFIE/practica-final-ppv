
class Peaje():
    def __init__(self, nombre):
        self.nombre = nombre
        self.actividad = []
        self.clientes = []

    def cobrar(self, vehiculo):
        self.actividad.append(vehiculo)
        if vehiculo not in self.clientes:
            self.clientes.append(vehiculo)
        return vehiculo.formaDePago.calcularCobro(vehiculo)

    def recaudacionTotal(self):
        total = 0
        for vehiculo in self.actividad:
            # Si uso la funcion cobrar, como anado a la lista de actividad cada vez que se cobra, entraria en un loop
            # por eso uso la funcion del vehiculo, calcularCobro
            total += vehiculo.formaDePago.calcularCobro(vehiculo)
        return total

    def totalVehiculo(self, vehiculoTotal): # Funcion que calcula el total segun la patente del vehiculo (ver de hacerla con filter)
        subtotal = 0
        for vehiculo in self.actividad:
            if vehiculo == vehiculoTotal:
                subtotal += vehiculo.formaDePago.calcularCobro(vehiculo)
        return subtotal

    def mejorCliente(self): # la tengo que hacer con max
        print(max(self.clientes, key=lambda vehiculo: self.totalVehiculo(vehiculo)))
        return 1
        # mejorClient = None
        # for vehiculo in self.clientes:
        #     if mejorClient is None or self.totalVehiculo(mejorClient) < self.totalVehiculo(vehiculo):
        #         mejorClient = vehiculo
        # return mejorClient

class Vehiculo:
    def __init__(self, patente, formaDePago):
        self.patente = patente
        self.formaDePago = formaDePago

    def __str__(self):
        return self.patente

    def calcularTarifa(self): pass

# TIPOS  VEHICULOS

class Auto(Vehiculo):
    valorAuto = 100
    def calcularTarifa(self):
        return self.valorAuto

class Moto(Auto):
    def calcularTarifa(self):
        return self.valorAuto / 2

class AutoElectrico(Auto):
    def calcularTarifa(self):
        return self.valorAuto * 0.2 # 20% del valor del auto

class Camion(Vehiculo):
    def __init__(self, patente, formaDepago, ejes):
        super().__init__(patente, formaDepago)
        self.ejes = ejes

    def calcularTarifa(self):
        return 200 * self.ejes

class AutoGubernamental(Vehiculo):
    def calcularTarifa(self):
        return 0

# FORMAS DE PAGO

class PagoTelepase:
    def calcularCobro(self, vehiculo):
        return vehiculo.calcularTarifa() * 0.5

class PagoSube:
    def calcularCobro(self, vehiculo):
        return vehiculo.calcularTarifa() * 0.7

class PagoEfectivo:
    def calcularCobro(self, vehiculo):
        return vehiculo.calcularTarifa()


# ************************ PRUEBAS ************************

peaje = Peaje("Peaje")

# Formas de pago
sube = PagoSube()
telepase = PagoTelepase()
efectivo = PagoEfectivo()

# Vehiculos
auto = Auto("AU 234 TO", formaDePago=sube)
moto = Moto("MO 789 TO", formaDePago=efectivo)
camion = Camion("CA 710 NN", ejes=3, formaDepago=telepase)

# *** PUNTO 1 ***

print("Punto 1)")
print(f"[{auto.patente}] total a cobrar: {peaje.cobrar(auto)}")       # Cobrar a un auto con SUBE       - 70
print(f"[{moto.patente}] total a cobrar: {peaje.cobrar(moto)}")       # Cobrar a una moto en efectivo   - 50
print(f"[{camion.patente}] total a cobrar: {peaje.cobrar(camion)}")   # Cobrar a un camion con telepase - 300

# *** PUNTO 2 ***
# Calcular el valor de recaudacion total de los peajes

print("\nPunto 2)")
print(f"Recaudacion total: {peaje.recaudacionTotal()}")   # Resultado esperado 300+50+70 = 420

# *** PUNTO 3 ***
# Encontrar la patente del mejor cliente, aquel que más gasto en los peajes

print("\nPunto 3)")

peaje.cobrar(auto)      # Le sumo +70 * 4 al auto
peaje.cobrar(auto)
peaje.cobrar(auto)
peaje.cobrar(camion)
peaje.cobrar(auto)      # En este punto el auto suma un total de 350

# Para verificar:
print(f"[{auto.patente}] - {peaje.totalVehiculo(auto)}")
print(f"[{moto.patente}] - {peaje.totalVehiculo(moto)}")
print(f"[{camion.patente}] - {peaje.totalVehiculo(camion)}")

print(f"El mejor cliente es - {peaje.mejorCliente()}")

# *** PUNTO 4 ***

autoElec = AutoElectrico("EL 327 IC", formaDePago=efectivo)
autoVip = AutoGubernamental("GO 777 BR", formaDePago=telepase)

print("\nPunto 3)")

# Como paga en efectivo (100) se le cobra el 100%, se aplica el 20% por ser electrico... total a cobrar 20
print(f"[{autoElec.patente}] total a cobrar: {peaje.cobrar(autoElec)}")

# No paga nada el auto gubernamental
print(f"[{autoVip.patente}] total a cobrar: {peaje.cobrar(autoVip)}")


