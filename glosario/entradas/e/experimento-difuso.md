# Experimento difuso

[↑ Glosario](../../README.md) · [← Experimento de demanda](./experimento-de-demanda.md) · [Experto en información →](./experto-en-informacion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Inyección repartida sobre toda la capacidad, absorbida por la holgura normal.

Definición de trabajo de [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Por qué importa

En [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), el tema «Experimentos difusos y concentrados» importa porque solo la concentración cruza los umbrales de saturación.

## Cómo funciona

Según [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Un experimento **difuso** reparte la falla sobre toda la capacidad: 5 % de las peticiones recibe una lentitud extra, y el aumento de consumo lo absorbe la holgura normal. Es útil para comprobar la corrección lógica de una alternativa y no para ver el comportamiento del sistema bajo falla a escala. Un experimento **concentrado** dirige una porción pequeña del tráfico a un grupo (un clúster de pocas instancias) y le aplica la falla a **todas** sus peticiones: el grupo cruza los umbrales críticos (hilos agotados, CPU de una alternativa costosa, cortacircuitos que se abren) mientras el resto del sistema no se entera.

Según [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Reproduce el fallo clásico de la clase: **confiar en un experimento difuso para validar la escala**. Aplica 5 % de lentitud de 300 ms al cliente B y declara resiliente al sistema; luego aplica 20 %.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe el plan de su primer experimento en producción: «con 2 % del tráfico dirigido a un clúster experimental de la API de entregas, una lentitud de 300 ms en el 100 % de sus llamadas al almacenamiento durante 20 minutos no cambia, en comparación con el clúster de control, la proporción de entregas aceptadas en menos de 400 ms más de 1,5 puntos».

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md)) son:

- **La evacuación de una región colapsa a las demás** — causa: holgura calculada con la capacidad nominal y no la real. Corrección: calcular `u·R/(R−1)` y probarlo con tráfico antes.
- **El experimento «pasa» y la falla real no** — causa: inyección difusa que no cruza el umbral. Corrección: concentrar la falla en un grupo pequeño.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- (c) el experimento difuso no cruzó el umbral de saturación. ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Holgura](../h/holgura.md), [Inyección](../i/inyeccion.md), [Sobre](../s/sobre.md), [Evacuación de una región](./evacuacion-de-una-region.md), [Experimento concentrado](./experimento-concentrado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: ChAP: Chaos Automation Platform](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — experimentos difusos y concentrados, control y experimento, interruptor; autoridad: blog de ingeniería de Netflix.
- [Netflix: Chaos Engineering Upgraded](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15fa) — Chaos Kong, evacuación de región y formalización de la disciplina; autoridad: blog de ingeniería de Netflix.
- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — Chaos Monkey y Chaos Gorilla; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — experimentar en producción y minimizar el radio; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — pérdida de capacidad y sobrecarga en cascada; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Experimento de demanda](./experimento-de-demanda.md) · [Experto en información →](./experto-en-informacion.md)
