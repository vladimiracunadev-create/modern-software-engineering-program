# Explicación

[↑ Glosario](../../README.md) · [← Experto en información](./experto-en-informacion.md) · [Explicación fiel →](./explicacion-fiel.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

En documentación técnica, una **explicación** es una página que aporta contexto, causas y alternativas para comprender, sin pasos ni listados. Es el sentido de [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (tutoriales, how-to, referencia y explicación), donde es uno de los cuatro tipos de página, junto al tutorial, la guía práctica y la referencia. No se usa aquí como «explicar algo en general», sino como tipo de documento con función propia.

## Por qué importa

Cambia dónde se escriben los porqués. Según [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), es la única página donde caben las tensiones entre dos buenas razones. Es también el tipo que más se omite, porque no tiene una tarea inmediata, y por eso la gente reinventa decisiones ya tomadas.

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

No todo componente necesita explicación: una opción de configuración solo necesita referencia, mientras que una decisión de diseño pide explicación ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md)). Una explicación sin fecha ni dueño envejece y se vuelve fuente de errores; conviene revisarla cuando cambia la decisión que describe. Tampoco sustituye a un registro de decisiones fechado donde haga falta trazabilidad formal.

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
