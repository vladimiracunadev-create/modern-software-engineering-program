# Contrato y corpus de comparación

[↑ Glosario](../../README.md) · [← Contrato versionado](./contrato-versionado.md) · [Contribución revisable →](./contribucion-revisable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

El proyecto congela vocabulario, esquema de entrada, resultados y errores.

Definición de trabajo de [SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md).

## Por qué importa

En [SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), el tema «Contrato y corpus de comparación» importa porque el proyecto congela vocabulario, esquema de entrada, resultados y errores.

## Cómo funciona

Según [SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), en la sección «Contrato y corpus de comparación»:

El proyecto congela vocabulario, esquema de entrada, resultados y errores. El corpus incluye ejemplos, límites, secuencias y cambios de política. Versionarlo evita ajustar casos después de ver qué implementación favorecen.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md)) son:

- **El informe afirma sin comando reproducible** — causa: no se registró la evidencia. Corrección: añadir comando, versión y salida a cada afirmación.
- **La suite pasa y hay defectos** — causa: casos de camino feliz sin límites ni inválidos. Corrección: derivar casos del contrato y de los mutantes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El proyecto demuestra equivalencia para el corpus y propiedades declaradas, no para todas las entradas posibles ni para cargas de producción. La [Parte 7](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md) usará el comportamiento acordado para estudiar estructuras y algoritmos bajo una carga explícita.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Esquema](../e/esquema.md), [Resultado](../r/resultado.md), [Informe de decisión](../i/informe-de-decision.md), [Métricas interpretadas](../m/metricas-interpretadas.md), [Oráculo y propiedades](../o/oraculo-y-propiedades.md), [Reproducción y revisión](../r/reproduccion-y-revision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-084 — Proyecto: comparación semántica con pruebas comunes](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Contrato versionado](./contrato-versionado.md) · [Contribución revisable →](./contribucion-revisable.md)
