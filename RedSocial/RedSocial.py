class RedSocial():
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []

    def totalPublicaciones(self, user):
        totalTamano = 0
        for publicacion in user.publicaciones:
            totalTamano += publicacion.calcularTamano()
        return totalTamano

    def mejoresAmigos(self, usuario):
        mejoresAmigos = None
        for publicacion in usuario.publicaciones:
            mejoresAmigos = list(filter(lambda amigo: publicacion.permiso(amigo), usuario.amigos))
        return mejoresAmigos

    def amigoMasPopular(self, usuario):
        print(max(usuario.amigos, key=lambda amigo: self.mejorPublicacion(amigo)))
        return 1

    # Devuelve el numero de likes de la mejor publicacion
    def mejorPublicacion(self, usuario):
        return (max(usuario.publicaciones, key=lambda publicacion: publicacion.meGusta))

class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre
        self.publicaciones = []
        self.amigos = []

    def __repr__(self):
        return self.nombre

    def publicar(self, publicacion):
        self.publicaciones.append(publicacion)

    def anadirAmigo(self, usuario):  # Se anaden mutuamente
        self.amigos.append(usuario)
        usuario.amigos.append(self)

    def like(self, publicacion):
        publicacion.meGusta += 1

class Publicacion:
    def __init__(self, estado):
        self.meGusta = 0
        self.estado = estado

        # El temanio se calcula por metodo, no es un atributo de clase

    def permiso(self, usuario):
        return self.estado.permiso(usuario)

class Texto(Publicacion):
    def __init__(self, texto, estado):
        super().__init__(estado)
        self.texto = texto

    def calcularTamano(self):
        return len(self.texto)

class Foto(Publicacion):
    factorDeCompresion = 0.7

    def __init__(self, alto, ancho, estado):
        super().__init__(estado)
        self.alto = alto
        self.ancho = ancho

    def calcularTamano(self):
        return self.alto * self.ancho * self.factorDeCompresion

class Video(Publicacion):
    def __init__(self, duracion, calidad, estado):
        super().__init__(estado)
        self.calidad = calidad
        self.duracion = duracion

    def calcularTamano(self):
        if self.calidad == "HD":
            return self.duracion * 3
        else:
            return self.duracion

# ESTADO DE LA PUBLICACION

class Publico:
    def permiso(self, usuario):
        return True

class Amigos:
    def __init__(self, user1):
        self.user1 = user1
    def permiso(self, user2):
        if user2 in self.user1.amigos:
            return True
        else:
            return False

class Algunos:
    def __init__(self, algunos):
        self.algunos = algunos

    def permiso(self, user):
        if user in self.algunos:
            return True
        else:
            return False


# TESTS

redSocial = RedSocial("faceless")

publico = Publico()

# Para crear un objeto amigos, paso por parametro el usuario dueno de la pubilcacion
# amigos = Amigos()

user1 = Usuario("Agustin")
redSocial.usuarios.append(user1)


print("Punto 1)\n")
"""Saber cuánto espacio ocupa el total de las publicaciones de un usuario"""

publ11 = Texto("Hoy es martes 4 de Octubre :D", publico)
publ12 = Foto(10, 50, publico)
publ13 = Video(120, "HD", publico)

user1.publicar(publ11)
user1.publicar(publ12)
user1.publicar(publ13)

print(f"El usuario {user1.nombre} ocupa un total de {redSocial.totalPublicaciones(user1)} KB")


print("\nPunto 2)\n")
"""Determinar los mejores amigos de un usuario. Estos serían, según la gente de
   faceless, los que puede ver todas sus publicaciones"""

user2 = Usuario("Franco")
user3 = Usuario("Lucia")
user4 = Usuario("Pedro")

redSocial.usuarios.extend([user2, user3, user4])

user1.anadirAmigo(user2)
user3.anadirAmigo(user1) # Anadir amigo es viceverso

print(f"Los amigos de {user1.nombre} son: {redSocial.mejoresAmigos(user1)}")

print("\nPunto 3)\n")
"""Saber cuál es el amigo más popular que tiene un usuario. Es decir, el amigo que
   tiene mas “me gusta” entre todas sus publicaciones."""

publ31 = Video(1000, "HD", publico) # Video tutorial de como resolver parcial de practica PPV
user3.publicaciones.append(publ31)

user1.like(publ31)
user2.like(publ31)
user3.like(publ31) #Auto like (podria ser el caso y deberia ser valido)

user2.like(publ11) #para comparar

print(redSocial.amigoMasPopular(user1))

print(f"El amigo mas popular de {user1.nombre} es: {redSocial.amigoMasPopular(user1)}") # Lucia con la publicacion 31
#
# print("\nPunto 4)\n")
# """ Permitir que un usuario publique un video que solo esté accesible para los amigos
# de un él"""
#
# user4.anadirAmigo(user1)
# user4.anadirAmigo(user2)
#
# publ41 = Video(60, "normal", amigos)
# user4.publicaciones.append(publ41)
#
# print(f"Usuario {user1.nombre} intenta likear la publicacion 41") # Puede dar like porque es amigo
# user1.like(publ41)
#
# print(f"Usuario {user3.nombre} intenta likear la publicacion 41")
# user3.like(publ41)  # No es amigo, no puede ver