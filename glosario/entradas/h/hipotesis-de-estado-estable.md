# Hipótesis de estado estable

[↑ Glosario](../../README.md) · [← Hipótesis](./hipotesis.md) · [Hipótesis de ruptura →](./hipotesis-de-ruptura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

La **hipótesis de estado estable** es una afirmación comprobable, con umbral, sobre el comportamiento normal del sistema, que un experimento de presión o de caos busca refutar. [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) la define así: por ejemplo, «el p95 de latencia por ventana de diez segundos es menor de X y la tasa de errores menor de Y». Es el punto de partida de la ingeniería del caos: sin una definición de «normal» medible, no hay forma de saber si el fallo inyectado cambió algo.

## Por qué importa

Convierte un experimento en un resultado interpretable. Sin hipótesis, «tiramos un servidor y parecía funcionar» es una impresión. Con ella, el experimento se aprueba o se refuta con datos, y la decisión de qué hacer con el sistema (confiar, corregir, volver a probar) tiene base. Además la hipótesis fuerza a elegir qué señales importan al usuario, y no solo las que son fáciles de medir.

## Cómo funciona

La hipótesis se expresa con **señales observables** (latencia p95, tasa de errores, fracción de peticiones correctas) y **umbrales**. El experimento introduce un fallo y comprueba si la hipótesis se sostiene; si no, se encontró una debilidad.

El umbral importa más de lo que parece ([SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md)):

- Uno tomado del **máximo de una sola ejecución base** falla solo con frecuencia: da falsas alarmas.
- Uno demasiado **holgado** no detecta fallos sutiles.

Por eso se mide el **ruido de base** con varias ejecuciones y se verifica con una **prueba A/A** (comparar el sistema contra sí mismo) que el umbral no se supera cuando no pasa nada. La causa es estadística: la métrica ya varía sin fallo, y el umbral debe separarse de esa variación natural.

## Ejemplo

[SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) trabaja con la API de entregas en tiempo virtual y semillas fijas. Se miden varias ejecuciones sin fallo para conocer el ruido del p95 por ventana de diez segundos. El umbral se fija con ese ruido, no con el máximo de una ejecución; se comprueba con A/A que no salta sin fallo; luego se inyecta el fallo y se comprueba si el p95 y la tasa de errores se mantienen dentro del umbral. Un resultado que supera el umbral refuta la hipótesis: hay un hallazgo. Uno que no lo supera solo confirma la hipótesis *para ese fallo y ese radio de impacto*.

## Errores y confusiones comunes

- **El experimento aborta sin fallo.** Umbral demasiado estrecho; fijarlo con varias ejecuciones base y una prueba A/A ([SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md)).
- **No se ve un fallo sutil.** Umbral holgado o radio demasiado pequeño; calcular la detección y ajustar.
- **Hipótesis vagas** («el sistema sigue funcionando»). No se pueden refutar; deben incluir señal, umbral y ventana.
- **Confundirla con un SLO.** Un SLO es un compromiso de servicio; la hipótesis es una afirmación de prueba, aunque puede apoyarse en los mismos indicadores.

## Límites y cuándo no aplica

Los experimentos de [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) son en tiempo virtual y con semillas fijas, no en producción; sus resultados ilustran el método. Una hipótesis confirmada no demuestra resiliencia general, solo ante la falla probada. Requiere buena observabilidad: si las señales no existen o no son fiables, no puede formularse. Y no aplica a sistemas cuyo comportamiento normal no es estable (cargas muy estacionales sin modelo de la variación), donde primero hay que caracterizar el ruido.

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
