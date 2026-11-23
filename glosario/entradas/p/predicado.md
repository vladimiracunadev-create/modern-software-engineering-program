# Predicado

[↑ Glosario](../../README.md) · [← Precondición y postcondición](./precondicion-y-postcondicion.md) · [Predicción →](./prediccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Afirmación parametrizada.

Definición de trabajo de [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md).

## Por qué importa

La clase donde se define, [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md), existe con este propósito: la clase existe para usar lógica para comprobar validez de inferencias y hacer visibles supuestos.

## Cómo funciona

Según [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md):

Un predicado depende de variables: `responde(host, prueba)`. `para todo` exige cubrir el dominio declarado; `existe` se demuestra con un testigo. Pasar de «falló en un cliente» a «falla para todos» cambia el cuantificador sin evidencia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md):

Las reglas del modelo de decisión diagnóstica no disparan acciones destructivas. Una conclusión incluye las premisas usadas, su vigencia y nivel de evidencia. Si falta una premisa, propone una prueba; si dos reglas concluyen estados incompatibles, eleva el conflicto en lugar de escoger silenciosamente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md)) son:

- **Se concluye «si no resuelve, falla DNS»** — causa: se invirtió la implicación (recíproca). Corrección: usar la contrapositiva y buscar una prueba que separe causas.
- **Una regla «todas pasan» se cumple sin ejecutar nada** — causa: verdad vacía sobre un conjunto vacío. Corrección: comprobar que el conjunto no es vacío antes de afirmar.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md)) son: Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada. La lógica valida forma, no verdad de premisas ni causalidad. La siguiente clase modela dominios, asociaciones y rutas mediante conjuntos, relaciones, funciones y grafos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Afirmación](../a/afirmacion.md), [Cuantificador](../c/cuantificador.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Implicación](../i/implicacion.md), [Inferencia](../i/inferencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Precondición y postcondición](./precondicion-y-postcondicion.md) · [Predicción →](./prediccion.md)
