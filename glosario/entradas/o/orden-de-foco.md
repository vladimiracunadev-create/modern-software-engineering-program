# Orden de foco

[↑ Glosario](../../README.md) · [← Oráculo y propiedades](./oraculo-y-propiedades.md) · [Orden de resolución de métodos →](./orden-de-resolucion-de-metodos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Secuencia en que el teclado y las tecnologías de apoyo recorren los controles; debe conservar significado y no retener ni omitir controles.

Definición de trabajo de [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md): Secuencia en la que los controles reciben el foco al pulsar Tab.

## Por qué importa

En [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), el tema «Teclado y orden de foco» importa porque el teclado recorre los controles en un orden que el código define y que puede tener trampas.

## Cómo funciona

Según [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md):

La persona que usa teclado o un conmutador se mueve por el orden de foco. Un control que retiene el foco, un salto que se salta controles, un control visible que no entra en el orden o un recorrido que vuelve al inicio antes de tiempo bloquean el uso. WCAG exige que el orden conserve significado y operabilidad. El recorrido automático encuentra los defectos de alcance; el sentido del orden lo juzga una persona.

Según [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md):

El equipo del cliente escribe una tabla de modos de entrada con una fila por función y una columna por entrada (tacto, teclado, puntero, lector). «Enviar entrega» se activa con un botón de 48 por 48, con la tecla Intro y con el rol de botón; «Reordenar adjuntos» deja de depender del arrastre y ofrece botones de subir y bajar. Las comprobaciones automáticas (tamaño de objetivo, recorrido del orden de foco, contraste) se ejecutan en cada cambio; las que no se pueden automatizar (sentido del orden, nombres para el lector) se revisan con una persona y un lector en cada versión.

## Ejemplo

Ejemplo de [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) (sección «Ejemplo profesional»):

El equipo del cliente escribe una tabla de modos de entrada con una fila por función y una columna por entrada (tacto, teclado, puntero, lector). «Enviar entrega» se activa con un botón de 48 por 48, con la tecla Intro y con el rol de botón; «Reordenar adjuntos» deja de depender del arrastre y ofrece botones de subir y bajar. Las comprobaciones automáticas (tamaño de objetivo, recorrido del orden de foco, contraste) se ejecutan en cada cambio; las que no se pueden automatizar (sentido del orden, nombres para el lector) se revisan con una persona y un lector en cada versión.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md)) son:

- **Los botones se pulsan mal en el teléfono** — causa: objetivos pequeños o juntos. Corrección: aumentar el tamaño y la separación; medir con usuarios.
- **El teclado se queda atascado en un control** — causa: trampa de foco. Corrección: permitir salir y añadir un recorrido a las pruebas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El orden de foco sigue el orden del documento salvo que se altere con `tabindex`. ([SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Tecnología de apoyo](../t/tecnologia-de-apoyo.md).
- **Ver también:** [Secuencia](../s/secuencia.md), [Árbol de accesibilidad](../a/arbol-de-accesibilidad.md), [Enlace de salto](../e/enlace-de-salto.md), [Nombre accesible](../n/nombre-accesible.md), [Objetivo táctil](./objetivo-tactil.md), [Región](../r/region.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C, «Understanding SC 2.4.3: Focus Order»](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — orden de foco; autoridad: W3C.
- [W3C, «WCAG 2.2»](https://www.w3.org/TR/WCAG22/) — pautas de accesibilidad del contenido web; autoridad: W3C.
- [W3C, «Understanding SC 2.5.8: Target Size (Minimum)»](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — tamaño mínimo de objetivos; autoridad: W3C.
- [W3C, «Understanding SC 1.4.3: Contrast (Minimum)»](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — contraste mínimo y su fórmula; autoridad: W3C.
- [Apple Developer, «Accessibility» (Human Interface Guidelines)](https://developer.apple.com/design/human-interface-guidelines/accessibility) — guía de accesibilidad de las plataformas de Apple; autoridad: Apple.

---

[↑ Glosario](../../README.md) · [← Oráculo y propiedades](./oraculo-y-propiedades.md) · [Orden de resolución de métodos →](./orden-de-resolucion-de-metodos.md)
