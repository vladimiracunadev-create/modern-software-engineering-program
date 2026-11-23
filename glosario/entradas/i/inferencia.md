# Inferencia

[↑ Glosario](../../README.md) · [← Índices ordenados y consultas de rango](./indices-ordenados-y-consultas-de-rango.md) · [Inferencia de pertenencia →](./inferencia-de-pertenencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Conclusión derivada de observaciones y supuestos.

Definición de trabajo de [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md): Explicación compatible con hechos, aún contrastable.
- En [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md): Derivación de una conclusión desde premisas.

## Por qué importa

En [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), el tema «Inferencia» importa porque ¿qué explicación conecta datos y conclusión?

## Cómo funciona

Según [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md):

Una **observación** registra qué ocurrió mediante un método: “el p95 fue 480 ms en estas solicitudes, intervalo y entorno”. Una **inferencia** conecta observaciones con una conclusión: “la dependencia contribuyó a la demora”. Una **hipótesis** formula una explicación contrastable: “si la dependencia es la causa dominante, aislarla reducirá la cola”. Un **supuesto** es una condición aceptada provisionalmente, como considerar representativa la carga de prueba.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md):

El benchmark de consulta se repite con datos fríos y calientes, mismos recursos y múltiples corridas. La mediana mejora, pero la cola empeora con alta concurrencia. La decisión cambia de «adoptar» a «probar bajo carga representativa».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **una métrica se presenta como conclusión** — causa: se omitieron inferencia y supuestos. Corrección: separa registro, interpretación y alternativa rival. ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **inferencia** conecta observaciones con una conclusión: “la dependencia contribuyó a la demora”. ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Explicación](../e/explicacion.md), [Hecho](../h/hecho.md), [Observación](../o/observacion.md), [Supuestos](../s/supuestos.md), [Confusor](../c/confusor.md), [Correlación](../c/correlacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (40 clases más lo mencionan; las que más):

[SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Event Logging](https://learn.microsoft.com/windows/win32/eventlog/event-logging) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd — journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Apple Developer — Logging](https://developer.apple.com/documentation/os/logging) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.
- [OpenTelemetry — Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.

---

[↑ Glosario](../../README.md) · [← Índices ordenados y consultas de rango](./indices-ordenados-y-consultas-de-rango.md) · [Inferencia de pertenencia →](./inferencia-de-pertenencia.md)
