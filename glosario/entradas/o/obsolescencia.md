# Obsolescencia

[↑ Glosario](../../README.md) · [← Observer](./observer.md) · [Ocurrió antes de →](./ocurrio-antes-de.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **obsolescencia** se usa en el programa con dos significados relacionados:

- **Deprecación** ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), *deprecation*): el aviso de que una funcionalidad se retirará, con alternativa y plazo.
- **Obsolescencia general** ([SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md)): pérdida de utilidad de un software por cambios técnicos u organizativos.

El primero es una acción deliberada del mantenedor; el segundo es un estado que se acumula si nadie decide.

## Por qué importa

Una ruptura anunciada es una transición; una ruptura sorpresa es un incidente ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md)). Planificar la obsolescencia evita acumular legado que nadie arregla y, a la vez, evita romper a quienes dependen del producto. [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md) observa que mantener todo indefinidamente tampoco es sostenible: aumenta costo, exposición y carga cognitiva.

## Cómo funciona

**Como política** ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md)): una funcionalidad se marca como pendiente de retiro con:

- un **aviso visible en tiempo de ejecución**;
- una **versión en la que se avisa** y otra **en la que se retira**;
- la **alternativa recomendada**;
- una **ventana mínima** publicada (por ejemplo, al menos dos versiones menores o seis meses antes de retirar).

Además hay que decidir cuánto tiempo se mantienen las versiones antiguas con correcciones de seguridad: sin fecha de fin de soporte, el ecosistema acumula versiones que nadie arregla.

**Como proceso** ([SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md)): la sostenibilidad técnica considera que el software pueda entenderse, adaptarse y retirarse. Dependencias sin mantenimiento, formatos cerrados y conocimiento concentrado crean obsolescencia. Las políticas de versión, migración y retiro equilibran continuidad con reducción de legado.

## Ejemplo

Ilustración en Python de un aviso de deprecación visible:

```python
import warnings
def f_vieja():
    warnings.warn("f_vieja se retira en 3.0; use f_nueva", DeprecationWarning, stacklevel=2)
```

Acompañada de una guía de migración y una entrada en el registro de cambios con formato fijo.

## Errores y confusiones comunes

- **Los clientes no se enteran de una ruptura.** Causa: registro de cambios genérico o sin aviso previo; corrección: formato fijo, guía de migración y obsolescencia anunciada ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md)).
- **Retirar sin alternativa.** El aviso sin camino de migración transfiere el problema.
- **Confundir obsolescencia con edad.** Un componente antiguo y estable no es obsoleto; uno sin mantenimiento sí puede serlo.

## Límites y cuándo no aplica

Una ventana de «dos versiones o seis meses» es un ejemplo de política razonable, no una norma universal. En software interno con pocos consumidores, un aviso corto y una conversación bastan. Y la deprecación no sustituye al versionado semántico: cuando se retira, el cambio incompatible sigue requiriendo señalarse en la versión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plazo](../p/plazo.md), [API pública](../a/api-publica.md), [Cambio incompatible](../c/cambio-incompatible.md), [Efecto sistémico](../e/efecto-sistemico.md), [Impacto directo](../i/impacto-directo.md), [Impacto habilitado](../i/impacto-habilitado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-009 — Sostenibilidad, inclusión y responsabilidad social](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/lang/es/) — significado de los componentes de la versión; autoridad: especificación de Tom Preston-Werner.
- [Keep a Changelog 1.1.0](https://keepachangelog.com/es-ES/1.1.0/) — registro de cambios para humanos; autoridad: proyecto Keep a Changelog.
- [PEP 440](https://peps.python.org/pep-0440/) — versiones en Python; autoridad: Python Enhancement Proposals.
- [PEP 387](https://peps.python.org/pep-0387/) — política de compatibilidad hacia atrás de Python; autoridad: Python Enhancement Proposals.
- [Hyrum's Law](https://www.hyrumslaw.com/) — dependencia de comportamientos no documentados; autoridad: autor de la formulación.

---

[↑ Glosario](../../README.md) · [← Observer](./observer.md) · [Ocurrió antes de →](./ocurrio-antes-de.md)
