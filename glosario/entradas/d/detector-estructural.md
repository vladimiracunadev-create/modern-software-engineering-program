# Detector estructural

[↑ Glosario](../../README.md) · [← Detector de fallos](./detector-de-fallos.md) · [Determinismo →](./determinismo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Regla que identifica un patrón por la forma del código y no por el nombre.

Definición de trabajo de [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md).

## Por qué importa

La clase donde se define, [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), existe con este propósito: el proyecto integra la parte en un entregable que un equipo puede mantener: un **catálogo de los patrones de un sistema** donde cada entrada responde por la fuerza que resuelve, dónde vive en el código, qué evidencia la sostiene, cuánto cuesta y bajo qué condición se retira.

## Cómo funciona

Según [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md):

El **detector por nombre** busca las palabras `Strategy`, `Observer`, `Decorator`, `Factory` y `Singleton` en los nombres de clase: obtiene 2 verdaderos positivos, **5 falsos positivos** y 6 falsos negativos, con **29 % de precisión** y **25 % de exhaustividad**. El **detector estructural** busca la forma con `ast`: una clase abstracta con al menos dos subclases, una subclase que guarda una instancia de su propia base, una lista de llamables con métodos que añaden y recorren, un diccionario de clases y un `__new__` que consulta un atributo de clase. Obtiene 6 verdaderos positivos, 1 falso positivo (el acumulador) y 2 falsos negativos (los dos patrones con diccionarios), con **86 % de precisión** y **75 % de exhaustividad**.

Según [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md):

El equipo de *Avisos* dedica dos tardes al catálogo. Ejecuta el detector estructural sobre sus 140 módulos y obtiene 31 candidatos; en una sesión de revisión de dos horas, tres personas leen cada uno contra la definición: 19 son patrones reales, 9 se descartan con razón (cuatro son utilidades con nombre de patrón, dos son acumuladores, tres son jerarquías con una sola implementación) y 3 quedan en duda. De los 19, 11 tienen medida de costo disponible; los 8 restantes se devuelven con el campo faltante. El catálogo entra al repositorio como `docs/patrones.md`, con una lista de descartes y una revisión trimestral. Dos patrones se marcan «simplificar»: la jerarquía de siete tarifas (la mitad de las variantes no se usa) y una capa de repositorio sobre una tabla de configuración.

## Ejemplo

Ejemplo de [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* dedica dos tardes al catálogo. Ejecuta el detector estructural sobre sus 140 módulos y obtiene 31 candidatos; en una sesión de revisión de dos horas, tres personas leen cada uno contra la definición: 19 son patrones reales, 9 se descartan con razón (cuatro son utilidades con nombre de patrón, dos son acumuladores, tres son jerarquías con una sola implementación) y 3 quedan en duda. De los 19, 11 tienen medida de costo disponible; los 8 restantes se devuelven con el campo faltante. El catálogo entra al repositorio como `docs/patrones.md`, con una lista de descartes y una revisión trimestral.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el corpus es pequeño, escrito por el autor, y el detector estructural se escribió conociéndolo; con código real, los patrones tienen más variantes y la precisión y la exhaustividad bajarían. ([SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Patrón](../p/patron.md).
- **Ver también:** [Regla](../r/regla.md), [ADR](../a/adr.md), [Candidato descartado](../c/candidato-descartado.md), [Catálogo de patrones de un sistema](../c/catalogo-de-patrones-de-un-sistema.md), [Condición de salida](../c/condicion-de-salida.md), [Exhaustividad](../e/exhaustividad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Detector de fallos](./detector-de-fallos.md) · [Determinismo →](./determinismo.md)
