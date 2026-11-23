# Experimento concentrado

[↑ Glosario](../../README.md) · [← Experimento A/A](./experimento-a-a.md) · [Experimento de aprendizaje →](./experimento-de-aprendizaje.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Inyección sobre un grupo pequeño al que se envía una porción del tráfico y en el que todas las peticiones sufren la falla.

Definición de trabajo de [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Por qué importa

La clase donde se define, [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), existe con este propósito: esta clase es un taller: se ejecuta, en simulación, un experimento de caos acotado con grupo de control y criterio de aborto, que es el paso previo a cualquiera en producción.

## Cómo funciona

Según [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Un experimento **difuso** reparte la falla sobre toda la capacidad: 5 % de las peticiones recibe una lentitud extra, y el aumento de consumo lo absorbe la holgura normal. Es útil para comprobar la corrección lógica de una alternativa y no para ver el comportamiento del sistema bajo falla a escala. Un experimento **concentrado** dirige una porción pequeña del tráfico a un grupo (un clúster de pocas instancias) y le aplica la falla a **todas** sus peticiones: el grupo cruza los umbrales críticos (hilos agotados, CPU de una alternativa costosa, cortacircuitos que se abren) mientras el resto del sistema no se entera.

Según [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** el experimento con 5 % de peticiones lentas confirma la hipótesis (100 % correctas) y en producción, con 20 % de peticiones lentas, el cliente cae a 0 %. **Hipótesis rivales:** (a) la inyección fue distinta; (b) el tráfico de producción es especial; (c) el experimento difuso no cruzó el umbral de saturación. **Prueba:** repite el experimento con 10 % y con 20 %; si el cliente se sostiene con 10 % y colapsa con 20 %, la hipótesis (c) explica la diferencia. **Conclusión:** existe un umbral que solo un experimento concentrado cruza.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe el plan de su primer experimento en producción: «con 2 % del tráfico dirigido a un clúster experimental de la API de entregas, una lentitud de 300 ms en el 100 % de sus llamadas al almacenamiento durante 20 minutos no cambia, en comparación con el clúster de control, la proporción de entregas aceptadas en menos de 400 ms más de 1,5 puntos».

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md)) son:

- **La evacuación de una región colapsa a las demás** — causa: holgura calculada con la capacidad nominal y no la real. Corrección: calcular `u·R/(R−1)` y probarlo con tráfico antes.
- **El experimento «pasa» y la falla real no** — causa: inyección difusa que no cruza el umbral. Corrección: concentrar la falla en un grupo pequeño.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un experimento **concentrado** dirige una porción pequeña del tráfico a un grupo (un clúster de pocas instancias) y le aplica la falla a **todas** sus peticiones: el grupo cruza los umbrales críticos (hilos agotados, CPU de una alternativa costosa, cortacircuitos que se abren) mientras el resto del sistema no se entera. ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Inyección](../i/inyeccion.md), [Sobre](../s/sobre.md), [Evacuación de una región](./evacuacion-de-una-region.md), [Experimento difuso](./experimento-difuso.md), [Grupo de control](../g/grupo-de-control.md), [Holgura](../h/holgura.md).
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

[↑ Glosario](../../README.md) · [← Experimento A/A](./experimento-a-a.md) · [Experimento de aprendizaje →](./experimento-de-aprendizaje.md)
