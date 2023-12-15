class Inmobiliaria():
    def __init__(self):
        self.agentes = []

    def mejorAgente(self):
        agenteMejorTrabaja = None
        maxComision = None
        for persona in self.agentes:
            if (maxComision is None or persona.calcularMontoTotal() > maxComision):
                maxComision = persona.calcularMontoTotal()
                agenteMejorTrabaja = persona
        return agenteMejorTrabaja

    def mostrarConflictivos(self, inmueble):
        mostrar = []
        for persona in self.agentes:
            for operacion in persona.operaciones:
               if operacion.inmueble == inmueble:
                   mostrar.append(str(persona))
                   persona.conflicto = 1
        print("El personal", *mostrar, "tiene problemas con el Inmueble", type(inmueble).__name__) #Como los inmuebles no tienen nombre, solo los nombro

    def conflictosPersonal(self):
        noRepetido = []
        repetido = []
        for persona in self.agentes:
            for operacion in persona.operaciones:
                if operacion.inmueble not in noRepetido:
                    noRepetido.append(operacion.inmueble)
                else:
                    repetido.append(operacion.inmueble)
                    self.mostrarConflictivos(operacion.inmueble)

    def renovarPersonal(self):
        for persona in self.agentes:
            if persona.conflicto == 1:   # Esta peleado
                pass
            else:
                return ("No necesita renovar Personal")  #Se portaron bien
        self.agentes = [] #Hechamos a todos
        return ("Renovamos TODO el personal")


class Inmueble():
    def __init__(self, cantAmb, metros):
        self.cantAmb = cantAmb
        self.metros = metros

class Casa(Inmueble):
    def __init__(self, cantAmb, metros, valor):
        super().__init__(cantAmb, metros)
        self.valor = valor

    def valorInmueble(self):
        return self.valor

class PH(Inmueble):
    def valorInmueble(self):
        valorph = self.metros * 4000
        if valorph < 50000:
            return 50000
        else:
            return valorph

class Departamento(Inmueble):
    def valorInmueble(self):
        return 35000 * self.cantAmb

class Agente():
    def __init__(self, nombre):
        self.nombre = nombre
        self.conflicto = 0
        self.operaciones = []

    def __str__(self):
        return self.nombre

    def calcularMontoTotal(self):
        total = 0
        for inmueble in self.operaciones:
            total += inmueble.comision()
        return total

class Venta():
    porcentaje = 0.01

    def __init__(self, inmueble, nomCliente):
        self.inmueble = inmueble
        self.nombCliente = nomCliente

    def comision(self):
        return self.inmueble.valorInmueble() * self.porcentaje

class Alquiler(Venta):
    def __init__(self, inmueble, nomCliente, meses):
        super().__init__(inmueble, nomCliente)
        self.meses = meses

    def comision(self):
        return self.inmueble.valorInmueble() / 5000 * self.meses


# ****************** PRUEBAS ******************

# declaro variables que utilizare en el ejercicio

agente1 = Agente("Fulano")
agente2 = Agente("Jaimito")
agente3 = Agente("Mengano")

InmobiliariaMaduro = Inmobiliaria()
InmobiliariaMaduro.agentes.extend([agente1, agente2, agente3])

# 1. Saber cual es el precion de una operacion venta o alquiler

casa1 = Casa(4, 50, 20000)
venta1 = Venta(casa1, "Jorge")

PH1 = PH(3, 40)
alquiler1 = Alquiler(PH1, "Agustin", 12)

print("Punto 1)\n")
print(f"Costo de la comision venta: {venta1.comision()}")
print(f"Costo de la comision alquiler: {alquiler1.comision()}")


# 2. Saber cual fue el agente que mejor trabaja según el monto toal de las comisiones que le corresponden por las operaciones
print("\nPunto 2)\n")

# Inmuebles:
# casa1 = Casa(4, 50, 2000)
# PH1 = PH(2, 25)
casa2 = Casa(2, 20, 10000)
depto1 = Departamento(2, 25)

# Operaciones
# venta1 = Venta(casa1, "Jorge")
# alquiler1 = Alquiler(PH1, "Agustin", 2)
venta2 = Venta(casa2, "Pablo")
venta3 = Venta(depto1, "Juan")

agente1.operaciones.extend([venta1, alquiler1])
agente2.operaciones.extend([venta2, venta3])

print(f"{agente1.nombre}: {agente1.calcularMontoTotal()}, {agente2.nombre}: {agente2.calcularMontoTotal()}, "
      f"{agente3.nombre}: {agente3.calcularMontoTotal()}")
print("Mejor agente:", InmobiliariaMaduro.mejorAgente())

# 3.a Saber si un agente tiene problemas con otro. Se cumple si ambos operan en el mismo inmueble
print("\nPunto 3.a)\n")

# Generamos conflicto

alquiler2 = Alquiler(casa1, "Martin", 24) #Misma Casa!!!
agente3.operaciones.append(alquiler2)

InmobiliariaMaduro.conflictosPersonal() #Muestro los conflictos del Personal

# 3.b Saber si la inmobiliaria necesita renovar el personal, cuando todos los agentes tienen problemas con algun otro
print("\nPunto 3.b)\n")

print("Antes del conflicto:", InmobiliariaMaduro.renovarPersonal(), "\n")

# Fuerzo a que se peleen todos!!

venta4 = Venta(casa2, "Marcos")
agente3.operaciones.append(venta4)

# Muestro los conflictos

InmobiliariaMaduro.conflictosPersonal()
print("\nDespues del conflicto:", InmobiliariaMaduro.renovarPersonal(), InmobiliariaMaduro.agentes)