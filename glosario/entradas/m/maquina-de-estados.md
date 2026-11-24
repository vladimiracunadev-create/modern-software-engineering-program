# Máquina de estados

[↑ Glosario](../../README.md) · [← Mapping](./mapping.md) · [Máquina virtual →](./maquina-virtual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Una **máquina de estados** es un modelo con un conjunto finito de estados, un estado inicial y transiciones etiquetadas con eventos o acciones, que describe cómo reacciona un sistema a su entorno. [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) la presenta como técnica de especificación; [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) la usa para el comportamiento de la interfaz; [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) la aplica al ciclo de vida de una suscripción (vigente, vencida, cancelada, etc.).

## Por qué importa

Hace explícito qué puede ocurrir y qué decide el acceso. Las reglas de negocio con tiempo suelen describirse con frases sueltas que dejan huecos («si el pago falla, se reintenta»), y los huecos aparecen como defectos. Dibujar estados y transiciones obliga a responder para cada estado qué evento puede ocurrir y a dónde lleva, y a declarar lo que no está permitido.

## Cómo funciona

El modelo tiene cuatro elementos: **estados** (situaciones estables), **eventos** (lo que ocurre), **transiciones** (de qué estado, con qué evento, a qué estado, con qué acción) y un **estado inicial**. La propiedad útil es que el comportamiento queda enumerable: se puede comprobar que cada par (estado, evento) tiene una respuesta definida, que no hay estados inalcanzables y que no hay estados sin salida salvo los finales intencionales. Una matriz estado × evento es una forma de revisar la completitud; las celdas vacías son preguntas pendientes.

[SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) sigue el ciclo de una suscripción con transiciones explícitas y el ciclo de facturación anclado, y propone un ejercicio de ingeniería inversa: tomar una suscripción real (streaming, nube) y reconstruir su máquina de estados respondiendo qué ocurre si se cancela hoy, si el pago falla o si se cambia de plan a mitad de ciclo; lo que no se pudo responder sin probar es lo que el producto debería haber puesto por escrito.

## Ejemplo

Una suscripción con estados `prueba`, `activa`, `en_mora`, `cancelada`. Transiciones: `prueba → activa` al pagar; `activa → en_mora` si el cobro falla; `en_mora → activa` si el reintento tiene éxito; `en_mora → cancelada` tras agotar reintentos; `activa → cancelada` si la persona cancela. La pregunta «¿qué ocurre si cancelo estando en mora?» expone una celda no definida: hay que decidir si cancela de inmediato o se debe lo adeudado. (Modelo ilustrativo; [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) desarrolla uno más completo.)

## Errores y confusiones comunes

- **Estados que son en realidad datos**: si el número de estados crece con cada valor posible de un campo, el modelo es inadecuado.
- **Transiciones implícitas**: el código permite cambios que el modelo no declara.
- **Confundir estado con evento**: «pago fallido» es un evento; «en mora», el estado resultante.
- **Creer que el modelo cubre todo el dominio**: solo cubre el comportamiento que se modeló.

## Límites y cuándo no aplica

[SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) es explícita en lo que la máquina de estados no decide: los impuestos aplicables (dependen de la jurisdicción del cliente y del producto), la regulación sobre cobros recurrentes y avisos previos, el reconocimiento contable del ingreso en planes anuales y la facturación electrónica que algunos países exigen. Son restricciones reales que se incorporan con asesoría especializada; un procesador de pagos o un servicio de facturación puede absorber parte, con su propio costo y dependencia. Además, con muchos estados concurrentes el modelo se vuelve inmanejable y se descompone en máquinas jerárquicas o en varias máquinas coordinadas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado inicial](../e/estado-inicial.md), [Conjunto](../c/conjunto.md), [Entorno](../e/entorno.md), [Estado](../e/estado.md), [Contraejemplo](../c/contraejemplo.md), [Dispersión](../d/dispersion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Therac-25](../../../casos/fallo/therac-25.md).

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

[↑ Glosario](../../README.md) · [← Mapping](./mapping.md) · [Máquina virtual →](./maquina-virtual.md)
