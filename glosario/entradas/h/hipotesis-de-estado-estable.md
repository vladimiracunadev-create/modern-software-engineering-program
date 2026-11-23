# Hipótesis de estado estable

[↑ Glosario](../../README.md) · [← Hipótesis](./hipotesis.md) · [Hipótesis de ruptura →](./hipotesis-de-ruptura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Afirmación comprobable, con umbral, sobre el comportamiento normal del sistema que el experimento busca refutar.

Definición de trabajo de [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md).

## Por qué importa

En [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), el tema «Hipótesis de estado estable» importa porque sin ella no hay manera de decir si el resultado fue bueno.

## Cómo funciona

Según [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), en la sección «Hipótesis de estado estable»:

Un experimento de presión empieza con una afirmación comprobable sobre el sistema en funcionamiento normal: «el p95 de latencia por ventana de diez segundos es menor de X y la tasa de errores menor de Y». Esa afirmación es la **hipótesis de estado estable**, y el experimento busca refutarla bajo un fallo. El umbral importa más de lo que parece: uno tomado del máximo de una sola ejecución base falla sola con frecuencia (da falsas alarmas); uno demasiado holgado no detecta fallos sutiles. Por eso se mide el ruido de base con varias ejecuciones y se verifica con una prueba A/A que el umbral no se supera cuando no pasa nada.

## Ejemplo

Ejemplo de [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el umbral de una hipótesis de estado estable desde varias ejecuciones base. Antes de ejecutarlo, predice si el máximo de una ejecución coincide con el percentil 99,9 de treinta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md)) son:

- **El experimento aborta sin fallo** — causa: umbral demasiado estrecho. Corrección: fijarlo con varias ejecuciones base y una prueba A/A.
- **No se ve un fallo sutil** — causa: umbral holgado o radio demasiado pequeño. Corrección: calcular la detección y ajustar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó el experimento con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Sobre](../s/sobre.md), [Criterio de aborto](../c/criterio-de-aborto.md), [Día de práctica](../d/dia-de-practica.md), [Inyección de fallos](../i/inyeccion-de-fallos.md), [Radio de impacto](../r/radio-de-impacto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Basiri et al., «Chaos Engineering»](https://doi.org/10.1109/MS.2016.60) — experimentación sobre sistemas para ganar confianza; autoridad: IEEE Software, 2016.
- [Principios del caos](https://principlesofchaos.org/) — hipótesis, variación de eventos y radio mínimo; autoridad: comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas de estrés y de recuperación; autoridad: Google, libro de ingeniería de confiabilidad.
- [AWS Well-Architected: probar la fiabilidad](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html) — pruebas de fallo y días de simulacro; autoridad: Amazon Web Services.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de eventos del modelo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Hipótesis](./hipotesis.md) · [Hipótesis de ruptura →](./hipotesis-de-ruptura.md)
