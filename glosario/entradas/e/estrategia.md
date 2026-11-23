# Estrategia

[↑ Glosario](../../README.md) · [← Estrangulamiento](./estrangulamiento.md) · [Estrategia de caché →](./estrategia-de-cache.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Forma de descomponer una afirmación en subafirmaciones.

Definición de trabajo de [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md).

## Por qué importa

En [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md), el tema «estrategia» importa porque ¿qué pasos producen el resultado?

## Cómo funciona

Según [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md):

**Cómo leer la figura.** Cada barra son las monedas que usa una estrategia para devolver 6. Mira primero que la codiciosa, coral, usa 3 monedas y la óptima solo 2: un contraejemplo basta para refutar su optimalidad. **Dónde deja de valer:** la programación dinámica es óptima pero cuesta tiempo y memoria proporcionales al monto; en problemas mayores la ventaja de la heurística es real y hay que decidir si el exceso es tolerable.

Según [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md):

El caso responde tres preguntas: qué se afirma («el *Horno de curado* es aceptablemente seguro para curar muestras en un laboratorio con operadores formados, sobre una mesa, a menos de 250 °C»), por qué se cree (estrategia de argumento: se argumenta por cada peligro identificado, que tiene un control verificado) y con qué evidencia (resultados de pruebas, análisis, revisiones). Lo que lo distingue de un informe es que cada eslabón es visible y desafiable: quien lee puede preguntar «¿y si falla el sensor?» y encontrar qué rama responde. La notación gráfica más usada es la de estructuración de metas (GSN), con nodos de meta, estrategia, solución (evidencia), contexto, supuesto y justificación.

## Ejemplo

Ejemplo de [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) (sección «Preguntas frecuentes»):

No. GSN es una notación entre varias; lo que importa es la estructura (afirmación, estrategia, evidencia, supuestos) y que sea revisable. Un argumento en texto estructurado o en una tabla puede ser igual de bueno si se mantiene trazable.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md)) son:

- **«Es óptimo» tras probar tres casos** — causa: muestra pequeña. Corrección: buscar contraejemplos en un dominio acotado.
- **Se reporta solo la media** — causa: se oculta el peor caso. Corrección: reportar media, peor y mejor observados.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El caso responde tres preguntas: qué se afirma («el *Horno de curado* es aceptablemente seguro para curar muestras en un laboratorio con operadores formados, sobre una mesa, a menos de 250 °C»), por qué se cree (estrategia de argumento: se argumenta por cada peligro identificado, que tiene un control verificado) y con qué evidencia (resultados de pruebas, análisis, revisiones). ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Afirmación](../a/afirmacion.md), [Abstracción](../a/abstraccion.md), [Cuantificador](../c/cuantificador.md), [Descomposición](../d/descomposicion.md), [Dominio](../d/dominio.md), [Implicación](../i/implicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (128 clases más lo mencionan; las que más):

[SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 18.404J — Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) — delimita computabilidad, complejidad y los límites de las soluciones algorítmicas.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Estrangulamiento](./estrangulamiento.md) · [Estrategia de caché →](./estrategia-de-cache.md)
