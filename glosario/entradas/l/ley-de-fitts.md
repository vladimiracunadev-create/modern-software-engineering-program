# Ley de Fitts

[↑ Glosario](../../README.md) · [← Ley de Conway](./ley-de-conway.md) · [Ley de Goodhart →](./ley-de-goodhart.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Relación entre el tiempo de apuntar a un objetivo y el logaritmo de la razón entre la distancia y su tamaño.

Definición de trabajo de [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md).

## Por qué importa

La clase donde se define, [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), existe con este propósito: la clase existe para que decidas cómo se ve, se alcanza y responde cada control de modo que la persona sepa qué puede hacer, qué pasó y cómo deshacerlo, y para que midas el costo de esas decisiones en errores y duplicados.

## Cómo funciona

Según [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md):

La ley de Fitts relaciona el tiempo con log2(D/W + 1): duplicar el tamaño ahorra un bit de dificultad. En una pantalla táctil, además del tiempo importa la probabilidad de caer fuera: con dispersión gaussiana de los toques, la proporción fuera del objetivo cae rápido al crecer W. Las pautas de accesibilidad fijan un mínimo (24 px o espaciado suficiente en WCAG 2.2) y las de plataforma suelen recomendar más; el cálculo ayuda a decidir cuánto margen se necesita para una dispersión mayor.

## Ejemplo

Ejemplo de [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el tiempo de apuntar con la ley de Fitts. Antes de ejecutarlo, predice si pasar de 24 a 48 px ahorra más o menos de 0,2 s.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md)) son:

- **Entregas duplicadas pese a un botón desactivado** — causa: la protección vive solo en el cliente. Corrección: clave de idempotencia en el servidor.
- **La gente confirma sin leer** — causa: diálogo genérico usado a menudo. Corrección: deshacer para acciones reversibles y confirmación específica para las irreversibles.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ninguna persona, no se usó ningún dispositivo táctil y las constantes de Fitts, las dispersiones, la latencia, la paciencia y los porcentajes de reflejo son supuestos del autor. La siguiente clase pregunta qué ve la persona cuando no hay datos, cuando se espera o cuando algo falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Relación](../r/relacion.md), [Affordance percibida](../a/affordance-percibida.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Operaciones idempotentes](../o/operaciones-idempotentes.md), [Retroalimentación](../r/retroalimentacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MacKenzie, «Fitts\' law as a research and design tool in HCI» (Human–Computer Interaction, 1992)](https://doi.org/10.1207/s15327051hci0701_3) — uso de la ley de Fitts en diseño; autoridad: Human–Computer Interaction.
- [Norman, «Affordance, conventions, and design» (Interactions, 1999)](https://doi.org/10.1145/301153.301168) — affordance real frente a percibida; autoridad: ACM Interactions.
- [Fitts, «The information capacity of the human motor system» (J. Exp. Psychol., 1954)](https://doi.org/10.1037/h0055392) — ley de apuntar; autoridad: Journal of Experimental Psychology.
- [Nielsen Norman Group: límites de tiempo de respuesta](https://www.nngroup.com/articles/response-times-3-important-limits/) — órdenes de magnitud de la percepción de respuesta; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: diálogos de confirmación](https://www.nngroup.com/articles/confirmation-dialog/) — cuándo confirmar y cuándo no; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Ley de Conway](./ley-de-conway.md) · [Ley de Goodhart →](./ley-de-goodhart.md)
