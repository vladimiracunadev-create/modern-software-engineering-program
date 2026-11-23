# Vigencia

[↑ Glosario](../../README.md) · [← Vértices, aristas y dirección](./vertices-aristas-y-direccion.md) · [Vigencia de la caché →](./vigencia-de-la-cache.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Estado actual, retirado o sustituido.

Definición de trabajo de [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md).

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md):

Escribe a propósito una afirmación apoyada en una referencia desactualizada, por ejemplo «según RFC 7231, el método X es seguro para reintento». **Síntoma:** el enlace funciona y el pasaje parece respaldar la afirmación, pero el encabezado del RFC indica que fue obsoleto. **Traza:** busca la relación «obsoleto por» en el propio documento, abre el sustituto (RFC 9110), localiza el pasaje equivalente y compara qué cambió. **Corrección:** actualiza la cita con identificador, edición y fecha, y reescribe la afirmación si el pasaje cambió. Registra además qué conclusiones de tu documento dependían de la edición antigua. No borres la referencia histórica si describe un sistema que todavía se ajusta a ella: añade el contexto de vigencia.

## Ejemplo

Caso medido en la sección «Edición, vigencia y cadena de sustitución» de [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md):

ISO/IEC 25010:2011 combinaba modelos de producto y calidad en uso. La edición de 2023 sitúa calidad del producto en ISO/IEC 25010 y el modelo de calidad en uso en ISO/IEC 25019. Por eso escribir solo “ISO 25010” puede ocultar qué edición y modelo se usa. De manera semejante, un RFC puede ser actualizado parcialmente por otros; el encabezado y las relaciones forman parte de la lectura.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **“según ISO” sin edición** — causa: se omitieron vigencia y alcance. Corrección: añade identificador, año, modelo usado y límite. ([SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No borres la referencia histórica si describe un sistema que todavía se ajusta a ella: añade el contexto de vigencia. ([SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estado actual](../e/estado-actual.md), [Estado](../e/estado.md), [Cita de proximidad](../c/cita-de-proximidad.md), [Edición](../e/edicion.md), [Especificación](../e/especificacion.md), [Informativo](../i/informativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), [SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Vértices, aristas y dirección](./vertices-aristas-y-direccion.md) · [Vigencia de la caché →](./vigencia-de-la-cache.md)
