# Declaración de límites

[↑ Glosario](../../README.md) · [← Declaración de conformidad](./declaracion-de-conformidad.md) · [Decorator →](./decorator.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Apartado que dice qué se probó, cómo y qué no se puede afirmar.

Definición de trabajo de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md): Lista de lo que no se verificó, con el motivo y lo que haría falta para verificarlo.

## Por qué importa

La clase donde se define, [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), existe con este propósito: el proyecto existe para que reúnas las piezas de la parte en un **paquete operativo** que otra persona pueda leer, validar y ejecutar: las preguntas y las señales que las responden, el objetivo de servicio y su presupuesto, las alertas derivadas, el runbook y la guardia, el protocolo de incidentes, la plantilla de postmortem, el plan de recuperación con una restauración verificada y un ejercicio con sus hallazgos.

## Cómo funciona

Según [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo construye el paquete `operacion-entregas/` en tres sesiones. Primero migra lo que existe: convierte el documento de runbooks a archivos con la estructura de `SE-499`, define el SLO con el SLI de `SE-497` y escribe la tabla de preguntas y señales (`SE-493`). Después deriva las alertas del SLO (`SE-498`), enlaza cada una con un runbook y un propietario, y escribe el validador, que en la primera ejecución encuentra cuatro alertas sin runbook y una copia sin restauración probada. Corrige las referencias, restaura la copia en un entorno aislado (38 minutos, con la lectura completa de las tablas y la huella) y registra el resultado.

Según [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md):

El paquete reúne las evidencias con enlaces y huellas, y una lista de lo que **no** se verificó con el motivo y lo que haría falta para verificarlo. Una persona que revisa debe poder ejecutar los comprobadores desde un checkout limpio, obtener las mismas cifras y encontrar la declaración de límites sin pedirla. Un paquete honesto dice «no se probó con un lector de pantalla concreto» y «no se ejecutó el service worker en un navegador»; uno que calla esas cosas parece más completo y es menos fiable.

## Ejemplo

Ejemplo de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo construye el paquete `operacion-entregas/` en tres sesiones. Primero migra lo que existe: convierte el documento de runbooks a archivos con la estructura de `SE-499`, define el SLO con el SLI de `SE-497` y escribe la tabla de preguntas y señales (`SE-493`). Después deriva las alertas del SLO (`SE-498`), enlaza cada una con un runbook y un propietario, y escribe el validador, que en la primera ejecución encuentra cuatro alertas sin runbook y una copia sin restauración probada.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son:

- **El validador da 0 problemas y el ejercicio falla** — causa: solo comprueba existencia y forma. Corrección: añadir coincidencias de significado verificables y mantener el ejercicio.
- **La huella cambia entre sistemas** — causa: codificación, orden o versión no declarados. Corrección: serializar con claves ordenadas y UTF-8, y declarar las versiones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una persona que revisa debe poder ejecutar los comprobadores desde un checkout limpio, obtener las mismas cifras y encontrar la declaración de límites sin pedirla. ([SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cadena de respuesta](../c/cadena-de-respuesta.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Huella](../h/huella.md), [Manifiesto de aplicación web](../m/manifiesto-de-aplicacion-web.md), [Paquete de evidencia](../p/paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

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

[↑ Glosario](../../README.md) · [← Declaración de conformidad](./declaracion-de-conformidad.md) · [Decorator →](./decorator.md)
