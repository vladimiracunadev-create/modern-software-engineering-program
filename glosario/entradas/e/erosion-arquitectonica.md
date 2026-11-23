# Erosión arquitectónica

[↑ Glosario](../../README.md) · [← Ergonomía y carga](./ergonomia-y-carga.md) · [Errata →](./errata.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Deterioro gradual de la estructura por cambios que violan las decisiones originales.

Definición de trabajo de [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md).

## Por qué importa

La clase donde se define, [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), existe con este propósito: la clase existe para que conviertas una decisión de arquitectura en una prueba automática que la defienda a lo largo del tiempo, y para que sepas elegir su umbral y su frecuencia sin que falle al azar ni deje pasar el deterioro.

## Cómo funciona

[SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md):

El equipo de la plataforma escribe un catálogo de siete funciones de aptitud: cuatro atómicas en cada commit (dominio sin importaciones de infraestructura, sin ciclos entre módulos, tamaño máximo del paquete, endpoints sin cambios incompatibles) y tres holísticas nocturnas (p95 del recorrido de entrega bajo 800 ms con 5 peticiones por segundo, capacidad en el pico, y tiempo de restauración).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md)) son:

- **Se descubren violaciones meses después** — causa: revisión infrecuente. Corrección: funciones atómicas baratas en cada commit.
- **La prueba de rendimiento falla al azar y se ignora** — causa: umbral cerca del valor esperado con pocas muestras. Corrección: más muestras o margen calibrado con la variabilidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún repositorio, pipeline ni sistema: la tasa de uso, las latencias lognormales, la deriva y los saltos son construcciones del autor. La siguiente clase registra las decisiones que estas funciones defienden y compara sus alternativas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](./estructura.md), [Alarma perdida](../a/alarma-perdida.md), [Falsa alarma](../f/falsa-alarma.md), [Función de aptitud arquitectónica](../f/funcion-de-aptitud-arquitectonica.md), [Trinquete](../t/trinquete.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Ford, Parsons y Kua, «Building Evolutionary Architectures» (O'Reilly)](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — funciones de aptitud y arquitectura evolutiva; autoridad: O'Reilly Media.
- [Thoughtworks Technology Radar, «Architectural fitness function»](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) — técnica de funciones de aptitud en la entrega; autoridad: Thoughtworks.
- [Google SRE, «Service Level Objectives»](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y percentiles; autoridad: Google SRE.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis de importaciones del ejemplo mínimo; autoridad: documentación de Python.
- [Python: `statistics`](https://docs.python.org/3/library/statistics.html) — mediana y cuantiles; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ergonomía y carga](./ergonomia-y-carga.md) · [Errata →](./errata.md)
