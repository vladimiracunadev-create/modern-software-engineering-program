# Corte vertical

[↑ Glosario](../../README.md) · [← Corte mínimo](./corte-minimo.md) · [Cortocircuito →](./cortocircuito.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

El **corte vertical** es la división del trabajo en incrementos que atraviesan todas las capas del sistema (interfaz, lógica, datos) y entregan algo utilizable. Es el sentido de [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), que lo contrapone al **corte horizontal**: dividir por capas técnicas (primero la base de datos, luego el servicio, luego la pantalla). Es una forma de partir historias, no una técnica de arquitectura.

## Por qué importa

Cambia cuándo alguien puede ver valor y cuándo puede corregirse un error de requisito. Según [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), el corte vertical permite mostrar algo pronto, y por tanto descubrir antes que un requisito estaba mal. Con cortes horizontales, nada es utilizable hasta que todas las capas están listas, y la corrección llega cuando ya cuesta más.

## Cómo funciona

Una historia cortada en vertical toca varias capas a la vez, pero entrega una capacidad completa aunque mínima: por ejemplo, «subir una entrega» desde la pantalla hasta el almacenamiento, con solo el camino principal. La siguiente historia amplía: validación de tamaño, luego mensajes de error.

El costo, según la clase, es que cada historia toca varias capas a la vez y exige disciplina de diseño: hay que mantener los acoplamientos bajo control para que cada incremento no se convierta en una reforma general. El corte horizontal no es incorrecto en sí; es un riesgo cuando se usa como estrategia principal de entrega, porque posterga el momento en que se prueba el conjunto. Para decidir dónde cortar, [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) muestra que el mismo requisito puede contarse de tres formas (caso de uso, historia, *job story*), cada una para una pregunta distinta.

## Ejemplo

En el requisito conductor de [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) el primer incremento vertical podría ser el caso más simple de entrega: un archivo válido se sube y aparece en la lista del docente. Es poco, pero atraviesa pantalla, regla y almacenamiento y puede enseñarse a una persona real. Lo que queda (fronteras de tamaño, alternativas de error, extensiones) son los incrementos siguientes. La clase insiste en que las extensiones no son «detalles»: se enumeran por paso y se decide cuáles se prueban.

## Errores y confusiones comunes

- **Confundir vertical con pequeño.** Un incremento pequeño que solo toca una capa sigue siendo horizontal.
- **Cortar por capas y llamarlo avance.** Hay mucho trabajo hecho y nada utilizable.
- **El caso de uso solo describe el camino feliz.** Las extensiones se consideraron detalles; enumerar las alternativas por paso.
- **Todas las historias empiezan con «Como usuario».** No hay catálogo de actores; crearlo con objetivo y contacto.

## Límites y cuándo no aplica

Hay trabajo que no admite corte vertical inmediato, como una migración de infraestructura o la preparación de una plataforma común; ahí un corte horizontal puede ser razonable, siempre que se vea como riesgo acotado. [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) no midió ningún equipo ni comparó la comprensión de personas con cada forma de relato: sus conclusiones se apoyan en un caso sintético, no en evidencia empírica de productividad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](./capa.md), [Trabajo](../t/trabajo.md), [Actores y objetivos](../a/actores-y-objetivos.md), [Casos de uso](./casos-de-uso.md), [Historias de usuario](../h/historias-de-usuario.md), [Job stories](../j/job-stories.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Wake: INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/) — criterios de una buena historia; autoridad: autor del acrónimo.
- [Klement: Replacing the User Story with the Job Story](https://medium.com/@jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27) — propuesta de job stories; autoridad: autor de la propuesta.
- [GOV.UK Service Manual: Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories) — historias basadas en necesidades; autoridad: Government Digital Service.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — información sobre conceptos de operación y requisitos de las partes interesadas; autoridad: ISO, IEC e IEEE.
- [Python: `itertools`](https://docs.python.org/3/library/itertools.html) — herramientas de enumeración.

---

[↑ Glosario](../../README.md) · [← Corte mínimo](./corte-minimo.md) · [Cortocircuito →](./cortocircuito.md)
