# Supuestos

[↑ Glosario](../../README.md) · [← Supuesto de vigilancia](./supuesto-de-vigilancia.md) · [Suscripción →](./suscripcion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Un **supuesto** es una creencia sobre personas, mercado, tecnología o negocio que debe ser cierta para que la idea funcione y que aún no ha sido verificada ([SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)). [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) lo usa en planificación: algo que damos por cierto para planificar y que puede comprobarse; si es falso, el plan estaba mal desde el principio. [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) lo usa en argumentos de seguridad: una condición que se da por cierta y que acota el argumento.

## Por qué importa

Toda idea descansa en creencias no verificadas; hacerlas explícitas es lo único que permite contrastarlas. Un supuesto oculto no se puede probar y falla por sorpresa. Cambia el modo de planificar: se pregunta qué tendría que ser cierto, y se decide qué comprobar primero.

## Cómo funciona

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) dice que un supuesto **no es un defecto**: es la parte de la idea que todavía es creencia. **El defecto es no nombrarlo.** Se encuentran preguntándose, para cada paso de la idea, qué tendría que ser cierto: que las personas tengan el problema, que lo reconozcan, que prefieran esta solución a las alternativas, que puedan usarla, que la institución la autorice. Unos son **observados** (hay 42 tickets al mes) y otros **esperados** (las docentes autorizarán guardar borradores).

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) los distingue del riesgo: un supuesto **no es un evento futuro sino una creencia presente**; si es falsa, el plan estaba mal desde el principio. Ejemplos: «las estudiantes usan navegadores actuales», «el rendimiento será de cinco a ocho elementos por semana». Se registra **con quién lo afirma, qué evidencia tiene y cómo se comprobaría**, y se valida **por orden de coste de fallar y de comprobar**: primero los de gran daño si fallan y barata comprobación.

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) añade la priorización: se ordenan por cuánto mueven el resultado y cuán inciertos son (sensibilidad e incertidumbre), y los críticos se convierten en hipótesis falsables. El mapa de supuestos conserva por cada uno enunciado, tipo, rango, impacto, costo de contrastarlo, hipótesis falsable, umbral, regla de decisión y fecha. Y la regla: ninguna hipótesis cambia de umbral tras observar.

## Ejemplo

Plan de lanzamiento. Supuesto A: «las estudiantes usan navegadores actuales» (afirma: producto; evidencia: estadísticas de acceso del año pasado; se comprobaría mirando el registro de accesos; barato). Supuesto B: «las docentes autorizarán guardar borradores» (esperado; costo de fallar: invalida la idea; se comprueba con cinco entrevistas). Orden de validación: B primero por su alto costo de fallar, A después por ser barato. (Ilustración del criterio de [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md).)

## Errores y confusiones comunes

- **Dar por hecho sin nombrarlo.**
- **Confundir supuesto con riesgo**: el supuesto es una creencia presente; el riesgo, un evento posible.
- **Supuestos sin responsable ni evidencia.**
- **Comprobar el más cómodo** y no el más sensible.

## Límites y cuándo no aplica

No se pueden enumerar todos los supuestos; se listan los relevantes. Algunos solo se comprueban construyendo. En el sentido de [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), un supuesto de un argumento de seguridad debe revisarse cuando cambia el entorno, o el argumento deja de valer.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Argumento](../a/argumento.md), [Condición](../c/condicion.md), [Plan](../p/plan.md), [Sobre](./sobre.md), [Evidencia y umbral](../e/evidencia-y-umbral.md), [Exposición](../e/exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (437 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [TSB Bank](../../../casos/fallo/tsb.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Supuesto», «supuesto».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stanford Encyclopedia of Philosophy: Karl Popper](https://plato.stanford.edu/entries/popper/) — falsabilidad como criterio de demarcación; autoridad: Stanford University.
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y ciclo construir-medir-aprender; autoridad: Eric Ries (fuente del autor).
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — cuantificar la incertidumbre con rangos y valor de la información; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar resultados, oportunidades y experimentos; autoridad: Teresa Torres (fuente del autor).
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — qué averiguar en una discovery y cómo compartir lo aprendido; autoridad: Government Digital Service.

---

[↑ Glosario](../../README.md) · [← Supuesto de vigilancia](./supuesto-de-vigilancia.md) · [Suscripción →](./suscripcion.md)
