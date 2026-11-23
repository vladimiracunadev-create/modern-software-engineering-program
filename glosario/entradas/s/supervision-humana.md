# Supervisión humana

[↑ Glosario](../../README.md) · [← Superficie de ataque](./superficie-de-ataque.md) · [Suposición →](./suposicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Capacidad de una persona de entender, ignorar o revertir la salida de un sistema.

Definición de trabajo de [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md).

## Por qué importa

La clase donde se define, [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), existe con este propósito: la clase existe para que conviertas el gobierno de la inteligencia artificial en trabajo de ingeniería con evidencia, y no en un documento que se redacta al final.

## Cómo funciona

Según [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md):

Para los sistemas de alto riesgo, el reglamento enumera requisitos que se traducen en trabajo de ingeniería: un sistema de gestión de riesgos durante todo el ciclo de vida (art. 9), gobierno de los datos de entrenamiento, validación y prueba, incluida la revisión de sesgos (art. 10), documentación técnica (art. 11), registro automático de eventos (art. 12), transparencia e instrucciones para quien lo usa (art. 13), supervisión humana diseñada en el sistema (art. 14) y niveles adecuados de exactitud, robustez y ciberseguridad a lo largo del ciclo de vida (art. 15). A ello se suman un sistema de gestión de la calidad, la evaluación de conformidad, la vigilancia posterior a la comercialización (art. 72) y la notificación de incidentes graves (art. 73).

Según [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md):

El equipo de *Avisos-ML* crea el expediente de gobierno antes de aceptar los dos usos nuevos. Empieza por un inventario de tres sistemas de IA con uso, dueño y datos. Aplica el triaje: el recordatorio queda en riesgo limitado; la priorización de llamadas se marca para revisión, porque afecta el acceso a apoyo; la asignación de plazas de refuerzo queda como candidata a alto riesgo, y el comité decide no proceder con ese uso hasta consultar al área jurídica. Construye la tabla de evidencia: de los veinte elementos de documentación, once existen y apuntan a artefactos, cinco están en preparación y cuatro (la supervisión humana y la transparencia ante la persona) no existen.

## Ejemplo

Ejemplo de [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* crea el expediente de gobierno antes de aceptar los dos usos nuevos. Empieza por un inventario de tres sistemas de IA con uso, dueño y datos. Aplica el triaje: el recordatorio queda en riesgo limitado; la priorización de llamadas se marca para revisión, porque afecta el acceso a apoyo; la asignación de plazas de refuerzo queda como candidata a alto riesgo, y el comité decide no proceder con ese uso hasta consultar al área jurídica.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La supervisión humana efectiva exige que la persona pueda entender la salida, tenga información suficiente, pueda ignorar o revertir la decisión y no esté presionada a aceptarla. ([SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Alto riesgo](../a/alto-riesgo.md), [Ficha del modelo](../f/ficha-del-modelo.md), [Registro de decisiones](../r/registro-de-decisiones.md), [Registro encadenado](../r/registro-encadenado.md), [Sistema de gestión de IA](./sistema-de-gestion-de-ia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Superficie de ataque](./superficie-de-ataque.md) · [Suposición →](./suposicion.md)
