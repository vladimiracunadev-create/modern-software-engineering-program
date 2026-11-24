# Condición de aborto

[↑ Glosario](../../README.md) · [← Condición](./condicion.md) · [Condición de carrera →](./condicion-de-carrera.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Una **condición de aborto** es una regla evaluada de forma automática durante un experimento que, si se cumple, lo detiene y revierte la falla ([SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)). [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) la usa en el sentido de umbral de una métrica que detiene el experimento. Es el freno de seguridad de la ingeniería del caos.

## Por qué importa

Un experimento de falla inyectada puede salirse de lo previsto: el servicio puede degradarse más de lo esperado o la falla puede alcanzar a otro servicio. Sin freno automático, el daño depende de que una persona mire a tiempo. La decisión que cambia es que el experimento solo se autoriza cuando se sabe, antes de empezar, en qué punto se detiene solo.

## Cómo funciona

[SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) cita dos implementaciones reales. AWS FIS usa **condiciones de parada**: alarmas de CloudWatch construidas a partir del estado estable que detienen el experimento si el servicio alcanza un estado inaceptable; un experimento detenido no se puede reanudar. ChAP incorpora un interruptor propio que lo termina automáticamente si se supera un presupuesto de error predefinido.

La clase da tres rasgos que separan una condición útil de una decorativa. El primero: se evalúa sobre el **grupo experimental** y no sobre el tráfico global, porque un grupo del 1 % no mueve el global. Los otros los muestra una simulación: el experimento planeado inyecta 20 % de errores, pero a los 60 s la falla empeora a 100 %. Se comparan cuatro políticas (sin aborto; abortar si el global falla más de 1 % en 10 s; abortar si el grupo experimental falla más de 50 % en 10 s; abortar al acumular 300 peticiones dañadas) y se mide el daño en peticiones. Sin aborto, el daño crece de 104 a 11 444 peticiones del radio menor al mayor; con 2 % del tráfico, los abortos por umbral se disparan a los 65 s y limitan el daño a 34.

## Ejemplo

Un experimento inyecta latencia en el 1 % del tráfico. Su condición de aborto es una alarma sobre la tasa de errores del grupo experimental; si supera el 50 % durante 10 segundos, el experimento se detiene y la falla se revierte. Si la falla empeora por compartir un recurso con otro servicio, el freno actúa en segundos en lugar de esperar a una persona.

## Errores y confusiones comunes

- **El experimento «terminó» sin conclusión**: falta el estado estable o la condición de aborto; se definen antes y se registra el resultado ([SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md)).
- **Medir sobre el tráfico global**: un grupo pequeño no mueve el global y la condición nunca dispara.
- **Condición inalcanzable**: un umbral que nunca se cumple es decorativo; un linter de forma, como el de [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), lo comprueba.
- **Confiar solo en el aborto**: no sustituye acotar el alcance.

## Límites y cuándo no aplica

La condición reduce el daño pero no lo elimina: entre la causa y la detección hay una ventana, y el daño acumulado en esa ventana ya ocurrió. [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) permite experimentos en producción solo con alcance acotado, hipótesis medible, condición de aborto y ensayo previo en entornos de prueba. Las cifras de la simulación son del escenario construido en la clase; el valor del umbral y de la ventana depende de cada servicio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica](../m/metrica.md), [Regla](../r/regla.md), [Costo del experimento](./costo-del-experimento.md), [Especificación del experimento](../e/especificacion-del-experimento.md), [Estado estable](../e/estado-estable.md), [Exploración con semilla](../e/exploracion-con-semilla.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Condiciones de aborto».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — minimizar el radio de explosión; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Netflix: «ChAP: Chaos Automation Platform»](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — tamaño de experimento, control y experimento, interruptor del experimento; autoridad: blog de ingeniería de Netflix.
- [AWS FIS: stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) — condiciones de parada basadas en alarmas; autoridad: documentación de Amazon Web Services.
- [Chaos Mesh: Define the Scope of Chaos Experiments](https://chaos-mesh.org/docs/define-chaos-experiment-scope/) — selectores y radio de explosión; autoridad: documentación del proyecto Chaos Mesh.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Condición](./condicion.md) · [Condición de carrera →](./condicion-de-carrera.md)
