# Contraejemplo mínimo

## Definición

Un **contraejemplo mínimo** es la entrada **más pequeña** que hace fallar una regla propuesta. En `SE-091`, cuando se sugiere una regla local (por ejemplo, «en cada paso elijo la opción que parece mejor ahora»), no se discute su plausibilidad: se busca la entrada de menor tamaño que la rompe. Basta un caso para refutar una afirmación universal, y el más pequeño es el más útil, porque cada elemento que sobra es ruido para entender por qué falla.

## Por qué importa

Los algoritmos voraces son atractivos porque son simples y rápidos, y muchas veces parecen correctos. Pero «parece correcto» no es una demostración. La decisión que cambia es qué se hace antes de adoptar una regla local: o se demuestra, o se la ataca con casos pequeños. Un contraejemplo no solo refuta; **revela qué interacción faltaba en el modelo**, es decir, qué decisión de hoy cambia lo que es posible mañana. Por eso la biblioteca de estructuras y algoritmos conserva esos casos como pruebas, y no los trata como *edge cases* irrelevantes.

## Cómo funciona

El procedimiento es sistemático:

1. **Formular la regla** como una afirmación precisa («elegir siempre la moneda mayor que cabe da el mínimo de monedas»).
2. **Buscar entradas pequeñas.** Enumerar o generar casos de tamaño creciente y comparar la regla con una referencia correcta (fuerza bruta o programación dinámica).
3. **Detenerse en la primera discrepancia** y reducirla: quitar elementos mientras siga fallando.
4. **Explicar la causa** con ese caso mínimo: dónde la elección local cerró un camino mejor.
5. **Guardarlo como prueba de regresión.**

La razón por la que lo mínimo importa es de diagnóstico: con tres monedas se ve el mecanismo; con treinta, no.

## Ejemplo

`SE-091` presenta dos fallos reales de reglas voraces. Con un sistema de monedas **no canónico**, la regla «tomar la mayor» devuelve más monedas de las necesarias. El ejemplo clásico de la literatura son monedas de 1, 3 y 4 para formar 6: la regla voraz toma 4+1+1 (tres monedas) y la mejor es 3+3 (dos). Ilustración mínima:

```python
def voraz(monedas, total):
    n = 0
    for m in sorted(monedas, reverse=True):
        n += total // m; total %= m
    return n

assert voraz([1, 3, 4], 6) == 3     # hay solución con 2: 3+3
```

El segundo caso de la clase: seleccionar actividades **por inicio** da menos actividades de las esperadas; la corrección es ordenar por **fin** y contrastar con fuerza bruta en casos pequeños. En ambos, el caso pequeño explica la causa.

## Errores y confusiones comunes

- **Probar con entradas grandes y aleatorias.** Pueden coincidir por azar; un fallo escondido se vuelve ilegible cuando aparece.
- **Parar en cualquier contraejemplo, no en el mínimo.** Un caso con diez elementos oculta cuál de ellos importa.
- **Llamarlos «casos extremos sin importancia».** Son la prueba de que la regla no vale en general.
- **Confundir contraejemplo con prueba de corrección.** Que no aparezca uno en las pruebas no demuestra que la regla sea correcta.

## Límites y cuándo no aplica

Buscar contraejemplos puede refutar, no demostrar: si no se encuentra ninguno en tamaños pequeños, la regla puede seguir siendo falsa en tamaños mayores, y solo una demostración (por ejemplo, un argumento de intercambio) la valida. Además, necesita una referencia correcta con la que comparar, y esa referencia (fuerza bruta, programación dinámica) debe ser manejable en tamaños pequeños. La programación dinámica, por su parte, exige un estado finito y abarcable (`SE-091`).
