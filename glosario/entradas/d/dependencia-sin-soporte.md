# Dependencia sin soporte

[↑ Glosario](../../README.md) · [← Dependencia nominal](./dependencia-nominal.md) · [Dependencia transitiva →](./dependencia-transitiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Dependencia cuyo mantenedor ya no publica correcciones, incluidas las de seguridad.

Definición de trabajo de [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

## Por qué importa

La clase donde se define, [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), existe con este propósito: la clase existe para que trates las dependencias desactualizadas como un riesgo que se acumula con el tiempo y se puede medir, no como una tarea pendiente más.

## Cómo funciona

[SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el inventario del módulo: 14 dependencias directas y 61 transitivas. De las directas, 4 llevan más de tres años sin actualizar, 1 no tiene soporte (la biblioteca de exportación) y 2 tienen avisos abiertos. Con el grafo, descubren que la biblioteca de fechas es un concentrador: de ella dependen 9 paquetes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)) son:

- **La actualización «de una hora» dura semanas** — causa: se acumularon cambios incompatibles. Corrección: actualizar en pasos pequeños con una cadencia.
- **Un aviso queda abierto meses** — causa: política por lotes sin prioridad. Corrección: añadir un carril rápido para avisos con explotación conocida.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se consultó ningún repositorio de paquetes, base de vulnerabilidades ni biblioteca real; la probabilidad de cambio incompatible, la fórmula de interacción, el ritmo de avisos, el retraso del proveedor y los grafos aleatorios son construcciones del autor, y las políticas de la simulación son versiones simplificadas de las reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](./dependencia.md), [Seguridad](../s/seguridad.md), [Archivo de bloqueo](../a/archivo-de-bloqueo.md), [Dependencia atrasada](./dependencia-atrasada.md), [Radio de impacto](../r/radio-de-impacto.md), [Ventana de exposición](../v/ventana-de-exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Versionado semántico 2.0.0](https://semver.org/) — convención de versiones con cambios incompatibles en la mayor; autoridad: especificación de la comunidad.
- [OSV](https://osv.dev/) — registro abierto de vulnerabilidades por paquete y versión; autoridad: proyecto abierto respaldado por Google.
- [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — vulnerabilidades con explotación conocida; autoridad: agencia de ciberseguridad de Estados Unidos.
- [NIST SP 800-218, SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas para componentes de terceros y respuesta a vulnerabilidades; autoridad: NIST.
- [Google, «Software Engineering at Google»: Dependency Management](https://abseil.io/resources/swe-book/html/ch21.html) — por qué es difícil gestionar dependencias; autoridad: libro de ingeniería de Google.

---

[↑ Glosario](../../README.md) · [← Dependencia nominal](./dependencia-nominal.md) · [Dependencia transitiva →](./dependencia-transitiva.md)
