# Cadena de respuesta

[↑ Glosario](../../README.md) · [← Cadena de huellas](./cadena-de-huellas.md) · [Cadencia de actualización →](./cadencia-de-actualizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Secuencia de etapas (detección, llegada, diagnóstico, mitigación y verificación) cuya probabilidad conjunta es el producto de las de cada una.

Definición de trabajo de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

## Por qué importa

En [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), el tema «Cadena de respuesta» importa porque la respuesta completa es el producto de sus etapas.

## Cómo funciona

Según [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

Se ejecutan, en Windows 11 con CPython 3.12.9 y en Ubuntu bajo WSL2 con CPython 3.12.3, los tres experimentos de tiempo virtual del paquete (el validador, la cadena de respuesta y la carga de la guardia). Se serializa el resultado con claves ordenadas y UTF-8, se calcula su SHA-256 y se muestran los primeros 16 caracteres. Además se ejecutan sondas de plataforma.

## Ejemplo

Caso medido en la sección «La cadena de respuesta» de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

La respuesta a un incidente es una cadena de etapas, cada una de las cuales puede fallar: **detección** (la alerta salta), **llegada** (la página alcanza a una persona), **diagnóstico** (se identifica una causa o una mitigación), **mitigación** (la acción funciona) y **verificación** (se comprueba que el servicio se recuperó). La probabilidad de que toda la cadena funcione es el producto de las probabilidades, y es menor que la de la peor etapa: cinco etapas del 80 % al 95 % dan alrededor del 55 %.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son:

- **El validador da 0 problemas y el ejercicio falla** — causa: solo comprueba existencia y forma. Corrección: añadir coincidencias de significado verificables y mantener el ejercicio.
- **La huella cambia entre sistemas** — causa: codificación, orden o versión no declarados. Corrección: serializar con claves ordenadas y UTF-8, y declarar las versiones.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos de tiempo virtual con semillas fijas y sondas de plataforma reales en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3): las cifras de tiempo virtual fueron idénticas y las sondas difieren por diseño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Diagnóstico](../d/diagnostico.md), [Mitigación](../m/mitigacion.md), [Producto](../p/producto.md), [Secuencia](../s/secuencia.md), [Declaración de límites](../d/declaracion-de-limites.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

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

[↑ Glosario](../../README.md) · [← Cadena de huellas](./cadena-de-huellas.md) · [Cadencia de actualización →](./cadencia-de-actualizacion.md)
