# Prueba de arquitectura

[↑ Glosario](../../README.md) · [← Prueba contractual](./prueba-contractual.md) · [Prueba de caracterización →](./prueba-de-caracterizacion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Prueba que comprueba reglas de dependencia o estructura del código.

Definición de trabajo de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Por qué importa

La clase donde se define, [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), existe con este propósito: el proyecto existe para que produzcas el artefacto con que se cierra una decisión arquitectónica en un equipo profesional: un registro de decisión (ADR) que otra persona pueda leer dentro de dos años, entender por qué se decidió así, comprobar si los supuestos siguen siendo ciertos y reabrirla con evidencia.

## Cómo funciona

Según [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

**Corrección.** Se añade a la prueba una regla que reprueba cualquier llamada a `import_module` en el dominio, se mueve la carga dinámica a un módulo de configuración de la capa de aplicación y se añade al ADR una sección «Lo que esta prueba no ve». La lección es que una prueba de arquitectura protege una forma de romper la regla, y el registro debe decir cuáles no.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md)) son: El analizador, la función de aptitud y la serie son herramientas del autor sobre registros y un paquete de juguete; no se evaluó ningún ADR real ni se ejecutó ninguna herramienta de terceros. La conclusión de que un ADR con estas características mejora las decisiones no se midió.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla de dependencia](../r/regla-de-dependencia.md), [Dependencia](../d/dependencia.md), [Estructura](../e/estructura.md), [Regla](../r/regla.md), [ADR](../a/adr.md), [Consecuencia negativa](../c/consecuencia-negativa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Prueba contractual](./prueba-contractual.md) · [Prueba de caracterización →](./prueba-de-caracterizacion.md)
