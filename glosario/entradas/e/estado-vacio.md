# Estado vacío

[↑ Glosario](../../README.md) · [← Estado seguro](./estado-seguro.md) · [Estado válido →](./estado-valido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Estado de una vista que pidió datos y no recibió ninguno, distinto del estado de carga inicial.

Definición de trabajo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), existe con este propósito: la clase existe para que diseñes lo que ve y puede hacer una persona cuando una vista no tiene datos, está esperando, falló o se recuperó, y para que representes esos casos como estados explícitos y no como un montón de banderas que pueden contradecirse.

## Cómo funciona

Según [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

Una vista que depende de datos remotos tiene al menos cuatro estados: carga, vacío (se pidió y no hay nada), error y con datos. Cada uno necesita un diseño: el vacío explica por qué no hay nada y qué hacer; la carga, que algo ocurre; el error, qué falló y cómo seguir. El estado vacío es la oportunidad de orientar, no un texto de relleno, y el estado de carga inicial no es el vacío: confundirlos produce el parpadeo de «no tienes entregas».

Según [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

Compara el caso normal con una lista sin entregas, un fallo de red a mitad de una actualización y una recarga con la sesión caducada. Una vista es apropiada cuando esos tres casos tienen un texto, una acción y un estado; es peligrosa cuando el estado vacío y el de carga se ven igual.

## Ejemplo

Ejemplo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con una lista sin entregas, un fallo de red a mitad de una actualización y una recarga con la sesión caducada. Una vista es apropiada cuando esos tres casos tienen un texto, una acción y un estado; es peligrosa cuando el estado vacío y el de carga se ven igual.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)) son:

- **«No tienes entregas» parpadea antes de aparecer la lista** — causa: el estado de carga inicial se trató como vacío. Corrección: estado de carga explícito y vacío solo tras una respuesta sin datos.
- **Indicador y error visibles a la vez** — causa: banderas independientes sin transiciones. Corrección: unión de estados con transiciones declaradas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El estado vacío es la oportunidad de orientar, no un texto de relleno, y el estado de carga inicial no es el vacío: confundirlos produce el parpadeo de «no tienes entregas». ([SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](./estado.md), [Vista](../v/vista.md), [Espera exponencial con aleatoriedad](./espera-exponencial-con-aleatoriedad.md), [Estado imposible](./estado-imposible.md), [Indicador de carga](../i/indicador-de-carga.md), [Unión etiquetada](../u/union-etiquetada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nielsen Norman Group: diseño de estados vacíos](https://www.nngroup.com/articles/empty-state-interface-design/) — contenido y propósito del estado vacío; autoridad: Nielsen Norman Group.
- [Harel, «Statecharts: a visual formalism for complex systems» (Science of Computer Programming, 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados jerárquicos y explosión de combinaciones; autoridad: Science of Computer Programming.
- [AWS Architecture Blog: Exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) — comparación de políticas de reintento; autoridad: Amazon Web Services (análisis de un proveedor).
- [Nielsen Norman Group: guía de mensajes de error](https://www.nngroup.com/articles/error-message-guidelines/) — qué debe contener un mensaje de error; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: indicadores de progreso](https://www.nngroup.com/articles/progress-indicators/) — cuándo y cómo mostrar progreso; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Estado seguro](./estado-seguro.md) · [Estado válido →](./estado-valido.md)
