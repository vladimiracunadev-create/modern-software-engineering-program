# Intervalo

[↑ Glosario](../../README.md) · [← Intersección de capacidades](./interseccion-de-capacidades.md) · [Intervalo de confianza →](./intervalo-de-confianza.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Intervalo expresa rango compatible con método y datos, no promesa absoluta.

Tomado del glosario de [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md).

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md):

Una **observación** registra qué ocurrió mediante un método: “el p95 fue 480 ms en estas solicitudes, intervalo y entorno”. Una **inferencia** conecta observaciones con una conclusión: “la dependencia contribuyó a la demora”. Una **hipótesis** formula una explicación contrastable: “si la dependencia es la causa dominante, aislarla reducirá la cola”. Un **supuesto** es una condición aceptada provisionalmente, como considerar representativa la carga de prueba.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md):

El benchmark de consulta se repite con datos fríos y calientes, mismos recursos y múltiples corridas. La mediana mejora, pero la cola empeora con alta concurrencia. La decisión cambia de «adoptar» a «probar bajo carga representativa».

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md)) son:

- **una métrica se presenta como conclusión** — causa: se omitieron inferencia y supuestos. Corrección: separa registro, interpretación y alternativa rival.
- **benchmark sin configuración** — causa: se perdió trazabilidad. Corrección: fija datos, entorno, versiones, orden y múltiples corridas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Buscar solo confirmación es fácil: elegir el intervalo que coincide, descartar outliers sin regla o consultar únicamente a quien adoptó el producto. ([SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Rango](../r/rango.md), [Confusor](../c/confusor.md), [Hecho observado](../h/hecho-observado.md), [Hipótesis](../h/hipotesis.md), [Incertidumbre](./incertidumbre.md), [Inferencia](./inferencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.

**También se usa en** (116 clases más lo mencionan; las que más):

[SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Intersección de capacidades](./interseccion-de-capacidades.md) · [Intervalo de confianza →](./intervalo-de-confianza.md)
