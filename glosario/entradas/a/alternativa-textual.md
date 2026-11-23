# Alternativa textual

[↑ Glosario](../../README.md) · [← ALPN](./alpn.md) · [Alternativas existentes →](./alternativas-existentes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Descripción en texto de lo esencial de un diagrama, disponible para quien no lo ve.

Definición de trabajo de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md).

## Por qué importa

En [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), el tema «Vigencia y accesibilidad» importa porque un diagrama que no se compara con el código miente, y uno sin alternativa textual excluye.

## Cómo funciona

Según [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md):

Un diagrama afirma que dos cosas se relacionan; esa afirmación puede contrastarse con el código. Comparar un diagrama de dependencias con las importaciones reales convierte «creo que está al día» en una lista de diferencias. Y un diagrama es información que debe llegar a quien no lo ve: los lineamientos de accesibilidad piden una alternativa textual que transmita lo esencial, y para imágenes complejas, una descripción más larga junto a la figura. El texto alternativo no repite las cajas; dice qué relación importa.

Según [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md):

El portal de la plataforma de entregas guarda un archivo `modelo.json` con servicios y dependencias, un generador que emite tres diagramas (contexto, contenedores y componentes del servicio de cálculo) y un comprobador que compara las aristas con las importaciones del paquete en cada pull request. Cada diagrama lleva una frase «responde a…» y una alternativa textual de tres líneas. Cuando alguien añade la importación de notas, el comprobador falla con «falta la arista servicio → importador en el modelo», y el cambio del modelo regenera los diagramas con un diff mínimo.

## Ejemplo

Ejemplo de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) (sección «Ejemplo profesional»):

El portal de la plataforma de entregas guarda un archivo `modelo.json` con servicios y dependencias, un generador que emite tres diagramas (contexto, contenedores y componentes del servicio de cálculo) y un comprobador que compara las aristas con las importaciones del paquete en cada pull request. Cada diagrama lleva una frase «responde a…» y una alternativa textual de tres líneas. Cuando alguien añade la importación de notas, el comprobador falla con «falta la arista servicio → importador en el modelo», y el cambio del modelo regenera los diagramas con un diff mínimo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Quien usa lector de pantalla no obtiene nada de la figura** — causa: no hay alternativa textual. Corrección: añadir una descripción de lo esencial y una larga si el diagrama es complejo. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y un diagrama es información que debe llegar a quien no lo ve: los lineamientos de accesibilidad piden una alternativa textual que transmita lo esencial, y para imágenes complejas, una descripción más larga junto a la figura. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Diagrama](../d/diagrama.md), [Cruce de aristas](../c/cruce-de-aristas.md), [Diagrama como código](../d/diagrama-como-codigo.md), [Nivel de abstracción](../n/nivel-de-abstraccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (67 clases más lo mencionan; las que más):

[SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md).

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

[↑ Glosario](../../README.md) · [← ALPN](./alpn.md) · [Alternativas existentes →](./alternativas-existentes.md)
