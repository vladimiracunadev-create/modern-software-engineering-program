# Holgura

[↑ Glosario](../../README.md) · [← HMAC](./hmac.md) · [Hook →](./hook.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

La **holgura** tiene en el programa dos sentidos relacionados. En planificación ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md)) es el tiempo que un elemento o tarea puede retrasarse sin retrasar la entrega. En capacidad y resiliencia ([SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md)) es la capacidad no usada que permite absorber un aumento de carga. Ambos comparten la idea de margen disponible antes de que algo se degrade.

## Por qué importa

La holgura dice dónde un retraso o un exceso de carga se absorbe y dónde no. En un plan, indica qué elementos pueden esperar sin consecuencias. En una infraestructura, indica si perder una región o recibir un pico traslada el problema a las demás.

## Cómo funciona

**En planificación.** Dada una red de dependencias con duraciones, el camino crítico es la cadena más larga; los elementos fuera de él tienen holgura. [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) da un ejemplo mínimo: el camino crítico es B → C → D (3 + 2 + 1 = 6 días) y A tiene 1 día de holgura; si A se alarga a 4 días, A pasa a ser parte del camino crítico y la duración sube. La holgura de un elemento es la diferencia entre el camino crítico y el camino más largo que lo atraviesa. En un flujo de datos ([SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md)), las tareas que no están en el camino crítico pueden tardar más sin retrasar la entrega.

**En capacidad.** [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) la usa para el análisis de pérdida de regiones: cuando una región falla, su carga se traslada a las demás. Un experimento **difuso** reparte la falla sobre toda la capacidad (por ejemplo, 5 % de las peticiones recibe una lentitud extra) y el aumento de consumo lo absorbe la holgura normal; sirve para comprobar la lógica de una alternativa, no el comportamiento a escala. La evacuación completa de una región exige que las demás tengan holgura suficiente: con R regiones a utilización u, perder una eleva la utilización de las restantes a u·R/(R−1). Si el resultado supera la capacidad, la evacuación colapsa a las demás.

La causa del colapso es calcular la holgura con la capacidad **nominal** y no la real; la corrección es calcular `u·R/(R−1)` y probarlo con tráfico antes. [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) pide además escribir las precondiciones de un experimento concentrado y comprobar cuáles no se cumplirían hoy.

## Ejemplo

Tres regiones a una utilización del 60 %. Al perder una, las dos restantes asumen su carga: 0,6 × 3 / 2 = 0,9, es decir 90 % de utilización; queda poca holgura para picos. Con cuatro regiones al 60 %, el resultado es 0,6 × 4 / 3 = 80 %. (Cálculo con la fórmula de [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md); los valores son de ejemplo.)

## Errores y confusiones comunes

- **La evacuación de una región colapsa a las demás**: holgura calculada con capacidad nominal; corrección: `u·R/(R−1)` y prueba con tráfico.
- **Confundir holgura con desperdicio**: es un margen que protege.
- **Asumir que un elemento con holgura puede alargarse sin límite.**
- **No recalcular tras cambios en la red.**

## Límites y cuándo no aplica

La holgura de planificación supone duraciones fijas; con duraciones inciertas, elementos con holgura pueden volverse críticos. La de capacidad depende de que la carga se redistribuya de forma pareja, lo que no siempre ocurre. Operar sin holgura abarata, pero reduce la tolerancia a fallos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Tarea](../t/tarea.md), [Atribución de costos](../a/atribucion-de-costos.md), [Bytes escaneados](../b/bytes-escaneados.md), [Camino crítico](../c/camino-critico.md), [Costo fijo por ejecución](../c/costo-fijo-por-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

**Aparece en los casos de estudio:** [Instagram](../../../casos/exito/instagram.md).

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

[↑ Glosario](../../README.md) · [← HMAC](./hmac.md) · [Hook →](./hook.md)
