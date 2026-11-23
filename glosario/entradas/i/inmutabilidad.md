# Inmutabilidad

[↑ Glosario](../../README.md) · [← Ingeniería del caos](./ingenieria-del-caos.md) · [Inmutabilidad y evolución de valores →](./inmutabilidad-y-evolucion-de-valores.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Propiedad de un dato que no puede modificarse después de crearse.

Definición de trabajo de [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md).

## Por qué importa

La clase donde se define, [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), existe con este propósito: la clase existe para que decidas dónde vive el estado y quién puede cambiarlo, y para que elijas entre funciones puras, flujos con contrapresión y datos con un solo dueño por lo que cada opción garantiza cuando hay varias cosas ocurriendo, no por la moda del estilo.

## Cómo funciona

[SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md):

El equipo de `tarifas` toma tres decisiones. El cálculo del costo pasa a ser una función pura sobre un registro inmutable (una tupla con nombre), con una prueba de tres niveles que se ejecuta en la suite. La cola de eventos se acota a 200 y la política es descartar lo viejo con un contador de descartes y una alarma si superan 1 % en una hora, porque un pedido antiguo ya tiene un cálculo posterior que lo reemplaza.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md)) son:

- **Una función «pura» deja a su llamador con datos reordenados** — causa: modifica su argumento. Corrección: devolver un valor nuevo y probar con copias.
- **Las respuestas llegan con horas de retraso en hora punta** — causa: cola sin límite con productor más rápido. Corrección: acotar la cola y elegir una política de desborde.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres modelos y análisis con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se ejecutó ningún hilo real, no se midió ningún tiempo de máquina y las llegadas y servicios exponenciales son un supuesto; las funciones, la cola y los programas de dos hilos son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Condición de carrera](../c/condicion-de-carrera.md), [Contrapresión](../c/contrapresion.md), [Función pura](../f/funcion-pura.md), [Sección crítica](../s/seccion-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md).

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

[↑ Glosario](../../README.md) · [← Ingeniería del caos](./ingenieria-del-caos.md) · [Inmutabilidad y evolución de valores →](./inmutabilidad-y-evolucion-de-valores.md)
