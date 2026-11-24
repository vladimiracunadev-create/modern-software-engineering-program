# Spec-anchored

## Definición

**Spec-anchored** es el uso de la especificación como un documento vivo que se mantiene junto con el código a lo largo de la vida del sistema (SE-165, SE-548). Es el segundo de tres niveles: spec-first (la especificación guía y se abandona), spec-anchored (se mantiene anclada al código) y spec-as-source (la especificación es la fuente de la que se genera el código).

## Por qué importa

Hace que la especificación siga siendo una fuente fiable para consumidores y revisores. Cuando cambia el comportamiento, cambian ambos. Su coste es disciplina: sin un mecanismo que detecte la discrepancia, el anclaje es una promesa y la deriva aparece en el primer apuro (SE-165). Cambia la decisión de qué artefactos merecen este nivel: los que otros consumen y cambian a menudo.

## Cómo funciona

El anclaje requiere un **mecanismo que haga fallar la integración continua cuando especificación y código discrepan**. SE-165 menciona tres formas de comprobarlo, con distinta potencia: por firmas (nombres y tipos), por ejemplos y por pruebas contractuales. SE-548 lo describe en el contexto de desarrollo guiado por especificaciones: cada regla tiene un identificador que el código y las pruebas citan; los valores que la especificación declara (umbrales, límites) se comparan con los del código; un cambio en el código sin cambio en la especificación se señala. La especificación es una fuente que se revisa con cada cambio, como una prueba.

El costo es disciplina y herramientas: alguien debe escribir el comprobador y alguien debe mantenerlo. En la plataforma de entregas (SE-165), cada artefacto tiene un nivel declarado: el documento de arquitectura es spec-first (guía y se archiva); el contrato de la API es spec-anchored, con un comprobador en integración continua que compara las operaciones del código con el documento OpenAPI y falla con el nombre del parámetro que discrepa; los clientes se generan desde el documento (spec-as-source).

## Ejemplo

El documento OpenAPI declara que `POST /entregas` acepta el parámetro `archivo` obligatorio. Un desarrollador renombra el parámetro a `adjunto` en el código sin tocar el documento. El comprobador de integración continua compara ambos y falla con el mensaje «parámetro `archivo` ausente en el código; `adjunto` ausente en la especificación». Hasta que alguien actualice uno, la integración no pasa. (Ilustración del mecanismo descrito en SE-165.)

## Errores y confusiones comunes

- **La especificación dice una cosa y el código otra, y nadie lo sabe**: anclaje sin comprobación automática.
- **Anclar todo**: el costo de mantener comprobadores para documentos que casi no cambian no se justifica.
- **Confundirlo con spec-as-source**: aquí el código se escribe aparte y se compara; allí se genera.
- **Comprobar solo la forma** y no el comportamiento.

## Límites y cuándo no aplica

Para decisiones puntuales que se toman una vez (un documento de arquitectura), el anclaje es excesivo y es preferible spec-first con archivo. Si la comprobación es débil (solo firmas), la deriva de comportamiento pasa sin ser detectada. Y si el equipo no tiene capacidad de mantener el comprobador, el anclaje se rompe en silencio.
