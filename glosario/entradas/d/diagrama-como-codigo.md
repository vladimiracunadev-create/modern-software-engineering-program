# Diagrama como código

[↑ Glosario](../../README.md) · [← Diagrama](./diagrama.md) · [Diario de pasos →](./diario-de-pasos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Un **diagrama como código** es un diagrama definido en un texto del que se genera el dibujo, y que se versiona y revisa como cualquier código. Es el sentido de [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), que cita Mermaid como ejemplo de lenguaje. La fuente de verdad es el texto (o un modelo del que se genera); la imagen es un artefacto derivado.

## Por qué importa

Cambia el destino de un diagrama: de dibujo que nadie se atreve a tocar a artefacto que se revisa en un pull request, se compara con el anterior y se regenera. Si el texto es la fuente, el diagrama puede comprobarse contra el sistema y deja de envejecer en silencio.

## Cómo funciona

Un diagrama escrito en texto se revisa en un pull request y se compara con su versión anterior. Puede incluso generarse desde un modelo (por ejemplo, un archivo con servicios y dependencias). Eso crea un problema nuevo que [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) señala: la salida generada debe ser **estable**. Si el generador recorre un conjunto en un orden que cambia entre ejecuciones, cada regeneración produce un diff aunque el modelo no haya cambiado y la revisión se llena de ruido. La regla es que el generador ordene todo lo que emite (nodos y aristas) y que el resultado sea una función determinista del modelo; en la comprobación se fija la semilla de hash.

Un segundo beneficio es la comprobación automática: se comparan las aristas del diagrama con las importaciones reales del paquete. Cuando divergen, falla la integración. Y un tercer requisito de calidad es independiente de la herramienta: todo diagrama necesita una pregunta que responde y un nivel de detalle; si no, tiene cuarenta cajas y no se entiende.

## Ejemplo

El portal de la plataforma de entregas guarda `modelo.json` con servicios y dependencias, un generador que emite tres diagramas (contexto, contenedores y componentes del servicio de cálculo) y un comprobador que compara las aristas con las importaciones del paquete en cada pull request. Cada diagrama lleva una frase «responde a…» y una alternativa textual de tres líneas.

## Errores y confusiones comunes

- **El diagrama tiene cuarenta cajas.** No tiene pregunta ni nivel; escribir la pregunta, dividir por nivel y dejar fuera lo que no la contesta.
- **Cada regeneración produce un diff enorme.** El generador no ordena su salida; ordenar nodos y aristas.
- **Creer que texto implica verdad.** Si nadie lo compara con el código, también puede divergir.
- **Olvidar la alternativa textual.** El dibujo no es accesible para todas las personas.

## Límites y cuándo no aplica

Los diagramas muy visuales o de disposición fina (diseños de interfaz, esquemas con composición manual) se expresan mal en texto. Los generadores automáticos pueden producir dibujos legibles para máquinas y confusos para personas. Las pruebas de [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) usan modelos sintéticos (un modelo de doce servicios y un paquete de diez módulos) y no evaluaron la comprensión de ningún lector.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Diagrama](./diagrama.md), [Alternativa textual](../a/alternativa-textual.md), [Cruce de aristas](../c/cruce-de-aristas.md), [Nivel de abstracción](../n/nivel-de-abstraccion.md).
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

[↑ Glosario](../../README.md) · [← Diagrama](./diagrama.md) · [Diario de pasos →](./diario-de-pasos.md)
