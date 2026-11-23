# Aliasing

[↑ Glosario](../../README.md) · [← Alias](./alias.md) · [Almacén →](./almacen.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Efecto por el cual una frecuencia por encima de la mitad de la tasa de muestreo se mide como otra más baja.

Definición de trabajo de [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md).

## Por qué importa

En [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), el tema «Muestreo y aliasing» importa porque marca qué información se puede conservar y cuál se pierde para siempre.

## Cómo funciona

Según [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** al reproducir se oye un tono de 3 kHz que no está en la fuente. **Hipótesis rivales:** (a) el altavoz introduce distorsión; (b) hay un error de reproducción de la aplicación; (c) la fuente contenía un tono sobre la mitad de la tasa de muestreo. **Prueba:** calcula `|5000 − 8000| = 3000` y comprueba que la transformada de las muestras da 3 000 Hz; con un filtro de paso bajo en 3,5 kHz antes de muestrear, el tono desaparece. **Conclusión:** aliasing. **Regresión:** añade el filtro y una prueba que muestree tonos por encima de la mitad de la tasa y verifique que su energía se atenúa.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md):

El equipo de la plataforma fija el audio de la sala virtual en 48 kHz con búfer de 256 muestras (5,3 ms) como valor por defecto y 512 para equipos con más fallos, medidos por el propio cliente con un contador de subcargas; si la tasa de bloques tardíos supera el 1 % durante un minuto, el cliente sube el búfer un nivel y lo avisa. Antes de muestrear las grabaciones de baja calidad aplica un filtro de paso bajo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md)) son:

- **Chasquidos en el audio** — causa: búfer demasiado pequeño o procesamiento que bloquea. Corrección: medir subcargas, subir el búfer o quitar asignaciones y bloqueos del callback.
- **Silbidos o tonos que no estaban** — causa: muestreo sin filtro previo. Corrección: filtro de paso bajo antes de muestrear o tasa mayor con filtro.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md)) son: Las definiciones son operativas para la sala virtual. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor de audio, tarjeta gráfica, casco ni persona: los costes de procesamiento, las distribuciones lognormales y la pantalla de 90 Hz son construcciones del autor, y no se midió confort ni percepción. La siguiente clase pasa al dominio del dinero, donde el error es una cifra.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Baja](../b/baja.md), [Efecto](../e/efecto.md), [Muestreo](../m/muestreo.md), [Búfer de audio](../b/bufer-de-audio.md), [Presupuesto de fotograma](../p/presupuesto-de-fotograma.md), [Reproyección](../r/reproyeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-293 — Gráficos, audio, XR y experiencias inmersivas](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), [SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md).

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

[↑ Glosario](../../README.md) · [← Alias](./alias.md) · [Almacén →](./almacen.md)
