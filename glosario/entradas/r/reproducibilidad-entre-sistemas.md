# Reproducibilidad entre sistemas

[↑ Glosario](../../README.md) · [← Reproducibilidad](./reproducibilidad.md) · [Reproduction →](./reproduction.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Un artefacto es **reproducible** si el mismo código y los mismos datos producen el mismo resultado, en sentido numérico o byte a byte. Los números de un experimento con semilla fija suelen coincidir entre sistemas.

Explicación de la sección «Reproducibilidad entre sistemas» de [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md).

## Por qué importa

En [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), el tema «Reproducibilidad entre sistemas» importa porque los bytes de los artefactos dependen del modo de escritura y del entorno.

En [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), el tema «Reproducibilidad entre sistemas» importa porque la huella debe ser independiente del sistema.

## Cómo funciona

Según [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), en la sección «Reproducibilidad entre sistemas»:

Un artefacto es **reproducible** si el mismo código y los mismos datos producen el mismo resultado, en sentido numérico o byte a byte. Los números de un experimento con semilla fija suelen coincidir entre sistemas. Los bytes de los archivos que se escriben, no siempre: la codificación por defecto, el fin de línea de los archivos de texto, el terminador de línea del módulo `csv` (que escribe `\r\n`, y en Windows el modo texto lo convierte en `\r\r\n`), el orden de iteración de un conjunto de cadenas (aleatorizado por proceso), la hora y el nombre del sistema varían. Algunas variaciones son defectos de escritura y se corrigen (abrir con `newline=""` y `encoding="utf-8"`, fijar el terminador); otras son legítimas (el reloj) y se excluyen del hash o se declaran.

Según [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), en la sección «Reproducibilidad entre sistemas»:

Una huella que depende del orden de `os.listdir`, de los finales de línea o del separador de ruta cambia entre sistemas aunque el contenido sea el mismo. La huella canónica ordena las rutas, usa separador `/`, normaliza `\r\n` a `\n` y fija la codificación. Es la misma idea de reproducibilidad que defiende Reproducible Builds para los binarios.

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
- **Ver también:** [Análisis confirmatorio y exploratorio](../a/analisis-confirmatorio-y-exploratorio.md), [Excepción](../e/excepcion.md), [Huella](../h/huella.md), [Huella canónica](../h/huella-canonica.md), [Manifiesto](../m/manifiesto.md), [Paquete de evidencia](../p/paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

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

[↑ Glosario](../../README.md) · [← Reproducibilidad](./reproducibilidad.md) · [Reproduction →](./reproduction.md)
