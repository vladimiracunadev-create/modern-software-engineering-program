# Registro de cambios

[↑ Glosario](../../README.md) · [← Registro de auditoría](./registro-de-auditoria.md) · [Registro de cambios archivado →](./registro-de-cambios-archivado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Documento para humanos que describe qué cambió en cada versión y qué debe hacer el cliente.

Definición de trabajo de [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md): Historial anunciado de cambios de significado y de esquema.

## Por qué importa

En [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), el tema «Registro de cambios» importa porque es el canal por el que el cliente se entera.

## Cómo funciona

Según [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), en la sección «Registro de cambios»:

El **registro de cambios** (*changelog*) es el documento por el que el cliente decide si actualizar. Es para humanos, no un volcado del historial de commits: agrupa los cambios por versión y por tipo (añadido, cambiado, obsoleto, eliminado, corregido, seguridad), con la fecha y, para lo incompatible, una guía de migración. Generarlo a partir de mensajes de commit con una convención ayuda a no olvidar cambios, pero la redacción, la clasificación y la advertencia siguen necesitando criterio. Un registro de cambios que dice «mejoras de rendimiento y correcciones» incumple su función. Una entrada útil responde tres preguntas: qué cambió desde el punto de vista del cliente, a quién afecta y qué debe hacer.

## Ejemplo

Ejemplo de [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) (sección «Ejemplo profesional»):

El equipo escribe una política de versionado de la API de entregas: la API pública son los puntos finales documentados, sus parámetros, sus campos de respuesta, sus códigos de error y el orden de los listados cuando está especificado; el comportamiento no documentado no se promete. Cada solicitud de integración ejecuta el comparador de firmas y las pruebas de contrato, y quien revisa elige el nivel; si hay discrepancia, gana el mayor. Una funcionalidad deprecada emite un aviso en tiempo de ejecución desde la versión que la marca hasta la que la retira, con un mínimo de dos versiones menores y seis meses.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los clientes no se enteran de una ruptura** — causa: registro de cambios genérico o sin aviso previo. Corrección: formato fijo, guía de migración y obsolescencia anunciada. ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para una aplicación sin consumidores externos, el número puede ser una fecha o un contador; lo importante es que sea monótono y que el registro de cambios sea veraz. ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Esquema](../e/esquema.md), [Versión](../v/version.md), [API pública](../a/api-publica.md), [Cambio incompatible](../c/cambio-incompatible.md), [Cambio semántico](../c/cambio-semantico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Keep a Changelog 1.1.0](https://keepachangelog.com/es-ES/1.1.0/) — registro de cambios para humanos; autoridad: proyecto Keep a Changelog.
- [Semantic Versioning 2.0.0](https://semver.org/lang/es/) — significado de los componentes de la versión; autoridad: especificación de Tom Preston-Werner.
- [PEP 440](https://peps.python.org/pep-0440/) — versiones en Python; autoridad: Python Enhancement Proposals.
- [PEP 387](https://peps.python.org/pep-0387/) — política de compatibilidad hacia atrás de Python; autoridad: Python Enhancement Proposals.
- [Hyrum's Law](https://www.hyrumslaw.com/) — dependencia de comportamientos no documentados; autoridad: autor de la formulación.

---

[↑ Glosario](../../README.md) · [← Registro de auditoría](./registro-de-auditoria.md) · [Registro de cambios archivado →](./registro-de-cambios-archivado.md)
