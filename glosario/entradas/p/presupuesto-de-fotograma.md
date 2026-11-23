# Presupuesto de fotograma

[↑ Glosario](../../README.md) · [← Presupuesto de error](./presupuesto-de-error.md) · [Presupuesto de pasos →](./presupuesto-de-pasos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Tiempo disponible para preparar un fotograma, igual al periodo de refresco de la pantalla.

Definición de trabajo de [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md).

## Por qué importa

En [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), el tema «Presupuesto de fotograma» importa porque convierte la tasa de refresco en un plazo para el cálculo y el dibujo.

## Cómo funciona

Según [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), en la sección «Presupuesto de fotograma»:

Una pantalla de 90 Hz muestra un fotograma cada 11,1 ms. La aplicación dispone de ese intervalo para entradas, actualización, dibujo y envío. Con **sincronización vertical**, un fotograma que llega tarde espera al siguiente refresco: se muestra el doble de tiempo (22,2 ms), y la tasa efectiva baja a la mitad en esos fotogramas. Sin ella, aparecen cortes en la imagen. Por eso lo que importa no es el coste medio sino el percentil alto: un coste medio por debajo del presupuesto puede perder una parte considerable de los fotogramas si la variabilidad es grande.

## Ejemplo

Ejemplo de [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma fija el audio de la sala virtual en 48 kHz con búfer de 256 muestras (5,3 ms) como valor por defecto y 512 para equipos con más fallos, medidos por el propio cliente con un contador de subcargas; si la tasa de bloques tardíos supera el 1 % durante un minuto, el cliente sube el búfer un nivel y lo avisa. Antes de muestrear las grabaciones de baja calidad aplica un filtro de paso bajo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md)) son:

- **Chasquidos en el audio** — causa: búfer demasiado pequeño o procesamiento que bloquea. Corrección: medir subcargas, subir el búfer o quitar asignaciones y bloqueos del callback.
- **Silbidos o tonos que no estaban** — causa: muestreo sin filtro previo. Corrección: filtro de paso bajo antes de muestrear o tasa mayor con filtro.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md)) son: Las definiciones son operativas para la sala virtual. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor de audio, tarjeta gráfica, casco ni persona: los costes de procesamiento, las distribuciones lognormales y la pantalla de 90 Hz son construcciones del autor, y no se midió confort ni percepción. La siguiente clase pasa al dominio del dinero, donde el error es una cifra.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aliasing](../a/aliasing.md), [Búfer de audio](../b/bufer-de-audio.md), [Reproyección](../r/reproyeccion.md), [Subcarga](../s/subcarga.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Shannon, «Communication in the Presence of Noise» (Proceedings of the IRE, 1949)](https://doi.org/10.1109/JRPROC.1949.232969) — teorema del muestreo; autoridad: Proceedings of the IRE.
- [W3C, Web Audio API](https://www.w3.org/TR/webaudio/) — procesamiento de audio por bloques y latencia; autoridad: W3C.
- [Khronos, especificación de OpenXR](https://registry.khronos.org/OpenXR/) — interfaz de realidad extendida con predicción de pose; autoridad: Khronos Group.
- [W3C, WebXR Device API](https://www.w3.org/TR/webxr/) — acceso a dispositivos de realidad extendida desde la web; autoridad: W3C.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Presupuesto de error](./presupuesto-de-error.md) · [Presupuesto de pasos →](./presupuesto-de-pasos.md)
