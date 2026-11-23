# Cruce de aristas

[↑ Glosario](../../README.md) · [← Cronología y hechos](./cronologia-y-hechos.md) · [CTO / Dirección de Tecnología →](./cto-direccion-de-tecnologia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Par de líneas de un dibujo de grafo que se intersecan sin ser vecinas.

Definición de trabajo de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md).

## Por qué importa

La clase donde se define, [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), existe con este propósito: la clase existe para que decidas cuándo un diagrama enseña algo que un párrafo no puede, cómo evitar que se vuelva ilegible o mentiroso, y cómo mantenerlo de forma que su diferencia con el código se pueda ver.

## Cómo funciona

[SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md):

El portal de la plataforma de entregas guarda un archivo `modelo.json` con servicios y dependencias, un generador que emite tres diagramas (contexto, contenedores y componentes del servicio de cálculo) y un comprobador que compara las aristas con las importaciones del paquete en cada pull request. Cada diagrama lleva una frase «responde a…» y una alternativa textual de tres líneas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md)) son:

- **El diagrama tiene cuarenta cajas y no se entiende** — causa: no tiene pregunta ni nivel. Corrección: escribir la pregunta, dividir por nivel y dejar fuera lo que no la contesta.
- **Cada regeneración produce un diff enorme** — causa: el generador no ordena su salida. Corrección: ordenar nodos y aristas, y fijar la semilla de hash en la comprobación.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ningún diagrama real ni la comprensión de ningún lector: los grafos de capas, el modelo de doce servicios y el paquete de diez módulos son construcciones del autor, y el análisis de importaciones solo cubre una forma de importar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Grafo](../g/grafo.md), [Alternativa textual](../a/alternativa-textual.md), [Diagrama](../d/diagrama.md), [Diagrama como código](../d/diagrama-como-codigo.md), [Nivel de abstracción](../n/nivel-de-abstraccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

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

[↑ Glosario](../../README.md) · [← Cronología y hechos](./cronologia-y-hechos.md) · [CTO / Dirección de Tecnología →](./cto-direccion-de-tecnologia.md)
