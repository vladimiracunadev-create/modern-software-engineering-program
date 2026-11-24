# Plataforma mínima

[↑ Glosario](../../README.md) · [← Plataforma interna](./plataforma-interna.md) · [Platform Engineer →](./platform-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Una **plataforma mínima** es el conjunto acotado de capacidades que una plataforma ofrece y puede sostener con evidencia comprobable ([SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md)). No es una plataforma pequeña: es la que ofrece solo lo que puede respaldar.

## Por qué importa

Una plataforma interna se mide por lo que los equipos pueden usar con confianza, no por lo que anuncia. Un catálogo largo y declarativo, con capacidades que nadie ha verificado, genera confianza falsa y deuda. La decisión que cambia es el criterio de ampliación: una capacidad solo se añade cuando existe el artefacto que la demuestra y alguien que lo revisó.

## Cómo funciona

[SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) ilustra con la plataforma de entregas, que ofrece cuatro capacidades, cada una atada a las clases que la construyen:

1. Un **entorno aislado y con identidad mínima**.
2. Su **descripción declarativa**, con estado y política de cambios.
3. Un **camino de creación con verificador**.
4. Un **ciclo de vida** con presupuesto, caducidad y prueba de destrucción.

Cada capacidad nombra el artefacto que la respalda y quién lo revisó. La regla es lo que no está respaldado no se ofrece: es mejor un catálogo corto y comprobable que uno largo y declarativo.

La causa de la regla es la confianza. Quien consume la plataforma toma decisiones basándose en lo que esta dice ofrecer; cada capacidad sin evidencia es una promesa que puede incumplirse en el peor momento. La evidencia tiene fecha: la clase advierte que un validador que solo comprueba la forma puede aprobar un paquete con evidencia vieja, por lo que añade revisión por otra persona y una fecha máxima de antigüedad. Y la evidencia debe ser reproducible: si la suma de verificación de un artefacto cambia entre máquinas, hay marcas de tiempo, orden o campos del sistema en el archivo; se normalizan y se compara en dos sistemas.

## Ejemplo

El equipo quiere anunciar «backups automáticos» como capacidad. No hay prueba de restauración reciente. Según el criterio de la clase, la capacidad no se ofrece hasta tener el artefacto (una restauración probada, con fecha y revisor). Mientras tanto el catálogo muestra cuatro capacidades respaldadas, no cinco con una sin respaldo. Aplicación del criterio de [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md).

## Errores y confusiones comunes

- **La suma cambia entre máquinas**: marcas de tiempo, orden o campos del sistema en el archivo; se normaliza y se compara en dos sistemas.
- **El validador aprueba un paquete con evidencia vieja**: solo comprueba la forma; se corrige con revisión por otra persona y fecha máxima de antigüedad.
- **Confundir mínima con pobre**: mínima es lo sostenible, no lo escaso.
- **Declarar capacidades sin artefacto**.

## Límites y cuándo no aplica

El criterio no dice cuántas capacidades debe tener una plataforma: eso depende de la organización. Una plataforma mínima puede no cubrir necesidades legítimas, que los equipos resolverán por su cuenta con el costo que eso implica; la clase prefiere eso a prometer lo que no puede sostenerse. Y la evidencia es de un momento: requiere renovarse, o la capacidad vuelve a quedar sin respaldo.

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
