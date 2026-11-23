# Validador de referencias

[↑ Glosario](../../README.md) · [← Validador de presencia](./validador-de-presencia.md) · [Validador de subida →](./validador-de-subida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Programa que comprueba que las piezas de un paquete se refieren entre sí de forma coherente y están al día.

Definición de trabajo de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

## Por qué importa

La clase donde se define, [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), existe con este propósito: el proyecto existe para que reúnas las piezas de la parte en un **paquete operativo** que otra persona pueda leer, validar y ejecutar: las preguntas y las señales que las responden, el objetivo de servicio y su presupuesto, las alertas derivadas, el runbook y la guardia, el protocolo de incidentes, la plantilla de postmortem, el plan de recuperación con una restauración verificada y un ejercicio con sus hallazgos.

## Cómo funciona

Según [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

**Cómo leer la figura.** Cada barra es un tipo de mutación de un paquete operativo (30 de cada una) y el tramo teal son las que el validador de referencias cruzadas detecta y el coral las que deja pasar. Detecta las siete que rompen una referencia y ninguna de las cinco que cambian el sentido sin romperla, como un objetivo laxo pero en rango, un RPO incoherente con la copia o runbooks intercambiados. **Dónde deja de valer:** el paquete base y los doce operadores son construcciones del autor y el validador se afinó con las mismas mutaciones que lo evalúan, de modo que 58 % es una cota optimista.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo construye el paquete `operacion-entregas/` en tres sesiones. Primero migra lo que existe: convierte el documento de runbooks a archivos con la estructura de `SE-499`, define el SLO con el SLI de `SE-497` y escribe la tabla de preguntas y señales (`SE-493`).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son:

- **El validador da 0 problemas y el ejercicio falla** — causa: solo comprueba existencia y forma. Corrección: añadir coincidencias de significado verificables y mantener el ejercicio.
- **La huella cambia entre sistemas** — causa: codificación, orden o versión no declarados. Corrección: serializar con claves ordenadas y UTF-8, y declarar las versiones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos de tiempo virtual con semillas fijas y sondas de plataforma reales en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3): las cifras de tiempo virtual fueron idénticas y las sondas difieren por diseño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Paquete](../p/paquete.md), [Cadena de respuesta](../c/cadena-de-respuesta.md), [Declaración de límites](../d/declaracion-de-limites.md), [Huella](../h/huella.md), [Paquete operativo](../p/paquete-operativo.md), [Reproducibilidad](../r/reproducibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md).

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

[↑ Glosario](../../README.md) · [← Validador de presencia](./validador-de-presencia.md) · [Validador de subida →](./validador-de-subida.md)
