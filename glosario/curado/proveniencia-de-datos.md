# Proveniencia de datos

## Definición

La **proveniencia de datos** (*data provenance*, también llamada linaje o *lineage*) es el registro de **de dónde viene un dato y qué se le hizo hasta llegar a donde se muestra**. En `SE-101`, la regla es: **toda tabla o gráfico debe indicar origen, transformación, versión y filtros**. Es el equivalente, para datos, de una cita bibliográfica: permite a otra persona (o a uno mismo meses después) saber qué se está viendo y reproducirlo. No debe confundirse con la «procedencia» de un artefacto de software (de qué fuente y con qué proceso se construyó), aunque comparten la idea.

## Por qué importa

Un gráfico sin origen es una afirmación sin evidencia: nadie sabe si usa los datos de este mes o de hace un año, si se excluyeron registros, si los valores se redondearon o se calcularon con otra fórmula. En trabajo exploratorio, donde se prueban muchas versiones rápidamente, la proveniencia se pierde con facilidad. La decisión que cambia es cuándo se anota: al producir la tabla, no después. `SE-101` agrega una regla fuerte: **copiar datos manualmente destruye la trazabilidad**; un número pegado a mano en un cuaderno ya no tiene origen verificable.

## Cómo funciona

Cuatro elementos hacen auditable un resultado:

- **Origen:** de qué fuente proceden los datos (archivo, consulta, servicio) y cómo se obtuvieron.
- **Transformación:** qué cálculos y limpiezas se aplicaron, de preferencia como código ejecutable y no como pasos manuales.
- **Versión:** de qué versión de los datos y del código se trata, para poder reproducirlo.
- **Filtros:** qué registros se excluyeron y por qué.

Cuando la fuente es **externa**, no siempre se puede reproducir la extracción (los datos cambian, o no se tiene acceso). Para eso sirven los **hashes**: se guarda el resumen criptográfico de los datos usados, de modo que se pueda comprobar después si son los mismos. En el entorno reproducible de diagnóstico del programa se usan **fixtures sintéticos guardados** (datos inventados que se versionan con el código) y hashes cuando la fuente es externa y autorizada. Así el análisis es reproducible sin exponer datos reales.

## Ejemplo

Un cuaderno que produce una tabla de tiempos de respuesta. Con proveniencia:

```python
import hashlib, pathlib
ruta = pathlib.Path("datos/tiempos_2026-11.csv")
sha = hashlib.sha256(ruta.read_bytes()).hexdigest()
print(f"Origen: {ruta} (sha256 {sha[:12]}...), filtro: percentil <= 99, "
      f"código: commit {COMMIT}")
tabla = cargar(ruta).query("percentil <= 99")
```

La salida de la celda acompaña a la tabla. Si alguien cambia el archivo, el resumen cambia. `SE-101` documenta dos síntomas relacionados del cuaderno: da otro resultado en otra máquina por estado oculto del orden de ejecución (se reinicia y se ejecuta todo antes de compartir) y el *diff* es enorme con cambios mínimos porque se guardan salidas y metadatos (se limpian las salidas antes de confirmar).

## Errores y confusiones comunes

- **Pegar números a mano.** Se pierde el vínculo con la fuente.
- **Omitir los filtros.** Dos personas obtienen resultados distintos de «los mismos datos».
- **Guardar solo el gráfico.** Sin código ni versión no se puede regenerar.
- **Incluir datos reales en un caso de ejemplo.** Mejor un conjunto sintético con hash.

## Límites y cuándo no aplica

Un proceso limpio aún puede usar otra versión del *runtime* (`SE-101`): la proveniencia de datos no cubre la del entorno de ejecución. Registrar todo cuesta; para una exploración desechable que nadie más verá, basta una nota breve. Y la proveniencia describe el camino de un dato, no garantiza que sea correcto: datos mal capturados en el origen siguen mal aunque su linaje sea impecable.
