# Característica de calidad

[↑ Glosario](../../README.md) · [← Característica autodeclarada](./caracteristica-autodeclarada.md) · [Característica de preferencia →](./caracteristica-de-preferencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Categoría de necesidades del modelo de calidad del producto, como eficiencia de desempeño o fiabilidad.

Definición de trabajo de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md).

## Por qué importa

La clase donde se define, [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), existe con este propósito: la clase existe para que conviertas una palabra como «rápido», «fiable» o «usable» en una promesa que se pueda comprobar: qué atributo de calidad importa, en qué situación, con qué estadístico, sobre qué ventana y con qué umbral.

## Cómo funciona

[SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md):

El equipo de la plataforma elige cuatro atributos para el cierre de plazos: eficiencia de desempeño, fiabilidad, compatibilidad y capacidad de interacción. Para cada uno escribe un escenario completo. El de eficiencia dice: *fuente:* docente; *estímulo:* abre la lista de 300 entregas de un curso; *artefacto:* endpoint de listado; *entorno:* día laboral con 50 consultas por segundo y datos de producción del último mes; *respuesta:* se muestra la primera página;

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)) son:

- **El informe dice «cumple» y hay quejas** — causa: ventana demasiado amplia o media como estadístico. Corrección: medir por ventana corta y con percentil.
- **Dos personas discuten si «300 ms» se cumple** — causa: falta estadístico, entorno o unidad. Corrección: escribir el escenario con las seis partes.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna API real, ningún usuario ni ningún sistema de producción; la proporción de peticiones lentas, el incidente del día 17, los diez escenarios base y los operadores de mutación son construcciones del autor, el verificador se escribió conociendo las mutaciones que lo evalúan y el texto de la norma no se reprodujo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calidad del producto](./calidad-del-producto.md), [Modelo](../m/modelo.md), [Necesidades](../n/necesidades.md), [Producto](../p/producto.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Indicador](../i/indicador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto con nueve características; autoridad: organismo de normalización (texto completo de pago).
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y percentiles; autoridad: Google, libro de ingeniería de confiabilidad.
- [Bass, Clements y Kazman, «Software Architecture in Practice»](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — media, mediana y cuantiles usados en los experimentos; autoridad: documentación de Python.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla para reproducir las muestras; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Característica autodeclarada](./caracteristica-autodeclarada.md) · [Característica de preferencia →](./caracteristica-de-preferencia.md)
