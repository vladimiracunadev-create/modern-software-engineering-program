# Reproductor mínimo

[↑ Glosario](../../README.md) · [← Reproduction](./reproduction.md) · [Reproyección →](./reproyeccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Programa pequeño y determinista que muestra un fallo con la menor cantidad posible de pasos.

Definición de trabajo de [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

## Por qué importa

La clase donde se define, [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), existe con este propósito: el taller existe para que practiques el oficio más caro de los sistemas concurrentes y distribuidos: convertir un síntoma esporádico («a veces se aceptan dos entregas con un solo cupo», «a veces el acuse llega y el registro no») en un caso que falla siempre, que es lo más pequeño posible y que queda como prueba de regresión estable.

## Cómo funciona

[SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md):

El equipo del reporte del lunes sigue el procedimiento del taller. Para el cupo duplicado, escribe el modelo de tres pasos, reproduce con el calendario mínimo de seis pasos y descubre que otra ruta (la importación masiva) también leía y escribía el cupo sin la comprobación atómica. La corrección reemplaza «leer y escribir» por `UPDATE cupo SET libres = libres - 1 WHERE libres > 0` y comprueba el número de filas afectadas; la regresión ejecuta el calendario mínimo y 200 semillas del planificador y falla antes del cambio.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md)) son:

- **El fallo desaparece al añadir registros** — causa: el registro cambia el orden de los pasos. Corrección: registrar fuera de la sección o grabar la ejecución.
- **El arreglo vuelve a fallar por otra ruta** — causa: solo se protegió una de las rutas. Corrección: proteger el dato, no la ruta, y probar cada ruta.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos deterministas en Windows y Ubuntu (WSL2) con resultados idénticos. No se usaron hilos del sistema operativo ni una red: el modelo de tres pasos, el ruido, el flujo de cinco pasos y la tasa de 1 en 70 son construcciones del autor, y la reducción puede devolver un mínimo local.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Corte](../c/corte.md), [Prueba de regresión](../p/prueba-de-regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Zeller y Hildebrandt, «Simplifying and isolating failure-inducing input»](https://doi.org/10.1109/32.988498) — reducción por delta; autoridad: artículo original (2002).
- [Musuvathi et al., CHESS](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/musuvathi/musuvathi.pdf) — planificador controlado y exploración sistemática; autoridad: artículo de OSDI (2008).
- [rr: grabación y reproducción](https://rr-project.org/) — reproducción determinista de ejecuciones; autoridad: proyecto rr.
- [Helland, «Idempotence is not a medical condition»](https://doi.org/10.1145/2181796.2187821) — reintentos y respuesta perdida; autoridad: artículo de ACM Queue (2012).
- [Python: unittest](https://docs.python.org/3/library/unittest.html) — pruebas de regresión ejecutables; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Reproduction](./reproduction.md) · [Reproyección →](./reproyeccion.md)
