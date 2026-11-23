# Incertidumbre

[↑ Glosario](../../README.md) · [← Inbox](./inbox.md) · [Incertidumbre residual →](./incertidumbre-residual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Falta de conocimiento relevante.

Definición de trabajo de [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md): Parte relevante que la evidencia disponible no permite determinar.

## Por qué importa

En [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), el tema «Incertidumbre» importa porque ¿qué no sabemos y cuánto cambia la decisión?

En [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), el tema «Incertidumbre» importa porque una métrica sin intervalo no se puede comparar.

## Cómo funciona

Según [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md):

La incertidumbre puede expresarse con rangos, escenarios, sensibilidad o confianza argumentada. Una cifra con decimales no es más honesta si el método no permite esa precisión. Conviene preguntar si cambiar un supuesto cambia la opción preferida. Si no la cambia, quizá investigar más no aporte valor; si invierte una decisión irreversible, la evidencia adicional puede ser esencial.

Según [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md):

Que, bajo ciertos supuestos del modelo, un resultado así sería poco probable si no hubiera efecto. No dice que el efecto sea grande, importante ni causal. Esta clase no es un curso de estadística: lo útil aquí es preguntar qué incertidumbre queda y si cambia la decisión.

## Ejemplo

Ejemplo de [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) (sección «Preguntas frecuentes»):

Que, bajo ciertos supuestos del modelo, un resultado así sería poco probable si no hubiera efecto. No dice que el efecto sea grande, importante ni causal. Esta clase no es un curso de estadística: lo útil aquí es preguntar qué incertidumbre queda y si cambia la decisión.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md)) son:

- **una métrica se presenta como conclusión** — causa: se omitieron inferencia y supuestos. Corrección: separa registro, interpretación y alternativa rival.
- **benchmark sin configuración** — causa: se perdió trazabilidad. Corrección: fija datos, entorno, versiones, orden y múltiples corridas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La decisión incluye siempre señales de parada y revisión: reconocer incertidumbre no es paralizarse, sino gobernar lo que todavía no se sabe. ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Alcance](../a/alcance.md), [Confusor](../c/confusor.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [Hecho observado](../h/hecho-observado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (84 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Therac-25](../../../casos/fallo/therac-25.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Inbox](./inbox.md) · [Incertidumbre residual →](./incertidumbre-residual.md)
