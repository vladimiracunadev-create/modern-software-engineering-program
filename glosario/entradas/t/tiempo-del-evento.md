# Tiempo del evento

[↑ Glosario](../../README.md) · [← Tiempo de visibilidad](./tiempo-de-visibilidad.md) · [Tiempo hasta detectar →](./tiempo-hasta-detectar.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Instante en que ocurrió el hecho, distinto del instante en que llegó al sistema.

Definición de trabajo de [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md): Instante en que ocurrió lo que el dato describe.

## Por qué importa

En [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), el tema «Tiempo del evento y ventanas» importa porque define cuándo un recuento es completo y qué pasa con lo que llega tarde.

## Cómo funciona

Según [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md):

Cada evento tiene dos tiempos: cuándo ocurrió y cuándo llegó. Contar «entregas por minuto» con el tiempo de llegada mezcla minutos; contarlas con el tiempo del evento exige decidir cuándo una ventana está completa. La **marca de agua** es la estimación de hasta qué tiempo del evento se espera que hayan llegado todos los datos; los que llegan después son **tardíos** y se descartan, se aplican como corrección o se envían a un canal aparte. La tolerancia de retraso fija ese compromiso: esperar más da resultados más completos y más tardíos. No existe una tolerancia correcta general: depende de la distribución de retrasos y de lo que cueste mostrar un número que luego cambia.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md):

El equipo de la plataforma separa la cadena en tres tablas: `eventos_crudos` (se añade, se conserva, tiene un identificador de evento), `entregas_por_curso_hora` (escritura por clave `curso+hora`) y `cuarentena` (eventos que fallan una regla). La carga usa el identificador del lote para no repetirlo y las ventanas esperan 120 s; lo que llega después se aplica como corrección a la fila de la hora y se anota en un contador de «correcciones tardías». El tablero muestra la hora actual como «provisional» y la anterior como «cerrada».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los informes mezclan minutos** — causa: se agrupa por tiempo de llegada. Corrección: usar el tiempo del evento y declarar la marca de agua. ([SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md)) son: Las definiciones son operativas para la cadena de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor de procesamiento, broker ni base de datos analítica: los fallos, los retrasos lognormales y la distribución de Zipf son construcciones del autor. La siguiente clase usa esas tablas como entrada de un componente de aprendizaje automático.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hecho](../h/hecho.md), [Instante](../i/instante.md), [Dato tardío](../d/dato-tardio.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Evento tardío](../e/evento-tardio.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Akidau et al., «The Dataflow Model» (VLDB, 2015)](https://doi.org/10.14778/2824032.2824076) — tiempo del evento, ventanas y marcas de agua; autoridad: Proceedings of the VLDB Endowment.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — fundamentos de sistemas de datos, reintentos y procesamiento por flujo; autoridad: autor del libro.
- [Apache Beam, guía de programación](https://beam.apache.org/documentation/programming-guide/) — marcas de agua y datos tardíos en un modelo unificado; autoridad: Apache Software Foundation.
- [Dean y Ghemawat, «MapReduce» (Communications of the ACM, 2008)](https://doi.org/10.1145/1327452.1327492) — reparto por clave y reejecución de tareas; autoridad: Communications of the ACM.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: Enterprise Integration Patterns.

---

[↑ Glosario](../../README.md) · [← Tiempo de visibilidad](./tiempo-de-visibilidad.md) · [Tiempo hasta detectar →](./tiempo-hasta-detectar.md)
