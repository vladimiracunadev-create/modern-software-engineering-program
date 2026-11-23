# Explicación

[↑ Glosario](../../README.md) · [← Experto en información](./experto-en-informacion.md) · [Explicación fiel →](./explicacion-fiel.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Página que aporta contexto, causas y alternativas para comprender, sin pasos ni listados.

Definición de trabajo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).

## Por qué importa

En [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), el tema «Explicación» importa porque aporta contexto, alternativas y porqués; es la única donde caben las tensiones.

## Cómo funciona

Según [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), en la sección «Explicación»:

La explicación responde a «¿por qué?» y «¿qué alternativas había?». Es la única donde caben el contexto histórico, las tensiones entre dos buenas razones y las decisiones que podrían cambiar. No se lee con prisa y no se ejecuta; se mide en lo que permite entender. Es también el tipo que más se omite, porque no tiene una tarea inmediata, y por eso la gente reinventa decisiones ya tomadas. En la plataforma, la explicación dice por qué la penalización es diaria y con tope, qué se probó antes y qué se rechazó, y enlaza al registro de decisiones.

## Ejemplo

Ejemplo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sección «Ejemplo profesional»):

La plataforma separa la penalización en cuatro páginas con nombres propios: un tutorial («Tu primera entrega con retraso»), una guía («Cambiar el tope de penalización de un curso»), una referencia («Parámetros de penalización») y una explicación («Por qué la penalización es diaria y con tope»). Cada una enlaza a las otras tres en una línea al comienzo o al final. El tutorial y la guía se ejecutan en la integración continua; la referencia se genera de la configuración; la explicación se revisa cuando cambia la política. Una persona nueva empieza por el tutorial, una docente va directo a la guía y una auditora lee la explicación.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El tutorial tiene una sección «Notas avanzadas» a mitad de los pasos** — causa: se mezcló explicación con guía de aprendizaje. Corrección: mover las notas a una explicación y dejar un enlace de una línea. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- **La guía práctica empieza con la historia de la política** — causa: se mezcló contexto con procedimiento. Corrección: mover la historia a la explicación y enlazarla desde el primer párrafo. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- **La referencia dice «se recomienda» en varios parámetros** — causa: se mezcló opinión con descripción. Corrección: trasladar las recomendaciones a una guía o una explicación. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No explica por qué las cosas son así; a lo sumo dice «ahora verás» y da una frase de contexto que lo enlaza a la explicación. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- Hay componentes que solo necesitan referencia (una opción de configuración) y otros que piden explicación (una decisión de diseño). ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Página](../p/pagina.md), [Guía práctica](../g/guia-practica.md), [Página mixta](../p/pagina-mixta.md), [Referencia](../r/referencia.md), [Tutorial](../t/tutorial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (468 clases más lo mencionan; las que más):

[SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md), [SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: explicación](https://diataxis.fr/explanation/) — contexto y alternativas; autoridad: proyecto Diátaxis.
- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.
- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Experto en información](./experto-en-informacion.md) · [Explicación fiel →](./explicacion-fiel.md)
