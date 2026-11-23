# Gate

[↑ Glosario](../../README.md) · [← Garantías de entrega](./garantias-de-entrega.md) · [Gateway →](./gateway.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Punto de la integración continua que bloquea o avisa según un umbral.

Definición de trabajo de [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md).

## Por qué importa

La clase donde se define, [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), existe con este propósito: el proyecto integra la parte en un artefacto: una estrategia de pruebas ejecutable para la plataforma de entregas, con riesgos y su reparto de horas, el nivel de prueba de cada clase de fallo, las pruebas que lo sostienen y su demostración, los criterios de bloqueo, las exclusiones con caducidad y los límites.

## Cómo funciona

Según [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md):

El paquete es un archivo estructurado (JSON) con las decisiones: por componente, su probabilidad y su impacto estimados, su clase de fallo, el nivel de prueba que la ve, las horas asignadas, los nombres de las pruebas y la demostración que las respalda; una lista de gates con su umbral y su acción (bloquear o avisar); una lista de exclusiones con razón y caducidad; y los límites. La estructura obliga a que cada riesgo tenga pruebas, cada prueba un riesgo y cada exclusión una fecha, y permite que un programa lo valide.

Según [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md):

El equipo de la plataforma versiona `estrategia.json` en el repositorio y lo valida en la integración continua con el programa de `SE-432`. El paquete lista nueve componentes probados con horas asignadas por el reparto marginal con exposición (con un piso de 4 horas para impacto 9 o 10 que añadió el equipo tras discutir la autenticación), tres exclusiones con razón y caducidad a 75 días y dos gates: el rápido (diez minutos, bloquea con pruebas unitarias, de contrato y las de integración por interfaz) y el nocturno (90 minutos, avisa con extremo a extremo, carga ligera y una sesión de exploración trimestral). Cada prueba del paquete tiene una demostración rojo-verde de `SE-431`.

## Ejemplo

Ejemplo de [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma versiona `estrategia.json` en el repositorio y lo valida en la integración continua con el programa de `SE-432`. El paquete lista nueve componentes probados con horas asignadas por el reparto marginal con exposición (con un piso de 4 horas para impacto 9 o 10 que añadió el equipo tras discutir la autenticación), tres exclusiones con razón y caducidad a 75 días y dos gates: el rápido (diez minutos, bloquea con pruebas unitarias, de contrato y las de integración por interfaz) y el nocturno (90 minutos, avisa con extremo a extremo, carga ligera y una sesión de exploración trimestral).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)) son:

- **La estrategia es un documento que nadie ejecuta** — causa: no hay validador ni vínculo con la integración continua. Corrección: paquete estructurado y validado en cada cambio.
- **Un riesgo alto queda sin horas o sin nivel que lo vea** — causa: falta de reglas de coherencia. Corrección: reglas de riesgo en el validador.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El paquete contiene los nueve componentes probados (con nivel, horas y pruebas), la exclusión de la búsqueda con razón y caducidad a 75 días, dos gates (uno bloquea y otro avisa) y los límites. ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Integración continua](../i/integracion-continua.md), [Escape](../e/escape.md), [Estrategia de pruebas](../e/estrategia-de-pruebas.md), [Exclusión](../e/exclusion.md), [Exposición](../e/exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Garantías de entrega](./garantias-de-entrega.md) · [Gateway →](./gateway.md)
