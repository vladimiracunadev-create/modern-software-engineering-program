# Kappa de Cohen

[↑ Glosario](../../README.md) · [← K-anonimato](./k-anonimato.md) · [Kappa ponderado →](./kappa-ponderado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

El **kappa de Cohen** (κ) es un estadístico que mide el acuerdo entre dos evaluadores que clasifican los mismos elementos, descontando el acuerdo que se esperaría por puro azar. El programa lo usa en [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (clasificación de solicitudes de cambio), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) (severidad de incidentes) y [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) (clasificación de cambios de mantenimiento).

## Por qué importa

El porcentaje de coincidencias crudo engaña: si el 90 % de los incidentes son de severidad baja, dos personas que pusieran «baja» siempre coincidirían el 90 % de las veces sin mirar nada. El kappa descuenta ese acuerdo de fondo y responde la pregunta útil: ¿el criterio de clasificación produce acuerdo por encima del azar? Cambia la decisión de si un criterio (por ejemplo, una escala de severidad) está lo bastante claro como para usarse.

## Cómo funciona

Se calcula como κ = (p₀ − pₑ) / (1 − pₑ), donde p₀ es la proporción observada de acuerdo y pₑ la proporción de acuerdo esperada por azar a partir de cómo reparte cada evaluador sus etiquetas. Un valor de 1 es acuerdo perfecto; 0, acuerdo igual al del azar; negativo, peor que el azar.

[SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) lo usa en una simulación: genera un impacto latente para 400 incidentes, asigna una severidad verdadera con tres umbrales y hace que tres personas perciban el impacto con un error multiplicativo (σ = 0,9, 0,35 y 0,15 en escala logarítmica según el criterio sea vago, numérico o numérico con un ejemplo por nivel). Calcula el kappa entre pares, el acuerdo con la severidad verdadera y los errores de dos o más niveles. El mecanismo que muestra: un criterio más preciso reduce el ruido de percepción y sube el kappa.

[SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) aporta la lectura de un kappa bajo: «ajustar el cálculo del promedio» puede ser corrección, mejora o adaptación, y el texto no decide, sino la intención y el contexto. El desacuerdo no es un defecto del procedimiento sino información: las solicitudes en las que dos revisoras discrepan son las que necesitan una conversación con quien pidió el cambio.

## Ejemplo

Dos personas clasifican diez incidentes como leve o grave. Coinciden en 8 (p₀ = 0,8). Si cada una puso «leve» en 7 de 10, el acuerdo esperado por azar es 0,7 × 0,7 + 0,3 × 0,3 = 0,58. Entonces κ = (0,8 − 0,58) / (1 − 0,58) ≈ 0,52: un acuerdo moderado, bastante menos impresionante que el 80 % crudo. (Cálculo propio de ilustración; [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) propone un ejercicio similar con predicción previa.)

## Errores y confusiones comunes

- **Reportar solo el porcentaje de acuerdo.**
- **Interpretar umbrales como reglas universales**: las escalas habituales de interpretación son convenciones, no leyes.
- **Usarlo con más de dos evaluadores o categorías ordenadas sin adaptar**: hay variantes (kappa ponderado, kappa de Fleiss).
- **Ignorar la prevalencia**: con categorías muy desbalanceadas el kappa puede ser bajo aun con alto acuerdo.

## Límites y cuándo no aplica

El kappa mide acuerdo, no corrección: dos personas pueden coincidir en un error. Depende de la distribución de las categorías, y con muestras pequeñas es inestable. En [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) los datos son simulados, de modo que muestran el mecanismo, no valores esperables en un equipo real. Para clasificaciones ordinales (severidad), un kappa ponderado respeta que «por dos niveles» es peor que «por uno».

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
