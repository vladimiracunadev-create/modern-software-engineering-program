# Reproducibilidad entre sistemas

## Definición

Un artefacto es **reproducible** si el mismo código y los mismos datos producen el mismo resultado, en sentido numérico o byte a byte. La **reproducibilidad entre sistemas** es esa propiedad exigida *a través de* sistemas operativos y entornos distintos (por ejemplo, Windows y Ubuntu). La define `SE-444` para informes de calidad y `SE-468` la aplica a las huellas de contenido; el sentido es el mismo en ambas.

## Por qué importa

Un resultado que solo se obtiene en una máquina no es verificable por nadie más. Cambia una decisión concreta: cuando un hash o un informe difiere entre sistemas, ¿es un defecto o una variación legítima? Distinguirlo evita dos errores simétricos: ignorar un defecto de escritura, o perseguir una diferencia irrelevante (como el reloj).

## Cómo funciona

`SE-444` distingue qué coincide y qué no. Los **números** de un experimento con semilla fija suelen coincidir entre sistemas. Los **bytes de los archivos escritos**, no siempre. Las causas habituales son:

- la **codificación** por defecto;
- el **fin de línea** de los archivos de texto;
- el terminador del módulo `csv`, que escribe `\r\n` y que en Windows, en modo texto, se convierte en `\r\r\n`;
- el **orden de iteración** de un conjunto de cadenas, aleatorizado por proceso;
- la **hora** y el **nombre del sistema**.

Algunas variaciones son **defectos de escritura** y se corrigen (abrir con `newline=""` y `encoding="utf-8"`, fijar el terminador). Otras son **legítimas** (el reloj) y se excluyen del hash o se declaran.

`SE-468` extiende la idea a las huellas: una huella que depende del orden de `os.listdir`, de los finales de línea o del separador de ruta cambia entre sistemas aunque el contenido sea el mismo. La **huella canónica** ordena las rutas, usa separador `/`, normaliza `\r\n` a `\n` y fija la codificación. Es la misma idea que defiende Reproducible Builds para los binarios.

## Ejemplo

```python
import csv
with open("informe.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["ruta", "p95_ms"])
```

Sin `newline=""`, en Windows el modo texto convierte el `\r\n` del módulo `csv` en `\r\r\n` y el hash difiere del de Ubuntu aunque los datos sean idénticos. `SE-444` ejecuta tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos en el validador y la selección y con diferencias esperables en los artefactos que dependen del sistema.

## Errores y confusiones comunes

- **Otra persona no puede reproducir el informe.** Faltan entorno, comando o semillas; corrección (`SE-444`): un manifiesto con esos tres y ejecución en un sistema limpio.
- **Los hashes difieren entre Windows y Ubuntu.** Escritura en modo texto sin `newline` ni `encoding`; abrir con `newline=""` y `encoding="utf-8"` y fijar terminadores.
- **Hashear lo que depende del reloj.** La hora es una variación legítima: se excluye o se declara.
- **Confundir reproducible con correcto.** El resultado puede ser idéntico y equivocado.

## Límites y cuándo no aplica

`SE-444` es operativa para el informe de calidad de la API de entregas y declara «diferencias esperables» en artefactos que dependen del sistema, de modo que no toda variación es evitable. La reproducibilidad *byte a byte* de binarios compilados exige además entradas declaradas y entornos controlados (véase la reconstrucción independiente). Y con aritmética de punto flotante en hardware distinto, la reproducibilidad numérica exacta puede no darse aunque el código sea idéntico; eso es un límite del cálculo, no de la escritura de archivos.
