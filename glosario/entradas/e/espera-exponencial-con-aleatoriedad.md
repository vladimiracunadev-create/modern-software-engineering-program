# Espera exponencial con aleatoriedad

[↑ Glosario](../../README.md) · [← Espera](./espera.md) · [Espía →](./espia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Política de reintento cuya espera crece de forma exponencial con un componente aleatorio.

Definición de trabajo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), existe con este propósito: la clase existe para que diseñes lo que ve y puede hacer una persona cuando una vista no tiene datos, está esperando, falló o se recuperó, y para que representes esos casos como estados explícitos y no como un montón de banderas que pueden contradecirse.

## Cómo funciona

Según [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

Mil clientes empiezan en un intervalo de 0,5 s, el servicio cae durante 10 s y vuelve. Reintentar cada segundo suma 10 000 peticiones durante la caída y un pico de 1 000 por segundo al recuperarse (total 11 000). La espera exponencial sin aleatoriedad suma 3 000 durante la caída y mantiene el pico de 1 000 al recuperarse: los clientes están sincronizados (total 4 000). La espera exponencial con aleatoriedad completa suma 3 978 durante la caída y baja el pico al recuperarse a 151 por segundo (total 4 978). La aleatoriedad cuesta algo más de tráfico y reparte la carga.

Según [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md):

En la plataforma, cada vista con datos remotos declara sus estados en una tabla (carga, vacío, error, con datos, parcial), el texto de cada uno y la acción de recuperación. Los componentes usan un único valor de estado, y una prueba recorre las transiciones declaradas y falla si aparece un par no declarado. Los reintentos usan espera exponencial con aleatoriedad, tope de cinco intentos y clave de idempotencia; el indicador de carga espera 300 ms y dura al menos 600 ms.

## Ejemplo

Ejemplo de [SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada vista con datos remotos declara sus estados en una tabla (carga, vacío, error, con datos, parcial), el texto de cada uno y la acción de recuperación. Los componentes usan un único valor de estado, y una prueba recorre las transiciones declaradas y falla si aparece un par no declarado. Los reintentos usan espera exponencial con aleatoriedad, tope de cinco intentos y clave de idempotencia; el indicador de carga espera 300 ms y dura al menos 600 ms.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El servicio cae de nuevo al recuperarse** — causa: reintentos sincronizados. Corrección: espera exponencial con aleatoriedad y tope de intentos. ([SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-172 — Estados vacíos, carga, error y recuperación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún servicio ni se midió ninguna latencia propia, y los eventos, la sincronía de los clientes y la latencia lognormal son supuestos del autor. La siguiente clase pregunta si todo lo anterior es perceptible, operable y comprensible para toda la población.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Espera](./espera.md), [Reintentos](../r/reintentos.md), [Estado imposible](./estado-imposible.md), [Estado vacío](./estado-vacio.md), [Indicador de carga](../i/indicador-de-carga.md).
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

[↑ Glosario](../../README.md) · [← Espera](./espera.md) · [Espía →](./espia.md)
