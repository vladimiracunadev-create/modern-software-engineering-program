# Matriz de compromisos

## Definición

Una **matriz de compromisos** (en inglés, *trade-off matrix*) es la tabla donde el taller de `SE-095` **registra, para cada alternativa evaluada, sus costos y propiedades en varias dimensiones**: **tiempo, espacio, orden, estabilidad, complejidad de implementación y recuperación** (cómo se comporta ante fallos o cómo se restablece). Cada fila es un candidato y cada columna un criterio, con valores medidos o razonados. Su propósito es hacer visible que ninguna alternativa gana en todo: mejorar una dimensión suele costar otra.

## Por qué importa

Cuando se elige una estructura de datos «por costumbre», no hay registro de qué se sacrificó. La matriz obliga a poner las dimensiones sobre la mesa y a comparar con evidencia. La decisión que cambia es cómo se justifica una elección: no «es la mejor», sino «es la mejor *para estos pesos*, y estos son los costos que aceptamos». `SE-095` pide además dos cautelas que evitan que la matriz se convierta en una falsa autoridad: los pesos pertenecen al contexto y se someten a **sensibilidad**, y la tabla **organiza evidencia pero no genera una decisión automática**.

## Cómo funciona

El uso correcto sigue un orden:

1. **Declarar el perfil de operaciones y los tamaños** antes de medir; sin carga declarada, las cifras no se interpretan.
2. **Llenar cada celda con medición o con un argumento** (tiempo y memoria medidos; estabilidad y orden como propiedades de la estructura).
3. **Asignar pesos** según el contexto: para un servicio con latencia estricta, el tiempo pesa más que la memoria.
4. **Probar la sensibilidad:** ¿la elección cambia si un peso cambia un poco? Si cambia, la decisión es frágil y hay que decirlo.
5. **Emitir una recomendación condicionada**, con la medición que la invalidaría.

La causa de que no decida sola es que los pesos son un juicio. Una suma ponderada puede dar un ganador por un peso mal puesto; la sensibilidad lo detecta. Un error documentado: elegir `set` para todo, porque se ignoró el costo de construirlo y la memoria. La corrección es calcular el **umbral de reutilización** (cuántas consultas amortizan la construcción) y la memoria.

## Ejemplo

Para decidir cómo comprobar pertenencia en una colección (ilustración, números inventados):

```text
candidato       construir    consultar    memoria    orden    estabilidad   implementación
lista           O(1)         O(n)         baja       sí       n/a           trivial
lista ordenada  O(n log n)   O(log n)     baja       sí       n/a           media
set             O(n)         O(1) esp.    alta       no       n/a           trivial
```

Con 10 consultas, la lista basta; con un millón, el `set` o la lista ordenada. La recomendación de `SE-095` es de la forma: «con consultas > N por construcción, usar `set`; si la memoria supera X, usar lista ordenada; esta recomendación cambia si la carga se vuelve de escritura intensiva».

## Errores y confusiones comunes

- **Recomendar sin declarar carga ni tamaño.** Otro equipo no se convence porque no puede reproducir el contexto.
- **Tratar la suma ponderada como decisión.** La matriz informa; la decisión la toma una persona.
- **Omitir la sensibilidad.** Una elección que cambia con un peso es frágil.
- **Pocas dimensiones.** Olvidar recuperación o complejidad de implementación sesga hacia lo rápido.

## Límites y cuándo no aplica

El taller cubre cargas sintéticas y una plataforma (`SE-095`): las mediciones de la matriz valen para ese entorno. Una matriz con demasiadas filas y columnas oculta lo importante bajo detalle. Para decisiones pequeñas y reversibles, una discusión breve es suficiente; la matriz se justifica cuando el costo de equivocarse es alto o cuando se necesita convencer a otros con evidencia.
