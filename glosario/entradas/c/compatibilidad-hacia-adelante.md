# Compatibilidad hacia adelante

[↑ Glosario](../../README.md) · [← Compatibilidad entre versiones](./compatibilidad-entre-versiones.md) · [Compatibilidad hacia atrás →](./compatibilidad-hacia-atras.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un cambio de contrato es **compatible hacia adelante** si un lector viejo entiende los datos escritos con el contrato nuevo. Es el sentido de [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), repetido en [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (un lector con el esquema viejo lee datos escritos con el nuevo) y [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md). Es la dirección opuesta a la compatibilidad hacia atrás, en la que el lector nuevo entiende datos viejos.

## Por qué importa

Cambia el orden en que se puede desplegar. Según [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), una API que se actualiza primero en el servidor necesita compatibilidad hacia adelante para los clientes que aún no se actualizaron: el servidor ya habla el contrato nuevo y los clientes viejos siguen leyendo. Sin ella, cada cambio exige actualizar a todos a la vez, algo imposible cuando hay aplicaciones móviles instaladas o consumidores de otros equipos.

## Cómo funciona

La compatibilidad se evalúa por dirección y por tipo de cambio. [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) ofrece el criterio: muchos cambios son compatibles en una sola dirección. Agregar un campo requerido rompe a quien lee datos viejos con el esquema nuevo (falla hacia atrás); quitarlo rompe a quien espera encontrarlo.

Hacia adelante, el lector viejo debe sobrevivir a lo que no conoce: campos nuevos, valores nuevos de una enumeración. Eso solo ocurre si el contrato exige a los consumidores **tolerar lo desconocido**. Un cliente estricto, que falla ante un campo o valor inesperado, convierte un cambio «que solo agrega» en una ruptura. Por eso [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) pide documentar la tolerancia y probar con un valor nuevo. Para gobernarlo, la política de la plataforma distingue cambios que agregan campos opcionales o valores de enumeración (se anuncian, sin versión mayor) de renombrados, campos requeridos nuevos y eliminaciones (versión mayor, aviso con `Deprecation` y `Sunset` y ventana mínima de 180 días), y un comprobador en integración continua compara esquemas.

## Ejemplo

En la API de entregas de [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), agregar un campo opcional `comentario` a la respuesta es compatible hacia adelante: un cliente viejo lo ignora. Agregar un valor nuevo `en_revision` a la enumeración de estados solo lo es si los clientes tratan un estado desconocido de forma segura. Si un cliente viejo lanza una excepción ante el valor, el cambio «solo agrega» y aun así rompe.

## Errores y confusiones comunes

- **«Solo agrega, no puede romper».** Rompe a clientes estrictos con lo desconocido; corrección de [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md): exigir tolerancia y probar con un valor nuevo.
- **Confundir las dos direcciones.** Hacia atrás: el lector nuevo, datos viejos; hacia adelante: el lector viejo, datos nuevos.
- **Subir el número de versión y creer que basta.** Se versionó por intención sin comprobar compatibilidad; corrección: comparar esquemas en integración continua.
- **Suponer que un esquema es compatible en ambas direcciones.** Muchos cambios lo son en una sola.

## Límites y cuándo no aplica

Exige que los lectores viejos se escriban con tolerancia desde el principio: no se puede obtener retroactivamente de un cliente ya desplegado y estricto. Donde el almacén se lee con código nuevo y datos antiguos, la dirección que importa es hacia atrás. Y para rupturas inevitables la solución es versionar, avisar y retirar con ventana, no forzar la compatibilidad.

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
