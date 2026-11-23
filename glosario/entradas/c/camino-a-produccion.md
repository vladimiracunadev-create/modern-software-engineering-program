# Camino a producción

[↑ Glosario](../../README.md) · [← Cambio sobre código existente](./cambio-sobre-codigo-existente.md) · [Camino crítico →](./camino-critico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Secuencia de etapas, compuertas y evidencia por las que pasa una versión hasta servir tráfico real.

Definición de trabajo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

## Por qué importa

La clase donde se define, [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), existe con este propósito: el proyecto existe para que entregues un camino completo a producción que pueda defenderse ante otra persona: qué comprueba cada etapa, qué evidencia deja, cómo se vuelve atrás y qué parte del riesgo sigue sin cubrirse.

## Cómo funciona

Según [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

Un camino a producción es la secuencia de etapas por las que pasa una versión desde que se integra hasta que sirve tráfico real, y cada etapa tiene una razón: detectar una clase de fallo antes de que cueste más. La integración con política de troncal detecta choques; la construcción y la verificación detectan regresiones de comportamiento; las comprobaciones de seguridad y política detectan secretos, dependencias vulnerables y configuraciones peligrosas; la preproducción detecta fallos de integración con el entorno; el canario detecta defectos que solo aparecen con tráfico real; la observación en producción detecta lo que ninguna etapa anterior vio. Cada paso hacia la derecha detecta lo que los anteriores no podían, y cuesta más cuando falla.

## Ejemplo

Ejemplo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sección «Caso conductor»):

La canalización de la API de entregas cierra aquí su recorrido en la [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md). Este proyecto deja el duodécimo artefacto: el camino a producción con retroceso ensayado y paquete de evidencia, que alimenta la [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), donde las señales de producción (observabilidad, SLO, incidentes) deciden si una versión sana lo es de verdad. Cambia después un solo dato, la fase en que contraes el esquema, y observa cuándo el retroceso deja de ser posible.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md)) son:

- **El retroceso falla con errores de columna** — causa: renombrado o borrado directo. Corrección: cambio en paralelo: expandir, migrar, contraer.
- **Tras retroceder faltan datos** — causa: la versión nueva escribe solo en lo nuevo. Corrección: doble escritura y relleno de los datos antiguos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un camino a producción es la secuencia de etapas por las que pasa una versión desde que se integra hasta que sirve tráfico real, y cada etapa tiene una razón: detectar una clase de fallo antes de que cueste más. ([SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compuerta](./compuerta.md), [Evidencia](../e/evidencia.md), [Secuencia](../s/secuencia.md), [Versión](../v/version.md), [Ablación](../a/ablacion.md), [Cambio en paralelo](./cambio-en-paralelo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler: ParallelChange](https://martinfowler.com/bliki/ParallelChange.html) — patrón expandir, migrar y contraer; autoridad: Martin Fowler.
- [Fowler y Sadalage: Evolutionary Database Design](https://martinfowler.com/articles/evodb.html) — cambios de base de datos continuos; autoridad: Martin Fowler y Pramod Sadalage.
- [SLSA: niveles de la especificación v1.1](https://slsa.dev/spec/v1.1/levels) — procedencia y garantías de un artefacto; autoridad: proyecto SLSA, OpenSSF.
- [Google SRE Book: Release Engineering](https://sre.google/sre-book/release-engineering/) — práctica de ingeniería de entregas; autoridad: Google.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — cambios de esquema admitidos por el motor; autoridad: documentación de SQLite.

---

[↑ Glosario](../../README.md) · [← Cambio sobre código existente](./cambio-sobre-codigo-existente.md) · [Camino crítico →](./camino-critico.md)
