import random

class Projectile:
    def __init__(self, penetration, damage):
        self.penetration = penetration
        self.damage = damage

# Tipos de Proyectiles que pueden disparar los tanques M4_Sherman
# Perforante (AP) y Obuses (HE)

# Tipos de Proyectiles que pueden disparar los tanques PzV_Panther
# Perforante (AP) y Obuses (HE)


class AP(Projectile):
    def __init__(self):
        super().__init__(92, 110)

class HE(Projectile):
    def __init__(self):
        super().__init__(38, 250)


class APDS(Projectile):
    def __init__(self):
        super().__init__(200, 150)  # Assuming values for APDS


class Tank:
   def __init__(self, armor, health, projectiles):
       self.armor = armor
       self.health = health
       self.projectiles = projectiles

   def fire(self, target):
       projectile = random.choice(self.projectiles)
       target.receive_damage(projectile)
       print(f"Proyectil elegido: {type(projectile).__name__}")

   def receive_damage(self, projectile):
       if projectile.penetration > self.armor:
            self.health -= projectile.damage
            if self.health <= 0:
                print("Tanque destruido!")

# Tipos de tanques:
# M4_Sherman, PzV_Panther y PzVI_Tiger
class M4_Sherman(Tank):
    def __init__(self):
        super().__init__(51, 400, [AP(), HE()])

class PzV_Panther(Tank):
    def __init__(self):
        super().__init__(85, 500, [AP(), HE()])

class PzVI_Tiger(Tank):
    def __init__(self):
        super().__init__(100, 1100, [AP(), HE(), APDS()])


# Funcion auxiliar para mostrar informacion (no es necesaria)
def mostrar_informacion(tank1, tank2):
    print(f"Vida restante del Tanque 1: {tank1.health}")
    print(f"Vida restante del Tanque 2: {tank2.health}")

# ****************** Pruebas ******************

# Creo los tanques

tank1 = M4_Sherman()
tank2 = PzV_Panther()

# Se atacan hasta que uno se destruye
while True:
    tank1.fire(tank2)

    mostrar_informacion(tank1, tank2);

    if tank2.health <= 0:
        print("Tanque 2 fue destruido!")
        break

    tank2.fire(tank1)
    if tank1.health <= 0:
        print("Tanque 1 fue destruido!")
        break