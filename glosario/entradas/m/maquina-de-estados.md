# Máquina de estados

[↑ Glosario](../../README.md) · [← Mapping](./mapping.md) · [Máquina virtual →](./maquina-virtual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Modelo con un conjunto de estados, un estado inicial y transiciones etiquetadas con acciones.

Definición de trabajo de [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md): Modelo con un conjunto finito de estados, eventos y transiciones que describe cómo reacciona un sistema a su entorno.

## Por qué importa

En [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), el tema «Máquina de estados» importa porque hace explícito qué puede ocurrir y qué decide el acceso.

## Cómo funciona

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

La máquina de estados no decide los impuestos aplicables (que dependen de la jurisdicción del cliente y del producto), ni la regulación sobre cobros recurrentes y avisos previos, ni el reconocimiento contable del ingreso en planes anuales, ni la facturación electrónica que algunos países exigen. Son restricciones reales que se incorporan al modelo con asesoría especializada; un procesador de pagos o un servicio de facturación puede absorber parte de ellas, con su propio costo y dependencia.

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

Toma una suscripción que tengas (streaming, nube, un servicio de software) y reconstruye su máquina de estados: qué ocurre si cancelas hoy, si el pago falla, si cambias de plan a mitad de ciclo. Anota lo que no pudiste responder sin probar. Eso es lo que el producto debería haber puesto por escrito.

## Ejemplo

Ejemplo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) (sección «Ejemplo mínimo»):

La máquina de estados con transiciones explícitas y el ciclo anclado:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La máquina de estados no decide los impuestos aplicables (que dependen de la jurisdicción del cliente y del producto), ni la regulación sobre cobros recurrentes y avisos previos, ni el reconocimiento contable del ingreso en planes anuales, ni la facturación electrónica que algunos países exigen. ([SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md))

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
