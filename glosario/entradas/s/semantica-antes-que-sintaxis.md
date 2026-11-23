# Semántica antes que sintaxis

[↑ Glosario](../../README.md) · [← Semántica](./semantica.md) · [Semánticas de entrega →](./semanticas-de-entrega.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error.

Definición de trabajo de [SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md).

## Por qué importa

En [SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), el tema «Semántica antes que sintaxis» importa porque dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error.

## Cómo funciona

Según [SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), en la sección «Semántica antes que sintaxis»:

Dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error. Contar líneas o tokens sin verificar semántica premia omisiones. El motor de reglas comparado usa fixtures comunes y normaliza solo diferencias de presentación.

Según [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), en la sección «Semántica antes que sintaxis»:

Primero se congela entrada, salida, orden de empate, errores y casos. Luego se busca una representación equivalente. `None` puede mapear a `Option`; excepción recuperable a `Result`; dict heterogéneo a struct. La equivalencia se juzga por comportamiento, no por parecido textual.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md)) son:

- **Se elige un paradigma por moda** — causa: falta de criterios explícitos. Corrección: escribir criterios y la evidencia de cada uno.
- **La comparación favorece al paradigma que se conoce** — causa: reglas simples que no ejercen lo propio de otros. Corrección: incluir una regla que dependa de otra o de estado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Una matriz organiza juicio, no sustituye un prototipo ni datos de mantenimiento. El taller siguiente implementa una regla en cinco modelos y obliga a contrastar sus trazas.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Dominio](../d/dominio.md), [Límite](../l/limite.md), [Resultado](../r/resultado.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Costo cognitivo y operativo](../c/costo-cognitivo-y-operativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Semántica](./semantica.md) · [Semánticas de entrega →](./semanticas-de-entrega.md)
