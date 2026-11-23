# Indicador de carga

[↑ Glosario](../../README.md) · [← Indicador](./indicador.md) · [Indicador de nivel de servicio →](./indicador-de-nivel-de-servicio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Señal visible de que una operación está en curso.

Definición de trabajo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), existe con este propósito: la clase existe para que diseñes lo que ve y puede hacer una persona cuando una vista no tiene datos, está esperando, falló o se recuperó, y para que representes esos casos como estados explícitos y no como un montón de banderas que pueden contradecirse.

## Cómo funciona

Según [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

Con tres banderas (cargando, hay error, hay datos) hay ocho combinaciones y solo cuatro tienen significado. Cada actualización puede ser correcta en aislamiento y el conjunto, imposible: al llegar los datos se olvida apagar el indicador de carga. Una unión etiquetada (un único valor entre carga, error, vacío, datos) hace imposible representar lo que no tiene sentido, y las transiciones se declaran en un solo lugar. Es la idea de los diagramas de estados de Harel aplicada a una vista.

Según [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

En la plataforma, cada vista con datos remotos declara sus estados en una tabla (carga, vacío, error, con datos, parcial), el texto de cada uno y la acción de recuperación. Los componentes usan un único valor de estado, y una prueba recorre las transiciones declaradas y falla si aparece un par no declarado. Los reintentos usan espera exponencial con aleatoriedad, tope de cinco intentos y clave de idempotencia; el indicador de carga espera 300 ms y dura al menos 600 ms.

## Ejemplo

Ejemplo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada vista con datos remotos declara sus estados en una tabla (carga, vacío, error, con datos, parcial), el texto de cada uno y la acción de recuperación. Los componentes usan un único valor de estado, y una prueba recorre las transiciones declaradas y falla si aparece un par no declarado. Los reintentos usan espera exponencial con aleatoriedad, tope de cinco intentos y clave de idempotencia; el indicador de carga espera 300 ms y dura al menos 600 ms.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)) son:

- **«No tienes entregas» parpadea antes de aparecer la lista** — causa: el estado de carga inicial se trató como vacío. Corrección: estado de carga explícito y vacío solo tras una respuesta sin datos.
- **Indicador y error visibles a la vez** — causa: banderas independientes sin transiciones. Corrección: unión de estados con transiciones declaradas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún servicio ni se midió ninguna latencia propia, y los eventos, la sincronía de los clientes y la latencia lognormal son supuestos del autor. La siguiente clase pregunta si todo lo anterior es perceptible, operable y comprensible para toda la población.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Señal](../s/senal.md), [Espera exponencial con aleatoriedad](../e/espera-exponencial-con-aleatoriedad.md), [Estado imposible](../e/estado-imposible.md), [Estado vacío](../e/estado-vacio.md), [Unión etiquetada](../u/union-etiquetada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

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

[↑ Glosario](../../README.md) · [← Indicador](./indicador.md) · [Indicador de nivel de servicio →](./indicador-de-nivel-de-servicio.md)
