# Kappa de Cohen

[↑ Glosario](../../README.md) · [← K-anonimato](./k-anonimato.md) · [Kappa ponderado →](./kappa-ponderado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Estadístico que mide el acuerdo entre dos evaluadores descontando el acuerdo esperado por azar.

Definición de trabajo de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md): Medida del acuerdo entre dos clasificadoras que descuenta el acuerdo esperado por azar.
- En [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md): Medida del acuerdo entre dos evaluadores corregida por el acuerdo esperado por azar.

## Por qué importa

La clase donde se define, [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), existe con este propósito: la clase existe para que coordines una respuesta en la que participan varias personas: quién decide, quién opera, quién comunica y quién escribe; cómo se declara y se clasifica un incidente; cada cuánto se informa y a quién; y cómo se miden los tiempos sin engañarse con un promedio.

## Cómo funciona

Según [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md):

Se genera un impacto latente (lognormal) para 400 incidentes y se asigna su severidad verdadera con tres umbrales. Tres personas perciben el impacto con un error multiplicativo (σ = 0,9, 0,35 y 0,15 en escala logarítmica según el criterio sea vago, numérico o numérico con un ejemplo por nivel) y clasifican. Se calcula el kappa de Cohen entre pares, el acuerdo con la severidad verdadera y los errores de dos o más niveles.

Según [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md):

«Ajustar el cálculo del promedio» puede ser una corrección (el cálculo está mal), una mejora (se quiere otro cálculo) o una adaptación (cambió la normativa). El texto no decide: decide la intención y el contexto. Un clasificador por palabras clave acierta lo que el vocabulario revela y falla en lo ambiguo, y dos personas razonables discrepan justo ahí. Esto no es un defecto del procedimiento sino información: las solicitudes en las que dos revisoras discrepan son las que necesitan una conversación con quien pidió el cambio, y una cartera con muchas solicitudes ambiguas dice que el equipo no sabe todavía qué le piden.

## Ejemplo

Ejemplo de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el kappa de Cohen de dos personas que clasifican diez incidentes. Antes de ejecutarlo, predice el resultado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)) son:

- **Veinte personas opinan y nadie decide** — causa: sin comandante ni roles. Corrección: asignar roles al declarar el incidente.
- **Quien arregla contesta preguntas** — causa: sin comunicaciones y sin cadencia. Corrección: rol de comunicaciones y actualizaciones periódicas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **kappa de Cohen** mide el acuerdo entre dos clasificadoras descontando el que habría por azar; un valor cercano a 0,7 se suele leer como acuerdo sustancial, pero el número agregado oculta que el acuerdo en las solicitudes ambiguas puede ser casi el del azar. ([SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evaluador](../e/evaluador.md), [Medida](../m/medida.md), [Cadencia de actualización](../c/cadencia-de-actualizacion.md), [Comandante del incidente](../c/comandante-del-incidente.md), [Declaración de conformidad](../d/declaracion-de-conformidad.md), [Incidente](../i/incidente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cohen, «A coefficient of agreement for nominal scales»](https://doi.org/10.1177/001316446002000104) — kappa de Cohen; autoridad: Educational and Psychological Measurement, 1960.
- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/) — roles y gestión de incidentes; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/) — casos de respuesta y ensayo de roles; autoridad: Google, SRE Workbook.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — roles y comunicación; autoridad: documentación pública de PagerDuty.
- [Atlassian Incident Management Handbook](https://www.atlassian.com/incident-management/handbook) — ciclo de vida y comunicación; autoridad: documentación pública de Atlassian.

---

[↑ Glosario](../../README.md) · [← K-anonimato](./k-anonimato.md) · [Kappa ponderado →](./kappa-ponderado.md)
