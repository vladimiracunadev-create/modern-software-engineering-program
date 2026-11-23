# Trinquete

[↑ Glosario](../../README.md) · [← Trie y prefijos](./trie-y-prefijos.md) · [Troncal →](./troncal.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Regla que impide que una medida empeore respecto de su mejor valor histórico más una tolerancia.

Definición de trabajo de [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md).

## Por qué importa

En [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), el tema «Tendencias y trinquetes» importa porque detectan el deterioro lento que un umbral fijo no ve.

## Cómo funciona

Según [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md):

Un umbral absoluto avisa cuando el daño ya está hecho. Dos alternativas avisan antes. El **trinquete** impide empeorar: la alarma salta si la medida supera el mejor valor histórico más una tolerancia, de modo que el listón solo sube. La **alarma por tendencia** mira la pendiente en una ventana y avisa del deterioro lento. Ambas adelantan la detección y ambas tienen un coste: son sensibles al ruido y generan más falsas alarmas. La combinación habitual es un trinquete con tolerancia más una revisión humana de las alarmas, y un umbral absoluto como red de seguridad de último recurso.

Según [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md):

El equipo de la plataforma escribe un catálogo de siete funciones de aptitud: cuatro atómicas en cada commit (dominio sin importaciones de infraestructura, sin ciclos entre módulos, tamaño máximo del paquete, endpoints sin cambios incompatibles) y tres holísticas nocturnas (p95 del recorrido de entrega bajo 800 ms con 5 peticiones por segundo, capacidad en el pico, y tiempo de restauración). Para la de latencia usa 500 muestras y margen ×1,10, porque con 30 las falsas alarmas eran del 25 %; para el acoplamiento usa un trinquete con tolerancia 2 y una revisión semanal de las alarmas. Cada función lleva su responsable y el ADR que la origina, y cuando se acepta un ADR que cambia el umbral se actualiza la función en el mismo cambio.

## Ejemplo

Ejemplo de [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma escribe un catálogo de siete funciones de aptitud: cuatro atómicas en cada commit (dominio sin importaciones de infraestructura, sin ciclos entre módulos, tamaño máximo del paquete, endpoints sin cambios incompatibles) y tres holísticas nocturnas (p95 del recorrido de entrega bajo 800 ms con 5 peticiones por segundo, capacidad en el pico, y tiempo de restauración). Para la de latencia usa 500 muestras y margen ×1,10, porque con 30 las falsas alarmas eran del 25 %; para el acoplamiento usa un trinquete con tolerancia 2 y una revisión semanal de las alarmas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La alarma por tendencia avisa constantemente** — causa: ventana corta frente al ruido. Corrección: ventana más larga, trinquete con tolerancia y revisión humana. ([SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **trinquete** impide empeorar: la alarma salta si la medida supera el mejor valor histórico más una tolerancia, de modo que el listón solo sube. ([SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Regla](../r/regla.md), [Valor](../v/valor.md), [Alarma perdida](../a/alarma-perdida.md), [Erosión arquitectónica](../e/erosion-arquitectonica.md), [Falsa alarma](../f/falsa-alarma.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

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

[↑ Glosario](../../README.md) · [← Trie y prefijos](./trie-y-prefijos.md) · [Troncal →](./troncal.md)
