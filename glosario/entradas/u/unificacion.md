# Unificación

[↑ Glosario](../../README.md) · [← Unidad menor](./unidad-menor.md) · [Unión etiquetada →](./union-etiquetada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Unificar busca una sustitución compatible entre estructuras.

Definición de trabajo de [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md).

## Por qué importa

En [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), el tema «Unificación» importa porque unificar busca una sustitución compatible entre estructuras.

## Cómo funciona

Según [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), en la sección «Unificación»:

Unificar busca una sustitución compatible entre estructuras. No es asignación mutable: una variable lógica queda vinculada dentro de una rama de búsqueda. El chequeo de ocurrencia y las extensiones del sistema determinan qué términos son admitidos, por lo que no conviene extrapolar desde pseudocódigo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una variable queda ligada a una estructura infinita** — causa: unificación sin comprobación de ocurrencia. Corrección: usar la versión con comprobación cuando el dominio lo requiera. ([SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para observar el costo se implementó un resolvedor mínimo en Python (unificación, retroceso, sin optimizaciones) y se contó cuántas comparaciones de unificación hacía. ([SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estructura](../e/estructura.md), [Sustitución](../s/sustitucion.md), [Negación y mundo cerrado](../n/negacion-y-mundo-cerrado.md), [Resolución y backtracking](../r/resolucion-y-backtracking.md), [Restricciones y explicación](../r/restricciones-y-explicacion.md), [Términos, hechos y consultas](../t/terminos-hechos-y-consultas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Unidad menor](./unidad-menor.md) · [Unión etiquetada →](./union-etiquetada.md)
