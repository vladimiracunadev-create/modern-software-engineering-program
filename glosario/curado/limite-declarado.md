# Límite declarado

## Definición

Un **límite declarado** es la afirmación explícita de lo que un artefacto no cubre o no demuestra: lo que ni el modelo ni el validador ven (`SE-336`), lo que un paquete no probó (`SE-360`) o la lista de lo que no se midió, no se probó o se supuso, escrita en el propio dossier (`SE-540`). Es la parte honesta de un documento técnico.

## Por qué importa

Un dossier o paquete sin límites parece más sólido, pero solo es más opaco: quien lo lee no sabe qué comprobar antes de confiar. La decisión que cambia es qué se entrega junto con el resultado: además de lo que se afirma, lo que no se afirma. `SE-360` lo dice con claridad: un paquete sin límites declarados no es más seguro, solo más opaco.

## Cómo funciona

`SE-336` agrupa los límites en tres:

1. **Lo que el validador no ve**: el sentido de los umbrales, funciones de aptitud triviales, contradicciones entre ADR.
2. **Lo que el modelo no ve**: degradación parcial, reintentos, colas reales, seguridad, correlaciones de fallos.
3. **Lo que nadie ha medido**: latencias reales, disponibilidades reales, carga real.

Cada límite lleva un **responsable** y una **señal para dejar de ser un supuesto** (una prueba de carga, un mes de telemetría). Eso lo vuelve un compromiso verificable, no una disculpa genérica.

`SE-360` lo concreta en un archivo, `LIMITES.md`, que declara qué no se probó (un motor distinto, el tiempo de restauración con el volumen real, el cifrado, el proveedor), qué se supuso (plazos de retención, volúmenes, popularidad de las claves) y qué ningún validador ve (las cuatro familias de mutación de sentido). Una lista así permite a quien opera el paquete decidir qué comprobar antes de confiar y a quien lo revisa saber qué exigir. `SE-540` lo lleva al nivel de gestión: la lista de lo que no se midió ni se probó va en el propio dossier.

## Ejemplo

Un paquete de recuperación de datos incluye una prueba de restauración con una base pequeña. Su `LIMITES.md` dice: no se probó el tiempo de restauración con el volumen real; se supuso un plazo de retención de 30 días; el validador no ve mutaciones que cambian el sentido de un umbral. Para cada uno, un responsable y la señal que lo cerraría (por ejemplo, una restauración con datos del tamaño real). Basado en la estructura de `SE-360`.

## Errores y confusiones comunes

- **El comité pregunta por una caída y no hay respuesta**: documento sin escenarios ni modelo; se corrige con escenarios medibles y un modelo que los evalúa.
- **Los diagramas se contradicen**: vistas mantenidas a mano; se corrige generándolas desde un modelo único.
- **Declarar límites genéricos** («puede haber errores»): no dicen qué comprobar.
- **Creer que declarar límites debilita el trabajo**: es lo que permite cuestionarlo con precisión.

## Límites y cuándo no aplica

Declarar un límite no lo resuelve: lo hace visible. Una lista de límites sin responsable ni señal de cierre se vuelve un descargo de responsabilidad. Y no hace falta para entregables triviales y desechables; su valor crece con el costo de equivocarse al confiar en el artefacto.
