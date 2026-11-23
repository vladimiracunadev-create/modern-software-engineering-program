# Espiral de la muerte

[↑ Glosario](../../README.md) · [← Espía](./espia.md) · [Esquema →](./esquema.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Realimentación en que un fotograma lento acumula más trabajo y provoca otro más lento.

Definición de trabajo de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md).

## Por qué importa

La clase donde se define, [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md), existe con este propósito: la clase existe para que diseñes el bucle de un juego sabiendo qué promete sobre el tiempo, el determinismo y la colisión, y para que distingas un problema de rendimiento de un problema de corrección que solo se manifiesta cuando el rendimiento cae.

## Cómo funciona

Según [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

Con 60 fotogramas por segundo, cada fotograma dispone de 16,7 ms para entrada, actualización, dibujo y presentación. Un fotograma que lo excede no solo se ve mal: con paso fijo, el tiempo acumulado exige más pasos en el siguiente, que tarda aún más. Es la **espiral de la muerte**. La defensa es un tope: no ejecutar más de unos pocos pasos por fotograma y descartar el resto, a cambio de que el juego corra más lento que el reloj. Otras formas de degradar son bajar la resolución, simplificar la física o reducir entidades activas. Lo importante es decidir de antemano qué se sacrifica.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

El equipo del laboratorio adopta el bucle de acumulador con paso fijo de 1/120 s para la física y un dibujo por fotograma con interpolación entre el estado anterior y el actual. Registra las entradas del estudiante con el número de paso, de modo que cualquier partida se puede reproducir paso a paso en una prueba automática sin pantalla. Los proyectiles usan prueba barrida y subdividen el paso por encima de una velocidad dada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El juego se congela y luego va lento** — causa: espiral de la muerte sin tope. Corrección: tope de pasos por fotograma y descarte del exceso, con aviso. ([SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md)) son: Las definiciones son operativas para el laboratorio de física. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor de juego, tarjeta gráfica ni medición de fotogramas reales: el resorte, la pared y los costes de actualización son construcciones del autor. La siguiente clase pasa a gráficos, audio y experiencias inmersivas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](../t/trabajo.md), [Bucle de juego](../b/bucle-de-juego.md), [Determinismo](../d/determinismo.md), [Paso fijo](../p/paso-fijo.md), [Túnel](../t/tunel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fiedler, «Fix Your Timestep!» (Gaffer On Games)](https://gafferongames.com/post/fix_your_timestep/) — paso fijo, acumulador y espiral de la muerte; autoridad: autor del artículo.
- [Nystrom, «Game Loop» (Game Programming Patterns)](https://gameprogrammingpatterns.com/game-loop.html) — variantes del bucle de juego; autoridad: autor del libro.
- [Godot Engine, documentación](https://docs.godotengine.org/en/stable/) — procesamiento de física con paso fijo en un motor concreto; autoridad: Godot Engine.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Espía](./espia.md) · [Esquema →](./esquema.md)
