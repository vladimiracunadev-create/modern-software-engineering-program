# Interruptor general

[↑ Glosario](../../README.md) · [← Interruptor del experimento](./interruptor-del-experimento.md) · [Intersección de capacidades →](./interseccion-de-capacidades.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Orden independiente de la herramienta que detiene todos los experimentos.

Definición de trabajo de [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md).

## Por qué importa

La clase donde se define, [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), existe con este propósito: la clase existe para que establezcas los **límites** de la práctica: cuánto daño puede pagar el presupuesto de error, quién carga con él, qué privilegios se conceden a la herramienta que inyecta, cuándo un experimento no debe hacerse y qué no puede demostrar la ingeniería del caos.

## Cómo funciona

Según [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md):

La herramienta de inyección es, por definición, una puerta con permiso para alterar componentes. AWS lo dice sin eufemismos: realiza acciones reales sobre recursos reales, y por eso recomienda planificar y ensayar antes en preproducción. La documentación de Chaos Mesh incluye una página sobre por qué su demonio corre con privilegios elevados (necesita acceso al nodo para alterar la red, los ficheros o el reloj de un contenedor) y otra sobre la gestión de permisos de usuario. De ahí una política mínima:

Según [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe la política de su programa. Presupuesto: los experimentos nunca consumen más de 10 % del presupuesto mensual y se omiten si queda menos de la mitad. Equidad: selección por petición en producción; por cliente solo con aviso previo y rotación, excluyendo a las instituciones en semana de evaluación. Permisos: la herramienta solo actúa sobre el espacio de nombres de la API de entregas, aprueba el líder y ejecuta la guardia, cualquier persona del equipo puede activar el interruptor general, y hay credenciales separadas para preproducción y producción. Calendario: martes a jueves, de 10:00 a 16:00, fuera de cierres de plazo. Registro: cada experimento deja hipótesis, radio, resultado y huella, y la compuerta se archiva con él.

## Ejemplo

Ejemplo de [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético y no como medición, que el equipo escribe la política de su programa. Presupuesto: los experimentos nunca consumen más de 10 % del presupuesto mensual y se omiten si queda menos de la mitad. Equidad: selección por petición en producción; por cliente solo con aviso previo y rotación, excluyendo a las instituciones en semana de evaluación. Permisos: la herramienta solo actúa sobre el espacio de nombres de la API de entregas, aprueba el líder y ejecuta la guardia, cualquier persona del equipo puede activar el interruptor general, y hay credenciales separadas para preproducción y producción.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md)) son:

- **El presupuesto se agota por experimentos** — causa: calendario fijo sin compuerta. Corrección: compuerta con reserva para incidentes.
- **Una institución sufre varias veces** — causa: selección por cliente sin regla de rotación. Corrección: seleccionar por petición o rotar con regla visible.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron dos experimentos con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se dañó ninguna petición real; los incidentes de 1,2 por mes, la duración lognormal, el costo proporcional al radio, los 40 clientes con cuota 1/k y las políticas son construcciones del autor, y la clase no sustituye una evaluación ética, legal ni de seguridad de tu organización.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Compuerta de presupuesto](../c/compuerta-de-presupuesto.md), [Costo de un experimento](../c/costo-de-un-experimento.md), [Privilegio mínimo](../p/privilegio-minimo.md), [Selección por cliente](../s/seleccion-por-cliente.md), [Selección por petición](../s/seleccion-por-peticion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

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

[↑ Glosario](../../README.md) · [← Interruptor del experimento](./interruptor-del-experimento.md) · [Intersección de capacidades →](./interseccion-de-capacidades.md)
