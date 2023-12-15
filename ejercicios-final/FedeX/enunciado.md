### PARADIGMAS DE PROGRAMACIÓN V
## Enunciado:

Nuestro amigo Fede tiene una empresa de envíos postales llamada FedeX y nos solicita
una pequeña aplicación para administrar los envíos. Los envíos tienen distintas
características como información básica, éstas son: lugar de origen (ciudad y país), lugar de
destino (idem), peso en kilogramos, precio base, categorías que brindan información del
contenido (por ejemplo: tecnología, libro, música, etc...), y varios impuestos asociados.
Existen recargos extra que aumentan el precio de envío de acuerdo al contenido, es decir,
si cumple o no con ciertas características en las cuales se basa cada uno de los recargos.
Ejemplos de algunos de estos son:

- Recargo categórico: Si el envío tiene una categoría X, se computa un porcentaje
dado del precio base, por ejemplo 10% para la tecnología (por frágil). ● Recargo por
sobrepeso: Si el peso es mayor a un peso dado (1kg) se le suma $80. ● Recargo
Arbitrario: $50 adicionales, ejemplo: por el Día del Trabajador de Correo. ● Podría
haber otros...

Los impuestos se aplican sobre el precio neto (el precio base sumado a todos los cargos
extra). Algunos de los impuestos que pueden aplicarse son:

- IVA: 20% del precio neto.
- Impuesto Multicategoría: 1% del precio neto, se aplica cuando el envío tiene más de
3 categorías.
- Impuesto Aduanero: 50%, pero sólo cuando el envío es internacional. Un pedido es
internacional cuando los países de origen y destino difieren.
- Impuesto Extraño: 10%, sólo si tiene precio base es par.
- Podría haber otros...

### Tarea:

1. Averiguar precio neto de envío con origen California, Estados Unidos y con destino
Miami, Estado Unidos, de 5kg de peso, precio base $1500, con categoría de libros.
2. Averiguar precio bruto (final) de envío con origen en Buenos Aires, Argentina y con
destino Utrecht, Países Bajos, de 2kg de peso, precio base de $220, con las
categorías de música, arte y tecnología.
3. Obtener todos los envíos internacionales y nacionales.
4. Obtener el envío “propicio a perderse” (tiene el precio bruto más barato de todos).