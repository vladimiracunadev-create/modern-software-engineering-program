# Fuente única

[↑ Glosario](../../README.md) · [← Fuente de verdad y transformación](./fuente-de-verdad-y-transformacion.md) · [Fuentes de no determinismo →](./fuentes-de-no-determinismo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

La **fuente única** (*single source of truth*) es el lugar donde un dato se escribe una vez; las demás menciones lo enlazan, lo incluyen o se generan desde él ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md)). No obliga a que exista un solo documento: obliga a que cada dato tenga un solo lugar donde se escribe.

## Por qué importa

Cada copia añade una oportunidad de olvido, y el coste crece con el número de copias. Cuando una regla cambia, las copias que nadie actualizó contradicen a la fuente y confunden a quien lee. Cambia cómo se organiza la documentación: se decide dónde vive cada dato y se enlaza, en lugar de repetirlo.

## Cómo funciona

En la plataforma de entregas, el tope del 50 % de la penalización vive en la política académica versionada, y las demás páginas lo **citan con enlace**. Cuando el tope cambia, hay un único commit en la fuente; las páginas que lo enlazan se actualizan solas o se marcan para revisar. Las formas de reutilizar sin copiar son tres: **enlazar** (una referencia), **incluir** (una transclusión que muestra el contenido) y **generar** (un artefacto producido desde la fuente, como una referencia generada de la configuración).

[SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) reconoce **dos excepciones razonables**: una página que debe leerse sin conexión (un PDF para el acta) puede copiar el dato si la copia declara su origen y fecha; y un texto que debe permanecer inalterado por razones de auditoría. En ambos casos la copia no es la fuente, y se comprueba que coincide con ella.

Para que funcione hay que **vigilarlo**: un comprobador de enlaces que falle cuando una página cita una fuente inexistente, y una lista de verificación que señale las vistas a revisar cuando la fuente cambia. El síntoma contrario es el de dos páginas con topes de penalización distintos porque el dato se copió en lugar de enlazarse; la corrección es elegir una fuente, enlazar desde las demás y añadir un comprobador de enlaces.

La fuente única se complementa con el inventario de tareas por audiencia: cada vista enlaza la fuente con una frase de contexto propia de su audiencia.

## Ejemplo

El tope de penalización está en `politica/penalizacion.md`. La página para estudiantes dice «el descuento tiene un tope (ver la política)» con enlace; la guía para docentes, igual; la referencia de parámetros se genera de la configuración. Al cambiar el tope al 30 %, se edita un solo archivo y la lista de verificación marca las cuatro vistas por revisar. El PDF del acta, que sí copia el valor, lleva la fecha y la versión de la política de la que proviene. (Ilustración del mecanismo de [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).)

## Errores y confusiones comunes

- **Dos páginas con topes distintos**: el dato se copió en vez de enlazarse.
- **Fuente que nadie sabe cuál es.**
- **Copiar «solo por esta vez».**
- **Confundirla con tener un único documento enorme**: lo único es el lugar de escritura del dato.

## Límites y cuándo no aplica

Enlazar introduce dependencias: si la fuente se mueve o se borra, los enlaces se rompen; por eso hay comprobadores. Las copias legítimas (offline, auditoría) requieren control. Para datos que casi nunca cambian y se usan en un solo lugar, el costo de la fuente única es mayor que el beneficio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Audiencia](../a/audiencia.md), [Prueba de recorrido](../p/prueba-de-recorrido.md), [Tarea](../t/tarea.md), [Vista](../v/vista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis](https://diataxis.fr/) — cuatro necesidades de quien usa documentación y las formas que les corresponden; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — define una guía por su orientación a un objetivo y no a un componente; autoridad: proyecto Diátaxis.
- [Google, Technical Writing One](https://developers.google.com/tech-writing/one) — curso con una unidad sobre audiencia; autoridad: Google for Developers.
- [Digital.gov, guías de lenguaje claro](https://www.plainlanguage.gov/) — escribir y probar el contenido para su audiencia; autoridad: Digital.gov.
- [Barrio-Cantalejo et al., «Validación de la Escala INFLESZ» (Anales del Sistema Sanitario de Navarra, 2008)](https://doi.org/10.4321/S1137-66272008000300004) — interpretación de un índice de legibilidad para español en textos para pacientes; autoridad: Anales del Sistema Sanitario de Navarra.

---

[↑ Glosario](../../README.md) · [← Fuente de verdad y transformación](./fuente-de-verdad-y-transformacion.md) · [Fuentes de no determinismo →](./fuentes-de-no-determinismo.md)
