# Reproducibilidad entre sistemas

[↑ Glosario](../../README.md) · [← Reproducibilidad](./reproducibilidad.md) · [Reproduction →](./reproduction.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Un artefacto es **reproducible** si el mismo código y los mismos datos producen el mismo resultado, en sentido numérico o byte a byte. La **reproducibilidad entre sistemas** es esa propiedad exigida *a través de* sistemas operativos y entornos distintos (por ejemplo, Windows y Ubuntu). La define [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) para informes de calidad y [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) la aplica a las huellas de contenido; el sentido es el mismo en ambas.

## Por qué importa

Un resultado que solo se obtiene en una máquina no es verificable por nadie más. Cambia una decisión concreta: cuando un hash o un informe difiere entre sistemas, ¿es un defecto o una variación legítima? Distinguirlo evita dos errores simétricos: ignorar un defecto de escritura, o perseguir una diferencia irrelevante (como el reloj).

## Cómo funciona

[SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) distingue qué coincide y qué no. Los **números** de un experimento con semilla fija suelen coincidir entre sistemas. Los **bytes de los archivos escritos**, no siempre. Las causas habituales son:

- la **codificación** por defecto;
- el **fin de línea** de los archivos de texto;
- el terminador del módulo `csv`, que escribe `\r\n` y que en Windows, en modo texto, se convierte en `\r\r\n`;
- el **orden de iteración** de un conjunto de cadenas, aleatorizado por proceso;
- la **hora** y el **nombre del sistema**.

Algunas variaciones son **defectos de escritura** y se corrigen (abrir con `newline=""` y `encoding="utf-8"`, fijar el terminador). Otras son **legítimas** (el reloj) y se excluyen del hash o se declaran.

[SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) extiende la idea a las huellas: una huella que depende del orden de `os.listdir`, de los finales de línea o del separador de ruta cambia entre sistemas aunque el contenido sea el mismo. La **huella canónica** ordena las rutas, usa separador `/`, normaliza `\r\n` a `\n` y fija la codificación. Es la misma idea que defiende Reproducible Builds para los binarios.

## Ejemplo

```python
import csv
with open("informe.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["ruta", "p95_ms"])
```

Sin `newline=""`, en Windows el modo texto convierte el `\r\n` del módulo `csv` en `\r\r\n` y el hash difiere del de Ubuntu aunque los datos sean idénticos. [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) ejecuta tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos en el validador y la selección y con diferencias esperables en los artefactos que dependen del sistema.

## Errores y confusiones comunes

- **Otra persona no puede reproducir el informe.** Faltan entorno, comando o semillas; corrección ([SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md)): un manifiesto con esos tres y ejecución en un sistema limpio.
- **Los hashes difieren entre Windows y Ubuntu.** Escritura en modo texto sin `newline` ni `encoding`; abrir con `newline=""` y `encoding="utf-8"` y fijar terminadores.
- **Hashear lo que depende del reloj.** La hora es una variación legítima: se excluye o se declara.
- **Confundir reproducible con correcto.** El resultado puede ser idéntico y equivocado.

## Límites y cuándo no aplica

[SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) es operativa para el informe de calidad de la API de entregas y declara «diferencias esperables» en artefactos que dependen del sistema, de modo que no toda variación es evitable. La reproducibilidad *byte a byte* de binarios compilados exige además entradas declaradas y entornos controlados (véase la reconstrucción independiente). Y con aritmética de punto flotante en hardware distinto, la reproducibilidad numérica exacta puede no darse aunque el código sea idéntico; eso es un límite del cálculo, no de la escritura de archivos.

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
