# Presupuesto de fotograma

[↑ Glosario](../../README.md) · [← Presupuesto de error](./presupuesto-de-error.md) · [Presupuesto de pasos →](./presupuesto-de-pasos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

El **presupuesto de fotograma** es el tiempo disponible para preparar un fotograma, igual al periodo de refresco de la pantalla. Es el sentido de [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md) (gráficos, audio, XR y experiencias inmersivas). Es un caso concreto de plazo duro: la pantalla no espera, de modo que cada fotograma tiene un tiempo máximo y no un tiempo «medio».

## Por qué importa

Convierte la tasa de refresco en un plazo para el cálculo y el dibujo. En experiencias inmersivas un fotograma tardío se nota como tirones, y en realidad virtual puede causar malestar. La decisión que cambia es qué se calcula en cada fotograma y qué se difiere.

## Cómo funciona

[SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md): una pantalla de 90 Hz muestra un fotograma cada 11,1 ms. La aplicación dispone de ese intervalo para entradas, actualización, dibujo y envío. Si un fotograma llega tarde:

- **Con sincronización vertical:** espera al siguiente refresco, así que se muestra el doble de tiempo (22,2 ms) y la tasa efectiva baja a la mitad en esos fotogramas.
- **Sin sincronización vertical:** aparecen cortes en la imagen (*tearing*).

De ahí la consecuencia estadística, igual a la de la latencia de cola: lo que importa no es el costo medio sino el **percentil alto**. Un costo medio por debajo del presupuesto puede perder una parte considerable de los fotogramas si la variabilidad es grande.

El mismo razonamiento vale para el audio, con un plazo distinto (el tamaño del búfer). [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md) fija el audio de la sala virtual en 48 kHz con búfer de 256 muestras (5,3 ms) por defecto y 512 para equipos con más fallos, medidos por el propio cliente con un contador de subcargas; si la tasa de bloques tardíos supera el 1 % durante un minuto, sube el búfer un nivel y lo avisa.

## Ejemplo

Ilustración numérica propia con la fórmula de la clase: a 90 Hz el presupuesto es 1 000/90 ≈ 11,1 ms; a 60 Hz, 16,7 ms. Si el cálculo cuesta 9 ms de media pero 14 ms en el 5 % de los fotogramas, a 90 Hz ese 5 % se pasa del presupuesto y aparece como tirón, aunque la media diga que sobra tiempo.

## Errores y confusiones comunes

- **Chasquidos en el audio:** búfer demasiado pequeño o procesamiento que lo supera; se sube el búfer ([SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md)).
- **Optimizar el costo medio** e ignorar el percentil alto.
- **Confundir la tasa de fotogramas por segundo con el tiempo por fotograma:** 60 fps promedio puede esconder fotogramas de 50 ms.
- **Confundirlo con el presupuesto de recursos,** que fija límites de energía y memoria en un dispositivo.

## Límites y cuándo no aplica

Supone una pantalla de tasa fija; con tasas variables el plazo se mueve. No aplica a aplicaciones que no animan de forma continua. Los valores de audio son los de la plataforma simulada de la clase.

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
