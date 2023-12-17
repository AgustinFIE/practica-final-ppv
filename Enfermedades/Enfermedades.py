from datetime import date, timedelta


class Persona:
    def __init__(self, nombre, temperatura, celulas):
        self.nombre = nombre
        self.temperatura = temperatura
        self.celulas = celulas
        self.enfermedades = []

    def __str__(self):
        return f"{self.nombre}\n - Temperatura: {self.temperatura}\n - Celulas: {self.celulas}\n"

    def contraerEnfermedad(self, enfermedad):
        self.enfermedades.append(enfermedad)

    def tomarMedicamento(self, cantidadMedicamento):
        for enfermedad in self.enfermedades:
            enfermedad.atenuar(cantidadMedicamento * 15)

    def curarPorCompleto(self, dosis):
        self.temperatura = 36.2  # Vuelve a su temperatura normal
        for enfermedad in self.enfermedades:
            while enfermedad.celulasAmenazadas != 0:
                self.tomarMedicamento(dosis)

    def estado(self):
        return list(filter(lambda enfermedad: enfermedad.celulasAmenazadas != 0, self.enfermedades))

    def pasarTiempo(self, cantDias):
        cantDias = cantDias.days
        for x in range(cantDias):
            for enfermedad in self.enfermedades:
                enfermedad.estado(self)

    # Funcion que unicamente muestra por pantalla
    def mostrarEstado(self):
        if len(self.estado()) == 0:
            return f"{self.nombre} esta sano!!\n"
        else:
            return f"{self.nombre} esta enfermo, tiene: {self.estado()}\n"


class Enfermedad():
    def __init__(self, nombreEnfermedad, celulasAmenazadas):
        self.nombreEnfermedad = nombreEnfermedad
        self.celulasAmenazadas = celulasAmenazadas

    def __repr__(self):
        return self.nombreEnfermedad

    def atenuar(self, atenuacion):
        self.celulasAmenazadas = self.celulasAmenazadas - atenuacion
        if self.celulasAmenazadas < 0:  # Si las "curo de mas", no pueden ser negativas
            self.celulasAmenazadas = 0

    def estado(self, persona): pass  # Lo necesito para la herencia multiple


class Infecciosa(Enfermedad):
    def estado(self, persona):
        super(Infecciosa, self).estado(persona)  # Lo necesito para la herencia multiple
        persona.temperatura += self.celulasAmenazadas / 1000
        self.celulasAmenazadas = self.celulasAmenazadas * 2


class Autoinmune(Enfermedad):
    def estado(self, persona):
        super(Autoinmune, self).estado(persona)  # Lo necesito para la herencia multiple
        persona.celulas -= self.celulasAmenazadas / 1000


class InfecciosaYAutoinmune(Infecciosa, Autoinmune):
    def estado(self, persona):
        super(InfecciosaYAutoinmune, self).estado(persona)


"""
Lo puedo hacer tambien por composicion, pero fui con herencia multiple

Aca venia el problema, si solo uso super(), heredo el metodo estado de UNA SOLA de las clases, no de las dos.
Tiene que usarse el metodo de forma constante, si las clases bases no utilizan super(), no funciona en los que heredan
Tengo que armar una "cadena" de super(), incluyendo la clase Base Enfermedad

https://stackoverflow.com/questions/3810410/python-multiple-inheritance-from-different-paths-with-same-method-name
"""

# PRUEBAS

malaria = Infecciosa("Malaria", 5000)
lupus = Autoinmune("Lupus", 10000)

"""
1. Hacer que una persona contraiga malaria y lupus, y que dicha persona 
viva un día de su vida para que las enfermedades hagan su efecto.
"""

persona = Persona("Juancito", 36.4, 3000000)  # 3M
persona.contraerEnfermedad(malaria)
persona.contraerEnfermedad(lupus)

# Para practicar date

fechaActual = date.today()
fechaSiguiente = date.today() + timedelta(days=1)  # Hago que pase un dia, o los que sean necesarios

print("Punto 1)")

print(persona)
persona.pasarTiempo(fechaSiguiente - fechaActual)
print(persona)

"""
2. Hacer que dicha malaria se atenúe en 5000 y el lupus en 500
Preguntar si la persona está sana.
"""

malaria.atenuar(5000)
lupus.atenuar(500)

print("\nPunto 2)")
print(persona.mostrarEstado())

"""
3. Hacer que la persona reciba una dosis de 300 ml de un medicamento 
las veces que haga falta hasta quedar sana.
"""

print("Punto 3)")

# Le paso la cantidad de medicamento que consume, y la funcion la aplica las veces necesarias

persona.curarPorCompleto(300)
print(persona.mostrarEstado())

"""
4. Modelar una enfermedad que sea tanto infecciosa como autoinmune.
"""

print("Punto 4)")

virusX = InfecciosaYAutoinmune("VirusX", 8000)
persona.enfermedades.append(virusX)

print(persona)
persona.pasarTiempo(fechaSiguiente - fechaActual)  # Sigue siendo 1 dia
print(persona.mostrarEstado())
print(persona)
