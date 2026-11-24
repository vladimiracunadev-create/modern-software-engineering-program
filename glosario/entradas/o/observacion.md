# Observación

[↑ Glosario](../../README.md) · [← Observable y contrato de notificaciones](./observable-y-contrato-de-notificaciones.md) · [Observador →](./observador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Una **observación** es el registro de qué ocurrió, obtenido mediante un método y acompañado de su fuente y su límite ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md)). En el trabajo con agentes ([SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md)), la observación es el resultado de una acción que el *harness* devuelve al contexto del agente. Lo común: es un dato sobre el mundo, no una conclusión sobre él.

## Por qué importa

Separar observación de interpretación evita el error más frecuente del diagnóstico: presentar una métrica como si fuera una conclusión. [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) pide registrar el dato, la inferencia que se hace de él y la alternativa rival por separado. En agentes, lo que el modelo «ve» tras una acción es la observación, y su calidad limita todo lo que viene después.

## Cómo funciona

[SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) define: una observación «registra qué ocurrió mediante un método: *el p95 fue 480 ms en estas solicitudes, intervalo y entorno*». Lleva consigo el método, la muestra, el intervalo y el entorno. Eso la distingue de la inferencia («la dependencia contribuyó a la demora»), de la hipótesis y del supuesto. [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) añade un criterio de calidad: una observación correcta se acompaña de su fuente y límite. `platform.machine()` informa una etiqueta de plataforma que el runtime expone y `sys.byteorder` el orden nativo que Python observa; ninguno demuestra el modelo exacto de CPU, el tamaño de caché ni la frecuencia efectiva, y la virtualización, la emulación y los contenedores pueden interponer capas. En [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), el *harness* ejecuta la acción y devuelve su salida como observación; el diseño decide qué se recorta, se resume o se marca como datos externos.

## Ejemplo

```text
Observación: tras el despliegue 1.4.2, p95=480 ms (n=2000, entorno de preproducción, 10 min).
Inferencia: la dependencia D contribuyó a la demora.
Alternativa rival: el pico de matrícula coincidió con el despliegue.
```

## Errores y confusiones comunes

- **Una métrica se presenta como conclusión.** Causa: se omitieron inferencia y supuestos; corrección: separar registro, interpretación y alternativa rival ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md)).
- **Benchmark sin configuración.** Causa: se perdió trazabilidad; corrección: fijar datos, entorno, versiones, orden y múltiples corridas ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md)).
- **Tomar una etiqueta de plataforma por una medición del hardware** ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md)).

## Límites y cuándo no aplica

Una observación vale para su método y su muestra: no se generaliza sin más. Observar puede alterar lo observado (instrumentar cambia el rendimiento). Y en agentes, una observación puede contener texto de terceros: no se trata como instrucción, sino como dato.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Harness](../h/harness.md), [Resultado](../r/resultado.md), [ABI](../a/abi.md), [Arquitectura](../a/arquitectura.md), [Confusor](../c/confusor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (490 clases más lo mencionan; las que más):

[SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Observable y contrato de notificaciones](./observable-y-contrato-de-notificaciones.md) · [Observador →](./observador.md)
