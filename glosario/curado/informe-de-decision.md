# Informe de decisión

## Definición

Un **informe de decisión** es, en el proyecto de `SE-084`, el documento que cierra una comparación de paradigmas **conectando cuatro cosas: fuerza, observación, consecuencia y elección por contexto**. Parte de las fuerzas del problema, presenta lo que se observó al implementarlo y probarlo, deduce las consecuencias y recomienda una elección **para un contexto**, no una verdad general. Es un entregable propio del programa, cercano a un registro de decisión de arquitectura pero centrado en la comparación de modelos.

## Por qué importa

Comparar soluciones produce datos, y los datos sin conclusión no deciden nada. El informe es el puente entre la medición y la acción, y obliga a que cada recomendación tenga apoyo visible. La decisión que cambia es qué se entrega al terminar una comparación: no «esta solución me gusta más», sino una recomendación **trazable** hasta una fuerza del problema y una observación reproducible, y con la indicación de cuándo dejaría de ser válida.

## Cómo funciona

La estructura sigue la cadena de justificación:

1. **Fuerza:** la propiedad del problema que decide (auditabilidad, tasa de cambio, concurrencia).
2. **Observación:** qué se vio al implementar y probar, con datos, comando y versión.
3. **Consecuencia:** qué implica esa observación para mantener y evolucionar el sistema.
4. **Elección por contexto:** qué se recomienda **dado ese contexto**.

`SE-084` ilustra que la recomendación puede ser **mixta**: reglas para la política y flujo reactivo para la telemetría, unidos por un adaptador pequeño. Y exige una cláusula honesta: el informe **declara cuándo esa combinación dejaría de ser adecuada**, es decir, qué cambio en las fuerzas invalidaría la elección. La causa de que esto importe es que las decisiones de diseño caducan cuando cambia el contexto, y sin esa cláusula nadie sabe cuándo revisarlas.

## Ejemplo

Un fragmento del informe del proyecto (ilustración, contenido inventado):

```text
Fuerza:        auditabilidad alta y reglas que cambian mensualmente.
Observación:   la versión de tabla de reglas cambió 1 archivo ante la regla nueva;
               la versión con clases tocó 3 (comando: pytest -k cambio_dirigido, v1.4.0).
Consecuencia:  la decisión de negocio vive en un solo lugar y es auditable.
Elección:      reglas como datos para la política; flujo reactivo para telemetría,
               unidos por un adaptador de 30 líneas.
Deja de valer: si las reglas pasan a depender de estado acumulado entre casos.
```

Dos errores documentados en la clase se evitan con este formato: el informe que afirma sin comando reproducible (se añade comando, versión y salida a cada afirmación) y la suite que pasa pero hay defectos, porque solo hay casos del camino feliz (se derivan casos del contrato y de los mutantes).

## Errores y confusiones comunes

- **Afirmaciones sin evidencia reproducible.** Nadie puede verificarlas.
- **Conclusiones universales.** «El paradigma X es mejor» en lugar de «para este contexto».
- **Omitir cuándo deja de valer.** La recomendación queda sin fecha de revisión.
- **Un informe que describe sin decidir.** Lista observaciones y no elige.

## Límites y cuándo no aplica

El proyecto demuestra equivalencia para el corpus y las propiedades declaradas, no para todas las entradas posibles ni para cargas de producción (`SE-084`). Un informe no sustituye datos de mantenimiento reales, que solo llegan con el tiempo. Para decisiones pequeñas y reversibles, una nota breve en el cambio basta; el informe completo se justifica cuando la decisión es costosa de revertir.
