# Semántica

[↑ Glosario](../../README.md) · [← Sellado](./sellado.md) · [Semántica antes que sintaxis →](./semantica-antes-que-sintaxis.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Comportamiento y significado observable.

Definición de trabajo de [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md).

## Por qué importa

La clase donde se define, [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), existe con este propósito: la clase existe para transferir una solución entre lenguajes preservando contrato y haciendo visibles diferencias semánticas.

## Cómo funciona

Según [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md):

Elige una diferencia semántica y haz que falle una transferencia ingenua. Por ejemplo, calcula `-7 % 2` en Python (1) y escribe la expectativa «resto 1» como contrato. Un puerto a un lenguaje con resto truncado devolverá -1 y la prueba compartida lo detecta. Añade el caso a una tabla común con el valor esperado y una nota («división entera hacia menos infinito»). Después altera un caso TSV del laboratorio (cambia un candidato esperado) y comprueba que la referencia en Python y, donde haya compilador, el puerto Rust dejan de coincidir; decide si cambió la regla o solo el puerto. Si no tienes `rustc`, registra «no compilado» en lugar de afirmar el resultado.

Según [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md):

Reimplementa el contrato, no la sintaxis. Identifica cómo el segundo lenguaje representa ausencia, error, mutabilidad y módulos. Conserva fixtures y resultados públicos para detectar una diferencia semántica.

## Ejemplo

Caso medido en la sección «La semántica cambia aunque la sintaxis se parezca» de [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md):

Transferir una solución a otro lenguaje no es traducir sintaxis. Seis diferencias concretas separan Python de Rust. Con enteros negativos, Python midió `-7 // 2 = -4` y `-7 % 2 = 1` (cociente hacia menos infinito, resto con el signo del divisor); según la documentación de Rust, `-7 / 2` es `-3` y `-7 % 2` es `-1` (cociente truncado hacia cero). Con enteros grandes, Python permite `2**63 = 9223372036854775808` porque su `int` crece; en Rust, `i64` tiene rango fijo y el desbordamiento provoca un pánico en compilaciones de depuración y una envoltura en las de release.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **el puerto da un resultado distinto con números negativos** — causa: división y resto con semántica distinta. Corrección: casos compartidos con negativos y su valor esperado. ([SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md)) son: Estas definiciones describen el uso concreto en la CLI diagnóstica. Cuando Python permita varias conductas, el contrato del programa elige una y la hace visible con validación y pruebas. El taller no enseña Rust completo ni compara rendimiento con un microbenchmark. El proyecto final integra el recorrido en una CLI Python probada.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md), [Equivalencia funcional](../e/equivalencia-funcional.md), [Idiomático](../i/idiomatico.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (154 clases más lo mencionan; las que más):

[SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), [SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `unittest` documentation](https://docs.python.org/3/library/unittest.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — documenta ownership, tipos de error, traits y concurrencia usados como contraste semántico.

---

[↑ Glosario](../../README.md) · [← Sellado](./sellado.md) · [Semántica antes que sintaxis →](./semantica-antes-que-sintaxis.md)
