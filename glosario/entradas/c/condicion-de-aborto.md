# Condición de aborto

[↑ Glosario](../../README.md) · [← Condición](./condicion.md) · [Condición de carrera →](./condicion-de-carrera.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Regla automática que detiene el experimento y revierte la falla al cumplirse.

Definición de trabajo de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md): Umbral de una métrica que detiene el experimento.

## Por qué importa

En [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), el tema «Condiciones de aborto» importa porque la medida de aborto debe verse el daño que pretende limitar.

## Cómo funciona

Según [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), en la sección «Condiciones de aborto»:

Una **condición de aborto** es una regla evaluada de forma automática durante el experimento que, si se cumple, lo detiene y revierte la falla. AWS FIS la implementa como condiciones de parada: alarmas de CloudWatch construidas a partir del estado estable que detienen el experimento si el servicio alcanza un estado inaceptable, y aclara que un experimento detenido no se puede reanudar. ChAP incorpora un interruptor propio del experimento que lo termina automáticamente si se supera un presupuesto de error predefinido. Tres rasgos separan una condición útil de una decorativa. Se evalúa sobre el **grupo experimental** y no sobre el tráfico global, porque un grupo del 1 % no mueve el global.

Se pone a prueba con una sorpresa. El experimento planeado inyecta 20 % de errores, pero a los 60 s la falla empeora a 100 %, como ocurriría si la falla compartiera un recurso con otro servicio. Se comparan cuatro políticas: sin aborto; abortar si el servicio global falla más de 1 % en una ventana de 10 s; abortar si el grupo experimental falla más de 50 % en 10 s; y abortar al acumular 300 peticiones dañadas. Se mide el daño total en peticiones para cuatro radios.

**Cómo leer la figura.** Cada grupo de barras es un radio y cada barra una política; la escala es logarítmica. Sin aborto, el daño crece de 104 a 11 444 peticiones del radio menor al mayor. Con 2 % del tráfico, el aborto por el SLO global y el del grupo experimental se disparan a los 65 s (cinco segundos después del cambio) y limitan el daño a 34; el presupuesto de 300 peticiones se agota a los 240 s y deja pasar 305. Con 10 % y 50 %, el SLO global aborta a los 10 s, **antes de que la falla empeore**, porque el 20 % de errores esperado ya consume más del 1 % global: el experimento nunca habría llegado a ver lo que quería probar.

## Ejemplo

Ejemplo de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) (sección «Ejemplo mínimo»):

Imprime `54.0 1350.0`. El experimento con 2 % daña unas 54 peticiones; el de 50 %, 1 350. Registra versión de Python, comando y salida; luego decide a qué fracción el costo supera 300 peticiones y compáralo con la condición de aborto por presupuesto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El experimento «terminó» sin conclusión** — causa: falta el estado estable o la condición de aborto. Corrección: definirlos antes y registrar el resultado. ([SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un linter de forma comprueba que cada campo exista, que el alcance no sea el 100 % del tráfico, que la condición de aborto sea alcanzable y que la hipótesis contenga un umbral. ([SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md))
- Puede hacerse, pero solo con un alcance acotado, una hipótesis medible y una condición de aborto, y después de haber ensayado en entornos de prueba. ([SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md))

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
