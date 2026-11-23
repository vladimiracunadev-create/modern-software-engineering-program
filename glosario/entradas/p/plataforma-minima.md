# Plataforma mínima

[↑ Glosario](../../README.md) · [← Plataforma interna](./plataforma-interna.md) · [Platform Engineer →](./platform-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Conjunto acotado de capacidades que una plataforma ofrece y puede sostener con evidencia comprobable.

Definición de trabajo de [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md).

## Por qué importa

En [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), el tema «Plataforma mínima» importa porque acota lo que se ofrece a lo que se puede sostener y comprobar.

## Cómo funciona

Según [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), en la sección «Plataforma mínima»:

Una plataforma mínima no es una plataforma pequeña sino la que ofrece solo lo que puede sostener con evidencia. Para la plataforma de entregas son cuatro capacidades: un entorno aislado y con identidad mínima (clases 350 y 353), su descripción declarativa con estado y política de cambios (354 y 355), un camino de creación con verificador (358) y un ciclo de vida con presupuesto, caducidad y prueba de destrucción (356 y 359). Cada capacidad nombra el artefacto que la respalda y quién lo revisó. Lo que no está respaldado no se ofrece: es mejor un catálogo corto y comprobable que uno largo y declarativo.

## Ejemplo

Ejemplo de [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma reúne en `plataforma-minima/` los artefactos de las once clases: la matriz de responsabilidades, el cuadro de fronteras, las peticiones y límites, la clasificación de piezas, el grafo de flujos y la política de permisos mínimos, el código declarativo con su política de estado, el mapa de cuentas, la política de capacidad, la estrategia de portabilidad, el camino dorado y el taller de entorno con su prueba de destrucción. Un manifiesto lista cada archivo con su suma y de qué clase proviene.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md)) son:

- **La suma cambia entre máquinas** — causa: marcas de tiempo, orden o campos del sistema en el archivo. Corrección: normalizar orden, fecha, permisos y sistema, y comparar en dos sistemas.
- **El validador aprueba un paquete con evidencia vieja** — causa: solo comprueba la forma. Corrección: revisión por otra persona y fecha máxima de antigüedad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una plataforma mínima no es una plataforma pequeña sino la que ofrece solo lo que puede sostener con evidencia. ([SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Conjunto](../c/conjunto.md), [Evidencia](../e/evidencia.md), [Plataforma](./plataforma.md), [Construcción reproducible](../c/construccion-reproducible.md), [Manifiesto](../m/manifiesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md).

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

[↑ Glosario](../../README.md) · [← Plataforma interna](./plataforma-interna.md) · [Platform Engineer →](./platform-engineer.md)
