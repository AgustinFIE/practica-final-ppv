class Pasaje:
    def __init__(self, cliente):
        self.cl = cliente

    def precio(self):
        return self.cl.calcular_precio()

class PasajeInvierno(Pasaje):
    def precio(self):
        return super().precio() * 0.90

class Cliente:
    def calcular_precio(self):
        return 500

class Turista(Cliente):
    pass

class TuristaEst(Cliente):
    def calcular_precio(self):
        return super().calcular_precio() * 0.7

class Business(Cliente):
    def calcular_precio(self):
        return super().calcular_precio() * 1.50

class BusinessEst(Business, TuristaEst):
    pass

# class BusinessEst(Cliente):
#     def calcular_precio(self):
#         return super().calcular_precio() * 1.5 * 0.7

class Premiun(Business):
    def calcular_precio(self):
        return super().calcular_precio() + 200


# Create a Turista
turista = Turista()
print(f"Turista price: {turista.calcular_precio()}")

# Create a TuristaEst
turista_est = TuristaEst()
print(f"TuristaEst price: {turista_est.calcular_precio()}")

# Create a Business
business = Business()
print(f"Business price: {business.calcular_precio()}")

# Create a BusinessEst
business_est = BusinessEst()
print(f"BusinessEst price: {business_est.calcular_precio()}")

# Create a Premium
premium = Premiun()
print(f"Premium price: {premium.calcular_precio()}")

# Ejemplo de Uso
un_pasaje = Pasaje(TuristaEst())
print(f"Precio pasaje TuristaEst: {un_pasaje.precio()}")

# Create a PasajeInvierno with a Turista
turista = Turista()
pasaje_invierno_turista = PasajeInvierno(turista)
print(f"PasajeInvierno with Turista price: {pasaje_invierno_turista.precio()}")