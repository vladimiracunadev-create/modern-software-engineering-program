# Entorno de vista previa

[↑ Glosario](../../README.md) · [← Entorno aislado](./entorno-aislado.md) · [Entorno virtual →](./entorno-virtual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Un **entorno de vista previa** (*preview environment*) es una instancia completa y temporal de la aplicación creada para un cambio propuesto, con una dirección propia donde revisar el resultado antes de integrarlo. Es la definición de [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

## Por qué importa

Convierte la revisión de algo que se *lee* en algo que se *prueba*. En lugar de imaginar el efecto de un diff, quien revisa abre la aplicación con ese cambio, la usa y comparte el enlace con producto o diseño. Cambia la decisión de cuándo se descubre un problema de integración: antes de fusionar, no después.

## Cómo funciona

[SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) le atribuye un requisito y un ciclo de vida.

**Requisito:** que el sistema se pueda levantar desde código. Eso significa infraestructura declarada, configuración por entorno y datos iniciales. Si levantar la aplicación exige pasos manuales, no hay vista previa automática posible.

**Ciclo de vida**, en cuatro momentos:

1. Se **crea** al abrir o actualizar la solicitud de integración.
2. Se **usa** durante la revisión.
3. Se **renueva** cuando hay actividad.
4. Se **destruye** al cerrarse la solicitud o al vencer su vida.

Un generador de aplicaciones a partir de las solicitudes abiertas (la clase menciona el generador por solicitud de integración de algunas herramientas de GitOps) automatiza la creación y la destrucción. La destrucción importa tanto como la creación: sin ella, cada solicitud deja infraestructura huérfana y costo.

La causa de su utilidad es que cada cambio recibe un aislamiento propio, de modo que dos solicitudes no se pisan una a otra como lo harían en un único entorno compartido de pruebas.

## Ejemplo

Se abre una solicitud que cambia la pantalla de entregas. La automatización levanta una instancia con su dirección propia, carga datos iniciales y publica el enlace en la solicitud. Quien revisa prueba el flujo; se actualiza la rama y la instancia se renueva; al fusionar o cerrar la solicitud, la instancia se destruye. Los datos iniciales son un asunto aparte: [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) advierte que un entorno de pruebas con datos que identifican a personas por vinculación es un riesgo, y por eso los datos se enmascaran.

## Errores y confusiones comunes

- **Una persona es identificable en un entorno de pruebas.** Cuasi-identificadores sin generalizar; corrección: medir la unicidad, generalizar y suprimir grupos pequeños.
- **Las pruebas de integridad fallan con datos enmascarados.** Sustitución aleatoria por tabla; corrección: sustitución determinista con clave protegida.
- **Confundirlo con el entorno de staging.** Staging es uno y compartido; la vista previa es uno por cambio y efímero.
- **Olvidar el apagado.** Sin destrucción automática, los entornos se acumulan.

## Límites y cuándo no aplica

Exige que el sistema sea reproducible desde código; en sistemas con dependencias que no se pueden replicar (un sistema externo único, hardware, grandes volúmenes de datos) la vista previa será parcial y conviene declarar qué simula. No prueba el rendimiento ni el comportamiento con carga real de producción. Y su costo debe acotarse con vida máxima y límite de instancias simultáneas.

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
