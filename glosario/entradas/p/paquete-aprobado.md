# Paquete aprobado

[↑ Glosario](../../README.md) · [← Paquete](./paquete.md) · [Paquete de aseguramiento →](./paquete-de-aseguramiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Paquete que pasó la validación y la revisión de otra persona, con fecha y con sus límites declarados.

Definición de trabajo de [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md).

## Por qué importa

La clase donde se define, [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), existe con este propósito: el proyecto existe para que entregues una plataforma mínima que otra persona pueda reconstruir, revisar y destruir sin pedirte contexto: un paquete con la descripción de la infraestructura, el plan, las políticas, el presupuesto, la prueba de destrucción y los límites.

## Cómo funciona

Según [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md):

El validador ve la forma y las coincidencias exactas y es ciego a lo que requiere interpretar, porque un paquete con una prueba de 2019 es tan completo y coherente en forma como uno con una de ayer. Un paquete aprobado por el validador solo está completo; su verdad la responde una persona. Los 16 de 16 describen estas reglas contra estos defectos, que escribí yo; no son una cobertura general.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md):

El equipo de la plataforma reúne en `plataforma-minima/` los artefactos de las once clases: la matriz de responsabilidades, el cuadro de fronteras, las peticiones y límites, la clasificación de piezas, el grafo de flujos y la política de permisos mínimos, el código declarativo con su política de estado, el mapa de cuentas, la política de capacidad, la estrategia de portabilidad, el camino dorado y el taller de entorno con su prueba de destrucción. Un manifiesto lista cada archivo con su suma y de qué clase proviene.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md)) son:

- **La suma cambia entre máquinas** — causa: marcas de tiempo, orden o campos del sistema en el archivo. Corrección: normalizar orden, fecha, permisos y sistema, y comparar en dos sistemas.
- **El validador aprueba un paquete con evidencia vieja** — causa: solo comprueba la forma. Corrección: revisión por otra persona y fecha máxima de antigüedad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un paquete aprobado por el validador solo está completo; su verdad la responde una persona. ([SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite declarado](../l/limite-declarado.md), [Límite](../l/limite.md), [Paquete](./paquete.md), [Revisión](../r/revision.md), [Construcción reproducible](../c/construccion-reproducible.md), [Manifiesto](../m/manifiesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds](https://reproducible-builds.org/docs/) — causas y prácticas de la construcción reproducible; autoridad: proyecto Reproducible Builds.
- [SLSA v1.0](https://slsa.dev/spec/v1.0/) — niveles de garantía sobre la producción de artefactos; autoridad: proyecto SLSA (OpenSSF).
- [NIST SP 800-218, SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.
- [Python: zipfile](https://docs.python.org/3/library/zipfile.html) — campos de cada entrada de un archivo ZIP; autoridad: documentación de Python.
- [FinOps Framework](https://www.finops.org/framework/) — presupuestos, asignación y operación del gasto; autoridad: FinOps Foundation.

---

[↑ Glosario](../../README.md) · [← Paquete](./paquete.md) · [Paquete de aseguramiento →](./paquete-de-aseguramiento.md)
