# Protocolos de mensajes

[↑ Glosario](../../README.md) · [← Prorrateo](./prorrateo.md) · [Prototipo →](./prototipo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Un **protocolo de mensajes** es, en [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), el acuerdo sobre la forma y el significado de los mensajes que intercambian los componentes de un modelo concurrente, como los actores. Un mensaje necesita **tipo, datos, correlación y respuesta esperada**. Quien envía y quien recibe no comparten variables: se comunican solo por mensajes, así que el protocolo es el contrato completo entre ellos. Cambiar la forma de un mensaje equivale a cambiar un contrato.

## Por qué importa

En un modelo de actores se evitan los datos compartidos mutables (fuente de condiciones de carrera) sustituyéndolos por mensajes. Pero el problema no desaparece: se traslada a los protocolos. [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md) lo dice: los actores **desplazan los problemas hacia protocolos, supervisión y entrega**. La decisión que cambia es dónde se ponen el cuidado y las pruebas: en el diseño de los mensajes (qué significan, qué orden asumen, qué pasa si no llegan) y no solo en cerrojos.

## Cómo funciona

Los cuatro elementos de un mensaje cumplen funciones distintas:

- **Tipo:** qué clase de petición o hecho es; permite al receptor decidir cómo tratarlo.
- **Datos:** la información necesaria, y solo ella.
- **Correlación:** un identificador que enlaza una respuesta con su petición, imprescindible cuando varias peticiones están en vuelo y las respuestas pueden llegar en otro orden.
- **Respuesta esperada:** si hay respuesta, de qué forma, en qué plazo y qué ocurre si no llega.

Hay riesgos específicos. Los **mensajes mutables o con referencias compartidas erosionan el aislamiento**: si emisor y receptor comparten el mismo objeto, vuelven los problemas de datos compartidos; por eso los mensajes se tratan como valores inmutables o se copian. Y en entornos **distribuidos**, los mensajes deben **serializarse** (convertirse en bytes) y **fallar de forma clara ante versiones distintas**: dos nodos con versiones diferentes del protocolo no pueden asumir que se entienden.

## Ejemplo

Un actor que gestiona un contador. El protocolo define dos mensajes con correlación:

```python
# mensajes inmutables (tuplas con nombre)
Incrementar = namedtuple("Incrementar", "cantidad")
Consultar   = namedtuple("Consultar",   "id_correlacion")
Valor       = namedtuple("Valor",       "id_correlacion total")
```

El actor procesa un mensaje a la vez desde su buzón, así que no hay carrera interna. El cliente envía `Consultar("c-17")` y espera `Valor("c-17", total)`; si llegan dos respuestas, la correlación dice a cuál petición corresponde. [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md) contrasta el enfoque con los defectos de datos compartidos: totales distintos entre ejecuciones por leer-modificar-escribir sin exclusión mutua (se corrige con cerrojo, cola con dueño único u operación atómica) y cuatro hilos que no aceleran un cálculo por el bloqueo global del intérprete (se usan procesos o se libera el GIL en código nativo).

## Errores y confusiones comunes

- **Mensajes sin correlación.** No se sabe a qué petición responde cada respuesta.
- **Mensajes mutables compartidos.** Reintroducen la carrera de datos.
- **Cambiar la forma del mensaje sin versionar.** Rompe a los receptores antiguos.
- **Suponer entrega y orden garantizados.** Un protocolo debe decir qué pasa con pérdidas, duplicados y reordenamientos.

## Límites y cuándo no aplica

Los actores no vuelven distribuido ni resiliente cualquier programa ([SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md)): añaden la necesidad de supervisión (qué ocurre si un actor falla), de gestión de buzones llenos y de pruebas de protocolo. Para un cálculo de un solo hilo, o para estado compartido pequeño bien protegido con un cerrojo, el modelo es más complejo de lo necesario. La clase siguiente construye un criterio para combinar modelos sin un collage arquitectónico.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Correlación](../c/correlacion.md), [Tipo](../t/tipo.md), [Actor, buzón y propiedad del estado](../a/actor-buzon-y-propiedad-del-estado.md), [Concurrencia, paralelismo e intercalación](../c/concurrencia-paralelismo-e-intercalacion.md), [Consistencia y presión del buzón](../c/consistencia-y-presion-del-buzon.md), [Fallo, enlaces y supervisión](../f/fallo-enlaces-y-supervision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Prorrateo](./prorrateo.md) · [Prototipo →](./prototipo.md)
