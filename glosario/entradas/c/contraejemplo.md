# Contraejemplo

[↑ Glosario](../../README.md) · [← Contradicción](./contradiccion.md) · [Contraejemplo mínimo →](./contraejemplo-minimo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

En verificación formal, un **contraejemplo** es la traza de pasos desde el estado inicial hasta una violación de una propiedad ([SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md)). [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) lo precisa: traza finita de transiciones que lleva del estado inicial a un estado que viola una propiedad. Es la salida de un verificador de modelos cuando la propiedad no se cumple.

## Por qué importa

Es la salida más útil de un verificador: un escenario concreto. Un resultado «la propiedad falla» no dice cómo reproducirlo; un contraejemplo da la secuencia exacta de pasos, que se puede leer, discutir y convertir en una prueba. Cambia cómo se encuentran los defectos de concurrencia y protocolo: no se esperan a observarlos en producción.

## Cómo funciona

[SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) describe el método. Un modelo describe el sistema como un conjunto de estados posibles (valores de las variables y posición de cada proceso) y las transiciones que pueden ocurrir. Una **propiedad de seguridad** es un invariante: una condición que debe cumplirse en todos los estados alcanzables («no hay dos procesos en la sección crítica»). El verificador parte del estado inicial, explora los sucesores con una **búsqueda en anchura** y comprueba el invariante en cada estado. Si encuentra uno que lo viola, reconstruye el camino que llevó hasta él: ese camino es el contraejemplo.

La búsqueda en anchura tiene una propiedad útil: el primer contraejemplo encontrado es de **longitud mínima**, lo que lo hace más fácil de leer (existe también el contraejemplo mínimo como concepto aparte). Si el verificador agota el espacio sin hallar violación, la propiedad se cumple en el modelo (no necesariamente en el sistema real, porque el modelo es una abstracción).

[SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) da un caso de laboratorio: un equipo modela en TLA+ el protocolo de reserva de un tramo entre dos controladores ferroviarios, con tres estados por controlador y un canal que puede perder mensajes. El verificador halla en la primera ejecución un contraejemplo de **once pasos**: un mensaje perdido y un reintento hacen que ambos controladores crean tener el tramo. En el sistema real nunca se había observado, y una prueba tradicional difícilmente lo habría producido.

## Ejemplo

Contraejemplo de cuatro pasos (ilustrativo): 1) el controlador A envía «reservar tramo»; 2) el canal pierde el mensaje; 3) A reintenta tras el tiempo de espera y B responde «concedido» al primer envío retrasado; 4) A y B creen tener el tramo. La traza es una receta para escribir una prueba que reproduzca el defecto y para corregir el protocolo. (Reducción didáctica del caso de [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md).)

## Errores y confusiones comunes

- **Confundir contraejemplo con prueba fallida**: el contraejemplo viene de explorar el modelo, no de ejecutar el sistema.
- **Corregir el modelo y no el sistema** (o al revés).
- **Ignorar un contraejemplo por «improbable».**
- **Creer que la ausencia de contraejemplo prueba el sistema**: solo prueba el modelo.

## Límites y cuándo no aplica

El modelo debe ser fiel a lo que importa; si abstrae mal, el contraejemplo puede ser espurio o faltar uno real. El número de estados crece muy rápido (explosión de estados) y limita lo que se verifica. En lógica y matemáticas, «contraejemplo» tiene también el sentido general de caso que refuta una afirmación universal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado inicial](../e/estado-inicial.md), [Estado](../e/estado.md), [Propiedad](../p/propiedad.md), [Transición](../t/transicion.md), [Bloqueo](../b/bloqueo.md), [Explosión de estados](../e/explosion-de-estados.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (239 clases más lo mencionan; las que más):

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-056](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md), [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Clarke y Emerson, «Design and synthesis of synchronization skeletons using branching time temporal logic» (1981)](https://doi.org/10.1007/BFb0025774) — origen del model checking; autoridad: Logics of Programs, Lecture Notes in Computer Science.
- [Holzmann, «The model checker SPIN» (IEEE TSE, 1997)](https://doi.org/10.1109/32.588521) — herramienta de exploración de estados de sistemas concurrentes; autoridad: IEEE Transactions on Software Engineering.
- [Pnueli, «The temporal logic of programs» (FOCS, 1977)](https://doi.org/10.1109/SFCS.1977.32) — lógica temporal para propiedades de seguridad y de vivacidad; autoridad: IEEE FOCS.
- [Harel, «Statecharts» (Science of Computer Programming, 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados jerárquicos y concurrentes; autoridad: Science of Computer Programming.
- [Newcombe et al., «How Amazon Web Services uses formal methods» (CACM, 2015)](https://doi.org/10.1145/2699417) — uso industrial de TLA+; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Contradicción](./contradiccion.md) · [Contraejemplo mínimo →](./contraejemplo-minimo.md)
