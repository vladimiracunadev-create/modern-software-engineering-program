# Reducción por simetría

[↑ Glosario](../../README.md) · [← Reducción por dimensiones](./reduccion-por-dimensiones.md) · [Reemplazo →](./reemplazo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Tratar como idénticos los estados que difieren solo por permutación de componentes intercambiables.

Definición de trabajo de [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md).

## Por qué importa

La clase donde se define, [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), existe con este propósito: la clase existe para modelar el comportamiento de una entidad como máquina de estados y explorar todos sus estados alcanzables con una búsqueda, de modo que una violación de un invariante llegue acompañada de la traza más corta que la produce y no de una sospecha.

## Cómo funciona

Según [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md):

Cada componente concurrente añade su propio estado y los estados globales son el producto. Con N estudiantes que envían a la vez y tres estados locales cada uno, el espacio crece exponencialmente. Las defensas son abstraer (modelar solo lo que importa), acotar (probar con N pequeño) y reducir por simetría (tratar como idénticos los estudiantes intercambiables). La reducción por simetría solo es válida si la intercambiabilidad es real: si una cola atiende por prioridad individual, ordenar el estado destruye diferencias que importan.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md):

En la plataforma, el ciclo de vida de la entrega vive en una tabla de transiciones (estado, acción, estado siguiente, condición) que usan tanto el código de producción como el verificador. El verificador, ejecutado en integración continua, explora el modelo con los invariantes (si hay nota, estado válido; una entrega anulada no vuelve a ningún estado; el contador de apelaciones no supera 2) y falla con la traza si hay violación. Un segundo modelo con la concurrencia de las revisoras explora los intercalados de lectura y escritura con k pequeño.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La reducción por simetría oculta un defecto** — causa: los componentes no eran intercambiables. Corrección: comprobar la intercambiabilidad y retirar la reducción si falla. ([SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La reducción por simetría solo es válida si la intercambiabilidad es real: si una cola atiende por prioridad individual, ordenar el estado destruye diferencias que importan. ([SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Estado](../e/estado.md), [Contraejemplo](../c/contraejemplo.md), [Explosión de estados](../e/explosion-de-estados.md), [Invariante](../i/invariante.md), [Máquina de estados](../m/maquina-de-estados.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

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

[↑ Glosario](../../README.md) · [← Reducción por dimensiones](./reduccion-por-dimensiones.md) · [Reemplazo →](./reemplazo.md)
