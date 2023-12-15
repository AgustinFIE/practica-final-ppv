### Enunciado:

Modelamos una situación donde un tanque dispara un proyectil a otro tanque. Un tanque
queda completamente destruido cuando sus puntos de daño se redujeron a 0.
Sabemos que los tanques M4 Sherman disparan proyectiles perforantes (AP) que son
capaces de penetrar un blindaje de 92mm y que provocan 110 puntos de daño y también
disparan obuses (HE) que penetran hasta 38mm de blindaje y realizan 250 puntos de
daño.

Por otro lado se sabe que los tanques PzV Panther disparan proyectiles perforantes que
son capaces de penetrar un blindaje de 135mm y que provocan 175 puntos de daño y
también disparan obuses que penetran hasta 53mm de blindaje y realizan 350 puntos de
daño. M4 tiene 51mm de blindaje y soporta hasta 400 puntos de daño. PzV tiene 85 mm
de blindaje y soporta hasta 500 puntos de daño. Vamos a considerar que un tanque
puede llevar cualquier cantidad de proyectiles de cualquier tipo y para disparar elige al
azar un proyectil.

- import random
- random.randrange(numeroMax)

En un futuro se pretende agregar un nuevo tipo de proyectiles que son perforantes con un
“sabot” descartable (APDS) que penetran blindaje mucho más grueso, y también se va a
agregar el tanque PzVI Tiger con 100mm de blindaje y que soporta 1100 puntos de daño.