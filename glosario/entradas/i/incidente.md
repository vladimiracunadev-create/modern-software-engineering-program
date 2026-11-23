# Incidente

[↑ Glosario](../../README.md) · [← Incertidumbre residual](./incertidumbre-residual.md) · [Inclusión →](./inclusion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Evento que degrada o amenaza el servicio y exige una respuesta coordinada.

Definición de trabajo de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md).

## Por qué importa

En [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), el tema «Medir tiempos» importa porque un promedio de pocos incidentes engaña.

## Cómo funciona

Según [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md):

Un **incidente** es un evento que degrada o amenaza el servicio de un modo que requiere una respuesta coordinada y no rutinaria. **Declararlo** pronto tiene un coste bajo (una persona avisa, se abre un canal) y es mucho más barato que declararlo tarde, cuando ya hay confusión. La **severidad** clasifica el impacto en niveles (por ejemplo, 1 a 4) y decide quién se involucra, con qué rapidez y con qué comunicación. Un criterio útil usa magnitudes observables: fracción de personas afectadas, funciones no disponibles, pérdida de datos, duración prevista. Una clasificación que dice «grave» o «moderado» depende de quien la lee; una que dice «más del 10 % de las entregas falla o hay pérdida de datos» se puede aplicar igual por dos personas.

Según [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo escribe el protocolo de incidentes de la API de entregas. Severidades: 1 (más del 10 % de las entregas falla o hay pérdida de datos), 2 (entre 1 % y 10 %), 3 (degradación sin pérdida visible), 4 (sin impacto externo). Las severidades 1 y 2 abren un canal propio con cuatro roles: comando, operaciones, comunicaciones y escriba, con suplentes asignados por rotación. Las comunicaciones publican en la página de estado una actualización inicial en 10 minutos y después cada 30, aunque no haya novedades, con el formato «qué sabemos, qué no, qué hacemos, próxima actualización».

## Ejemplo

Ejemplo de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el kappa de Cohen de dos personas que clasifican diez incidentes. Antes de ejecutarlo, predice el resultado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Veinte personas opinan y nadie decide** — causa: sin comandante ni roles. Corrección: asignar roles al declarar el incidente. ([SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md))
- **La media mejora y no se sabe si es real** — causa: pocos incidentes y variación por azar. Corrección: medianas, percentiles y rango esperado. ([SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **incidente** es un evento que degrada o amenaza el servicio de un modo que requiere una respuesta coordinada y no rutinaria. ([SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md))
- La transferencia está lograda cuando puedes decir qué incidente clasificaría distinto cada persona y cómo lo resolverías, no cuando existe una plantilla. ([SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Servicio](../s/servicio.md), [Cadencia de actualización](../c/cadencia-de-actualizacion.md), [Comandante del incidente](../c/comandante-del-incidente.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Severidad](../s/severidad.md).
- **Se confunde con:** Las siglas habituales (MTTD, MTTA, MTTR) resumen cada tramo con una media, que es un estadístico engañoso cuando la distribución tiene cola larga y muestra pequeña: unos pocos incidentes largos mueven la media y una buena racha se confunde con una mejora.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (175 clases más lo mencionan; las que más):

[SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/) — roles y gestión de incidentes; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/) — casos de respuesta y ensayo de roles; autoridad: Google, SRE Workbook.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — roles y comunicación; autoridad: documentación pública de PagerDuty.
- [Atlassian Incident Management Handbook](https://www.atlassian.com/incident-management/handbook) — ciclo de vida y comunicación; autoridad: documentación pública de Atlassian.
- [Cohen, «A coefficient of agreement for nominal scales»](https://doi.org/10.1177/001316446002000104) — kappa de Cohen; autoridad: Educational and Psychological Measurement, 1960.

---

[↑ Glosario](../../README.md) · [← Incertidumbre residual](./incertidumbre-residual.md) · [Inclusión →](./inclusion.md)
