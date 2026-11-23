# Artefacto

[↑ Glosario](../../README.md) · [← Arrepentimiento](./arrepentimiento.md) · [Artefacto de verificación →](./artefacto-de-verificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Salida inmutable de un build, identificada por su contenido.

Definición de trabajo de [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md): Archivo producido por la compilación o el empaquetado que se entrega a los usuarios.

## Por qué importa

En [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), el tema «Artefacto y huella» importa porque identificar por contenido permite verificar.

## Cómo funciona

Según [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md):

Un **artefacto** es la salida inmutable de un build: un archivo, una imagen de contenedor, un paquete. Su **huella** (digest) es el resultado de aplicarle una función hash; dos artefactos con la misma huella son el mismo contenido, y un solo byte distinto produce otra huella. Esto permite un direccionamiento por contenido: pedirle al repositorio «dame lo que tiene esta huella» devuelve exactamente eso o nada. Un repositorio de artefactos añade a ese almacén un índice (nombre y versión que apuntan a una huella), metadatos y control de acceso, pero el contenido sigue identificado por su huella. Por eso un registro de contenedores permite referirse a una imagen por etiqueta (`api:1.4.0`) o por resumen (`api@sha256:…`), y solo la segunda es inmutable.

Según [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md):

El equipo define la canalización de la API de entregas. El build produce un artefacto y registra su huella; el repositorio acepta etiquetas de versión una sola vez. Integración y preproducción ejecutan sus pruebas contra esa huella y escriben un metadato por etapa (resultado, fecha, versión de las pruebas); la promoción a producción solo se permite si ambos metadatos existen. El despliegue recibe la huella y la configuración del entorno por separado. La política de retención conserva las cinco últimas versiones, todas las que estuvieron en producción en los últimos 90 días y las que tienen una atestación vigente; cada trimestre se ensaya un retroceso a la tercera versión anterior para comprobar que el artefacto y su cadena de verificación siguen disponibles.

## Ejemplo

Ejemplo de [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) (sección «Ejemplo profesional»):

El equipo define la canalización de la API de entregas. El build produce un artefacto y registra su huella; el repositorio acepta etiquetas de versión una sola vez. Integración y preproducción ejecutan sus pruebas contra esa huella y escriben un metadato por etapa (resultado, fecha, versión de las pruebas); la promoción a producción solo se permite si ambos metadatos existen. El despliegue recibe la huella y la configuración del entorno por separado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un artefacto de producción incluye una dirección de integración** — causa: configuración incrustada en el artefacto. Corrección: inyectar la configuración en el despliegue. ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md))
- **Nadie sabe qué pruebas pasó un artefacto** — causa: el estado vive en el nombre o en la cabeza de alguien. Corrección: metadatos asociados a la huella. ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md))
- **El artefacto conservado no se puede verificar** — causa: se borró su atestación o su clave pública. Corrección: conservar la cadena de verificación con el artefacto. ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su **huella** (digest) es el resultado de aplicarle una función hash; dos artefactos con la misma huella son el mismo contenido, y un solo byte distinto produce otra huella. ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md))
- Traslada el análisis a otro tipo de artefacto (un paquete de biblioteca publicado en un índice, una aplicación móvil enviada a una tienda): cambia el almacén y conserva el procedimiento de identificar por contenido, promover sin reconstruir, guardar el estado como metadatos y justificar la retención con la profundidad de los retrocesos. ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Empaquetado](../e/empaquetado.md), [Despliegue escalonado](../d/despliegue-escalonado.md), [Etiqueta](../e/etiqueta.md), [Firma digital](../f/firma-digital.md), [Huella](../h/huella.md), [Huella o digest](../h/huella-o-digest.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (412 clases más lo mencionan; las que más):

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «DeploymentPipeline»](https://martinfowler.com/bliki/DeploymentPipeline.html) — artefacto único que avanza por etapas; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — builds herméticos y promoción; autoridad: Google, libro de ingeniería de confiabilidad.
- [OCI Image Specification: descriptores](https://github.com/opencontainers/image-spec/blob/main/descriptor.md) — identificación por resumen; autoridad: Open Container Initiative.
- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec) — referencias por etiqueta y por resumen; autoridad: Open Container Initiative.
- [PyPI: ayuda](https://pypi.org/help/) — inmutabilidad de los nombres de archivo publicados; autoridad: Python Packaging Authority.

---

[↑ Glosario](../../README.md) · [← Arrepentimiento](./arrepentimiento.md) · [Artefacto de verificación →](./artefacto-de-verificacion.md)
