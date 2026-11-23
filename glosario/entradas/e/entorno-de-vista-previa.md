# Entorno de vista previa

[↑ Glosario](../../README.md) · [← Entorno aislado](./entorno-aislado.md) · [Entorno virtual →](./entorno-virtual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Instancia temporal y completa de la aplicación creada para un cambio propuesto.

Definición de trabajo de [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

## Por qué importa

En [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), el tema «Entornos de vista previa» importa porque dan retroalimentación temprana y obligan a que el sistema se pueda crear y destruir con código.

## Cómo funciona

Según [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), en la sección «Entornos de vista previa»:

Un **entorno de vista previa** (preview) es una instancia completa y temporal de la aplicación creada para un cambio propuesto, con una dirección propia donde revisar el resultado antes de integrarlo. Convierte la revisión en algo que se prueba y no solo se lee, y exige que el sistema se pueda levantar desde código: infraestructura declarada, configuración por entorno y datos iniciales. Su ciclo de vida tiene cuatro momentos: se **crea** al abrir o actualizar la solicitud, se **usa** durante la revisión, se **renueva** cuando hay actividad y se **destruye** al cerrarse la solicitud o al vencer su vida. Un generador de aplicaciones a partir de las solicitudes abiertas (como el generador por solicitud de integración de algunas herramientas de GitOps) automatiza la creación y la destrucción.

## Ejemplo

Ejemplo de [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas fija la política de sus entornos de vista previa. Los datos son sintéticos, generados desde un esquema con las distribuciones de producción y con casos raros añadidos a mano (nombres con tilde, archivos vacíos, entregas fuera de plazo); no hay datos reales en ningún entorno.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md)) son:

- **Una persona es identificable en un entorno de pruebas** — causa: cuasi-identificadores sin generalizar. Corrección: medir la unicidad; generalizar y suprimir grupos pequeños.
- **Las pruebas de integridad fallan con datos enmascarados** — causa: sustitución aleatoria por tabla. Corrección: sustitución determinista con clave protegida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **entorno de vista previa** (preview) es una instancia completa y temporal de la aplicación creada para un cambio propuesto, con una dirección propia donde revisar el resultado antes de integrarlo. ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md))
- **un entorno de vista previa con datos sin nombre que identifican a personas por vinculación**. ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instancia](../i/instancia.md), [Cuasi-identificador](../c/cuasi-identificador.md), [Enmascarado determinista](./enmascarado-determinista.md), [K-anonimato](../k/k-anonimato.md), [Reidentificación](../r/reidentificacion.md), [Vigencia de la caché](../v/vigencia-de-la-cache.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Entornos de vista previa».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-188: de-identificación de conjuntos de datos](https://csrc.nist.gov/pubs/sp/800/188/final) — técnicas y riesgos de reidentificación; autoridad: NIST.
- [Sweeney, «k-anonymity: a model for protecting privacy»](https://doi.org/10.1142/S0218488502001648) — modelo de k-anonimato (International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 2002); autoridad: artículo con DOI verificado en Crossref.
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — definición de seudonimización; autoridad: Unión Europea, EUR-Lex.
- [GitHub: despliegues y entornos](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — entornos con protecciones y secretos propios; autoridad: documentación de GitHub.
- [Argo CD: ApplicationSet](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/) — generación de aplicaciones desde plantillas; autoridad: documentación de Argo CD.

---

[↑ Glosario](../../README.md) · [← Entorno aislado](./entorno-aislado.md) · [Entorno virtual →](./entorno-virtual.md)
