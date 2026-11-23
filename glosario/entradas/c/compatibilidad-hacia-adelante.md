# Compatibilidad hacia adelante

[↑ Glosario](../../README.md) · [← Compatibilidad entre versiones](./compatibilidad-entre-versiones.md) · [Compatibilidad hacia atrás →](./compatibilidad-hacia-atras.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un lector viejo entiende datos escritos con el contrato nuevo.

Definición de trabajo de [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md): Propiedad por la cual un lector con el esquema viejo lee datos escritos con el nuevo.
- En [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md): Un lector viejo lee datos nuevos.

## Por qué importa

La clase donde se define, [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), existe con este propósito: la clase existe para cambiar un contrato sin romper a quien ya lo usa: saber qué cambios son compatibles en qué dirección, cómo el tipo de consumidor cambia la respuesta y cuánto tarda en retirarse una versión que nadie quiere mantener.

## Cómo funciona

Según [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md):

Un cambio es **compatible hacia atrás** si el lector nuevo entiende los datos viejos, y **compatible hacia adelante** si el lector viejo entiende los datos nuevos. Una API que se actualiza primero en el servidor necesita compatibilidad hacia adelante para los clientes que aún no se actualizaron; un almacén de datos que se lee con el código nuevo necesita compatibilidad hacia atrás. Muchos cambios son compatibles en una sola dirección: agregar un campo requerido rompe a quien lee datos viejos con el esquema nuevo; quitarlo rompe a quien espera encontrarlo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md):

En la plataforma, el contrato de la API de entregas tiene una política escrita: los cambios que agregan campos opcionales o valores de enum se anuncian en el registro de cambios y no cambian la versión mayor; los renombrados, los campos requeridos nuevos y las eliminaciones exigen versión mayor, aviso con `Deprecation` y `Sunset` y una ventana mínima de 180 días. Un comprobador de integración continua compara el esquema nuevo con el anterior y falla si un cambio de la lista de rupturas no incrementa la versión mayor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)) son:

- **Un cambio «solo agrega» y rompe a un cliente** — causa: el cliente es estricto con campos o valores desconocidos. Corrección: documentar que los consumidores deben tolerar lo desconocido y probar con un valor nuevo.
- **El número de versión sube y los clientes se rompen igual** — causa: se versionó por intención y no se comprobó la compatibilidad. Corrección: comparar esquemas en integración continua y exigir versión mayor para las rupturas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una API que se actualiza primero en el servidor necesita compatibilidad hacia adelante para los clientes que aún no se actualizaron; un almacén de datos que se lee con el código nuevo necesita compatibilidad hacia atrás. ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](./contrato.md), [Esquema](../e/esquema.md), [Propiedad](../p/propiedad.md), [Cambio semántico](./cambio-semantico.md), [Compatibilidad hacia atrás](./compatibilidad-hacia-atras.md), [Compatibilidad hacia atrás y hacia adelante](./compatibilidad-hacia-atras-y-hacia-adelante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/) — convención de versiones mayor, menor y parche; autoridad: especificación de SemVer.
- [Google API Design Guide: Compatibility](https://cloud.google.com/apis/design/compatibility) — cambios compatibles e incompatibles de una API; autoridad: Google Cloud.
- [Fowler: Tolerant Reader](https://martinfowler.com/bliki/TolerantReader.html) — lector que ignora lo desconocido; autoridad: autor del patrón.
- [RFC 793: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc793) — origen de la recomendación de ser liberal en lo que se acepta; autoridad: IETF.
- [RFC 8594: The Sunset HTTP Header Field](https://www.rfc-editor.org/rfc/rfc8594) — aviso de retirada de un recurso; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Compatibilidad entre versiones](./compatibilidad-entre-versiones.md) · [Compatibilidad hacia atrás →](./compatibilidad-hacia-atras.md)
