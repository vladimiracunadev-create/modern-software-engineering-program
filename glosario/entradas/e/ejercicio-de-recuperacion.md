# Ejercicio de recuperación

[↑ Glosario](../../README.md) · [← Ejercicio de mesa](./ejercicio-de-mesa.md) · [Ejercicio de runbook →](./ejercicio-de-runbook.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Prueba programada del plan de recuperación con alcance, criterios y registro de hallazgos.

Definición de trabajo de [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Por qué importa

La clase donde se define, [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), existe con este propósito: la clase existe para que prepares lo que todavía no ha ocurrido: que fijes cuántos datos puedes perder (RPO) y cuánto puedes tardar en volver (RTO), que verifiques las copias restaurándolas en lugar de confiar en que el trabajo terminó sin error, que descubras el orden real de recuperación y sus dependencias circulares antes de necesitarlo y que ensayes el plan con ejercicios.

## Cómo funciona

Según [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md):

Un **ejercicio de recuperación** prueba el plan con un alcance declarado. Hay tres niveles de realismo: el de **mesa** (el equipo recorre el plan hablando; encuentra huecos de proceso y de comunicación), el **simulacro técnico** (se ejecuta la restauración en un entorno aislado; mide tiempos y encuentra dependencias) y la **inyección de fallos en producción controlada** (se retira un componente real con un radio y un criterio de aborto, como en `SE-443`). Cada ejercicio tiene objetivos escritos antes, un registro de lo que ocurrió y una lista de hallazgos con propietario y fecha. El ritmo lo dan los cambios del sistema y el riesgo, pero lo habitual es una restauración verificada cada mes o trimestre y un simulacro completo cada seis meses o un año.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo fija para la API de entregas un RPO de 15 minutos y un RTO de 2 horas, con una justificación: las instituciones pueden reprogramar un plazo si el servicio vuelve en dos horas, y 15 minutos de entregas se reenvían con un aviso. Para el RPO usa una réplica asíncrona con alerta si el retraso supera 2 minutos y copias cada hora enviadas a una cuenta distinta con borrado protegido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)) son:

- **Se pierde más de lo previsto tras un borrado** — causa: la réplica copió el error y la copia es antigua. Corrección: copias separadas y un RPO diferenciado por tipo de fallo.
- **La copia no se puede restaurar** — causa: nunca se probó la restauración. Corrección: restauración periódica con consulta y alerta.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3): dos de tiempo virtual y semillas fijas con resultados idénticos, y una medición real de copias de una base SQLite con un daño inyectado por el autor, con detecciones idénticas y tiempos de reloj distintos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Hallazgo](../h/hallazgo.md), [Plan](../p/plan.md), [Recuperación](../r/recuperacion.md), [Dependencia circular](../d/dependencia-circular.md), [Réplica asíncrona](../r/replica-asincrona.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

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

[↑ Glosario](../../README.md) · [← Ejercicio de mesa](./ejercicio-de-mesa.md) · [Ejercicio de runbook →](./ejercicio-de-runbook.md)
