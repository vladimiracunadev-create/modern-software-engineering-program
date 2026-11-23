# Costo de un experimento

[↑ Glosario](../../README.md) · [← Costo de reversión](./costo-de-reversion.md) · [Costo del experimento →](./costo-del-experimento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Minutos equivalentes de caída total que consume del presupuesto de error.

Definición de trabajo de [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md).

## Por qué importa

La clase donde se define, [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), existe con este propósito: la clase existe para que establezcas los **límites** de la práctica: cuánto daño puede pagar el presupuesto de error, quién carga con él, qué privilegios se conceden a la herramienta que inyecta, cuándo un experimento no debe hacerse y qué no puede demostrar la ingeniería del caos.

## Cómo funciona

[SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas.

## Ejemplo

Ejemplo de [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el costo de un experimento y cuántos caben en un presupuesto. Antes de ejecutarlo, predice cuántos experimentos de 5 % de radio, 20 minutos y 60 % de daño caben en 43,2 minutos reservando la mitad para incidentes.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md)) son:

- **El presupuesto se agota por experimentos** — causa: calendario fijo sin compuerta. Corrección: compuerta con reserva para incidentes.
- **Una institución sufre varias veces** — causa: selección por cliente sin regla de rotación. Corrección: seleccionar por petición o rotar con regla visible.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron dos experimentos con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se dañó ninguna petición real; los incidentes de 1,2 por mes, la duración lognormal, el costo proporcional al radio, los 40 clientes con cuota 1/k y las políticas son construcciones del autor, y la clase no sustituye una evaluación ética, legal ni de seguridad de tu organización.

## Relación con otros conceptos

- **Prerrequisito:** [Presupuesto de error](../p/presupuesto-de-error.md).
- **Ver también:** [Presupuesto](../p/presupuesto.md), [Compuerta de presupuesto](./compuerta-de-presupuesto.md), [Interruptor general](../i/interruptor-general.md), [Privilegio mínimo](../p/privilegio-minimo.md), [Selección por cliente](../s/seleccion-por-cliente.md), [Selección por petición](../s/seleccion-por-peticion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

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

[↑ Glosario](../../README.md) · [← Costo de reversión](./costo-de-reversion.md) · [Costo del experimento →](./costo-del-experimento.md)
