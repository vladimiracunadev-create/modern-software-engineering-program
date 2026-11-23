# Algoritmo

[↑ Glosario](../../README.md) · [← Alertas por consumo](./alertas-por-consumo.md) · [Alias →](./alias.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Procedimiento finito y no ambiguo para un problema.

Definición de trabajo de [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md).

## Por qué importa

La clase donde se define, [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), existe con este propósito: la clase existe para separar corrección parcial, terminación y adecuación del algoritmo al contrato.

## Cómo funciona

Según [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md):

El problema define entradas válidas y salidas aceptables; una instancia es un caso concreto; el algoritmo es un procedimiento finito y no ambiguo. Un programa incorpora representación, errores y recursos. Confundirlos hace que una limitación de implementación parezca imposibilidad del problema.

Según [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md):

Verifica el borde de terminación con una variante defectuosa del algoritmo de Euclides: usa `a % b` sin intercambiar, de modo que `b` no decrece, y ejecútalo con un tope de 100 pasos. **Síntoma:** la ejecución alcanza el tope. **Hipótesis:** la medida no decrece. **Prueba:** imprime `a` y `b` en cada paso. **Conclusión:** el invariante gcd se conserva, pero sin medida decreciente no hay terminación; corregir el intercambio la restaura. Guarda el par de entradas, el tope y la corrección en `checks.md`. Además, compara tu burbuja con `sorted` en 200 casos y añade tres casos deliberados (vacío, duplicados, ya ordenado).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md):

El planificador del modelo de decisión diagnóstica selecciona el nodo autorizado de menor costo entre candidatos. El argumento prueba que nunca retorna fuera del conjunto elegible y que elimina un candidato por paso. Las pruebas cubren empate, vacío, costo límite y datos inválidos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El algoritmo «funciona» pero a veces no termina** — causa: falta una medida decreciente. Corrección: identificar la medida o imponer un tope. ([SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El problema define entradas válidas y salidas aceptables; una instancia es un caso concreto; el algoritmo es un procedimiento finito y no ambiguo. ([SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Problemas](../p/problemas.md), [Corrección parcial](../c/correccion-parcial.md), [Corrección total](../c/correccion-total.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Terminación](../t/terminacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (116 clases más lo mencionan; las que más):

[SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), [SE-089](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), [SE-056](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Alertas por consumo](./alertas-por-consumo.md) · [Alias →](./alias.md)
