# Lector estricto

[↑ Glosario](../../README.md) · [← Lead time](./lead-time.md) · [Lector tolerante →](./lector-tolerante.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Consumidor que rechaza los campos que no conoce.

Definición de trabajo de [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md).

## Por qué importa

La clase donde se define, [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), existe con este propósito: la clase existe para cambiar un contrato sin romper a quien ya lo usa: saber qué cambios son compatibles en qué dirección, cómo el tipo de consumidor cambia la respuesta y cuánto tarda en retirarse una versión que nadie quiere mantener.

## Cómo funciona

Según [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md):

Un lector **tolerante** lee los campos que necesita e ignora los campos que no conoce; un lector **estricto** rechaza lo que no reconoce (campos desconocidos). En el experimento de esta clase ninguno de los dos acepta valores de enum nuevos, un tercer eje de tolerancia que el consumidor debe decidir por separado. El mismo cambio produce resultados distintos: agregar un campo opcional es inocuo para el tolerante y rompe al estricto. Postel formuló la idea en el RFC 793 como «sé liberal en lo que aceptas de los demás»; el reverso es que la tolerancia puede esconder cambios de significado. Elegir es una decisión de diseño del consumidor, y el productor debe suponer que hay de los dos tipos.

## Ejemplo

Ejemplo de [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra que agregar un valor de enum rompe a un lector estricto. Antes de ejecutarlo, predice qué ocurre con cada lector.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)) son:

- **Un cambio «solo agrega» y rompe a un cliente** — causa: el cliente es estricto con campos o valores desconocidos. Corrección: documentar que los consumidores deben tolerar lo desconocido y probar con un valor nuevo.
- **El número de versión sube y los clientes se rompen igual** — causa: se versionó por intención y no se comprobó la compatibilidad. Corrección: comparar esquemas en integración continua y exigir versión mayor para las rupturas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un lector **tolerante** lee los campos que necesita e ignora los campos que no conoce; un lector **estricto** rechaza lo que no reconoce (campos desconocidos). ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Compatibilidad hacia atrás y hacia adelante](../c/compatibilidad-hacia-atras-y-hacia-adelante.md), [Lector tolerante](./lector-tolerante.md), [Ventana de deprecación](../v/ventana-de-deprecacion.md), [Versionado semántico](../v/versionado-semantico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

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

[↑ Glosario](../../README.md) · [← Lead time](./lead-time.md) · [Lector tolerante →](./lector-tolerante.md)
