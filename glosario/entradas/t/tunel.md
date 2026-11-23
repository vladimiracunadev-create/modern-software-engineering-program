# Túnel

[↑ Glosario](../../README.md) · [← TUI](./tui.md) · [Tutorial →](./tutorial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Efecto por el cual un objeto rápido atraviesa uno fino porque nunca se solapa en un instante muestreado.

Definición de trabajo de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md).

## Por qué importa

La clase donde se define, [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md), existe con este propósito: la clase existe para que diseñes el bucle de un juego sabiendo qué promete sobre el tiempo, el determinismo y la colisión, y para que distingas un problema de rendimiento de un problema de corrección que solo se manifiesta cuando el rendimiento cae.

## Cómo funciona

Según [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

La detección **discreta** comprueba si dos formas se solapan en el instante del fotograma. Si un objeto se mueve más de su propio tamaño (o del grosor del obstáculo) entre dos fotogramas, puede estar de un lado en uno y del otro en el siguiente sin solaparse nunca en un instante muestreado: es el efecto de **túnel**. La detección **continua** o barrida comprueba el segmento recorrido entre ambos instantes. Alternativas: subdividir el paso cuando la velocidad es alta, o limitar la velocidad máxima. Cada una tiene un coste, y todas necesitan una prueba que lance objetos rápidos contra obstáculos finos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

El equipo del laboratorio adopta el bucle de acumulador con paso fijo de 1/120 s para la física y un dibujo por fotograma con interpolación entre el estado anterior y el actual. Registra las entradas del estudiante con el número de paso, de modo que cualquier partida se puede reproducir paso a paso en una prueba automática sin pantalla. Los proyectiles usan prueba barrida y subdividen el paso por encima de una velocidad dada.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md)) son:

- **Dos máquinas dan resultados distintos con las mismas entradas** — causa: paso variable. Corrección: paso fijo con acumulador y entradas con número de paso.
- **Los objetos rápidos atraviesan las paredes** — causa: colisión discreta con paso mayor que el grosor. Corrección: prueba barrida, subdivisión del paso o límite de velocidad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si un objeto se mueve más de su propio tamaño (o del grosor del obstáculo) entre dos fotogramas, puede estar de un lado en uno y del otro en el siguiente sin solaparse nunca en un instante muestreado: es el efecto de **túnel**. ([SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Instante](../i/instante.md), [Objeto](../o/objeto.md), [Bucle de juego](../b/bucle-de-juego.md), [Determinismo](../d/determinismo.md), [Espiral de la muerte](../e/espiral-de-la-muerte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md).

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

[↑ Glosario](../../README.md) · [← TUI](./tui.md) · [Tutorial →](./tutorial.md)
