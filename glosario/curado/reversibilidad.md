# Reversibilidad

## Definición

La **reversibilidad** es una estimación de lo que cuesta deshacer una decisión (`SE-348`). `SE-333` la expresa como coste y plazo de volver atrás; `SE-582`, como la posibilidad de volver al estado anterior; `SE-032`, como la capacidad *demostrada* de retirar cambios o volver a un estado definido. `SE-348` insiste en que no es un adjetivo: es una estimación, con magnitud.

## Por qué importa

Decide cuánto cuidado merece un cambio. Una decisión barata de deshacer se toma rápido y se corrige después; una cara o imposible exige análisis, pruebas y aprobaciones antes. Con agentes que actúan (`SE-582`, `SE-589`), la reversibilidad de una acción es el criterio principal para permitirla sin confirmación.

## Cómo funciona

Se estima por tres elementos: qué hace falta para volver (una copia, un *commit*, una migración inversa), cuánto cuesta en tiempo y trabajo, y qué se pierde en el camino. `SE-582` la clasifica en tres niveles: se puede deshacer con una copia o un *commit*; se puede deshacer con esfuerzo; no se puede deshacer.

En migraciones de datos (`SE-354`), una migración tiene un `up` y, por convención, un `down`; pero el `down` restaura la **estructura**, no necesariamente los **datos**: si el `up` quitó una columna, el `down` puede volver a crearla vacía. Hay operaciones totalmente reversibles (renombrar), parcialmente (convertir un decimal a entero pierde la parte decimal) y no reversibles (quitar datos). Declarar cuál es cada una, con una prueba de ida y vuelta sobre datos de ejemplo, es más honesto que escribir un `down` por rutina y presentarlo como garantía.

## Ejemplo

Para desplegar un cambio incompatible en un esquema, `SE-354` aplica *expandir, migrar y contraer* en despliegues separados: primero se añade lo nuevo (reversible), luego se migran datos (reversible mientras lo viejo exista) y, mucho después, se elimina lo viejo (irreversible, con aprobación). Ilustración:

```text
1. expandir:  ADD COLUMN correo_nuevo        (reversible: DROP COLUMN)
2. migrar:    copiar y validar datos         (reversible: se conserva la columna vieja)
3. contraer:  DROP COLUMN correo_viejo       (irreversible: respaldo y segunda aprobación)
```

## Errores y confusiones comunes

- **Errores en las instancias viejas durante un despliegue.** Causa: cambio incompatible en un solo paso; corrección: expandir, migrar y contraer en despliegues separados (`SE-354`).
- **El panel se congela al migrar.** Causa: actualización de muchas filas en una transacción; corrección: relleno por lotes idempotente y reanudable (`SE-354`).
- **Un `down` escrito por rutina presentado como garantía.** Restaura estructura, no datos.

## Límites y cuándo no aplica

La reversibilidad se estima, no se mide con certeza: depende del estado y de lo que haya ocurrido después del cambio. Los efectos externos (correos enviados, cobros, datos leídos por terceros) no se revierten con un retroceso técnico. Y el coste de preservar reversibilidad (mantener lo viejo) es un precio real que hay que sopesar.
