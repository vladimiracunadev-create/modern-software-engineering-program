# Fuente única

## Definición

La **fuente única** (*single source of truth*) es el lugar donde un dato se escribe una vez; las demás menciones lo enlazan, lo incluyen o se generan desde él (SE-205). No obliga a que exista un solo documento: obliga a que cada dato tenga un solo lugar donde se escribe.

## Por qué importa

Cada copia añade una oportunidad de olvido, y el coste crece con el número de copias. Cuando una regla cambia, las copias que nadie actualizó contradicen a la fuente y confunden a quien lee. Cambia cómo se organiza la documentación: se decide dónde vive cada dato y se enlaza, en lugar de repetirlo.

## Cómo funciona

En la plataforma de entregas, el tope del 50 % de la penalización vive en la política académica versionada, y las demás páginas lo **citan con enlace**. Cuando el tope cambia, hay un único commit en la fuente; las páginas que lo enlazan se actualizan solas o se marcan para revisar. Las formas de reutilizar sin copiar son tres: **enlazar** (una referencia), **incluir** (una transclusión que muestra el contenido) y **generar** (un artefacto producido desde la fuente, como una referencia generada de la configuración).

SE-205 reconoce **dos excepciones razonables**: una página que debe leerse sin conexión (un PDF para el acta) puede copiar el dato si la copia declara su origen y fecha; y un texto que debe permanecer inalterado por razones de auditoría. En ambos casos la copia no es la fuente, y se comprueba que coincide con ella.

Para que funcione hay que **vigilarlo**: un comprobador de enlaces que falle cuando una página cita una fuente inexistente, y una lista de verificación que señale las vistas a revisar cuando la fuente cambia. El síntoma contrario es el de dos páginas con topes de penalización distintos porque el dato se copió en lugar de enlazarse; la corrección es elegir una fuente, enlazar desde las demás y añadir un comprobador de enlaces.

La fuente única se complementa con el inventario de tareas por audiencia: cada vista enlaza la fuente con una frase de contexto propia de su audiencia.

## Ejemplo

El tope de penalización está en `politica/penalizacion.md`. La página para estudiantes dice «el descuento tiene un tope (ver la política)» con enlace; la guía para docentes, igual; la referencia de parámetros se genera de la configuración. Al cambiar el tope al 30 %, se edita un solo archivo y la lista de verificación marca las cuatro vistas por revisar. El PDF del acta, que sí copia el valor, lleva la fecha y la versión de la política de la que proviene. (Ilustración del mecanismo de SE-205.)

## Errores y confusiones comunes

- **Dos páginas con topes distintos**: el dato se copió en vez de enlazarse.
- **Fuente que nadie sabe cuál es.**
- **Copiar «solo por esta vez».**
- **Confundirla con tener un único documento enorme**: lo único es el lugar de escritura del dato.

## Límites y cuándo no aplica

Enlazar introduce dependencias: si la fuente se mueve o se borra, los enlaces se rompen; por eso hay comprobadores. Las copias legítimas (offline, auditoría) requieren control. Para datos que casi nunca cambian y se usan en un solo lugar, el costo de la fuente única es mayor que el beneficio.
