# Oráculo

[↑ Glosario](../../README.md) · [← Option value](./option-value.md) · [Oráculo y propiedades →](./oraculo-y-propiedades.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Mecanismo que decide si un resultado es correcto.

Definición de trabajo de [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md): Modelo de referencia independiente y más simple que lo probado, con el que se compara el resultado.
- En [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md): Mecanismo para determinar el resultado esperado.
- En [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md): Criterio que decide el resultado esperado.
- En [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md): Modelo de referencia independiente con el que se compara el resultado de una operación.

## Por qué importa

En [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), el tema «Metodología, práctica y oráculo» importa porque sin separar el nombre de lo que produce, la elección es de gusto.

## Cómo funciona

Según [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md):

Una **metodología de desarrollo** es un conjunto de prácticas con un orden y una razón. Una **práctica** es una actividad concreta («escribir una prueba que falla antes de escribir el código»). Un **oráculo** es el mecanismo que decide si un resultado es correcto: una aserción, un ejemplo acordado, un esquema, un contrato, una especificación ejecutable, una evaluación con umbral. Casi toda disputa metodológica es una disputa de oráculo disfrazada de disputa de proceso: ¿quién decide que esto está bien, cuándo y con qué información? Poner el oráculo en el centro permite comparar lo comparable. No se compara «TDD frente a BDD» como si fueran equipos rivales; se compara qué oráculo deja cada una, qué cuesta mantenerlo y qué defectos no ve.

Según [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md):

El equipo de *Avisos* decide el cambio «silenciar un curso». Antes de escribir código rellena una tabla con una fila por práctica candidata: pregunta que responde, oráculo que deja, defectos que no ve y costo de ejecución. Para este cambio, la regla («un curso silenciado conserva solo el aviso de 1 hora») está acordada con las docentes; el riesgo es medio, porque un aviso omitido hace perder una entrega; no hay frontera entre servicios y no hay salida probabilística. La tabla recomienda ocho pruebas de ejemplo con un par de casos en los límites, más un contrato de propiedades sobre estados al azar.

## Ejemplo

Ejemplo de [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* decide el cambio «silenciar un curso». Antes de escribir código rellena una tabla con una fila por práctica candidata: pregunta que responde, oráculo que deja, defectos que no ve y costo de ejecución. Para este cambio, la regla («un curso silenciado conserva solo el aviso de 1 hora») está acordada con las docentes; el riesgo es medio, porque un aviso omitido hace perder una entrega; no hay frontera entre servicios y no hay salida probabilística. La tabla recomienda ocho pruebas de ejemplo con un par de casos en los límites, más un contrato de propiedades sobre estados al azar.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No se compara «TDD frente a BDD» como si fueran equipos rivales; se compara qué oráculo deja cada una, qué cuesta mantenerlo y qué defectos no ve. ([SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md))
- Aplica el mapa a un cambio real: escribe la pregunta dominante, la práctica que elegirías, el oráculo que deja y el defecto que no vería. ([SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Referencia independiente](../r/referencia-independiente.md), [Mecanismo](../m/mecanismo.md), [Modelo](../m/modelo.md), [Operación](./operacion.md), [Contrato](../c/contrato.md), [Control](../c/control.md).
- **Se confunde con:** **Cómo leer la figura.** Cada barra es un oráculo (una forma de decidir si el comportamiento es correcto) y su largo cuenta los mutantes que mata, de los 18 no equivalentes; la línea discontinua es el total.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (30 clases más lo mencionan; las que más):

[SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-218, «Secure Software Development Framework (SSDF)»](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro y conservación de evidencia; autoridad: NIST.
- [Architectural Decision Records](https://adr.github.io/) — registro de decisiones con contexto y consecuencias; autoridad: comunidad ADR.
- [Saltelli et al., «Global Sensitivity Analysis: The Primer» (2008)](https://doi.org/10.1002/9780470725184) — análisis de sensibilidad global; autoridad: Wiley.
- [Peng, «Reproducible Research in Computational Science» (Science, 2011)](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad; autoridad: Science.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Option value](./option-value.md) · [Oráculo y propiedades →](./oraculo-y-propiedades.md)
