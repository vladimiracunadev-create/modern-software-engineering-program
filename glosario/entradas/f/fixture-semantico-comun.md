# Fixture semántico común

[↑ Glosario](../../README.md) · [← Fixture](./fixture.md) · [Flujo →](./flujo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Un **fixture semántico común** es, en el taller de [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md), el conjunto de **entradas y salidas canónicas** compartido por todas las implementaciones de una misma regla de negocio. El taller **comienza por él, no por el código**: antes de escribir la regla en cinco paradigmas, se fijan los casos con sus resultados esperados. «Semántico» indica que describe el *significado* de la regla (qué debe resultar de qué), con independencia de cómo cada paradigma lo calcule. Es un término propio del programa; *fixture* en pruebas suele designar datos de preparación, y aquí abarca además los resultados esperados.

## Por qué importa

Si cada implementación nace con sus propios ejemplos, nada garantiza que estén resolviendo el mismo problema; comparar sus diffs o su legibilidad entonces compara cosas distintas. El fixture fija **qué es correcto** antes de discutir **cómo expresarlo**. La decisión que cambia es el orden de trabajo: primero el acuerdo sobre el comportamiento, después las soluciones. Y sirve de árbitro: cuando dos versiones difieren, el fixture dice cuál se equivoca o qué caso el contrato no cubría.

## Cómo funciona

El fixture debe cubrir, como mínimo, los casos que ponen a prueba la regla ([SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)): **autorización falsa**, **evidencia vacía**, **empate** y **dato inválido**. Cada caso es una entrada con su salida esperada, expresada en términos del dominio (no del lenguaje). Todas las implementaciones se ejecutan contra el mismo fixture.

Hay una regla importante sobre lo que no se puede expresar: si un modelo **no puede representar un caso**, esa imposibilidad es **un hallazgo** y no se elimina del fixture. Por ejemplo, un paradigma que no distingue «evidencia vacía» de «evidencia ausente» muestra una limitación real de ese modelo para esta regla. Quitar el caso para que todas pasen escondería justo lo que la comparación quería descubrir.

La causa de que funcione es la misma que la de los *tests* de caracterización: un oráculo común convierte la comparación en un experimento controlado, con una sola variable (el paradigma).

## Ejemplo

Para la regla del motor de reglas de [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md), el fixture podría ser una tabla de casos (ilustración; los valores son inventados):

```text
caso                       entrada                          salida
autorización falsa         {autorizado: false, ...}         rechazar
evidencia vacía            {evidencia: []}                  pedir más datos
empate entre dos reglas    {puntaje_a: 5, puntaje_b: 5}     elegir por prioridad
dato inválido              {monto: "abc"}                   error de validación
```

Dos de los defectos documentados en la clase se descubren por el fixture: pruebas que pasan pero un defecto plantado sobrevive, porque falta el caso que ejercita esa regla (se añade el caso mínimo y se comprueba que el mutante falla), y dos versiones que divergen solo con ciertos tipos, porque el contrato no definía tipos inválidos (se amplían el contrato y los casos fijos).

## Errores y confusiones comunes

- **Escribir primero el código.** Cada solución trae su propia idea de correcto.
- **Eliminar el caso que un modelo no puede expresar.** Se pierde el hallazgo.
- **Fixture solo con casos felices.** No distingue las soluciones sólidas de las ingenuas.
- **No ejercitar con defectos plantados.** Sin mutantes, no se sabe si las pruebas detectan algo.

## Límites y cuándo no aplica

El taller compara un cambio y una carga pequeña, y no demuestra mantenibilidad a largo plazo ([SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)): un fixture común hace justa la comparación, no completa. Su valor depende de que los casos representen el dominio real; si los elige alguien que favorece un paradigma, sesga el resultado. Para reglas triviales con un solo caso, formalizar un fixture es más ceremonia que ayuda.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Cambio dirigido](../c/cambio-dirigido.md), [Implementaciones idiomáticas](../i/implementaciones-idiomaticas.md), [Retrospectiva basada en evidencia](../r/retrospectiva-basada-en-evidencia.md), [Trazas comparables](../t/trazas-comparables.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-083 — Taller: una regla de negocio en cinco paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Fixture](./fixture.md) · [Flujo →](./flujo.md)
