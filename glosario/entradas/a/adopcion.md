# Adopción

[↑ Glosario](../../README.md) · [← Adapter](./adapter.md) · [ADR →](./adr.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

La **adopción** es la parte de una población objetivo declarada que comienza a usar el servicio en una ventana de tiempo ([SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)). Es una fracción: un numerador (quienes empezaron a usarlo) sobre un denominador (la población que podía hacerlo). [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) usa el término en otro sentido cercano, de despliegue: la fracción de la base instalada que ya tiene una versión determinada en un momento dado.

## Por qué importa

Una cifra de adopción sin población objetivo es un porcentaje sin referente: «60 %» puede significar casi cualquier cosa. Cambia la decisión de qué se informa y cómo se compara: dos paneles pueden dar cifras distintas para el mismo producto simplemente porque eligieron denominadores distintos. En el sentido de despliegue, cambia la planificación: cuánto tardará una corrección urgente en llegar a la mayoría depende de cómo se adopta cada versión.

## Cómo funciona

Su punto delicado es el denominador. [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) plantea la pregunta: ¿todos los centros con cuenta, los que activaron, los que firmaron? Cada elección cambia el valor, y por eso la guía del Gobierno británico sobre adopción digital exige declarar la población para que la cifra tenga referente. También hay que fijar el **evento** que cuenta como «empezar a usar» (crear la cuenta no es lo mismo que lograr una entrega aceptada) y la **ventana** (los primeros 14 días, por ejemplo).

El contrato de la plataforma de entregas lo materializa en un archivo de métricas que define cada una con población, evento, ventana y filtros: adopción es «centros con al menos una entrega aceptada en los primeros 14 días, sobre centros con cuenta activada». Y ninguna cifra se publica sin su n, sin la edad mínima de la cohorte y sin su intervalo.

En el sentido de despliegue ([SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)), la adopción de una versión sigue una curva que depende del **canal**: una actualización automática llega a casi todos en días; una que exige acción de la persona, en semanas o nunca. Medirla por canal es lo que permite saber cuánto tarda una corrección urgente en cubrir a la mayoría.

## Ejemplo

La plataforma tiene 100 centros con cuenta, de los cuales 40 activaron la cuenta y 18 lograron una entrega aceptada en 14 días. Con denominador «cuentas» la adopción es 18 %; con «activaron» es 45 %. Ambas son legítimas, pero no comparables. Si la base crece a 200 centros por una campaña y los nuevos aún no activan, la adopción «baja» sin que nadie haya dejado de usar el producto: cambió el denominador. (Cifras ilustrativas del mecanismo de [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).)

## Errores y confusiones comunes

- **La adopción baja al crecer la base**: el denominador cambió; corrección: fijar y declarar la población objetivo.
- **Corrección urgente que tarda semanas en llegar a la mayoría**: se supuso un canal rápido; corrección: medir la adopción por canal y planear en consecuencia ([SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md)).
- **Confundir adopción con retención**: la primera mide quién empieza; la segunda, quién sigue.
- **Informar sin n ni intervalo.**

## Límites y cuándo no aplica

Con poblaciones muy pequeñas la fracción tiene mucha incertidumbre y el intervalo importa más que el porcentaje. La adopción mide inicio, no valor: un producto muy adoptado puede no servir. Y en productos obligatorios (de uso impuesto por la organización) la adopción es poco informativa; interesa más la tarea útil.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Servicio](../s/servicio.md), [Ventana](../v/ventana.md), [Versión](../v/version.md), [Canal de distribución](../c/canal-de-distribucion.md), [Censura](../c/censura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-259 — Actualizaciones, tiendas y distribución empresarial](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (27 clases más lo mencionan; las que más):

[SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Slack](../../../casos/exito/slack.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring digital take-up](https://www.gov.uk/service-manual/measuring-success/measuring-digital-take-up) — adopción sobre una población declarada; autoridad: Government Digital Service.
- [Google Research: HEART framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — marco de métricas de experiencia de usuario (felicidad, compromiso, adopción, retención, éxito en la tarea); autoridad: Google Research.
- [GOV.UK Service Manual: Measuring completion rate](https://www.gov.uk/service-manual/measuring-success/measuring-completion-rate) — finalización con numerador y denominador explícitos; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — qué medir y para qué decisión; autoridad: Government Digital Service.
- [NIST/SEMATECH e-Handbook of Statistical Methods: Proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) — intervalos de confianza para proporciones; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Adapter](./adapter.md) · [ADR →](./adr.md)
