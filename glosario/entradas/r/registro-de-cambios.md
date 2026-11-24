# Registro de cambios

[↑ Glosario](../../README.md) · [← Registro de auditoría](./registro-de-auditoria.md) · [Registro de cambios archivado →](./registro-de-cambios-archivado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

El **registro de cambios** (*changelog*) es el documento para humanos que describe qué cambió en cada versión y qué debe hacer el cliente ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md)). [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) lo usa en el contexto de datos como el historial anunciado de cambios de significado y de esquema. No es un volcado del historial de commits.

## Por qué importa

Quien consume una biblioteca, una API o un conjunto de datos decide si actualizar según lo que este documento le diga. Si es vago u omite una ruptura, el cliente se entera cuando algo falla en producción. La decisión que cambia es quién es el lector: se escribe pensando en quien debe decidir y actuar, no en quien hizo el cambio.

## Cómo funciona

[SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) fija el formato. El registro agrupa los cambios **por versión** y **por tipo**: añadido, cambiado, obsoleto, eliminado, corregido, seguridad. Cada versión lleva fecha y, para lo incompatible, una **guía de migración**. Una entrada útil responde tres preguntas: **qué cambió desde el punto de vista del cliente, a quién afecta y qué debe hacer**.

Un registro que dice «mejoras de rendimiento y correcciones» incumple su función: no dice a quién afecta ni qué hacer. Generarlo a partir de mensajes de commit con una convención ayuda a no olvidar cambios, pero la redacción, la clasificación y la advertencia siguen necesitando criterio humano: un commit describe lo que hizo el autor, no lo que el cliente nota.

Va de la mano del versionado semántico: el número de versión indica el tipo de cambio y el registro explica su contenido. La obsolescencia anunciada («este campo se eliminará en la versión X») permite que el cliente se prepare, y el error típico (clientes que no se enteran de una ruptura) se corrige con formato fijo, guía de migración y obsolescencia anunciada. En datos ([SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)), el equivalente es el aviso de cambios de significado y esquema para los consumidores.

## Ejemplo

Una entrada: «**Cambiado**: el campo `nota` pasa de entero a decimal (afecta a quienes lo leen como entero; usar `round()` o actualizar el tipo antes de la 2.0). **Obsoleto**: `calificacion_vieja`, se eliminará en 3.0». Responde qué cambió, a quién afecta y qué debe hacerse. Formato de [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md).

## Errores y confusiones comunes

- **Los clientes no se enteran de una ruptura**: registro genérico o sin aviso previo; se corrige con formato fijo, guía de migración y obsolescencia anunciada.
- **Pegar la lista de commits**: no es un registro de cambios.
- **Entradas escritas desde el punto de vista del autor** («refactor del módulo X»).
- **Omitir los cambios de seguridad** o los cambios de significado sin cambio de firma.

## Límites y cuándo no aplica

Según [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), para una aplicación sin consumidores externos el número de versión puede ser una fecha o un contador; lo importante es que sea monótono y que el registro sea veraz. Un registro solo es útil si es veraz y se mantiene al día: uno desactualizado es peor que ninguno. No sustituye la documentación del uso ni la comunicación directa con consumidores críticos.

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
