# Alto riesgo

[↑ Glosario](../../README.md) · [← Alternativas existentes](./alternativas-existentes.md) · [Ambassador →](./ambassador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Categoría del reglamento europeo con requisitos estrictos, definida por el uso y el ámbito.

Definición de trabajo de [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md).

## Por qué importa

En [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), el tema «Requisitos de alto riesgo» importa porque piden riesgo, datos, documentación, registro, supervisión y robustez.

## Cómo funciona

Según [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md):

El AI Act clasifica por el uso previsto: unas prácticas se prohíben (art. 5), unos usos se consideran de alto riesgo (art. 6 y el anexo III, que incluye ciertos usos en educación, empleo, servicios esenciales, biometría y otros), algunos sistemas tienen obligaciones de transparencia (art. 50: informar de que se interactúa con una IA, marcar contenido sintético) y el resto queda en un régimen de buenas prácticas voluntarias. Para la educación, el anexo III cita, entre otros usos, determinar el acceso o la admisión a instituciones, evaluar los resultados de aprendizaje y vigilar conductas prohibidas durante los exámenes. La consecuencia de ingeniería: antes de discutir controles hay que escribir el uso, y cualquier cambio de uso reabre la clasificación.

Según [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md):

El equipo de *Avisos-ML* crea el expediente de gobierno antes de aceptar los dos usos nuevos. Empieza por un inventario de tres sistemas de IA con uso, dueño y datos. Aplica el triaje: el recordatorio queda en riesgo limitado; la priorización de llamadas se marca para revisión, porque afecta el acceso a apoyo; la asignación de plazas de refuerzo queda como candidata a alto riesgo, y el comité decide no proceder con ese uso hasta consultar al área jurídica. Construye la tabla de evidencia: de los veinte elementos de documentación, once existen y apuntan a artefactos, cinco están en preparación y cuatro (la supervisión humana y la transparencia ante la persona) no existen.

## Ejemplo

Ejemplo de [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* crea el expediente de gobierno antes de aceptar los dos usos nuevos. Empieza por un inventario de tres sistemas de IA con uso, dueño y datos. Aplica el triaje: el recordatorio queda en riesgo limitado; la priorización de llamadas se marca para revisión, porque afecta el acceso a apoyo; la asignación de plazas de refuerzo queda como candidata a alto riesgo, y el comité decide no proceder con ese uso hasta consultar al área jurídica.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md)) son: El triaje, la lista de verificación, el generador de dos grupos y los umbrales son construcciones del autor sobre ocho usos inventados y datos sintéticos; no son una clasificación jurídica ni una evaluación de conformidad. El calendario del reglamento se tomó de la página de la Comisión consultada para esta clase y puede haber cambiado. No se evaluó ninguna herramienta de gobierno ni se auditó ninguna organización.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ficha del modelo](../f/ficha-del-modelo.md), [Registro de decisiones](../r/registro-de-decisiones.md), [Registro encadenado](../r/registro-encadenado.md), [Sistema de gestión de IA](../s/sistema-de-gestion-de-ia.md), [Sistema de IA](../s/sistema-de-ia.md), [Supervisión humana](../s/supervision-humana.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Alternativas existentes](./alternativas-existentes.md) · [Ambassador →](./ambassador.md)
