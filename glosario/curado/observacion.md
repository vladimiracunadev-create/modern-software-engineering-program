# Observación

## Definición

Una **observación** es el registro de qué ocurrió, obtenido mediante un método y acompañado de su fuente y su límite (`SE-006`, `SE-013`). En el trabajo con agentes (`SE-577`), la observación es el resultado de una acción que el *harness* devuelve al contexto del agente. Lo común: es un dato sobre el mundo, no una conclusión sobre él.

## Por qué importa

Separar observación de interpretación evita el error más frecuente del diagnóstico: presentar una métrica como si fuera una conclusión. `SE-006` pide registrar el dato, la inferencia que se hace de él y la alternativa rival por separado. En agentes, lo que el modelo «ve» tras una acción es la observación, y su calidad limita todo lo que viene después.

## Cómo funciona

`SE-006` define: una observación «registra qué ocurrió mediante un método: *el p95 fue 480 ms en estas solicitudes, intervalo y entorno*». Lleva consigo el método, la muestra, el intervalo y el entorno. Eso la distingue de la inferencia («la dependencia contribuyó a la demora»), de la hipótesis y del supuesto. `SE-013` añade un criterio de calidad: una observación correcta se acompaña de su fuente y límite. `platform.machine()` informa una etiqueta de plataforma que el runtime expone y `sys.byteorder` el orden nativo que Python observa; ninguno demuestra el modelo exacto de CPU, el tamaño de caché ni la frecuencia efectiva, y la virtualización, la emulación y los contenedores pueden interponer capas. En `SE-577`, el *harness* ejecuta la acción y devuelve su salida como observación; el diseño decide qué se recorta, se resume o se marca como datos externos.

## Ejemplo

```text
Observación: tras el despliegue 1.4.2, p95=480 ms (n=2000, entorno de preproducción, 10 min).
Inferencia: la dependencia D contribuyó a la demora.
Alternativa rival: el pico de matrícula coincidió con el despliegue.
```

## Errores y confusiones comunes

- **Una métrica se presenta como conclusión.** Causa: se omitieron inferencia y supuestos; corrección: separar registro, interpretación y alternativa rival (`SE-006`).
- **Benchmark sin configuración.** Causa: se perdió trazabilidad; corrección: fijar datos, entorno, versiones, orden y múltiples corridas (`SE-006`).
- **Tomar una etiqueta de plataforma por una medición del hardware** (`SE-013`).

## Límites y cuándo no aplica

Una observación vale para su método y su muestra: no se generaliza sin más. Observar puede alterar lo observado (instrumentar cambia el rendimiento). Y en agentes, una observación puede contener texto de terceros: no se trata como instrucción, sino como dato.
