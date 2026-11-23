# Estado imposible

[↑ Glosario](../../README.md) · [← Estado estable](./estado-estable.md) · [Estado inalcanzable →](./estado-inalcanzable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Combinación de valores que el modelo permite representar y que no corresponde a ninguna situación del producto.

Definición de trabajo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), existe con este propósito: la clase existe para que diseñes lo que ve y puede hacer una persona cuando una vista no tiene datos, está esperando, falló o se recuperó, y para que representes esos casos como estados explícitos y no como un montón de banderas que pueden contradecirse.

## Cómo funciona

[SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

En la plataforma, cada vista con datos remotos declara sus estados en una tabla (carga, vacío, error, con datos, parcial), el texto de cada uno y la acción de recuperación. Los componentes usan un único valor de estado, y una prueba recorre las transiciones declaradas y falla si aparece un par no declarado. Los reintentos usan espera exponencial con aleatoriedad, tope de cinco intentos y clave de idempotencia; el indicador de carga espera 300 ms y dura al menos 600 ms.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)) son:

- **«No tienes entregas» parpadea antes de aparecer la lista** — causa: el estado de carga inicial se trató como vacío. Corrección: estado de carga explícito y vacío solo tras una respuesta sin datos.
- **Indicador y error visibles a la vez** — causa: banderas independientes sin transiciones. Corrección: unión de estados con transiciones declaradas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún servicio ni se midió ninguna latencia propia, y los eventos, la sincronía de los clientes y la latencia lognormal son supuestos del autor. La siguiente clase pregunta si todo lo anterior es perceptible, operable y comprensible para toda la población.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Modelo](../m/modelo.md), [Producto](../p/producto.md), [Valor](../v/valor.md), [Espera exponencial con aleatoriedad](./espera-exponencial-con-aleatoriedad.md), [Estado vacío](./estado-vacio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Harel, «Statecharts: a visual formalism for complex systems» (Science of Computer Programming, 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados jerárquicos y explosión de combinaciones; autoridad: Science of Computer Programming.
- [AWS Architecture Blog: Exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) — comparación de políticas de reintento; autoridad: Amazon Web Services (análisis de un proveedor).
- [Nielsen Norman Group: diseño de estados vacíos](https://www.nngroup.com/articles/empty-state-interface-design/) — contenido y propósito del estado vacío; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: guía de mensajes de error](https://www.nngroup.com/articles/error-message-guidelines/) — qué debe contener un mensaje de error; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: indicadores de progreso](https://www.nngroup.com/articles/progress-indicators/) — cuándo y cómo mostrar progreso; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Estado estable](./estado-estable.md) · [Estado inalcanzable →](./estado-inalcanzable.md)
