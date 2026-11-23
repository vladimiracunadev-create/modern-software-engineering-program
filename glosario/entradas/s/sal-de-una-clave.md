# Sal de una clave

[↑ Glosario](../../README.md) · [← Sal](./sal.md) · [Salida accesible →](./salida-accesible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Sufijo aleatorio que reparte una clave frecuente entre varias particiones a costa de recombinar después.

Definición de trabajo de [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md).

## Por qué importa

La clase donde se define, [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), existe con este propósito: la clase existe para que construyas una cadena de datos cuyo resultado no cambie porque algo falló a la mitad, porque un evento llegó tarde o porque una clave es mucho más popular que las demás, y para que sepas decir cuándo el número de un tablero es completo y cuándo es provisional.

## Cómo funciona

[SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la cadena de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md):

El equipo de la plataforma separa la cadena en tres tablas: `eventos_crudos` (se añade, se conserva, tiene un identificador de evento), `entregas_por_curso_hora` (escritura por clave `curso+hora`) y `cuarentena` (eventos que fallan una regla). La carga usa el identificador del lote para no repetirlo y las ventanas esperan 120 s; lo que llega después se aplica como corrección a la fila de la hora y se anota en un contador de «correcciones tardías». El tablero muestra la hora actual como «provisional» y la anterior como «cerrada».

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md)) son:

- **Aparecen filas duplicadas «a veces»** — causa: carga que añade y reintentos a mitad de lote. Corrección: escritura por clave, tabla temporal con publicación atómica o registro de lotes.
- **Un recuento cambia después de publicarlo** — causa: eventos tardíos sin política. Corrección: marcar provisional/cerrado y aplicar correcciones con contador.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md)) son: Las definiciones son operativas para la cadena de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor de procesamiento, broker ni base de datos analítica: los fallos, los retrasos lognormales y la distribución de Zipf son construcciones del autor. La siguiente clase usa esas tablas como entrada de un componente de aprendizaje automático.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Partición](../p/particion.md), [Evento tardío](../e/evento-tardio.md), [Idempotencia](../i/idempotencia.md), [Marca de agua](../m/marca-de-agua.md), [Tiempo del evento](../t/tiempo-del-evento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — fundamentos de sistemas de datos, reintentos y procesamiento por flujo; autoridad: autor del libro.
- [Akidau et al., «The Dataflow Model» (VLDB, 2015)](https://doi.org/10.14778/2824032.2824076) — tiempo del evento, ventanas y marcas de agua; autoridad: Proceedings of the VLDB Endowment.
- [Apache Beam, guía de programación](https://beam.apache.org/documentation/programming-guide/) — marcas de agua y datos tardíos en un modelo unificado; autoridad: Apache Software Foundation.
- [Dean y Ghemawat, «MapReduce» (Communications of the ACM, 2008)](https://doi.org/10.1145/1327452.1327492) — reparto por clave y reejecución de tareas; autoridad: Communications of the ACM.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: Enterprise Integration Patterns.

---

[↑ Glosario](../../README.md) · [← Sal](./sal.md) · [Salida accesible →](./salida-accesible.md)
