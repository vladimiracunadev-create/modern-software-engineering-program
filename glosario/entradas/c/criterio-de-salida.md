# Criterio de salida

[↑ Glosario](../../README.md) · [← Criterio de retroceso](./criterio-de-retroceso.md) · [Criterio delegado →](./criterio-delegado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Condición comprobable que debe cumplirse para dar un trabajo por terminado.

Definición de trabajo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-012 — Proyecto: mapa profesional y contrato personal de aprendizaje](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md): Condición verificable para avanzar.
- En [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md): Condición observable para cerrar una fase.

## Por qué importa

En [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), el tema «Criterios de salida» importa porque sin criterios no hay forma de decir que está terminado.

## Cómo funciona

Según [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

El equipo de la API de entregas ensambla su camino. Cada versión pasa por la integración con ramas de menos de dos días, el grafo de trabajos con un camino crítico de 14 minutos, las compuertas ordenadas por razón de detección, el escaneo de secretos que siempre bloquea, la política sobre el plan de infraestructura, una preproducción con datos sintéticos, un canario del 5 % con criterio de retroceso automático y la observación de las métricas con intervalos. Los cambios de esquema siguen el cambio en paralelo: el equipo ensaya el retroceso cada mes en preproducción, con la versión anterior leyendo los datos que escribió la nueva, y la contracción es un cambio aparte, treinta días después, con aprobación de una segunda persona.

Según [SE-012 — Proyecto: mapa profesional y contrato personal de aprendizaje](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md):

El trabajo en curso limitado evita acumular diez cursos sin evidencia. Un experimento breve produce un artefacto revisable y una decisión: avanzar, repetir, dividir o cambiar estrategia. El criterio de salida no es “sentirme experto”, sino una observación que una persona revisora puede verificar.

## Ejemplo

Ejemplo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas ensambla su camino. Cada versión pasa por la integración con ramas de menos de dos días, el grafo de trabajos con un camino crítico de 14 minutos, las compuertas ordenadas por razón de detección, el escaneo de secretos que siempre bloquea, la política sobre el plan de infraestructura, una preproducción con datos sintéticos, un canario del 5 % con criterio de retroceso automático y la observación de las métricas con intervalos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **completar un curso es criterio de salida** — causa: consumo confundido con desempeño. Corrección: exige tarea, evidencia y revisión externa. ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El criterio de salida no es “sentirme experto”, sino una observación que una persona revisora puede verificar. ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md))
- **Corrección:** reduce el trabajo en curso a uno, dos o tres experimentos; ordena por dependencia (qué habilita qué) y por riesgo; y exige para cada uno un artefacto, un criterio de salida y una revisión. ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Trabajo](../t/trabajo.md), [Actor](../a/actor.md), [Ambigüedad](../a/ambiguedad.md), [Brecha](../b/brecha.md), [Competencia](./competencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-012 — Proyecto: mapa profesional y contrato personal de aprendizaje](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Criterios de salida».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler: ParallelChange](https://martinfowler.com/bliki/ParallelChange.html) — patrón expandir, migrar y contraer; autoridad: Martin Fowler.
- [Fowler y Sadalage: Evolutionary Database Design](https://martinfowler.com/articles/evodb.html) — cambios de base de datos continuos; autoridad: Martin Fowler y Pramod Sadalage.
- [SLSA: niveles de la especificación v1.1](https://slsa.dev/spec/v1.1/levels) — procedencia y garantías de un artefacto; autoridad: proyecto SLSA, OpenSSF.
- [Google SRE Book: Release Engineering](https://sre.google/sre-book/release-engineering/) — práctica de ingeniería de entregas; autoridad: Google.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — cambios de esquema admitidos por el motor; autoridad: documentación de SQLite.

---

[↑ Glosario](../../README.md) · [← Criterio de retroceso](./criterio-de-retroceso.md) · [Criterio delegado →](./criterio-delegado.md)
