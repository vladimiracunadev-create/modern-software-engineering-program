# Exclusión

[↑ Glosario](../../README.md) · [← Excepción registrada](./excepcion-registrada.md) · [Exhaustividad →](./exhaustividad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Decisión de no probar algo, con razón, responsable y fecha de revisión.

Definición de trabajo de [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md): Decisión explícita de no probar un componente o una clase de fallo, con razón y fecha de revisión.

## Por qué importa

En [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), el tema «Exclusiones y límites» importa porque lo que no se prueba debe constar.

## Cómo funciona

Según [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md):

El paquete es un archivo estructurado (JSON) con las decisiones: por componente, su probabilidad y su impacto estimados, su clase de fallo, el nivel de prueba que la ve, las horas asignadas, los nombres de las pruebas y la demostración que las respalda; una lista de gates con su umbral y su acción (bloquear o avisar); una lista de exclusiones con razón y caducidad; y los límites. La estructura obliga a que cada riesgo tenga pruebas, cada prueba un riesgo y cada exclusión una fecha, y permite que un programa lo valide.

Según [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md):

El equipo de la plataforma versiona `estrategia.json` en el repositorio y lo valida en la integración continua con el programa de `SE-432`. El paquete lista nueve componentes probados con horas asignadas por el reparto marginal con exposición (con un piso de 4 horas para impacto 9 o 10 que añadió el equipo tras discutir la autenticación), tres exclusiones con razón y caducidad a 75 días y dos gates: el rápido (diez minutos, bloquea con pruebas unitarias, de contrato y las de integración por interfaz) y el nocturno (90 minutos, avisa con extremo a extremo, carga ligera y una sesión de exploración trimestral). Cada prueba del paquete tiene una demostración rojo-verde de `SE-431`.

## Ejemplo

Ejemplo de [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) (sección «Ejemplo mínimo»):

El fragmento valida una exclusión. Antes de ejecutarlo, predice cuál de las dos pasa.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las exclusiones nunca se revisan** — causa: sin caducidad. Corrección: fecha de caducidad menor de 90 días y revisión. ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md))
- **Lo que no se prueba nadie lo sabe** — causa: omisión silenciosa. Corrección: lista de exclusiones con razón, responsable y caducidad. ([SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una exclusión sin caducidad se convierte en una omisión; una con caducidad vence y obliga a revisarla. ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fecha de revisión](../f/fecha-de-revision.md), [Componente](../c/componente.md), [Revisión](../r/revision.md), [Escape](./escape.md), [Estrategia de pruebas](./estrategia-de-pruebas.md), [Exposición](./exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (25 clases más lo mencionan; las que más):

[SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de verificación; autoridad: NIST.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — atributos de calidad; autoridad: ISO/IEC.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — evaluación de riesgos; autoridad: NIST.
- [Libro de SRE de Google: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas y fiabilidad; autoridad: Google SRE.
- [DORA: automatización de pruebas](https://dora.dev/capabilities/test-automation/) — capacidad de pruebas automatizadas; autoridad: DORA.

---

[↑ Glosario](../../README.md) · [← Excepción registrada](./excepcion-registrada.md) · [Exhaustividad →](./exhaustividad.md)
