# Dominio

## Definición

**Dominio** es una palabra con dos sentidos que el programa usa en lugares distintos:

- **Dominio de un problema o de un predicado** (`SE-050`, `SE-052`, `SE-056`): el conjunto de valores sobre el que se afirma algo. Un `para todo` exige cubrir el dominio declarado; un `existe` se demuestra con un testigo.
- **Dominio de negocio** (`SE-343`): un área del negocio con su propio lenguaje y su propio equipo.

La relación entre ambos es el hilo común: fijar dónde vale una afirmación o dónde viven unas reglas.

## Por qué importa

En el primer sentido, declarar el dominio es lo que distingue una prueba de una anécdota: «falló en un cliente» no es «falla para todos», y pasar de lo uno a lo otro cambia el cuantificador sin evidencia (`SE-050`). En el segundo, el dominio es la unidad natural para dividir equipos y servicios (`SE-343`): un límite que sigue el lenguaje del negocio es más estable que uno que sigue la tecnología.

## Cómo funciona

- **Lógica** (`SE-050`): un predicado depende de variables, por ejemplo `responde(host, prueba)`. El dominio dice qué hosts y qué pruebas cuentan. Solo se puede cubrir enumerando cuando es finito: la clase advierte que su enfoque solo alcanza dominios finitos y enumerables.
- **Pruebas** (`SE-052`, `SE-056`): enumerar un dominio pequeño completo da más garantía que unos cuantos ejemplos; buscar contraejemplos en un dominio acotado refuta un «es óptimo» afirmado tras tres casos.
- **Diseño** (`SE-343`): cada dominio de negocio tiene vocabulario propio, y la separación en servicios se discute en términos de esos dominios.

## Ejemplo

`SE-052`: una prueba con ejemplos pasa y otra con otros falla porque la muestra no era representativa; la corrección es enumerar un dominio pequeño completo, por ejemplo todos los arreglos de longitud 0 a 4 con valores de 0 a 2. Ilustración:

```python
from itertools import product
for xs in (list(p) for n in range(5) for p in product(range(3), repeat=n)):
    assert busca(xs) == referencia(xs)
```

## Errores y confusiones comunes

- **El bucle de búsqueda no termina en un borde.** Causa: la variante no decrece; corrección: ajustar la actualización y probar el dominio pequeño (`SE-052`).
- **«Es óptimo» tras tres casos.** Causa: muestra pequeña; corrección: buscar contraejemplos en un dominio acotado (`SE-056`).
- **Confundir los dos sentidos.** El dominio de un predicado no es un área de negocio.

## Límites y cuándo no aplica

La enumeración exhaustiva no escala a dominios infinitos o enormes (`SE-050`); allí se necesitan demostraciones o muestreo con sus límites declarados. Al trasladar un razonamiento a otro dominio se conserva la estructura del argumento, no los nombres, y hay que identificar qué supuesto pertenecía al caso original. Y un dominio de negocio mal delimitado produce servicios que no coinciden con ningún equipo.
