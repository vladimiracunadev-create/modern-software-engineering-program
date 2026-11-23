# Paquete operativo

[↑ Glosario](../../README.md) · [← Paquete operable](./paquete-operable.md) · [Paquete reproducible →](./paquete-reproducible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Conjunto versionado de documentos y datos que describen cómo se observa, se responde y se recupera un servicio.

Definición de trabajo de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

## Por qué importa

En [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), el tema «Paquete operativo» importa porque sin conexiones, las piezas no forman un sistema.

## Cómo funciona

Según [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

Un **paquete operativo** es el conjunto versionado de documentos y datos que describen cómo se observa, se responde y se recupera un servicio. Para la API de entregas contiene: los **servicios** y sus dependencias; la **tabla de preguntas y señales** (`SE-493`); el **SLI, el SLO y el presupuesto** con su política (`SE-497`); las **alertas** derivadas del consumo (`SE-498`); los **runbooks** con propietario y fecha de verificación (`SE-499`); la **guardia** y el escalamiento; el **protocolo de incidentes** con severidades medibles y la cadencia de comunicación (`SE-500`); la plantilla de **postmortem** y la lista de acciones (`SE-501`); el **plan de recuperación** con RPO, RTO, la última restauración verificada y el mapa de dependencias (`SE-502`); y el registro de los **ejercicios** con sus hallazgos.

## Ejemplo

Ejemplo de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) (sección «Caso conductor»):

La API de entregas fue el caso conductor de toda la [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md): de la tabla de preguntas (`SE-493`) a los registros (`SE-494`), las métricas (`SE-495`), las trazas (`SE-496`), el objetivo (`SE-497`), las alertas (`SE-498`), la guardia (`SE-499`), los incidentes (`SE-500`), los postmortems (`SE-501`), la recuperación (`SE-502`) y el diagnóstico (`SE-503`). Este proyecto deja el artefacto final: un paquete operativo validado, con su huella y su declaración de límites. La [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) abre otro frente, el mantenimiento y la modernización de sistemas existentes, donde lo operado debe cambiar sin romperse.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son:

- **El validador da 0 problemas y el ejercicio falla** — causa: solo comprueba existencia y forma. Corrección: añadir coincidencias de significado verificables y mantener el ejercicio.
- **La huella cambia entre sistemas** — causa: codificación, orden o versión no declarados. Corrección: serializar con claves ordenadas y UTF-8, y declarar las versiones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos de tiempo virtual con semillas fijas y sondas de plataforma reales en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3): las cifras de tiempo virtual fueron idénticas y las sondas difieren por diseño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Documento](../d/documento.md), [Servicio](../s/servicio.md), [Versionado](../v/versionado.md), [Cadena de respuesta](../c/cadena-de-respuesta.md), [Declaración de límites](../d/declaracion-de-limites.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) — documentación de SLI, SLO y política; autoridad: Google, SRE Workbook.
- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/) — roles y gestión de incidentes; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — postmortems sin culpa y seguimiento; autoridad: libro de ingeniería de confiabilidad de Google.
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planes de contingencia, pruebas y ejercicios; autoridad: NIST.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — funciones de huella; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Paquete operable](./paquete-operable.md) · [Paquete reproducible →](./paquete-reproducible.md)
