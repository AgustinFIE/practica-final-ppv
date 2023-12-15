from datetime import date

class Proyecto():
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.tareas = []

    def actividad(self, fechaDesde, fechaHasta):
        provincias = []
        for tarea in self.tareas:
            if fechaDesde < tarea.fecha < fechaHasta and (tarea.ubicacion).provincia not in provincias:
                provincias.append((tarea.ubicacion).provincia)
        return provincias

    def superficiePromedio(self):
        superficieTotal = 0
        cantTareas = 0
        for tarea in self.tareas:
            superficieTotal += tarea.ubicacion.calcularSuperficie()
            cantTareas += 1
        return superficieTotal/cantTareas

    def saldoActual(self, fechaActual):
        for tarea in self.tareas:
            self.presupuesto = tarea.costoTarea(fechaActual, self.presupuesto)
        return self.presupuesto

class Tarea():
    def __init__(self, ubicacion, fecha):
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.dependencias = []

    def margenAnterior(self):
        ultimaTarea = max(self.dependencias, key=lambda dependencia: dependencia.fecha)
        return self.fecha - ultimaTarea.fecha


class TareaProduccion(Tarea):
    def __init__(self, ubicacion, fecha, servicio):
        super().__init__(ubicacion, fecha)
        self.servicios = servicio

    def costoTarea(self, fechaActual, presupuesto):
        if self.fecha < fechaActual:                    # Ya paso la tarea, se cobra
            for servicio in self.servicios:
                presupuesto -= servicio.monto
        return presupuesto

class TareaRecaudacion(Tarea):
    def __init__(self, ubicacion, fecha, ingreso):
        super().__init__(ubicacion, fecha)
        self.ingreso = ingreso

    def costoTarea(self, fechaActual, presupuesto):
        if self.fecha < fechaActual:
            return presupuesto + self.ingreso

class TareaReunion(Tarea):
    def __init__(self, ubicacion, fecha):
        super().__init__(ubicacion, fecha)

    def costoTarea(self, fechaActual, presupuesto):
        return presupuesto

# ----- Clases para ubicar al proyecto -----

class Oficina():
    superficie = 100 # Lo mismo para todas (100 m2)

    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.provincia = ciudad.provincia

    def calcularSuperficie(self):
        return self.superficie

class Ciudad():
    def __init__(self, provincia, superficie):
        self.provincia = provincia
        self.superficie = superficie

    def calcularSuperficie(self):
        return self.superficie

class ZonaRural():
    def __init__(self, provincia, ancho, largo):
        self.provincia = provincia
        self.ancho = ancho
        self.largo = largo

    def calcularSuperficie(self):
        return self.ancho * self.largo

# ----- Clase Servicio -----

class Servicio():
    def  __init__(self, monto):
        self.monto = monto

    def calcularMonto(self):
        return self.monto

# ----- PRUEBAS -----

proyectoFinal = Proyecto(10000)

# Servicios

limpieza = Servicio(25)
seguridad = Servicio(50)

# Las ubicaciones

zonaRural = ZonaRural("Chubut", 80, 50)
ciudad1 = Ciudad("BuenosAires", 500)
ciudad2 = Ciudad("Chubut", 500)
ciudad3 = Ciudad("Cordoba", 500)
oficina = Oficina(ciudad1)

tarea1 = TareaProduccion(ciudad1,  date(2022, 3, 28), [limpieza, seguridad])    # Provincia: BsAs
tarea2 = TareaProduccion(zonaRural,  date(2022, 3, 22), [limpieza])             # Provincia: Chubut
tarea3 = TareaReunion(ciudad2, date(2022, 3, 20))                               # Provincia: Chubut
# (se repite a proposito, no tiene que aparecer duplicados en lista)
tarea4 = TareaReunion(ciudad3, date(2022, 4, 20))   # Esta no tiene que figurar en la lista de abajo por la fecha (Cordoba)

proyectoFinal.tareas.extend([tarea1, tarea2, tarea3, tarea4])

# PUNTO 1

print(proyectoFinal.actividad(date(2022, 1, 1), date(2022, 3, 29))) # Solo BsAs y Chubut

# PUNTO 2

print(proyectoFinal.superficiePromedio())   # tarea1 (500) + tarea2 (80*50=4000) + tarea3 (500) + tarea4 (500)
# Total 5500 / 4 = 1375

# PUNTO 3

print(proyectoFinal.saldoActual(date(2022, 10, 30))) # Abarca todas las tareas
# Inicial: 10000 - tarea1(50+25=75) - tarea2(25) - tarea3(0) - tarea4(0) = 9900

# PUNTO 5 - Saber si es coherente; es coherente si pueden hacerse todas las tareas en la fecha indicada


# PUNTO 6

tarea10 = TareaReunion(ciudad3, date(2022, 4, 30))   # Tiene un margen de 5 dias

tarea11 = TareaReunion(ciudad3, date(2022, 4, 25))
tarea12 = TareaReunion(ciudad3, date(2022, 4, 22))

tarea10.dependencias.extend([tarea11, tarea12])

print(tarea10.margenAnterior())                     # 5 dias

# print(fecha222 - fecha111)
# delta = fecha222 - fecha111
# print(delta.days)

