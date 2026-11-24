# Estados e invariantes

[↑ Glosario](../../README.md) · [← Estado válido](./estado-valido.md) · [Estampida →](./estampida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Los **estados** son las situaciones por las que pasa una entidad (por ejemplo, una entrega: borrador, enviada, en revisión, calificada), y los **invariantes** son las propiedades que deben cumplirse en todas ellas ([SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)). La pareja es una herramienta de requisitos: el ciclo de vida de la entidad se modela con estados y lo que nunca debe romperse se escribe como invariante.

## Por qué importa

Lo que siempre debe ser cierto se verifica en cada transición. Sin invariantes explícitos, las reglas viven repartidas en el código y cada ruta de cambio las respeta o no. Cambia el modo de especificar: en lugar de repetir la misma regla en cada operación, se escribe una vez como invariante y se comprueba siempre.

## Cómo funciona

[SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) ilustra con una entrega que pasa por borrador, enviada, en revisión y calificada. Ciertas propiedades deben cumplirse **siempre**: una entrega calificada no se modifica sin reabrirse; una entrega enviada tiene fecha de envío. Un **invariante** es una regla que **no depende de la transición que ocurra**: se escribe una vez y se comprueba en cada una (en la frontera de cada operación que cambia el estado).

La utilidad analítica es doble. Primero, los estados delimitan qué operaciones son válidas en cada situación: «editar» no está permitido en «calificada». Segundo, **descubrir que algo debería ser un invariante** es parte del análisis de requisitos: aparece cuando alguien pregunta «¿puede pasar que…?» y la respuesta es «nunca». Escribirlo evita que cada operación tenga que recordarlo.

Los estados se representan con una máquina de estados (transiciones entre ellos) y, para verificar, los invariantes se comprueban sobre todos los estados alcanzables. Un invariante que falla lejos de donde se corrompió el estado indica que se comprueba tarde: la corrección es comprobarlo en la frontera de cada operación pública, al menos en pruebas.

La política de entregas tardías de la plataforma se registra como regla con identificador, texto, responsable y fecha, separada del requisito que la aplica, de modo que la regla vive en un solo punto.

## Ejemplo

Estados de una entrega: borrador → enviada → en revisión → calificada. Invariantes: (1) toda entrega enviada tiene fecha de envío; (2) una entrega calificada tiene nota entre 0 y 100; (3) una entrega calificada no se modifica sin reabrirse. La operación «editar texto» se rechaza si el estado es «calificada»; la operación «calificar» comprueba que el resultado respete (2) antes de confirmar. (Ejemplo derivado de [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).)

## Errores y confusiones comunes

- **Dos módulos calculan notas distintas**: la regla vive duplicada; corrección: único punto con identificador y responsable.
- **El comité pregunta «¿qué pasa si…?» y nadie lo sabe**: solo se redactaron casos felices; corrección: enumerar combinaciones y asignar acción o decisión pendiente.
- **Confundir estado con dato**: no todo valor de un campo es un estado.
- **Invariantes comprobados solo al final.**

## Límites y cuándo no aplica

El modelo de estados cubre el comportamiento modelado; si falta un estado, falta una regla. Con muchos estados y componentes concurrentes, el espacio se multiplica (explosión de estados). Algunos invariantes dependen de más de una entidad o de tiempo, y son más difíciles de comprobar localmente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Regla de negocio](../r/regla-de-negocio.md), [Requisito funcional](../r/requisito-funcional.md), [Tablas de decisión](../t/tablas-de-decision.md), [Tiempo, plazos y zonas](../t/tiempo-plazos-y-zonas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de frase para requisitos; autoridad: IEEE International Requirements Engineering Conference.
- [Sitio de EARS (Alistair Mavin)](https://alistairmavin.com/ears/) — descripción de las plantillas por su autor.
- [Business Rules Manifesto](https://www.businessrulesgroup.org/brmanifesto.htm) — reglas como requisito de primer nivel; autoridad: Business Rules Group.
- [RFC 3339: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc3339) — formato de instantes con desplazamiento; autoridad: IETF.
- [IANA: Time Zone Database](https://www.iana.org/time-zones) — origen de las reglas de zona y de sus cambios; autoridad: IANA.

---

[↑ Glosario](../../README.md) · [← Estado válido](./estado-valido.md) · [Estampida →](./estampida.md)
