# Réplica asíncrona

[↑ Glosario](../../README.md) · [← Réplica](./replica.md) · [Réplica pequeña →](./replica-pequena.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Copia que se actualiza con retraso variable respecto de la original.

Definición de trabajo de [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Por qué importa

La clase donde se define, [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), existe con este propósito: la clase existe para que prepares lo que todavía no ha ocurrido: que fijes cuántos datos puedes perder (RPO) y cuánto puedes tardar en volver (RTO), que verifiques las copias restaurándolas en lugar de confiar en que el trabajo terminó sin error, que descubras el orden real de recuperación y sus dependencias circulares antes de necesitarlo y que ensayes el plan con ejercicios.

## Cómo funciona

Según [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md):

Una **copia de seguridad** es una instantánea periódica y separada: protege contra la pérdida y el borrado, pero su RPO es su intervalo, porque lo escrito después de la última copia se pierde. Una **réplica** mantiene una segunda instancia al día: protege contra la pérdida de una máquina o una región y reduce el RPO a su retraso, pero replica también el borrado, la corrupción y el error de migración. Una réplica asíncrona tiene un retraso variable que se dispara con la carga, y el RPO real es el peor retraso, no el habitual. Las dos se complementan: la réplica para el fallo de infraestructura, la copia para el error lógico.

Según [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo fija para la API de entregas un RPO de 15 minutos y un RTO de 2 horas, con una justificación: las instituciones pueden reprogramar un plazo si el servicio vuelve en dos horas, y 15 minutos de entregas se reenvían con un aviso. Para el RPO usa una réplica asíncrona con alerta si el retraso supera 2 minutos y copias cada hora enviadas a una cuenta distinta con borrado protegido. Cada noche una tarea restaura la última copia en un entorno aislado, cuenta las filas, lee todas las tablas, compara con la huella registrada y publica el resultado y el tiempo; si falla, genera una página (`SE-498`).

## Ejemplo

Ejemplo de [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo fija para la API de entregas un RPO de 15 minutos y un RTO de 2 horas, con una justificación: las instituciones pueden reprogramar un plazo si el servicio vuelve en dos horas, y 15 minutos de entregas se reenvían con un aviso. Para el RPO usa una réplica asíncrona con alerta si el retraso supera 2 minutos y copias cada hora enviadas a una cuenta distinta con borrado protegido.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)) son:

- **Se pierde más de lo previsto tras un borrado** — causa: la réplica copió el error y la copia es antigua. Corrección: copias separadas y un RPO diferenciado por tipo de fallo.
- **La copia no se puede restaurar** — causa: nunca se probó la restauración. Corrección: restauración periódica con consulta y alerta.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una réplica asíncrona tiene un retraso variable que se dispara con la carga, y el RPO real es el peor retraso, no el habitual. ([SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia circular](../d/dependencia-circular.md), [Ejercicio de recuperación](../e/ejercicio-de-recuperacion.md), [RPO (objetivo de punto de recuperación)](./rpo-objetivo-de-punto-de-recuperacion.md), [RTO (objetivo de tiempo de recuperación)](./rto-objetivo-de-tiempo-de-recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planes de contingencia, pruebas y ejercicios; autoridad: NIST.
- [AWS Well-Architected: objetivos de recuperación ante desastres](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html) — RTO y RPO; autoridad: documentación de AWS.
- [Google Cloud: guía de planificación de DR](https://cloud.google.com/architecture/dr-scenarios-planning-guide) — patrones de recuperación; autoridad: documentación de Google Cloud.
- [SQLite: API de copia en línea](https://www.sqlite.org/backup.html) — copia consistente de una base en uso; autoridad: documentación de SQLite.
- [SQLite: PRAGMA integrity_check](https://www.sqlite.org/pragma.html) — chequeo de integridad; autoridad: documentación de SQLite.

---

[↑ Glosario](../../README.md) · [← Réplica](./replica.md) · [Réplica pequeña →](./replica-pequena.md)
