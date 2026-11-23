# Idiomático

[↑ Glosario](../../README.md) · [← Identificadores y expresiones spdx](./identificadores-y-expresiones-spdx.md) · [Igualdad de oportunidad →](./igualdad-de-oportunidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Alineado con convenciones y mecanismos del lenguaje.

Definición de trabajo de [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md).

## Por qué importa

La clase donde se define, [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), existe con este propósito: la clase existe para transferir una solución entre lenguajes preservando contrato y haciendo visibles diferencias semánticas.

## Cómo funciona

[SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md):

El taller ejecuta el mismo archivo de casos en ambas implementaciones y compara JSON canónico. Un documento separa equivalencia funcional, diferencias de tipos, costo y experiencia de mantenimiento. No declara un lenguaje ganador universal.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md)) son:

- **el puerto da un resultado distinto con números negativos** — causa: división y resto con semántica distinta. Corrección: casos compartidos con negativos y su valor esperado.
- **la longitud de un texto no coincide** — causa: caracteres frente a bytes. Corrección: decidir qué se cuenta y fijar un caso con acentos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. El taller no enseña Rust completo ni compara rendimiento con un microbenchmark. El proyecto final integra el recorrido en una CLI Python probada.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Mecanismo](../m/mecanismo.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md), [Equivalencia funcional](../e/equivalencia-funcional.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — documenta ownership, tipos de error, traits y concurrencia usados como contraste semántico.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `unittest` documentation](https://docs.python.org/3/library/unittest.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Identificadores y expresiones spdx](./identificadores-y-expresiones-spdx.md) · [Igualdad de oportunidad →](./igualdad-de-oportunidad.md)
