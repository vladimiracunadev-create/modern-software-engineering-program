# Affordance percibida

[↑ Glosario](../../README.md) · [← ADR retrospectivo](./adr-retrospectivo.md) · [Afirmación →](./afirmacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Señal de una acción posible que la persona reconoce a partir del aspecto y el contexto del objeto.

Definición de trabajo de [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md).

## Por qué importa

La clase donde se define, [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), existe con este propósito: la clase existe para que decidas cómo se ve, se alcanza y responde cada control de modo que la persona sepa qué puede hacer, qué pasó y cómo deshacerlo, y para que midas el costo de esas decisiones en errores y duplicados.

## Cómo funciona

[SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md):

En la plataforma, el contrato de interacción de «Enviar entrega» fija un objetivo de al menos 44 px, una respuesta visible antes de 0,1 s (estado pulsado), un indicador de progreso si pasa de un segundo, una clave de idempotencia generada por el cliente y una ventana de deshacer de 30 s para el retiro de una entrega. Las pruebas comprueban que dos peticiones con la misma clave crean un solo registro y que un reintento tras un fallo de red devuelve el resultado anterior.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md)) son:

- **Entregas duplicadas pese a un botón desactivado** — causa: la protección vive solo en el cliente. Corrección: clave de idempotencia en el servidor.
- **La gente confirma sin leer** — causa: diálogo genérico usado a menudo. Corrección: deshacer para acciones reversibles y confirmación específica para las irreversibles.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ninguna persona, no se usó ningún dispositivo táctil y las constantes de Fitts, las dispersiones, la latencia, la paciencia y los porcentajes de reflejo son supuestos del autor. La siguiente clase pregunta qué ve la persona cuando no hay datos, cuando se espera o cuando algo falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Objeto](../o/objeto.md), [Señal](../s/senal.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Ley de Fitts](../l/ley-de-fitts.md), [Operaciones idempotentes](../o/operaciones-idempotentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Norman, «Affordance, conventions, and design» (Interactions, 1999)](https://doi.org/10.1145/301153.301168) — affordance real frente a percibida; autoridad: ACM Interactions.
- [Fitts, «The information capacity of the human motor system» (J. Exp. Psychol., 1954)](https://doi.org/10.1037/h0055392) — ley de apuntar; autoridad: Journal of Experimental Psychology.
- [MacKenzie, «Fitts\' law as a research and design tool in HCI» (Human–Computer Interaction, 1992)](https://doi.org/10.1207/s15327051hci0701_3) — uso de la ley de Fitts en diseño; autoridad: Human–Computer Interaction.
- [Nielsen Norman Group: límites de tiempo de respuesta](https://www.nngroup.com/articles/response-times-3-important-limits/) — órdenes de magnitud de la percepción de respuesta; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: diálogos de confirmación](https://www.nngroup.com/articles/confirmation-dialog/) — cuándo confirmar y cuándo no; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← ADR retrospectivo](./adr-retrospectivo.md) · [Afirmación →](./afirmacion.md)
