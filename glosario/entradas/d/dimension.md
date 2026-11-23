# Dimensión

[↑ Glosario](../../README.md) · [← Difusión por rumor](./difusion-por-rumor.md) · [Dimensión de cambio lento →](./dimension-de-cambio-lento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Contexto con el que se agrupa o filtra un hecho.

Definición de trabajo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md): Variable del problema cuyos valores definen casos.

## Por qué importa

En [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), el tema «Hechos y dimensiones» importa porque separan lo que se mide de aquello por lo que se mide.

## Cómo funciona

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

Un hecho es una medición de un evento de negocio: una línea de pedido, una entrega, una lectura. Una dimensión es el contexto con el que se agrupa o filtra: cliente, producto, curso, fecha. La frase que hace de contrato es «una fila de este hecho es un ____ por ____»: una línea de pedido por pedido y por producto. Todo lo que se sume debe pertenecer a ese grano: el importe de la línea sí; el costo de envío del pedido no, porque se repite en cada línea. Declarar el grano antes de diseñar columnas es la regla más barata y más ignorada del modelado.

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

El equipo de *Avisos* modela los avisos leídos. Escribe la frase «una fila es una lectura de un aviso por un estudiante en un instante», sus dimensiones (estudiante, aviso, curso, fecha) y decide que la dimensión de estudiante conserva historia porque los estudiantes cambian de curso a mitad de año. Añade una prueba: la suma de lecturas del hecho debe coincidir con la cuenta de eventos de la zona intermedia cada día. A la tercera semana la prueba falla un día con un 8 % de diferencia; la causa es una unión con la dimensión de curso que no filtraba por vigencia y duplicaba las lecturas de quienes cambiaron de curso ese día.

## Ejemplo

Ejemplo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* modela los avisos leídos. Escribe la frase «una fila es una lectura de un aviso por un estudiante en un instante», sus dimensiones (estudiante, aviso, curso, fecha) y decide que la dimensión de estudiante conserva historia porque los estudiantes cambian de curso a mitad de año. Añade una prueba: la suma de lecturas del hecho debe coincidir con la cuenta de eventos de la zona intermedia cada día.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El costo es que cada carga debe resolver de clave de negocio a clave sustituta, y que los datos huérfanos (un hecho sin dimensión) deben tener una fila especial «desconocido» y no desaparecer en una unión interna. ([SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md))
- Si la suite tiene cien ejemplos y una dimensión no varía, el problema no es de cantidad. ([SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Hecho](../h/hecho.md), [Problemas](../p/problemas.md), [Valor](../v/valor.md), [Abanico de uniones](../a/abanico-de-uniones.md), [ATDD](../a/atdd.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (62 clases más lo mencionan; las que más):

[SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Difusión por rumor](./difusion-por-rumor.md) · [Dimensión de cambio lento →](./dimension-de-cambio-lento.md)
