# Restricción dura

[↑ Glosario](../../README.md) · [← Restricción de integridad](./restriccion-de-integridad.md) · [Restricción única →](./restriccion-unica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Condición no negociable dentro del alcance.

Definición de trabajo de [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md).

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md):

**Cómo leer la figura.** Cada etapa tiene una función distinta. Las restricciones duras *eliminan*; las preferencias *ordenan* lo que queda; los supuestos *completan* lo que falta y llevan una condición de revisión. El recuadro rojo muestra el fallo clásico: si todo deseo se declara innegociable, el filtro deja una opción y la comparación se vuelve teatro. **Dónde deja de valer:** el embudo presenta las restricciones como datos. En la práctica también se negocian: una restricción con autoridad capaz de cambiarla puede relajarse si el costo de mantenerla es mayor que el de discutirla; por eso debe registrar fuente y quién puede modificarla.

Según [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md):

Toma la tabla de tres opciones y declara a propósito todas las preferencias como restricciones duras («debe ser instantáneo, mínimo costo, máxima seguridad y entrega inmediata»). **Síntoma:** no queda ninguna opción viable, o queda exactamente la que alguien prefería de antemano. **Causa:** se confundieron preferencias con restricciones. **Corrección:** para cada restricción registra fuente (contrato, norma, límite físico), vigencia y autoridad capaz de cambiarla; las que no tengan fuente pasan a preferencias con un peso. Después cambia una restricción en una revisión cruzada y comprueba que la conclusión cambie *sin reescribir los criterios* una vez conocido el resultado: esa es la prueba de que la tabla no fue construida hacia una respuesta.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md):

Una entidad evalúa biometría: reduce fraude, pero agrega datos sensibles, exclusión y dependencia. Compara biometría obligatoria, opcional con alternativa y no adopción; incluye borrado y apelación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md)) son:

- **solo existe una opción “viable”** — causa: preferencias se presentaron como restricciones. Corrección: verifica fuente, vigencia y autoridad de cada límite.
- **riesgo escrito como sustantivo** — causa: faltan causa y consecuencia. Corrección: formula cadena causal, señal, mitigación y contingencia.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md)) son: La matriz no monetiza dignidad ni resuelve regulación. `SE-009` amplía horizonte social y ambiental.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Condición](../c/condicion.md), [Contingencia](../c/contingencia.md), [Exposición](../e/exposicion.md), [Mitigación](../m/mitigacion.md), [Preferencia](../p/preferencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-056](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Restricción de integridad](./restriccion-de-integridad.md) · [Restricción única →](./restriccion-unica.md)
