# Compuerta de presupuesto

[↑ Glosario](../../README.md) · [← Compuerta de abandono](./compuerta-de-abandono.md) · [Cómputo de entrenamiento →](./computo-de-entrenamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Regla que omite un experimento si el presupuesto restante no cubre su costo con margen.

Definición de trabajo de [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md).

## Por qué importa

La clase donde se define, [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), existe con este propósito: la clase existe para que establezcas los **límites** de la práctica: cuánto daño puede pagar el presupuesto de error, quién carga con él, qué privilegios se conceden a la herramienta que inyecta, cuándo un experimento no debe hacerse y qué no puede demostrar la ingeniería del caos.

## Cómo funciona

Según [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md):

Reproduce el fallo clásico de la clase: **un calendario fijo de experimentos sin compuerta de presupuesto**. Aplica cuatro experimentos al mes con radio de 50 % durante 4 000 meses y compara con la compuerta.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe la política de su programa. Presupuesto: los experimentos nunca consumen más de 10 % del presupuesto mensual y se omiten si queda menos de la mitad. Equidad: selección por petición en producción; por cliente solo con aviso previo y rotación, excluyendo a las instituciones en semana de evaluación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md)) son:

- **El presupuesto se agota por experimentos** — causa: calendario fijo sin compuerta. Corrección: compuerta con reserva para incidentes.
- **Una institución sufre varias veces** — causa: selección por cliente sin regla de rotación. Corrección: seleccionar por petición o rotar con regla visible.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **un calendario fijo de experimentos sin compuerta de presupuesto**. ([SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](./costo.md), [Margen](../m/margen.md), [Presupuesto](../p/presupuesto.md), [Regla](../r/regla.md), [Costo de un experimento](./costo-de-un-experimento.md), [Interruptor general](../i/interruptor-general.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — responsabilidad de minimizar y contener el daño; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) — evitar el daño y mitigarlo; autoridad: Association for Computing Machinery.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error; autoridad: libro de ingeniería de confiabilidad de Google.
- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) — acciones reales sobre recursos reales; autoridad: documentación de Amazon Web Services.
- [Chaos Mesh](https://chaos-mesh.org/docs/) — privilegios del demonio y gestión de permisos; autoridad: documentación del proyecto Chaos Mesh.

---

[↑ Glosario](../../README.md) · [← Compuerta de abandono](./compuerta-de-abandono.md) · [Cómputo de entrenamiento →](./computo-de-entrenamiento.md)
