# Último momento responsable

[↑ Glosario](../../README.md) · [← Última escritura gana](./ultima-escritura-gana.md) · [Umbral de adopción →](./umbral-de-adopcion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Punto en el que seguir esperando cuesta más que el riesgo de decidir con la evidencia disponible.

Definición de trabajo de [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md).

## Por qué importa

La clase donde se define, [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), existe con este propósito: la clase existe para que registres una decisión de arquitectura con sus alternativas, sus consecuencias y su reversibilidad, para que sepas cuánto confiar en una matriz de comparación y para que decidas cuándo conviene esperar más evidencia antes de decidir.

## Cómo funciona

Según [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md):

Decidir pronto evita el coste de la indecisión; decidir tarde permite aprender. Con una decisión **reversible y barata de revertir** conviene decidir ya y corregir si hace falta. Con una **costosa de revertir** y una evidencia que mejorará pronto, conviene esperar hasta el último momento responsable, el punto en que seguir esperando cuesta más que el riesgo de equivocarse. Esperar tiene un coste (retraso, equipos bloqueados) y solo compensa si la evidencia mejora de verdad: esperar sin aprender es solo demora. El ADR debe decir qué se sabrá después y cuándo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md):

El equipo de la plataforma escribe cuatro ADR (subir archivos por URL firmada, monolito modular, revisión asíncrona con cola, tres instancias de la aplicación) con la plantilla MADR y un comprobador de forma en el CI. Para el de servicios frente a monolito modular ejecuta el análisis de sensibilidad: el monolito gana con los pesos base y con 64,5 % de los pesos al azar, de modo que la decisión se apoya en el escenario de despliegue (un equipo de seis) y no en la suma.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se decide pronto algo caro de revertir** — causa: se ignoró el coste de la reversión. Corrección: estimarlo y esperar al último momento responsable. ([SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna arquitectura real: los puntajes, los ADR, sus defectos y el modelo de espera son construcciones del autor. La siguiente clase mira a las personas y a los equipos que toman y ejecutan estas decisiones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Riesgo](../r/riesgo.md), [ADR](../a/adr.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Registro de decisiones](../r/registro-de-decisiones.md), [Reversibilidad](../r/reversibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — origen de los ADR; autoridad: Michael Nygard.
- [MADR, Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla de ADR; autoridad: comunidad ADR.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — análisis de compromisos contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Fowler, «Architecture Decision Record»](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — práctica de ADR; autoridad: Martin Fowler.
- [Python: `re`](https://docs.python.org/3/library/re.html) — expresiones regulares del comprobador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Última escritura gana](./ultima-escritura-gana.md) · [Umbral de adopción →](./umbral-de-adopcion.md)
