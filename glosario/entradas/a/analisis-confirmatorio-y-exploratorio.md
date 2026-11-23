# Análisis confirmatorio y exploratorio

[↑ Glosario](../../README.md) · [← Análisis](./analisis.md) · [Análisis de alcance →](./analisis-de-alcance.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

El primero está fijado en el plan antes de ver los datos; el segundo se decide después y solo sugiere hipótesis.

Definición de trabajo de [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md).

## Por qué importa

La clase donde se define, [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), existe con este propósito: el proyecto existe para que entregues un informe de calidad que otra persona pueda volver a ejecutar, auditar y refutar: la pregunta, la hipótesis y el umbral fijados antes; el entorno y las semillas; los datos crudos con su huella; los resultados recalculados desde esos datos; el veredicto derivado del umbral; y una lista honesta de lo que no se midió.

## Cómo funciona

[SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el informe de calidad de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md):

El proyecto entrega el paquete `informe-calidad/` con esta estructura: el plan (pregunta, hipótesis «p95 ≤ 300 ms con 200 usuarios simulados», umbral, estadístico, 30 repeticiones, criterio de exclusión) en un commit anterior a la ejecución; `ejecutar.py`, que corre la medición con semilla fija y escribe los datos con `newline=""` y `encoding="utf-8"`; `datos/raw.csv` con su SHA-256; `manifiesto.json` generado por el script;

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md)) son:

- **Otra persona no puede reproducir el informe** — causa: falta el entorno, el comando o las semillas. Corrección: manifiesto con entorno, comando y semillas, y ejecución en un sistema limpio.
- **Los hashes difieren entre Windows y Ubuntu** — causa: escritura en modo texto sin `newline` ni `encoding`. Corrección: abrir con `newline=""` y `encoding="utf-8"` y fijar terminadores.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md)) son: Las definiciones son operativas para el informe de calidad de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron los tres experimentos en Windows y Ubuntu (WSL2), con resultados idénticos en el validador y la selección y diferencias esperables en los artefactos que dependen del sistema.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hipótesis](../h/hipotesis.md), [Plan](../p/plan.md), [Huella](../h/huella.md), [Manifiesto](../m/manifiesto.md), [Paquete de informe](../p/paquete-de-informe.md), [Reproducibilidad](../r/reproducibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng, «Reproducible research in computational science»](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad; autoridad: Science, 2011.
- [Simmons, Nelson y Simonsohn, «False-positive psychology»](https://doi.org/10.1177/0956797611417632) — flexibilidad analítica y falsos positivos; autoridad: Psychological Science, 2011.
- [Reproducible Builds](https://reproducible-builds.org/docs/) — artefactos idénticos byte a byte y fuentes de variación; autoridad: proyecto Reproducible Builds.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — huellas SHA-256; autoridad: documentación de Python.
- [Python: csv](https://docs.python.org/3/library/csv.html) — `newline=''` y terminadores; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Análisis](./analisis.md) · [Análisis de alcance →](./analisis-de-alcance.md)
