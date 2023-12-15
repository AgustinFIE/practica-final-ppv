from datetime import date

class Empresa():
    def __init__(self):
        self.envios = []

    def envioInternacional(self):
        return list(filter(lambda envio: (envio.origen[1] != envio.destino[1]), self.envios))  # Ahora si usando filter

    def propicioPerderse(self): #Como son objetos, guardo un objeto tipo Envio
        envioPerdido = None
        for envio in self.envios:
            if (envioPerdido is None or envio.calcularPrecioBruto() < envioPerdido.calcularPrecioBruto()):
                envioPerdido = envio
        return envioPerdido

class Envio():
    recargos = []
    impuestos = []

    def __init__(self, origen, destino, peso, precioBase, categoria):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.precioBase = precioBase
        self.categoria = categoria      # Lista de objetos

    def __repr__(self):
        return str(self.__dict__)   # Funcion para mostrar los envios con todos sus atributos

    def calcularPrecioNeto(self):       # Correccion: precioBruto y Neto los tengo que calcular por un metodo
        precioNeto = self.precioBase
        for cadaRecargo in self.recargos:
            precioNeto = cadaRecargo.calcularRecargo(self, precioNeto)
        return precioNeto

    def calcularPrecioBruto(self):
        precioBruto = self.calcularPrecioNeto()
        for cadaImpuesto in self.impuestos:
            precioBruto = cadaImpuesto.calcularImpuesto(self, precioBruto)
        return precioBruto

# RECARGOS

class RecargoCategorico:
    def calcularRecargo(self, envio, precioNeto):
        for categ in envio.categoria:
            precioNeto += categ.calcularRecargo(envio)
        return precioNeto

class RecargoSobrepeso:
    def calcularRecargo(self, envio, precioNeto):
        if envio.peso > 1:
            precioNeto += 80
        return precioNeto

class RecargoArbitrario:
    def calcularRecargo(self, envio, precioNeto):
        diaDelCorreo = date(2022, 9, 27)
        fechaHoy = date.today()
        if fechaHoy == diaDelCorreo:
            precioNeto += 50
        return precioNeto

# IMPUESTOS

class ImpuestoIVA:
    def calcularImpuesto(self, envio, precioBruto):
        precioBruto += envio.calcularPrecioNeto() * 0.20
        return precioBruto

class ImpuestoMulticategoria:
    def calcularImpuesto(self, envio, precioBruto):
        if len(envio.categoria) > 3:
            precioBruto += envio.calcularPrecioNeto() * 0.01
        return precioBruto

class ImpuestoAduanero:
    def calcularImpuesto(self, envio, precioBruto):
        if envio.origen[1] != envio.destino[1]:
            precioBruto += envio.calcularPrecioNeto() * 0.5
        return precioBruto

class ImpuestoExtranio:
    def calcularImpuesto(self, envio, precioBruto):
        if envio.precioBase % 2 == 0:
            precioBruto += envio.calcularPrecioNeto() * 0.10
        return precioBruto

class ImpuestoMunicipal: #Mismo pais y misma ciudad
    def calcularImpuesto(self, envio, precioBruto):
        if envio.origen[0] == envio.destino[0] and envio.origen[1] == envio.destino[1]:
            precioBruto += envio.calcularPrecioNeto() * 0.05
        return precioBruto

# Junto las categorias en una sola clase para reutilizar el codigo

class Categoria:
    def __init__(self, porcentajeCategoria):
        self.porcentaje = porcentajeCategoria

    def calcularRecargo(self, envio):
        return envio.precioBase * self.porcentaje


# Primero creo todas las categorias que necesite, cada una con su comportamiento

tecnologia = Categoria(0.10)
arte = Categoria(0.20)
libros = Categoria(0.05)
musica = Categoria(0.15)

# Lo mismo con los recargos e impuestos

recCat = RecargoCategorico()
recSob = RecargoSobrepeso()
recArb = RecargoArbitrario()

iva = ImpuestoIVA()
iMulticategoria = ImpuestoMulticategoria()
iAduanero = ImpuestoAduanero()
iExtranio = ImpuestoExtranio()

# Los añado en una lista, para poder agregar y quitar elementos
Envio.impuestos.extend([iva, iMulticategoria, iAduanero, iExtranio])
Envio.recargos.extend([recCat, recSob, recArb])

FedeX = Empresa()

envio1 = Envio(("BsAs", "Argentina"), ("Cordoba", "Argentina"), 10, 2500, [tecnologia, arte])
envio2 = Envio(("BsAs", "Argentina"), ("Santiago", "Chile"), 2, 1000, [tecnologia])
envio3 = Envio(("BsAs", "Argentina"), ("Lisboa", "Portugal"), 5, 5000, [arte])

FedeX.envios.extend([envio1, envio2, envio3])

print("Punto 1)\n")

print(FedeX.envioInternacional())

print("\nPunto 2)\n")
"""Averiguar precio neto de envío con origen California, Estados Unidos y con destino
Miami, Estado Unidos, de 5kg de peso, precio base $1500, con categoría de libros."""

# Creo el envio
envio4 = Envio(("California", "EstadosUnidos"), ("Miami", "EstadosUnidos"), 5, 1500, [libros])

print(f"Precio Base: {envio4.precioBase}, Precio Neto: {envio4.calcularPrecioNeto()}")

print("\nPunto 3)\n")
"""veriguar precio bruto (final) de envío con origen en Buenos Aires, Argentina y con
destino Utrecht, Países Bajos, de 2kg de peso, precio base de $220, con las
categorías de música, arte y tecnología"""

envio5 = Envio(("BsAs", "Argentina"), ("Utrecht", "PaisesBajos"), 2, 220, [musica, arte, tecnologia])

print(f"Precio Base: {envio5.precioBase}, Precio Neto: {envio5.calcularPrecioNeto()}, "
      f"Precio Bruto: {round(envio5.calcularPrecioBruto(), 2)}")

print("\nPunto 4)\n")
"""Obtener el envío “propicio a perderse” (tiene el precio bruto más barato de todos)."""

FedeX.envios.extend([envio3, envio5])
print(f"El envio propicio a perderse es: {FedeX.propicioPerderse().origen},{FedeX.propicioPerderse().destino} "
      f"con un precioBruto de: {round(FedeX.propicioPerderse().calcularPrecioBruto(), 2)}")

print("\nPunto 5)\n")
"""
Modificar la configuración del sistema quitando el “Impuesto Extraño” y “Recargo
Arbitrario” y agregando el “Impuesto Municipal” de 5% que afecta a los envíos cuyo
origen y destino tengan el mismo país y ciudad.
"""

Envio.recargos.remove(recArb)
Envio.impuestos.remove(iExtranio)

iMunicipal = ImpuestoMunicipal()

Envio.impuestos.append(iMunicipal)

print(type(Envio.impuestos[3]).__name__)

