# Explosión de estados

[↑ Glosario](../../README.md) · [← Exploración frente a producto](./exploracion-frente-a-producto.md) · [Explotación conocida →](./explotacion-conocida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

La **explosión de estados** es el crecimiento del número de estados globales de un sistema con el número de componentes concurrentes ([SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md)). [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) la precisa como el crecimiento exponencial del espacio de estados con el tamaño del modelo. Es el principal obstáculo práctico de la verificación de modelos.

## Por qué importa

El costo de verificar crece con el espacio de estados, y este crece de forma exponencial. Con unos pocos componentes la verificación puede tardar horas o no terminar. Cambia cómo se modela: hay que decidir qué se abstrae, qué se acota y qué se reduce, o la herramienta no llega a ningún resultado.

## Cómo funciona

Cada componente concurrente añade su propio estado, y los estados globales son el **producto** de los locales. [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) ejemplifica con N estudiantes que envían a la vez, con tres estados locales cada uno: el espacio tiene 3ᴺ combinaciones. [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) lo mide en un laboratorio: n procesos independientes de cuatro pasos tienen 4ⁿ estados: **16 con 2, 1.024 con 5 y 16.384 con 7**. Cada proceso añadido multiplica por cuatro.

Tres defensas, según [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md):

- **Abstraer**: modelar solo lo que importa para la propiedad, descartando detalles irrelevantes.
- **Acotar**: probar con N pequeño (dos o tres procesos), con la hipótesis de que un defecto de coordinación suele manifestarse con pocos participantes.
- **Reducir por simetría**: tratar como idénticos los componentes intercambiables (los estudiantes son equivalentes entre sí), de modo que estados que difieren solo en el orden de los nombres se cuentan una vez. La reducción por simetría solo es válida si la intercambiabilidad es real; si los componentes se distinguen (uno es administrador), la reducción puede ocultar defectos.

La razón de que funcione es que la propiedad suele depender de una estructura pequeña del sistema; el resto del espacio es redundante respecto de ella. El riesgo es que la abstracción elimine justo lo que causaba el defecto.

## Ejemplo

Tres estudiantes que envían entregas en paralelo, cada uno con estados «sin enviar», «enviando» y «enviado»: 3³ = 27 estados globales. Con diez estudiantes, 3¹⁰ = 59.049. Con simetría (los estudiantes son intercambiables), basta contar cuántos hay en cada estado: la combinación (2 sin enviar, 1 enviando, 0 enviado) representa a todas las asignaciones equivalentes, y el espacio se reduce a unas decenas de configuraciones. (Cálculo propio para ilustrar la defensa de [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md).)

## Errores y confusiones comunes

- **La verificación tarda horas con pocos componentes**: explosión sin reducción; corrección: abstraer detalles, acotar N y aplicar simetría solo a componentes intercambiables.
- **Reducir por simetría componentes que no lo son.**
- **Abstraer lo que causa el defecto.**
- **Confundirla con la complejidad de un algoritmo**: aquí crece el número de configuraciones del sistema.

## Límites y cuándo no aplica

Las defensas aceptan perder garantía: lo verificado con N pequeño no prueba N grande. En modelos muy secuenciales con pocos componentes, el problema no aparece. Algunas técnicas (verificación simbólica, ejecución parcial del espacio) amplían lo verificable, pero no eliminan el crecimiento exponencial en general.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espacio de estados](./espacio-de-estados.md), [Componente](../c/componente.md), [Estado](./estado.md), [Modelo](../m/modelo.md), [Bloqueo](../b/bloqueo.md), [Contraejemplo](../c/contraejemplo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md).

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

[↑ Glosario](../../README.md) · [← Exploración frente a producto](./exploracion-frente-a-producto.md) · [Explotación conocida →](./explotacion-conocida.md)
