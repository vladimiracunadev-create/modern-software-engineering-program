# Criterio de salida

[↑ Glosario](../../README.md) · [← Criterio de retroceso](./criterio-de-retroceso.md) · [Criterio delegado →](./criterio-delegado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Un **criterio de salida** es la condición comprobable que debe cumplirse para dar un trabajo por terminado o para avanzar a la etapa siguiente ([SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md)). Según el contexto: condición verificable para avanzar ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md)) o condición observable para cerrar una fase ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md)). Lo esencial es que lo pueda verificar alguien distinto de quien hizo el trabajo.

## Por qué importa

Sin criterio de salida, «terminado» es una sensación. El trabajo se declara completo por cansancio, por calendario o por completar actividades en vez de resultados. [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md) lo muestra en el aprendizaje profesional: el criterio no es «sentirme experto» sino una observación que una persona revisora puede verificar. En entrega continua ([SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md)), cada etapa tiene criterio de paso o de retroceso, y eso es lo que permite automatizar la decisión.

## Cómo funciona

Un buen criterio es **observable, binario y externo**:

- *observable:* se puede medir o inspeccionar, no depende de opinión;
- *binario:* se cumple o no;
- *externo:* lo verifica otra persona o un sistema, no solo el autor.

[SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md) pide para cada experimento un artefacto, un criterio de salida y una revisión, y limita el trabajo en curso para no acumular diez cursos sin evidencia. En [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), el camino de entrega encadena criterios: ramas de menos de dos días, compuertas ordenadas por razón de detección, escaneo de secretos que siempre bloquea, canario del 5 % con criterio de retroceso automático y observación de métricas con intervalos. Cada paso responde a la pregunta «¿qué debe ser verdad para pasar?».

## Ejemplo

[SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md): un canario del 5 % tiene un criterio de retroceso automático; si la métrica cruza el umbral, la versión se retira sin pedir permiso. Ilustración de formulación débil frente a fuerte:

- Débil: «el módulo está casi listo».
- Fuerte: «las 12 pruebas de aceptación pasan en CI y una segunda persona revisó el diff».

## Errores y confusiones comunes

- **«Completar un curso» como criterio de salida.** Causa: consumo confundido con desempeño; corrección: exigir tarea, evidencia y revisión externa ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md)).
- **Criterio que depende de una opinión.** No puede automatizarse ni discutirse.
- **Confundir criterio de salida con criterio de aceptación.** El primero cierra una fase o etapa; el segundo valida un requisito concreto.

## Límites y cuándo no aplica

Un criterio verificable puede medir lo equivocado y dar falsa seguridad (cumplir el umbral sin cumplir el objetivo). En trabajo exploratorio, fijar un criterio demasiado temprano puede cerrar preguntas; entonces el criterio es una decisión (avanzar, repetir, dividir o cambiar estrategia, [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md)) más que un umbral. Y un criterio que nadie revisa es solo un texto.

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
