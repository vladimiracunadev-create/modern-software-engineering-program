# Falsable

[↑ Glosario](../../README.md) · [← Falsa denegación](./falsa-denegacion.md) · [Falso negativo →](./falso-negativo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Capaz de resultar incompatible con una observación.

Definición de trabajo de [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md).

## Por qué importa

La clase donde se define, [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md), existe con este propósito: la clase existe para resolver problemas registrando hipótesis rivales y observaciones que realmente las discriminan.

## Cómo funciona

Según [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md):

Una hipótesis propone un mecanismo que predice señales. Debe poder perder: «algo de red» no es falsable; «el resolver excede 500 ms y domina el total» predice tiempos y un resultado bajo override. Se mantienen alternativas para evitar anclaje.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md):

El modelo de decisión diagnóstica genera un registro append-only y no sobreescribe la primera interpretación. Cuando cambia una hipótesis, enlaza la evidencia. El informe final muestra la primera divergencia y alternativas descartadas, evitando una historia retrospectiva perfecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md)) son:

- **La bisección señala un cambio inocente** — causa: prueba intermitente. Corrección: estabilizar la prueba o repetirla según la fórmula.
- **«Ya no falla» tras tres corridas** — causa: pocas repeticiones. Corrección: calcular el mínimo con la probabilidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md)) son: Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada. El método reduce sesgos, no garantiza acceso a toda evidencia ni elimina incertidumbre. El taller siguiente lo aplica a un problema deliberadamente ambiguo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Observación](../o/observacion.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Guardrail](../g/guardrail.md), [Hipótesis](../h/hipotesis.md), [Primera divergencia](../p/primera-divergencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.

---

[↑ Glosario](../../README.md) · [← Falsa denegación](./falsa-denegacion.md) · [Falso negativo →](./falso-negativo.md)
