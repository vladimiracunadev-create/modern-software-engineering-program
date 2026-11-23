# Relación de contraste

[↑ Glosario](../../README.md) · [← Relación](./relacion.md) · [Release candidate →](./release-candidate.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Cociente calculado con la luminancia relativa de dos colores que WCAG usa para fijar mínimos de legibilidad.

Definición de trabajo de [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md): Cociente de luminancias de dos colores definido por WCAG.

## Por qué importa

La clase donde se define, [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), existe con este propósito: la clase existe para que diseñes el cliente para varias formas de entrada (dedo, teclado, mouse, lector de pantalla) a la vez, y para que verifiques con cálculos y recorridos automáticos lo que se puede verificar (tamaño de objetivo, orden de foco, contraste) y reserves a las personas lo que no.

## Cómo funciona

Según [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md):

WCAG define la relación de contraste a partir de la luminancia relativa de dos colores y fija 4,5 a 1 para texto normal y 3 a 1 para texto grande y elementos de interfaz. Un cálculo automático detecta los pares que no cumplen. No cubre el tamaño de fuente, el espaciado, los estados de foco ni las condiciones de luz.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md):

El equipo del cliente escribe una tabla de modos de entrada con una fila por función y una columna por entrada (tacto, teclado, puntero, lector). «Enviar entrega» se activa con un botón de 48 por 48, con la tecla Intro y con el rol de botón; «Reordenar adjuntos» deja de depender del arrastre y ofrece botones de subir y bajar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md)) son:

- **Los botones se pulsan mal en el teléfono** — causa: objetivos pequeños o juntos. Corrección: aumentar el tamaño y la separación; medir con usuarios.
- **El teclado se queda atascado en un control** — causa: trampa de foco. Corrección: permitir salir y añadir un recorrido a las pruebas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada barra es la relación de contraste del par sobre blanco; las verdes cumplen 4,5 a 1, la dorada queda cerca sin llegar y la coral está por debajo de 3. ([SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Legibilidad](../l/legibilidad.md), [Árbol de accesibilidad](../a/arbol-de-accesibilidad.md), [Exploración](../e/exploracion.md), [Heurística de prueba](../h/heuristica-de-prueba.md), [Misión](../m/mision.md), [Objetivo táctil](../o/objetivo-tactil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C, «WCAG 2.2»](https://www.w3.org/TR/WCAG22/) — pautas de accesibilidad del contenido web; autoridad: W3C.
- [W3C, «Understanding SC 2.5.8: Target Size (Minimum)»](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — tamaño mínimo de objetivos; autoridad: W3C.
- [W3C, «Understanding SC 1.4.3: Contrast (Minimum)»](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — contraste mínimo y su fórmula; autoridad: W3C.
- [W3C, «Understanding SC 2.4.3: Focus Order»](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — orden de foco; autoridad: W3C.
- [Apple Developer, «Accessibility» (Human Interface Guidelines)](https://developer.apple.com/design/human-interface-guidelines/accessibility) — guía de accesibilidad de las plataformas de Apple; autoridad: Apple.

---

[↑ Glosario](../../README.md) · [← Relación](./relacion.md) · [Release candidate →](./release-candidate.md)
