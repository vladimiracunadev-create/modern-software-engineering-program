# Control

## Definición

**Control** tiene en el programa tres sentidos que conviene separar:

- **Compuerta** (`SE-372`): conjunto de reglas que decide si algo se publica (por ejemplo, un conjunto de datos).
- **Medida de riesgo** (`SE-299`): medida que reduce la probabilidad o el impacto de un riesgo.
- **Referencia** (`SE-024`): condición que se mantiene constante, o referencia contra la que se compara una medición.

Un cuarto uso, el *control de flujo* de un programa (`SE-061` a `SE-065`), es la forma en que condiciones, bucles y excepciones deciden qué se ejecuta.

## Por qué importa

Un control convierte una intención («los datos deben ser buenos») en una comprobación ejecutable que puede fallar. Sin él, la política es un deseo. Con él mal puesto, hay falsa seguridad: un control que no se revisa, que nadie ejecuta o que contrasta contra una lista desactualizada. `SE-372` lo resume: un registro sin control es un wiki, y un control sin registro no sabe qué comparar.

## Cómo funciona

- **Como compuerta** (`SE-372`): el registro de cada conjunto de datos (propietario, capa, columnas con tipo, columnas con datos personales, retención, comprobaciones, entradas, antigüedad máxima) se guarda como código junto al pipeline y pasa por la misma revisión. El control contrasta «lo que es» con «lo que debería ser» y bloquea la publicación si difieren.
- **Como medida** (`SE-299`): actúa sobre la causa (probabilidad) o la consecuencia (impacto) de un riesgo identificado.
- **Como referencia** (`SE-024`): una medición sin línea de control no permite saber si un cambio fue efecto de la intervención o del entorno.
- **Como flujo** (`SE-062`, `SE-065`): los umbrales se prueban en ambos lados y, cuando la ausencia es parte esperada del dominio, un resultado etiquetado evita usar excepciones como control ordinario.

## Ejemplo

`SE-065` midió el costo de un `try` que no lanza: 15,5 ns frente a 36,8 ns de la línea de control en Windows (y 9,1 frente a 8,5 en Linux). Aquí «control» es la referencia que da sentido a la medición.

## Errores y confusiones comunes

- **Clases mal asignadas en el límite.** Causa: `<=` y `<` intercambiados, sin prueba de frontera; corrección: probar ambos lados de cada umbral (`SE-062`).
- **`if budget:` responde igual con 0 y con `None`.** Causa: la verdad de Python mezcla ausencia y cero; corrección: comparar con `is None` y con 0 por separado (`SE-062`).
- **Un control sin dueño.** Sin responsable, la compuerta se desactiva «temporalmente» y no vuelve.

## Límites y cuándo no aplica

Un control reduce un riesgo, no lo elimina, y solo comprueba lo que su registro describe. Las cifras de `SE-065` dependen del entorno medido. Y como el término cambia de significado según la clase, hay que fijar cuál se usa antes de discutir si «hay control».
