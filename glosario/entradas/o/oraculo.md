# Oráculo

[↑ Glosario](../../README.md) · [← Option value](./option-value.md) · [Oráculo y propiedades →](./oraculo-y-propiedades.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Un **oráculo** es el mecanismo que decide si el resultado de una prueba o de una operación es el esperado. Las clases lo definen con ese núcleo: [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) como el mecanismo para determinar el resultado esperado, [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) como el criterio que decide el resultado esperado, [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) como el mecanismo que decide si un resultado es correcto, y [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) y [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) como un modelo de referencia independiente (y, en [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), más simple que lo probado) con el que se compara el resultado. Una aserción, un ejemplo acordado, un esquema, un contrato, una especificación ejecutable o una evaluación con umbral son oráculos.

## Por qué importa

Una prueba solo es tan buena como su oráculo: sin una fuente de «lo correcto» independiente de lo que se prueba, la prueba confirma lo que el código ya hace. [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) lleva la idea al plano de las metodologías: casi toda disputa metodológica es una disputa de oráculo disfrazada de disputa de proceso: quién decide que algo está bien, cuándo y con qué evidencia.

## Cómo funciona

La causa de que el oráculo importe es la independencia. [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) distingue dos cosas que se complementan: las **invariantes** dicen lo que nunca debe suceder; el **oráculo** es un modelo de referencia independiente que dice qué debe suceder. [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) mostró que las primeras no bastan: un importe equivocado puede conservar el total, de modo que una invariante de suma no lo detecta y un oráculo que calcula el importe esperado sí. En cada dominio el oráculo toma una forma distinta ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)): una suma exacta en ciencia, una tabla ya idempotente en datos, un umbral con línea base en aprendizaje automático, una simulación de paso fino en juegos, una implementación lenta y simple en dinero. Lo que importa es que sea más simple que lo probado, porque un oráculo tan complejo como el sistema reproduce sus mismos errores.

## Ejemplo

En [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), una operación monetaria que reparte mal un importe puede dejar el total correcto. Una invariante («el total se conserva») pasa; un oráculo, una implementación lenta y simple del cálculo de dinero, calcula el reparto esperado y detecta la diferencia. En [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), el límite de un menú de compuertas es justamente que una prueba que replica el error escapa: se mitiga con una fuente independiente del oráculo (una especificación, una revisión humana o una evaluación de otro tipo).

## Errores y confusiones comunes

- **Una prueba que replica el error.** El valor esperado se cambió para coincidir con el código incorrecto; corrección ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)): una fuente independiente del oráculo.
- **Tomar las invariantes por oráculo.** Dicen lo que nunca debe pasar, no qué debe suceder ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)).
- **Un oráculo tan complejo como lo probado.** Reproduce los mismos errores; debe ser más simple ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)).

## Límites y cuándo no aplica

Un oráculo decide solo lo que su fuente permite decidir: una evaluación con umbral depende de su línea base ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)). [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) declara que ningún menú lo ve todo y que declarar ese límite es parte del diseño.

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
