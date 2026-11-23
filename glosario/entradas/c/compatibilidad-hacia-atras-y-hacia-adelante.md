# Compatibilidad hacia atrás y hacia adelante

[↑ Glosario](../../README.md) · [← Compatibilidad hacia atrás](./compatibilidad-hacia-atras.md) · [Compatibilidad y sintaxis →](./compatibilidad-y-sintaxis.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Capacidad de un lector nuevo de leer datos viejos y de un lector viejo de leer datos nuevos.

Definición de trabajo de [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

## Por qué importa

En [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), el tema «Compatibilidad hacia atrás y hacia adelante» importa porque un cambio es compatible en una dirección determinada; confundirlas rompe a alguien.

## Cómo funciona

Según [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), en la sección «Compatibilidad hacia atrás y hacia adelante»:

Un cambio es **compatible hacia atrás** si el lector nuevo entiende los datos viejos, y **compatible hacia adelante** si el lector viejo entiende los datos nuevos. Una API que se actualiza primero en el servidor necesita compatibilidad hacia adelante para los clientes que aún no se actualizaron; un almacén de datos que se lee con el código nuevo necesita compatibilidad hacia atrás. Muchos cambios son compatibles en una sola dirección: agregar un campo requerido rompe a quien lee datos viejos con el esquema nuevo; quitarlo rompe a quien espera encontrarlo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md):

En la plataforma, el contrato de la API de entregas tiene una política escrita: los cambios que agregan campos opcionales o valores de enum se anuncian en el registro de cambios y no cambian la versión mayor; los renombrados, los campos requeridos nuevos y las eliminaciones exigen versión mayor, aviso con `Deprecation` y `Sunset` y una ventana mínima de 180 días. Un comprobador de integración continua compara el esquema nuevo con el anterior y falla si un cambio de la lista de rupturas no incrementa la versión mayor.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)) son:

- **Un cambio «solo agrega» y rompe a un cliente** — causa: el cliente es estricto con campos o valores desconocidos. Corrección: documentar que los consumidores deben tolerar lo desconocido y probar con un valor nuevo.
- **El número de versión sube y los clientes se rompen igual** — causa: se versionó por intención y no se comprobó la compatibilidad. Corrección: comparar esquemas en integración continua y exigir versión mayor para las rupturas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los lectores son dos modelos extremos, la mezcla de cambios y la migración de consumidores son supuestos del autor y no se midió ningún cliente real. La siguiente clase pregunta cómo mantener la especificación como fuente de verdad frente al código.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](./capacidad.md), [Bandeja de salida](../b/bandeja-de-salida.md), [Compatibilidad hacia adelante](./compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](./compatibilidad-hacia-atras.md), [Doble escritura](../d/doble-escritura.md), [Lector estricto](../l/lector-estricto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

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

[↑ Glosario](../../README.md) · [← Compatibilidad hacia atrás](./compatibilidad-hacia-atras.md) · [Compatibilidad y sintaxis →](./compatibilidad-y-sintaxis.md)
