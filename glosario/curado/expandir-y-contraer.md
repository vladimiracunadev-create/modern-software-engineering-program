# Expandir y contraer

## Definición

**Expandir y contraer** (también llamado cambio paralelo) es el patrón que divide un cambio incompatible en fases compatibles: añadir lo nuevo, migrar a los clientes y quitar lo viejo (`SE-354`). El programa lo usa en varios contextos con el mismo núcleo: esquemas de base de datos (`SE-354`, `SE-523`), datos analíticos (`SE-366`), interfaces entre sistemas (`SE-380`) y releases (`SE-476`), donde ambas versiones coexisten durante el cambio.

## Por qué importa

Un cambio incompatible hecho en un solo paso exige que todas las piezas cambien a la vez, y eso no ocurre en un sistema con varias instancias, versiones desplegadas y clientes. La decisión que cambia es cómo se renombra o reestructura algo compartido: en varios pasos pequeños, cada uno reversible, en lugar de uno solo irreversible.

## Cómo funciona

`SE-354` lo explica con un renombrado de columna. Tres fases:

1. **Expandir**: se añade la columna nueva, se rellena y se mantiene sincronizada con la vieja mediante una escritura doble (por la aplicación o por un disparador). Ambas versiones funcionan.
2. **Migrar**: se despliegan las instancias nuevas, que leen y escriben lo nuevo.
3. **Contraer**: cuando ya no corre ninguna versión vieja, se quita la columna vieja y los disparadores.

La clave, según `SE-523`, es que en cada paso existen versiones de la aplicación válidas tanto con el esquema en ese estado como con el estado anterior; esto permite desplegar y revertir el código **sin tocar los datos**. Cada fase se despliega y se revierte por separado, y el tiempo entre ellas lo fija la última instancia vieja, no el calendario.

La ventaja se ve contando fallos: renombrar en un solo paso deja en rojo a una versión en cada fase, mientras que expandir y contraer solo deja en rojo a la versión 2 antes del cambio y a la 1 tras quitar la columna vieja, es decir, en los extremos que se evitan por orden de despliegue.

## Ejemplo

Para renombrar `nota` a `calificacion`: se añade `calificacion`, se rellena desde `nota` y se mantiene sincronizada; se despliega la aplicación que lee y escribe `calificacion`; cuando la última instancia vieja se apaga y no quedan lecturas de `nota`, se elimina `nota`. Si algo falla en cualquier fase, se revierte el código y los datos siguen legibles. Ejemplo de `SE-354`.

## Errores y confusiones comunes

- **Tras revertir hay datos ilegibles**: migración destructiva con el despliegue; se corrige expandiendo y contrayendo en despliegues separados (`SE-476`).
- **Contraer antes de tiempo**: se quita lo viejo mientras alguien aún lo usa.
- **Olvidar contraer**: la estructura vieja y la doble escritura se quedan para siempre.
- **Creer que sirve solo para bases de datos**: es un patrón de compatibilidad general.

## Límites y cuándo no aplica

Tiene un costo: más pasos, más despliegues, escritura doble y un periodo en que conviven dos estructuras; para un cambio compatible o en un sistema que se puede detener y actualizar entero, es excesivo. Exige disciplina para completar la fase final. Y no resuelve cambios de significado sin cambio de forma (cambio semántico), que requieren además coordinación con los consumidores.
