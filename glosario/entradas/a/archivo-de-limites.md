# Archivo de límites

[↑ Glosario](../../README.md) · [← Archivo de instrucciones para agentes](./archivo-de-instrucciones-para-agentes.md) · [Archivo de relevo →](./archivo-de-relevo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Documento que lista lo que no se midió, lo que es supuesto y los entornos no probados.

Definición de trabajo de [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md).

## Por qué importa

La clase donde se define, [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), existe con este propósito: el proyecto existe para que entregues un servicio del que se pueda decir con evidencia qué garantiza, qué deja de garantizar cuando una dependencia falla o la carga lo supera, y qué ve la persona usuaria en cada caso.

## Cómo funciona

Según [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md):

Un paquete se compone de promesas y de evidencia de cada una. Una prueba ejecutable por promesa es el estándar; cuando no la hay, se declara. El **archivo de límites** lista lo que nadie midió: qué supuestos son del autor, qué entornos no se probaron, qué fallos no se inyectaron. Un validador de forma puede verificar que los campos existan y que los números cuadren a simple vista, pero no puede saber si una evidencia fue copiada de otro servicio, si una prueba se ejecutó alguna vez o si una garantía es físicamente posible. Eso lo ve una revisión cruzada por otra persona que intente romper el paquete.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md):

El equipo ensambla el paquete. `GARANTIAS.md` declara, por operación, la garantía con su condición (por ejemplo, «el acuse se emite tras confirmar en dos de tres réplicas; sin mayoría se rechaza con un error reintentable») y lo que no garantiza. `PRESUPUESTOS.md` reparte 800 ms entre tres llamadas con un máximo de un reintento de 150 ms solo en la primera, con un máximo de 700 ms comprobado por una prueba.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md)) son:

- **El servicio tarda más que el plazo sin que nadie falle** — causa: tiempos límite que se suman por capa. Corrección: presupuesto de tiempo comprobado con una prueba.
- **Un estudiante tiene acuse y no entrega** — causa: acuse emitido al encolar sin distinguir estados. Corrección: estados «recibida» y «guardada» en la garantía.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **archivo de límites** lista lo que nadie midió: qué supuestos son del autor, qué entornos no se probaron, qué fallos no se inyectaron. ([SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Entorno](../e/entorno.md), [Supuestos](../s/supuestos.md), [Escalera de degradación](../e/escalera-de-degradacion.md), [Garantía](../g/garantia.md), [Ley de Little](../l/ley-de-little.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: manejo de sobrecarga](https://sre.google/sre-book/handling-overload/) — descarte y prioridad; autoridad: Google.
- [AWS Builders' Library: load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) — rechazo de carga; autoridad: Amazon Web Services.
- [Little, «A proof for the queuing formula»](https://doi.org/10.1287/opre.9.3.383) — `L = λ · W`; autoridad: artículo original (1961).
- [Microsoft Azure: patrón de interruptor](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — protección de dependencias; autoridad: Microsoft.
- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) — estados del interruptor; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Archivo de instrucciones para agentes](./archivo-de-instrucciones-para-agentes.md) · [Archivo de relevo →](./archivo-de-relevo.md)
