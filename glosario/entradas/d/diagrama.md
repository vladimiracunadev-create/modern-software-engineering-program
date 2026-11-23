# Diagrama

[↑ Glosario](../../README.md) · [← Diagnóstico incorporado](./diagnostico-incorporado.md) · [Diagrama como código →](./diagrama-como-codigo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Representación visual de una parte del sistema que responde a una pregunta de una audiencia.

Definición de trabajo de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md).

## Por qué importa

En [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), el tema «Pregunta del diagrama» importa porque un diagrama sin pregunta intenta mostrarlo todo y no sirve para nada.

## Cómo funciona

Según [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md):

Un diagrama es útil cuando responde a una pregunta concreta de una audiencia concreta: «¿qué sistemas externos toca la plataforma?», «¿en qué orden se llaman estos servicios?», «¿qué módulos dependen de este?». Sin pregunta, el diagrama acumula elementos hasta que todo cabe y nada se distingue. La pregunta también marca lo que se deja fuera: un diagrama de contexto no dibuja módulos internos. Escribir la pregunta en el encabezado obliga a decidir antes de dibujar, y permite a quien revisa preguntarse si el diagrama la contesta.

Según [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md):

El portal de la plataforma de entregas guarda un archivo `modelo.json` con servicios y dependencias, un generador que emite tres diagramas (contexto, contenedores y componentes del servicio de cálculo) y un comprobador que compara las aristas con las importaciones del paquete en cada pull request. Cada diagrama lleva una frase «responde a…» y una alternativa textual de tres líneas. Cuando alguien añade la importación de notas, el comprobador falla con «falta la arista servicio → importador en el modelo», y el cambio del modelo regenera los diagramas con un diff mínimo.

## Ejemplo

Ejemplo de [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) (sección «Ejemplo mínimo»):

El fragmento genera un diagrama Mermaid ordenado desde un modelo. Antes de ejecutarlo, predice cuántas líneas tiene la salida.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El diagrama tiene cuarenta cajas y no se entiende** — causa: no tiene pregunta ni nivel. Corrección: escribir la pregunta, dividir por nivel y dejar fuera lo que no la contesta. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))
- **El diagrama muestra una dependencia retirada** — causa: se dibujó a mano y no se compara con el código. Corrección: generarlo del modelo y comparar con las importaciones. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))
- **Quien usa lector de pantalla no obtiene nada de la figura** — causa: no hay alternativa textual. Corrección: añadir una descripción de lo esencial y una larga si el diagrama es complejo. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin pregunta, el diagrama acumula elementos hasta que todo cabe y nada se distingue. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))
- **un diagrama con una dependencia que ya no existe**. ([SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Audiencia](../a/audiencia.md), [Representación](../r/representacion.md), [Alternativa textual](../a/alternativa-textual.md), [Cruce de aristas](../c/cruce-de-aristas.md), [Diagrama como código](./diagrama-como-codigo.md), [Nivel de abstracción](../n/nivel-de-abstraccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-209 — Diagramas, modelos y documentación visual](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (158 clases más lo mencionan; las que más):

[SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Modelo C4](https://c4model.com/) — niveles de abstracción de diagramas de arquitectura; autoridad: proyecto C4 model.
- [Mermaid: introducción](https://mermaid.js.org/intro/) — diagramas definidos en texto; autoridad: proyecto Mermaid.
- [W3C WAI: imágenes complejas](https://www.w3.org/WAI/tutorials/images/complex/) — alternativas textuales para diagramas; autoridad: W3C.
- [Moody, «The Physics of Notations» (IEEE TSE, 2009)](https://doi.org/10.1109/TSE.2009.67) — principios de diseño de notaciones visuales; autoridad: IEEE Transactions on Software Engineering.
- [Kruchten, «The 4+1 View Model of Architecture» (IEEE Software, 1995)](https://doi.org/10.1109/52.469759) — vistas de arquitectura unidas por escenarios; autoridad: IEEE Software.

---

[↑ Glosario](../../README.md) · [← Diagnóstico incorporado](./diagnostico-incorporado.md) · [Diagrama como código →](./diagrama-como-codigo.md)
