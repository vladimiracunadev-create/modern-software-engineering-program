# RPO (objetivo de punto de recuperación)

[↑ Glosario](../../README.md) · [← RPN](./rpn.md) · [RRF →](./rrf.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Cantidad máxima de datos, medida en tiempo, que se acepta perder tras una recuperación.

Definición de trabajo de [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Por qué importa

La clase donde se define, [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), existe con este propósito: la clase existe para que prepares lo que todavía no ha ocurrido: que fijes cuántos datos puedes perder (RPO) y cuánto puedes tardar en volver (RTO), que verifiques las copias restaurándolas en lugar de confiar en que el trabajo terminó sin error, que descubras el orden real de recuperación y sus dependencias circulares antes de necesitarlo y que ensayes el plan con ejercicios.

## Cómo funciona

[SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo fija para la API de entregas un RPO de 15 minutos y un RTO de 2 horas, con una justificación: las instituciones pueden reprogramar un plazo si el servicio vuelve en dos horas, y 15 minutos de entregas se reenvían con un aviso. Para el RPO usa una réplica asíncrona con alerta si el retraso supera 2 minutos y copias cada hora enviadas a una cuenta distinta con borrado protegido.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)) son:

- **Se pierde más de lo previsto tras un borrado** — causa: la réplica copió el error y la copia es antigua. Corrección: copias separadas y un RPO diferenciado por tipo de fallo.
- **La copia no se puede restaurar** — causa: nunca se probó la restauración. Corrección: restauración periódica con consulta y alerta.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3): dos de tiempo virtual y semillas fijas con resultados idénticos, y una medición real de copias de una base SQLite con un daño inyectado por el autor, con detecciones idénticas y tiempos de reloj distintos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Recuperación](./recuperacion.md), [Dependencia circular](../d/dependencia-circular.md), [Ejercicio de recuperación](../e/ejercicio-de-recuperacion.md), [Réplica asíncrona](./replica-asincrona.md), [RTO (objetivo de tiempo de recuperación)](./rto-objetivo-de-tiempo-de-recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-502 — Continuidad, disaster recovery y ejercicios](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md).

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

[↑ Glosario](../../README.md) · [← RPN](./rpn.md) · [RRF →](./rrf.md)
