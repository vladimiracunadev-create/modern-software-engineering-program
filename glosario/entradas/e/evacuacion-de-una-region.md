# Evacuación de una región

[↑ Glosario](../../README.md) · [← ETL](./etl.md) · [Evaluación →](./evaluacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Desviar todo el tráfico de una región a las demás, como ejercicio o como respuesta a una falla.

Definición de trabajo de [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Por qué importa

La clase donde se define, [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), existe con este propósito: esta clase es un taller: se ejecuta, en simulación, un experimento de caos acotado con grupo de control y criterio de aborto, que es el paso previo a cualquiera en producción.

## Cómo funciona

Según [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe el plan de su primer experimento en producción: «con 2 % del tráfico dirigido a un clúster experimental de la API de entregas, una lentitud de 300 ms en el 100 % de sus llamadas al almacenamiento durante 20 minutos no cambia, en comparación con el clúster de control, la proporción de entregas aceptadas en menos de 400 ms más de 1,5 puntos». Antes verifica las ocho precondiciones; el aborto detiene el experimento si el clúster experimental baja de 90 % durante 10 s; la reversión es devolver ese tráfico a la flota; la ventana es un martes a las 11:00, fuera de cierres.

## Ejemplo

Ejemplo de [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético y no como medición, que el equipo escribe el plan de su primer experimento en producción: «con 2 % del tráfico dirigido a un clúster experimental de la API de entregas, una lentitud de 300 ms en el 100 % de sus llamadas al almacenamiento durante 20 minutos no cambia, en comparación con el clúster de control, la proporción de entregas aceptadas en menos de 400 ms más de 1,5 puntos».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La evacuación de una región colapsa a las demás** — causa: holgura calculada con la capacidad nominal y no la real. Corrección: calcular `u·R/(R−1)` y probarlo con tráfico antes. ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron dos experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Región](../r/region.md), [Experimento concentrado](./experimento-concentrado.md), [Experimento difuso](./experimento-difuso.md), [Grupo de control](../g/grupo-de-control.md), [Holgura](../h/holgura.md), [Interruptor del experimento](../i/interruptor-del-experimento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: Chaos Engineering Upgraded](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15fa) — Chaos Kong, evacuación de región y formalización de la disciplina; autoridad: blog de ingeniería de Netflix.
- [Netflix: ChAP: Chaos Automation Platform](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — experimentos difusos y concentrados, control y experimento, interruptor; autoridad: blog de ingeniería de Netflix.
- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — Chaos Monkey y Chaos Gorilla; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — experimentar en producción y minimizar el radio; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — pérdida de capacidad y sobrecarga en cascada; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← ETL](./etl.md) · [Evaluación →](./evaluacion.md)
