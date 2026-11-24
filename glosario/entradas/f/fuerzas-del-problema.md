# Fuerzas del problema

[↑ Glosario](../../README.md) · [← Fuerza](./fuerza.md) · [Fuga de datos →](./fuga-de-datos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Las **fuerzas del problema** son las propiedades del problema que, según [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), deben guiar la elección de un paradigma: **estado**, **temporalidad**, **concurrencia**, **tasa de cambio**, **auditabilidad** y **habilidades del equipo**. La elección parte de ellas, no de la preferencia: un paradigma es adecuado cuando vuelve **directas** las propiedades dominantes del problema. Es un uso del programa del término «fuerzas» (*forces*) de la literatura de patrones, donde designa las presiones que un diseño debe equilibrar.

## Por qué importa

Los paradigmas (procedural, orientado a objetos, funcional, declarativo, concurrente) no son mejores o peores en abstracto: cada uno hace fácil cierto tipo de problema y costoso otro. Elegir por popularidad, por gusto o porque el código resulta más corto genera sistemas que pelean contra su propio modelo. [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) lo dice así: **popularidad o brevedad no son fuerzas técnicas suficientes**. La decisión que cambia es el punto de partida del diseño: no «qué estilo uso», sino «qué propiedades dominan este problema y qué modelo las expresa mejor».

## Cómo funciona

Cada fuerza hace una pregunta:

- **Estado:** ¿hay entidades con identidad que cambian a lo largo del tiempo, o transformaciones de datos sin memoria? Mucho estado con reglas sobre sus transiciones favorece objetos con invariantes; poco estado, funciones.
- **Temporalidad:** ¿importa el orden y el momento de los hechos (eventos, historial)?
- **Concurrencia:** ¿varias cosas ocurren a la vez y comparten datos? La inmutabilidad y el paso de mensajes reducen conflictos.
- **Tasa de cambio:** ¿qué parte cambia con frecuencia, las reglas o las entidades? El modelo debe hacer local lo que más cambia.
- **Auditabilidad:** ¿hay que explicar y reproducir cada decisión? Funciones puras y reglas declarativas facilitan la trazabilidad.
- **Habilidades del equipo:** un modelo que nadie sabe mantener es un riesgo real, aunque sea técnicamente ideal.

Se evalúa cada fuerza para el problema concreto, se identifican las **dominantes** y se contrasta con lo que cada paradigma hace directo. La causa de que sirva es que convierte una discusión de gustos en una de propiedades verificables y, por tanto, de evidencia.

## Ejemplo

Para el motor de reglas del programa, que produce una recomendación con acción, evidencia, versión de política y explicación, las fuerzas dominantes podrían ser la **auditabilidad** (disputar una decisión incorrecta exige reproducirla) y la **tasa de cambio de las reglas**. Eso favorece un núcleo de funciones puras y reglas expresadas como datos, con trazas de qué regla disparó. Si en cambio el problema fuera una simulación con miles de entidades que cambian de estado y reaccionan a eventos, dominarían el estado y la temporalidad, y los objetos con invariantes o un modelo de eventos serían más directos. Ilustración de una matriz de decisión:

```text
fuerza             peso   funcional   objetos   reglas
auditabilidad       alto     ++          +         ++
tasa de cambio      alto     +           -         ++
estado              bajo     +           ++        -
```

## Errores y confusiones comunes

- **Elegir por moda.** Sin criterios explícitos, el paradigma lo decide la tendencia; se escriben criterios y la evidencia de cada uno.
- **Comparar con reglas simples.** La comparación favorece al paradigma conocido; hay que incluir una regla que dependa de otra o de estado.
- **Ignorar las habilidades del equipo.** El mejor modelo sobre el papel puede ser inmantenible.
- **Tratar todas las fuerzas igual.** Hay que identificar cuáles dominan.

## Límites y cuándo no aplica

Una matriz organiza el juicio, no sustituye un prototipo ni datos de mantenimiento ([SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md)). Muchos sistemas tienen partes con fuerzas dominantes distintas, y la respuesta correcta es combinar modelos con fronteras explícitas, no uno solo. Para problemas pequeños, el lenguaje y la costumbre del equipo deciden razonablemente y el análisis es excesivo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Concurrencia](../c/concurrencia.md), [Estado](../e/estado.md), [Habilidad](../h/habilidad.md), [Costo cognitivo y operativo](../c/costo-cognitivo-y-operativo.md), [Decisión reversible y experimento](../d/decision-reversible-y-experimento.md), [Fronteras entre modelos](./fronteras-entre-modelos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

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

[↑ Glosario](../../README.md) · [← Fuerza](./fuerza.md) · [Fuga de datos →](./fuga-de-datos.md)
