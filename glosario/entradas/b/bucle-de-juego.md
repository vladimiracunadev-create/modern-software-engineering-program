# Bucle de juego

[↑ Glosario](../../README.md) · [← Bucle de eventos y cola](./bucle-de-eventos-y-cola.md) · [Bucle de realimentación →](./bucle-de-realimentacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Ciclo repetido de lectura de entrada, actualización del estado y dibujo.

Definición de trabajo de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md).

## Por qué importa

En [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md), el tema «El bucle de juego» importa porque define qué ocurre en cada fotograma y quién manda sobre el tiempo.

## Cómo funciona

[SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el laboratorio de física. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

El equipo del laboratorio adopta el bucle de acumulador con paso fijo de 1/120 s para la física y un dibujo por fotograma con interpolación entre el estado anterior y el actual. Registra las entradas del estudiante con el número de paso, de modo que cualquier partida se puede reproducir paso a paso en una prueba automática sin pantalla. Los proyectiles usan prueba barrida y subdividen el paso por encima de una velocidad dada.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md)) son:

- **Dos máquinas dan resultados distintos con las mismas entradas** — causa: paso variable. Corrección: paso fijo con acumulador y entradas con número de paso.
- **Los objetos rápidos atraviesan las paredes** — causa: colisión discreta con paso mayor que el grosor. Corrección: prueba barrida, subdivisión del paso o límite de velocidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md)) son: Las definiciones son operativas para el laboratorio de física. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor de juego, tarjeta gráfica ni medición de fotogramas reales: el resorte, la pared y los costes de actualización son construcciones del autor. La siguiente clase pasa a gráficos, audio y experiencias inmersivas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo](../c/ciclo.md), [Estado](../e/estado.md), [Determinismo](../d/determinismo.md), [Espiral de la muerte](../e/espiral-de-la-muerte.md), [Paso fijo](../p/paso-fijo.md), [Túnel](../t/tunel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nystrom, «Game Loop» (Game Programming Patterns)](https://gameprogrammingpatterns.com/game-loop.html) — variantes del bucle de juego; autoridad: autor del libro.
- [Fiedler, «Fix Your Timestep!» (Gaffer On Games)](https://gafferongames.com/post/fix_your_timestep/) — paso fijo, acumulador y espiral de la muerte; autoridad: autor del artículo.
- [Godot Engine, documentación](https://docs.godotengine.org/en/stable/) — procesamiento de física con paso fijo en un motor concreto; autoridad: Godot Engine.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Bucle de eventos y cola](./bucle-de-eventos-y-cola.md) · [Bucle de realimentación →](./bucle-de-realimentacion.md)
