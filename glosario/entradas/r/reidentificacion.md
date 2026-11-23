# Reidentificación

[↑ Glosario](../../README.md) · [← Regresión de resiliencia](./regresion-de-resiliencia.md) · [Reintentos →](./reintentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Recuperación de la identidad de una persona a partir de datos que no la nombran, combinando atributos como lugares frecuentes.

Definición de trabajo de [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md).

## Por qué importa

En [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), el tema «Reidentificación» importa porque quitar el nombre no anonimiza; los cuasi-identificadores sí identifican.

## Cómo funciona

Según [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md):

Un entorno sin datos prueba poco; un entorno con datos de producción traslada el riesgo. Hay tres opciones. Los **datos sintéticos** se generan desde cero con las distribuciones y relaciones que importan: no contienen a nadie, pero pueden no reproducir los casos raros que rompen el sistema. Un **subconjunto enmascarado** de producción conserva la forma real a costa de transformarlo; tiene un riesgo residual de reidentificación. Una **copia completa de producción** es la más fiel y la más peligrosa, y debería tratarse con las mismas protecciones que producción, lo que contradice la razón de tener entornos baratos y abiertos. La decisión por defecto razonable es sintéticos, con un subconjunto enmascarado solo cuando hay una necesidad demostrada y un propietario de la decisión.

Según [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md):

No hay valor universal. Valores de 5 a 10 son frecuentes como mínimo; el adecuado depende del riesgo, de los datos auxiliares disponibles y del daño de una reidentificación. Más k significa más generalización y menos utilidad.

## Ejemplo

Ejemplo de [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) (sección «Preguntas frecuentes»):

No hay valor universal. Valores de 5 a 10 son frecuentes como mínimo; el adecuado depende del riesgo, de los datos auxiliares disponibles y del daño de una reidentificación. Más k significa más generalización y menos utilidad.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md)) son:

- **Una persona es identificable en un entorno de pruebas** — causa: cuasi-identificadores sin generalizar. Corrección: medir la unicidad; generalizar y suprimir grupos pequeños.
- **Las pruebas de integridad fallan con datos enmascarados** — causa: sustitución aleatoria por tabla. Corrección: sustitución determinista con clave protegida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Valores de 5 a 10 son frecuentes como mínimo; el adecuado depende del riesgo, de los datos auxiliares disponibles y del daño de una reidentificación. ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Recuperación](./recuperacion.md), [Capacidad](../c/capacidad.md), [Cuasi-identificador](../c/cuasi-identificador.md), [Enmascarado determinista](../e/enmascarado-determinista.md), [Entorno de vista previa](../e/entorno-de-vista-previa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-257 — Permisos, sensores y capacidades del dispositivo](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-188: de-identificación de conjuntos de datos](https://csrc.nist.gov/pubs/sp/800/188/final) — técnicas y riesgos de reidentificación; autoridad: NIST.
- [Sweeney, «k-anonymity: a model for protecting privacy»](https://doi.org/10.1142/S0218488502001648) — modelo de k-anonimato (International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 2002); autoridad: artículo con DOI verificado en Crossref.
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — definición de seudonimización; autoridad: Unión Europea, EUR-Lex.
- [GitHub: despliegues y entornos](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — entornos con protecciones y secretos propios; autoridad: documentación de GitHub.
- [Argo CD: ApplicationSet](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/) — generación de aplicaciones desde plantillas; autoridad: documentación de Argo CD.

---

[↑ Glosario](../../README.md) · [← Regresión de resiliencia](./regresion-de-resiliencia.md) · [Reintentos →](./reintentos.md)
