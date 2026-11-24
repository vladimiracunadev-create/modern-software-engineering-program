# Retroalimentación

## Definición

La **retroalimentación** (*feedback*) es información que vuelve a quien actuó, a tiempo para modificar su siguiente decisión (`SE-002`). El programa la usa con tres matices:

- **De una interfaz** (`SE-171`): la respuesta perceptible de un sistema a una acción de la persona.
- **De un agente** (`SE-583`): la información que el agente recibe tras una acción.
- **De una persona** (`SE-532`): la que recibe en mentoría o revisión, que mejora el desempeño solo si es oportuna y específica.

## Por qué importa

Sin retroalimentación, no hay corrección. Un ciclo corto (probar, ver, ajustar) es lo que distingue el aprendizaje del repetir errores, tanto en personas como en sistemas. Cambia el diseño del trabajo: qué se mide, cuándo se avisa, y a quién.

## Cómo funciona

**En desarrollo** (`SE-002`): la ingeniería continua acorta el ciclo entre una decisión y su efecto observable (pruebas, integración continua, revisión); la información debe llegar a tiempo para cambiar la decisión.

**En personas** (`SE-532`): la práctica deliberada (Ericsson y colegas) describe la mejora como resultado de tareas precisas, de dificultad ligeramente superior al nivel actual, con retroalimentación inmediata y oportunidad de repetir. Los comentarios útiles tienen forma: «esta línea convierte fechas sin zona horaria; en la exportación de marzo causó dos filas erróneas; prueba `datetime.fromisoformat` con zona explícita» (línea, efecto, siguiente paso). El metaanálisis de Kluger y DeNisi mostró que la retroalimentación mejora el desempeño de media, pero que en más de un tercio de los casos lo empeora, sobre todo cuando atrae la atención hacia la persona (cómo se ve a sí misma) y no hacia la tarea (qué se hizo y cómo mejorarlo).

**En agentes** (`SE-583`): lo que el agente recibe tras cada acción determina qué hace después: un resultado claro de una compuerta permite corregir; uno ambiguo, no.

## Ejemplo

Revisión de código el mismo día, con línea, efecto y camino de mejora, frente a un comentario genérico («esto está mal») una semana después. Ilustración de retroalimentación de un agente:

```text
pytest: 1 failed — test_exporta_fecha: esperado 2026-03-01T00:00+00:00, obtenido 2026-03-01T00:00
```

## Errores y confusiones comunes

- **La persona repite el mismo error.** Causa: retroalimentación tardía o vaga; corrección: dar el aviso en el mismo cambio, con línea y efecto (`SE-532`).
- **Se percibe como ataque.** Causa: se dirige a la persona; corrección: describir el comportamiento y su efecto (`SE-532`).
- **Confundir cantidad con calidad.** Más comentarios no mejoran si no son específicos y accionables.

## Límites y cuándo no aplica

La retroalimentación no corrige un problema de diseño del trabajo: si la tarea es demasiado difícil, solo informa del fracaso. Un ciclo muy corto sin criterio de qué importa genera ruido. Y la evidencia citada (Kluger y DeNisi) indica que puede empeorar el desempeño: hay que diseñarla, no solo darla.
