# Reformular como problema

[↑ Glosario](../../README.md) · [← Reformulación](./reformulacion.md) · [Refresco incremental →](./refresco-incremental.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

**Reformular como problema** es pasar de una petición a un enunciado de actor, intención, obstáculo y consecuencia que no nombra la solución y que se puede confirmar o refutar con observaciones ([SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md)). Es el paso que sigue a descomponer la petición y a agrupar por necesidad.

## Por qué importa

El problema reformulado admite varias soluciones y puede contrastarse con observaciones. Una petición como «necesito un panel» fija una solución y esconde el problema; reformularla abre alternativas y permite comprobar si el problema existe. Cambia la conversación con quien pide: de discutir la solución a acordar el problema.

## Cómo funciona

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) da el ejemplo: de «necesito un panel» se pasa a «los docentes tardan 40 minutos por entrega en saber quiénes no han entregado porque deben abrir cada archivo por separado, y por eso avisan tarde». El enunciado **mantiene el actor** (los docentes), **expresa el obstáculo** (abrir cada archivo por separado) y **la consecuencia** (avisan tarde), y **deja abiertas varias soluciones**: un panel, un correo automático, una lista exportable.

El enunciado se **contrasta** pidiendo a dos o tres docentes que cuenten el último episodio y comprobando si el tiempo y el obstáculo aparecen. Para decidir si un enunciado está bien formado, se aplica la **rúbrica de investigabilidad**: actor reconocible, obstáculo observable, consecuencia y ausencia de solución embebida. Un script puede comprobar la forma, pero una segunda persona debe confirmar que el problema es real: un enunciado puede pasar el linter y no reconocerse como real.

Dos reglas del archivo de trabajo: la **petición original no se sobrescribe**, y el problema reformulado indica **qué observación lo confirmaría**. Así queda claro qué dato haría cambiar de idea. La reformulación se relaciona con las necesidades («necesito… para…»), pero es más específica: incluye el obstáculo y la consecuencia observados.

## Ejemplo

Petición: «Necesito un panel para ver quién no entregó». Problema reformulado: «Los docentes tardan unos 40 minutos por lote en saber quiénes no han entregado, porque abren cada archivo por separado, y por eso reclaman tarde». Observación que lo confirmaría: tiempos medidos o relatados por dos o tres docentes sobre su último lote. Soluciones abiertas: panel, correo automático, lista exportable. (Caso de [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md).)

## Errores y confusiones comunes

- **«Sí» a todo y el panel no se usa**: preguntas guiadas o hipotéticas; corrección: preguntar por episodios pasados.
- **Backlog con peticiones distintas que son iguales**: no se agruparon por necesidad.
- **Enunciado con solución disfrazada** («falta un botón…»).
- **No indicar qué observación lo confirmaría.**

## Límites y cuándo no aplica

Un buen enunciado no prueba que el problema merezca resolverse; eso depende de su tamaño. Los experimentos de [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) usan peticiones sintéticas y una sola persona etiquetó, de modo que el método es ilustrativo. Para peticiones triviales y reversibles, el rodeo no se justifica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actor](../a/actor.md), [Consecuencia](../c/consecuencia.md), [Evidencia](../e/evidencia.md), [Intención](../i/intencion.md), [Agrupar por necesidad](../a/agrupar-por-necesidad.md), [Descomponer la petición](../d/descomponer-la-peticion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — reformular una solución dada como problema; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato y validación de necesidades; autoridad: Government Digital Service.
- [The Mom Test](https://www.momtestbook.com/) — preguntar por hechos pasados; autoridad: autor (guía práctica, no estudio empírico).
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — introducción a la entrevista de usuario; autoridad: Nielsen Norman Group.
- [McHugh: Interrater reliability, the kappa statistic](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) — kappa frente al acuerdo bruto; autoridad: revisión indexada en PubMed Central.

---

[↑ Glosario](../../README.md) · [← Reformulación](./reformulacion.md) · [Refresco incremental →](./refresco-incremental.md)
