# Explicación

## Definición

En documentación técnica, una **explicación** es una página que aporta contexto, causas y alternativas para comprender, sin pasos ni listados. Es el sentido de `SE-206` (tutoriales, how-to, referencia y explicación), donde es uno de los cuatro tipos de página, junto al tutorial, la guía práctica y la referencia. No se usa aquí como «explicar algo en general», sino como tipo de documento con función propia.

## Por qué importa

Cambia dónde se escriben los porqués. Según `SE-206`, es la única página donde caben las tensiones entre dos buenas razones. Es también el tipo que más se omite, porque no tiene una tarea inmediata, y por eso la gente reinventa decisiones ya tomadas.

## Cómo funciona

La explicación responde a «¿por qué?» y «¿qué alternativas había?». Es el lugar del contexto histórico, de las tensiones y de las decisiones que podrían cambiar. No se lee con prisa y no se ejecuta; se mide en lo que permite entender. Cada tipo de página tiene su función, y mezclarlas las degrada:

- El **tutorial** lleva a una persona de la mano para aprender; no explica por qué las cosas son así, a lo sumo dice «ahora verás» y enlaza.
- La **guía práctica** resuelve una tarea concreta.
- La **referencia** describe sin opinar.
- La **explicación** da el porqué.

La regla de mantenimiento es separar y enlazar: cada página lleva una línea hacia las otras. Los síntomas de mezcla tienen corrección concreta: una sección de «notas avanzadas» a mitad de un tutorial se mueve a una explicación; una guía que empieza con la historia de la política mueve esa historia a la explicación; una referencia que dice «se recomienda» traslada la recomendación a una guía o explicación.

## Ejemplo

La plataforma separa la penalización en cuatro páginas con nombres propios: un tutorial («Tu primera entrega con retraso»), una guía («Cambiar el tope de penalización de un curso»), una referencia («Parámetros de penalización») y una explicación («Por qué la penalización es diaria y con tope»). Cada una enlaza a las otras tres en una línea. El tutorial y la guía se ejecutan en la integración continua; la referencia se genera de la configuración.

## Errores y confusiones comunes

- **Notas avanzadas dentro del tutorial.** Mezcla de explicación y aprendizaje; mover a una explicación y dejar un enlace.
- **La guía empieza con la historia de la política.** Mezcla contexto con procedimiento.
- **La referencia que recomienda.** Mezcla opinión con descripción.
- **No escribir ninguna.** Las decisiones se reinventan.

## Límites y cuándo no aplica

No todo componente necesita explicación: una opción de configuración solo necesita referencia, mientras que una decisión de diseño pide explicación (`SE-206`). Una explicación sin fecha ni dueño envejece y se vuelve fuente de errores; conviene revisarla cuando cambia la decisión que describe. Tampoco sustituye a un registro de decisiones fechado donde haga falta trazabilidad formal.
