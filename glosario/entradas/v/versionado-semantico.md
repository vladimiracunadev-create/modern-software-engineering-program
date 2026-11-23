# Versionado semántico

[↑ Glosario](../../README.md) · [← Versionado del protocolo](./versionado-del-protocolo.md) · [Vértices, aristas y dirección →](./vertices-aristas-y-direccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Convención de numeración que comunica la compatibilidad mediante MAYOR.MENOR.PARCHE.

Definición de trabajo de [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md).

## Por qué importa

En [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), el tema «Versionado semántico» importa porque un número comunica una intención; no verifica la compatibilidad.

En [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), el tema «Versionado semántico» importa porque es una promesa sobre compatibilidad.

## Cómo funciona

Según [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), en la sección «Versionado semántico»:

SemVer comunica la intención: un incremento mayor indica ruptura, uno menor indica funcionalidad compatible y uno de parche corrige defectos. Sirve como lenguaje común, y su límite es que nadie verifica que el número diga la verdad: una «versión menor» que cambia el significado de un campo rompe a los consumidores igualmente. Conviene acompañar el número con una comprobación automática de compatibilidad (comparar esquemas) y con un registro de cambios que explique qué cambió y a quién afecta.

## Ejemplo

Caso medido en la sección «Versionado semántico como promesa» de [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md):

El **versionado semántico** asigna significado a los tres números de una versión: el **mayor** sube cuando hay cambios incompatibles de la API pública, el **menor** cuando se añade funcionalidad compatible y el **parche** cuando se corrige un error sin cambiar la API. Es una promesa que quien publica hace a quien depende: «si actualizas dentro del mismo mayor, tu código seguirá funcionando». Su valor es que permite expresar rangos de dependencia (`>=1.4,<2`) y automatizar actualizaciones menores.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)) son:

- **Un cambio «solo agrega» y rompe a un cliente** — causa: el cliente es estricto con campos o valores desconocidos. Corrección: documentar que los consumidores deben tolerar lo desconocido y probar con un valor nuevo.
- **El número de versión sube y los clientes se rompen igual** — causa: se versionó por intención y no se comprobó la compatibilidad. Corrección: comparar esquemas en integración continua y exigir versión mayor para las rupturas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **versionado semántico** asigna significado a los tres números de una versión: el **mayor** sube cuando hay cambios incompatibles de la API pública, el **menor** cuando se añade funcionalidad compatible y el **parche** cuando se corrige un error sin cambiar la API. ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [API pública](../a/api-publica.md), [Cambio incompatible](../c/cambio-incompatible.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Compatibilidad hacia atrás y hacia adelante](../c/compatibilidad-hacia-atras-y-hacia-adelante.md), [Lector estricto](../l/lector-estricto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

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

[↑ Glosario](../../README.md) · [← Versionado del protocolo](./versionado-del-protocolo.md) · [Vértices, aristas y dirección →](./vertices-aristas-y-direccion.md)
