# Guía práctica

[↑ Glosario](../../README.md) · [← Guardrail o barrera](./guardrail-o-barrera.md) · [Guion de inyección →](./guion-de-inyeccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Página orientada a un objetivo de trabajo concreto que supone competencia previa y admite bifurcaciones.

Definición de trabajo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).

## Por qué importa

En [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), el tema «Guía práctica» importa porque resuelve un objetivo de trabajo y supone competencia previa; no enseña desde cero.

## Cómo funciona

Según [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), en la sección «Guía práctica»:

Una guía práctica responde a un objetivo concreto del trabajo («cambiar el tope de penalización»), da por sentado que quien la lee sabe lo básico y evita enseñar. Es una receta con precondiciones, pasos y una forma de comprobar que funcionó. Se distingue del tutorial porque admite bifurcaciones («si el curso tiene prórrogas activas, antes haz esto») y porque no garantiza que sea la primera vez de nadie. Su error típico es crecer: se le añaden definiciones, el porqué del tope, una tabla de parámetros, y deja de ser una guía. Lo que sobra se enlaza.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md):

La plataforma separa la penalización en cuatro páginas con nombres propios: un tutorial («Tu primera entrega con retraso»), una guía («Cambiar el tope de penalización de un curso»), una referencia («Parámetros de penalización») y una explicación («Por qué la penalización es diaria y con tope»). Cada una enlaza a las otras tres en una línea al comienzo o al final. El tutorial y la guía se ejecutan en la integración continua; la referencia se genera de la configuración; la explicación se revisa cuando cambia la política.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La guía práctica empieza con la historia de la política** — causa: se mezcló contexto con procedimiento. Corrección: mover la historia a la explicación y enlazarla desde el primer párrafo. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md)) son: Las definiciones son operativas para el portal; no reemplazan la formulación de Diátaxis, que se enlaza abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ningún lector ni se evaluó una documentación existente: el clasificador usa las palabras con que se escribieron los párrafos, el orden aleatorio de secciones es un supuesto y el tutorial es una biblioteca de juguete.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Competencia](../c/competencia.md), [Página](../p/pagina.md), [Trabajo](../t/trabajo.md), [Explicación](../e/explicacion.md), [Página mixta](../p/pagina-mixta.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.
- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.
- [Diátaxis: explicación](https://diataxis.fr/explanation/) — contexto y alternativas; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Guardrail o barrera](./guardrail-o-barrera.md) · [Guion de inyección →](./guion-de-inyeccion.md)
