# Paso fijo

[↑ Glosario](../../README.md) · [← Paso de comprobación](./paso-de-comprobacion.md) · [Pass@k →](./pass-k.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Duración constante con que se avanza el estado, independiente del tiempo real del fotograma.

Definición de trabajo de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md).

## Por qué importa

En [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md), el tema «Paso fijo y determinismo» importa porque decide si una partida se puede repetir, grabar y sincronizar.

## Cómo funciona

Según [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

Un juego repite tres etapas: leer la entrada, actualizar el estado del mundo y dibujarlo. Lo que distingue un diseño de otro es cómo se relaciona el tiempo real con el tiempo simulado. Nystrom describe las variantes: avanzar el estado una cantidad proporcional al tiempo que pasó desde el fotograma anterior (paso variable), avanzarlo siempre una cantidad constante (paso fijo) o combinar ambas con un acumulador. Cada una compra algo: el paso variable es simple y suave; el fijo da repetibilidad; el acumulador da ambas a cambio de interpolar al dibujar. La elección no es de gusto: depende de si una partida debe poder reproducirse, grabarse o sincronizarse con otra máquina.

Según [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

El equipo del laboratorio adopta el bucle de acumulador con paso fijo de 1/120 s para la física y un dibujo por fotograma con interpolación entre el estado anterior y el actual. Registra las entradas del estudiante con el número de paso, de modo que cualquier partida se puede reproducir paso a paso en una prueba automática sin pantalla. Los proyectiles usan prueba barrida y subdividen el paso por encima de una velocidad dada. El tope es de 5 pasos por fotograma; cuando se alcanza, se muestra un indicador de «ralentizado» y se registra en la telemetría local. Una prueba de regresión lanza 200 proyectiles a velocidades crecientes contra una pared fina y exige que ninguno la atraviese.

## Ejemplo

Ejemplo de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra que con paso fijo el resultado no depende de cuántos fotogramas se usen. Antes de ejecutarlo, predice si ambas ejecuciones coinciden.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos máquinas dan resultados distintos con las mismas entradas** — causa: paso variable. Corrección: paso fijo con acumulador y entradas con número de paso. ([SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con paso fijo la secuencia de pasos es la misma, y el resultado solo depende de las entradas. ([SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Bucle de juego](../b/bucle-de-juego.md), [Determinismo](../d/determinismo.md), [Espiral de la muerte](../e/espiral-de-la-muerte.md), [Túnel](../t/tunel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fiedler, «Fix Your Timestep!» (Gaffer On Games)](https://gafferongames.com/post/fix_your_timestep/) — paso fijo, acumulador y espiral de la muerte; autoridad: autor del artículo.
- [Godot Engine, documentación](https://docs.godotengine.org/en/stable/) — procesamiento de física con paso fijo en un motor concreto; autoridad: Godot Engine.
- [Nystrom, «Game Loop» (Game Programming Patterns)](https://gameprogrammingpatterns.com/game-loop.html) — variantes del bucle de juego; autoridad: autor del libro.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Paso de comprobación](./paso-de-comprobacion.md) · [Pass@k →](./pass-k.md)
