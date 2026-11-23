# Consenso perezoso

[↑ Glosario](../../README.md) · [← Consenso](./consenso.md) · [Consentimiento →](./consentimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Regla por la que una propuesta se acepta si nadie objeta en un plazo.

Definición de trabajo de [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md).

## Por qué importa

La clase donde se define, [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), existe con este propósito: la clase existe para que abrir un proyecto a personas que no pertenecen al equipo sea una decisión con reglas visibles: cómo se contribuye, quién decide, qué pasa cuando alguien se va y cómo se mantiene al día una copia propia.

## Cómo funciona

Según [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md):

Un proyecto decide cómo acepta cambios o propuestas: un líder con la última palabra, votación por mayoría, aprobación por consenso con veto, o consenso por falta de objeción en un plazo (consenso perezoso). Cada regla tolera errores distintos: la que acepta por silencio es rápida y deja pasar lo que nadie leyó; la que exige votos mínimos se bloquea si faltan votantes. La disponibilidad de las personas decide cuál es adecuada.

Según [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md):

Reproduce el fallo clásico de la clase: **aceptar por silencio una propuesta que nadie leyó**. Usa el consenso perezoso con 30 % de disponibilidad.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md):

La plataforma publica `CONTRIBUTING.md` con el entorno, el formato de ramas, la plantilla de PR, el tiempo objetivo de primera respuesta y lo que no se acepta. Una regla de decisión escrita: los cambios pequeños los aprueba una mantenedora; los que modifican una regla de negocio exigen dos aprobaciones y un plazo de 72 horas; los cambios de gobierno exigen consenso. Un indicador mensual muestra cuántas personas cubren la mitad de los commits y qué rutas solo conoce una, para planificar relevos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se aceptan cambios de reglas que nadie leyó** — causa: consenso perezoso con poca disponibilidad. Corrección: exigir aprobación explícita para cambios de riesgo. ([SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos y repositorios temporales en Windows y Ubuntu (WSL2) con resultados idénticos. Los contribuyentes, las probabilidades y los desfases son supuestos del autor, con seis semillas en el experimento de Git, y no se midió ninguna comunidad real. La siguiente clase pregunta bajo qué licencia se reciben y se redistribuyen las contribuciones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plazo](../p/plazo.md), [Regla](../r/regla.md), [Código de conducta](./codigo-de-conducta.md), [Concentración de conocimiento](./concentracion-de-conocimiento.md), [Fork](../f/fork.md), [Regla de decisión](../r/regla-de-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Open Source Guides: liderazgo y gobernanza](https://opensource.guide/leadership-and-governance/) — estructuras de gobierno habituales; autoridad: Open Source Guides.
- [Apache: proceso de votación](https://www.apache.org/foundation/voting.html) — tipos de voto, consenso y periodos mínimos; autoridad: Apache Software Foundation.
- [PEP 13: modelo de gobierno de Python](https://peps.python.org/pep-0013/) — transición de un líder benevolente a un consejo; autoridad: Python Software Foundation.
- [Contributor Covenant](https://www.contributor-covenant.org/) — código de conducta para comunidades digitales; autoridad: Contributor Covenant.
- [GitHub: sincronizar un fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) — actualizar una copia con el original; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Consenso](./consenso.md) · [Consentimiento →](./consentimiento.md)
