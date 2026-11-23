# Puerta de entrada a la modernización

[↑ Glosario](../../README.md) · [← Puerta de aprobación](./puerta-de-aprobacion.md) · [Puerta de entrada a producción →](./puerta-de-entrada-a-produccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Conjunto de condiciones verificables que debe cumplir un sistema antes de iniciar su modernización.

Definición de trabajo de [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md).

## Por qué importa

La clase donde se define, [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), existe con este propósito: el taller existe para que no empieces una modernización sobre un terreno que se mueve.

## Cómo funciona

[SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo ejecuta el taller en seis estaciones durante dos semanas. Estación 1: construye el artefacto dos veces en máquinas distintas, encuentra que las fechas del empaquetado lo impiden, las fija y vuelve a comparar. Estación 2: ejecuta la suite cien veces sobre un commit sano, identifica 7 pruebas inestables de 412 y las pone en cuarentena con dueño y plazo; desactiva los reintentos automáticos de la integración.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md)) son:

- **La suite sale roja y verde sin cambios** — causa: pruebas inestables. Corrección: cuarentena con dueño y plazo, y corregir la causa.
- **Un defecto intermitente llega a producción** — causa: reintentos globales que lo escondieron. Corrección: eliminar los reintentos globales y repetir solo lo nuevo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): el ruido y los intervalos son sintéticos y con cifras idénticas, la construcción se ejecutó de verdad con treinta módulos creados para la ocasión y los veredictos coincidieron, y las huellas difieren entre sistemas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Conjunto](../c/conjunto.md), [Construcción reproducible](../c/construccion-reproducible.md), [Línea base](../l/linea-base.md), [Prueba inestable](./prueba-inestable.md), [Riesgo aceptado](../r/riesgo-aceptado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: FSE 2014.
- [Python: zipfile](https://docs.python.org/3/library/zipfile.html) — fechas y orden de los miembros de un archivo; autoridad: documentación de Python.
- [DORA: las cuatro claves](https://dora.dev/guides/dora-metrics-four-keys/) — métricas de entrega; autoridad: DORA.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo para una proporción; autoridad: Journal of the American Statistical Association.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — gestión del riesgo con un presupuesto; autoridad: Google, libro de ingeniería de confiabilidad.

---

[↑ Glosario](../../README.md) · [← Puerta de aprobación](./puerta-de-aprobacion.md) · [Puerta de entrada a producción →](./puerta-de-entrada-a-produccion.md)
