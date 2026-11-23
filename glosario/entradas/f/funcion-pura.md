# Función pura

[↑ Glosario](../../README.md) · [← Función hash y buckets](./funcion-hash-y-buckets.md) · [Funciones de orden superior →](./funciones-de-orden-superior.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Función cuyo resultado depende solo de sus argumentos y que no produce efectos observables fuera de él.

Definición de trabajo de [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md).

## Por qué importa

En [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), el tema «Funciones puras y datos inmutables» importa porque sin estado oculto, la función se prueba y se compone sin sorpresas.

## Cómo funciona

Según [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md):

**Cómo leer la figura.** Cada barra es un nivel de prueba acumulativo y su altura son las impurezas detectadas de las 8 que existen (la línea discontinua). Mira primero el salto de cuatro a siete al perturbar lo global y la distancia que aún queda hasta 8. **Dónde deja de valer:** el detector es una construcción sencilla del autor y la función que devuelve su estado interno pasa los tres niveles: se descubre cuando alguien modifica el valor devuelto. Una función «pura» según estas pruebas puede no serlo si depende de algo que no se perturbó. La figura muestra que un ejemplo no demuestra pureza, no que siete de ocho sea una cifra general.

Según [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md):

El equipo de `tarifas` toma tres decisiones. El cálculo del costo pasa a ser una función pura sobre un registro inmutable (una tupla con nombre), con una prueba de tres niveles que se ejecuta en la suite. La cola de eventos se acota a 200 y la política es descartar lo viejo con un contador de descartes y una alarma si superan 1 % en una hora, porque un pedido antiguo ya tiene un cálculo posterior que lo reemplaza. El total del día deja de ser una variable compartida: lo acumula un único hilo que recibe cada monto por una cola, y una prueba verifica que el total coincide con la suma de los montos de la entrada.

## Ejemplo

Ejemplo de [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) (sección «Ejemplo profesional»):

El equipo de `tarifas` toma tres decisiones. El cálculo del costo pasa a ser una función pura sobre un registro inmutable (una tupla con nombre), con una prueba de tres niveles que se ejecuta en la suite. La cola de eventos se acota a 200 y la política es descartar lo viejo con un contador de descartes y una alarma si superan 1 % en una hora, porque un pedido antiguo ya tiene un cálculo posterior que lo reemplaza.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una función «pura» deja a su llamador con datos reordenados** — causa: modifica su argumento. Corrección: devolver un valor nuevo y probar con copias. ([SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una función «pura» según estas pruebas puede no serlo si depende de algo que no se perturbó. ([SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Argumento](../a/argumento.md), [Efecto](../e/efecto.md), [Función](./funcion.md), [Resultado](../r/resultado.md), [Condición de carrera](../c/condicion-de-carrera.md), [Contrapresión](../c/contrapresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), [SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hughes, «Why Functional Programming Matters» (The Computer Journal, 1989)](https://doi.org/10.1093/comjnl/32.2.98) — modularidad con funciones sin efectos; autoridad: The Computer Journal.
- [Lee, «The Problem with Threads» (IEEE Computer, 2006)](https://doi.org/10.1109/MC.2006.180) — hilos y no determinismo; autoridad: IEEE Computer.
- [Reactive Streams](https://www.reactive-streams.org/) — flujo asincrónico con contrapresión; autoridad: la iniciativa Reactive Streams.
- [The Reactive Manifesto](https://www.reactivemanifesto.org/) — sistemas reactivos y paso de mensajes; autoridad: sus autores.
- [Little, «A Proof for the Queuing Formula: L = λW» (Operations Research, 1961)](https://doi.org/10.1287/opre.9.3.383) — relación entre cola, llegada y espera; autoridad: Operations Research.

---

[↑ Glosario](../../README.md) · [← Función hash y buckets](./funcion-hash-y-buckets.md) · [Funciones de orden superior →](./funciones-de-orden-superior.md)
