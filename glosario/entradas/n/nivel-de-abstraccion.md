# Nivel de abstracción

[↑ Glosario](../../README.md) · [← NISQ](./nisq.md) · [Nivel de integridad →](./nivel-de-integridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Grado de detalle de un diagrama, desde el contexto del sistema hasta el código.

Definición de trabajo de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md).

## Por qué importa

En [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), el tema «Nivel de abstracción» importa porque contexto, contenedores, componentes y código son vistas distintas; mezclarlas confunde.

## Cómo funciona

Según [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), en la sección «Nivel de abstracción»:

Una función legible mantiene un nivel: coordinar fases o calcular una regla, no ambos. Mezclar `json.loads`, política de autorización y `print` obliga a saltar entre detalles. Extraer debe crear conceptos, no fragmentos arbitrarios.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md):

El portal de la plataforma de entregas guarda un archivo `modelo.json` con servicios y dependencias, un generador que emite tres diagramas (contexto, contenedores y componentes del servicio de cálculo) y un comprobador que compara las aristas con las importaciones del paquete en cada pull request. Cada diagrama lleva una frase «responde a…» y una alternativa textual de tres líneas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md)) son:

- **El diagrama tiene cuarenta cajas y no se entiende** — causa: no tiene pregunta ni nivel. Corrección: escribir la pregunta, dividir por nivel y dejar fuera lo que no la contesta.
- **Cada regeneración produce un diff enorme** — causa: el generador no ordena su salida. Corrección: ordenar nodos y aristas, y fijar la semilla de hash en la comprobación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `_partition_size` explica que mide el tamaño del grupo más grande; ambos mantienen un mismo nivel de abstracción en su cuerpo (no mezclan detalles de bajo nivel con decisiones de alto nivel). ([SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Diagrama](../d/diagrama.md), [Abstracción](../a/abstraccion.md), [Alternativa textual](../a/alternativa-textual.md), [Caracterización](../c/caracterizacion.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Moody, «The Physics of Notations» (IEEE TSE, 2009)](https://doi.org/10.1109/TSE.2009.67) — principios de diseño de notaciones visuales; autoridad: IEEE Transactions on Software Engineering.
- [Kruchten, «The 4+1 View Model of Architecture» (IEEE Software, 1995)](https://doi.org/10.1109/52.469759) — vistas de arquitectura unidas por escenarios; autoridad: IEEE Software.
- [Sugiyama, Tagawa y Toda, «Methods for Visual Understanding of Hierarchical System Structures» (IEEE Trans. SMC, 1981)](https://doi.org/10.1109/TSMC.1981.4308636) — ordenación por capas y reducción de cruces; autoridad: IEEE Transactions on Systems, Man, and Cybernetics.
- [Modelo C4](https://c4model.com/) — niveles de abstracción de diagramas de arquitectura; autoridad: proyecto C4 model.
- [Mermaid: introducción](https://mermaid.js.org/intro/) — diagramas definidos en texto; autoridad: proyecto Mermaid.

---

[↑ Glosario](../../README.md) · [← NISQ](./nisq.md) · [Nivel de integridad →](./nivel-de-integridad.md)
