# Incidente

[↑ Glosario](../../README.md) · [← Incertidumbre residual](./incertidumbre-residual.md) · [Inclusión →](./inclusion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Un **incidente** es un evento que degrada o amenaza el servicio de un modo que requiere una respuesta coordinada y no rutinaria. Es la definición de [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md).

## Por qué importa

Distinguir un incidente de un fallo cotidiano decide cuándo se activa la maquinaria de respuesta (canal propio, roles, comunicación). [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) señala una asimetría: **declararlo** pronto tiene un costo bajo (una persona avisa, se abre un canal) y es mucho más barato que declararlo tarde, cuando ya hay confusión.

## Cómo funciona

La **severidad** clasifica el impacto en niveles (por ejemplo, 1 a 4) y decide quién se involucra, con qué rapidez y con qué comunicación. Un criterio útil usa magnitudes observables: fracción de personas afectadas, funciones no disponibles, pérdida de datos, duración prevista. «Grave» o «moderado» dependen de quien lo lee; «más del 10 % de las entregas falla o hay pérdida de datos» se aplica igual por dos personas. Los incidentes graves abren un canal con roles definidos y comunicación periódica.

## Ejemplo

[SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) (caso hipotético, no medición): severidad 1 si más del 10 % de las entregas falla o hay pérdida de datos; 2 entre 1 % y 10 %; 3 degradación sin pérdida visible; 4 sin impacto externo. Las severidades 1 y 2 abren un canal con cuatro roles (comando, operaciones, comunicaciones, escriba) con suplentes por rotación; la página de estado publica una actualización a los 10 minutos y luego cada 30, aunque no haya novedades.

## Errores y confusiones comunes

- **Veinte personas opinan y nadie decide.** Sin comandante ni roles; asignarlos al declarar.
- **La media mejora y no se sabe si es real.** Pocos incidentes y variación por azar; usar medianas, percentiles y rango esperado.

## Límites y cuándo no aplica

Los umbrales de severidad son decisiones de cada organización; los de la clase son ilustrativos. No todo fallo merece un incidente: declararlos de más agota a las personas y desvaloriza el proceso. Tras el incidente sigue el postmortem sin culpa.

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
