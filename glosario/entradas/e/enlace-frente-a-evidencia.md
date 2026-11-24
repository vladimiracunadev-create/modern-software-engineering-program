# Enlace frente a evidencia

[↑ Glosario](../../README.md) · [← Enlace de salto](./enlace-de-salto.md) · [Enlace profundo →](./enlace-profundo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La distinción **enlace frente a evidencia** es la diferencia entre declarar que una prueba pertenece a un requisito y demostrar, con una ejecución fechada, que lo verifica ([SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)). Un enlace es una afirmación de pertenencia; la evidencia es un resultado observado.

## Por qué importa

Una matriz de trazabilidad con todos los enlaces puestos puede dar una falsa sensación de cobertura. Cambia lo que se acepta en una auditoría o en una decisión de entrega: no basta que el requisito tenga una prueba enlazada; hay que saber que la prueba se ejecutó, cuándo, sobre qué versión y con qué resultado.

## Cómo funciona

Según [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), un enlace dice «esta prueba pertenece a este requisito»; **no dice que la prueba lo verifique**. Una prueba puede ejecutar el código del requisito sin comprobar su resultado (no tiene aserciones), o comprobar algo distinto de lo que el requisito pide. La **evidencia** es el resultado de ejecutar la prueba en una versión concreta, con fecha y entorno.

La trazabilidad completa conecta **tres cosas**: el enlace, la prueba y su última ejecución. Cualquiera de las tres ausente deja una brecha: sin enlace, la prueba no se sabe de qué requisito es; sin prueba, el enlace apunta a nada; sin ejecución reciente, no se sabe si sigue pasando. El mecanismo práctico de la clase es poner una **etiqueta en cada artefacto** (la prueba lleva el identificador del requisito) y un **verificador al integrar** que comprueba que los enlaces existen y que las pruebas enlazadas se ejecutan y pasan. Así el enlace deja de ser una promesa en un documento aparte (que, si nadie actualiza, hace que una auditoría tarde un día en encontrar una prueba) y se convierte en algo comprobado en cada integración.

Esto se conecta con la evidencia de cumplimiento: una afirmación vale lo que la evidencia que la sostiene.

## Ejemplo

El requisito REQ-12 («un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza») tiene una prueba `test_limite_subida` etiquetada con `REQ-12`. Enlace: existe. Pero si la prueba solo sube el archivo y no comprueba el rechazo, el enlace no demuestra nada. Evidencia: el informe de la última ejecución en integración continua muestra que la prueba pasó sobre el commit X en la fecha Y, y una mutación que quita el rechazo hace fallar la prueba. (Ilustración del argumento de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md).)

## Errores y confusiones comunes

- **Una auditoría tarda un día en encontrar una prueba**: la matriz está en un documento que nadie actualiza; corrección: etiqueta en la prueba y verificación al integrar.
- **Casi todo cambio «afecta» a casi todo**: se enlazó todo con todo.
- **Tomar el enlace por demostración.**
- **Evidencia sin fecha ni versión.**

## Límites y cuándo no aplica

Exigir evidencia fechada para cada enlace tiene un costo; para requisitos de bajo riesgo, un enlace verificado puede bastar. Incluso con evidencia, la calidad de la prueba importa: una prueba débil que pasa sigue siendo evidencia débil, por lo que conviene complementar con mutación o lectura humana.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis de impacto](../a/analisis-de-impacto.md), [Granularidad de los enlaces](../g/granularidad-de-los-enlaces.md), [Mantenimiento y deterioro](../m/mantenimiento-y-deterioro.md), [Trazabilidad bidireccional](../t/trazabilidad-bidireccional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gotel y Finkelstein: An analysis of the requirements traceability problem (1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad; autoridad: IEEE International Conference on Requirements Engineering.
- [Cleland-Huang et al.: Software traceability, trends and future directions (2014)](https://doi.org/10.1145/2593882.2593891) — estado y retos; autoridad: ACM, Future of Software Engineering.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — trazabilidad entre necesidades, requisitos y verificación; autoridad: ISO, IEC e IEEE.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de requisitos y trazabilidad; autoridad: IEEE Computer Society.
- [Python: `sys.settrace`](https://docs.python.org/3/library/sys.html#sys.settrace) — registro de llamadas durante la ejecución.

---

[↑ Glosario](../../README.md) · [← Enlace de salto](./enlace-de-salto.md) · [Enlace profundo →](./enlace-profundo.md)
