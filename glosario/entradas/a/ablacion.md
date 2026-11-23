# Ablación

[↑ Glosario](../../README.md) · [← ABI](./abi.md) · [Abreviatura de flag →](./abreviatura-de-flag.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Retirada de un componente para medir qué dejaba de ocurrir sin él.

Definición de trabajo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md): Quitar una pieza para medir qué cambia.

## Por qué importa

En [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), el tema «Ablación de compuertas» importa porque algunos fallos tienen un único guardián; quitarlo los hace escapar.

## Cómo funciona

Según [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

Para saber si el camino es suficiente se construye una matriz con los fallos que se quieren cubrir y las compuertas que pueden detectar cada uno: un error de sintaxis lo ven el análisis y las pruebas unitarias; una dependencia vulnerable, solo el escaneo de dependencias; un permiso excesivo en la infraestructura, la política sobre el plan; un fallo que aparece solo con tráfico real, el canario y la alerta. La **ablación** consiste en quitar una compuerta y ver qué ocurre: algunos fallos se detectan más tarde, a un costo mayor; otros dejan de detectarse. Los fallos con un único guardián son el riesgo concentrado.

Según [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

Traslada el proyecto a otro sistema (por ejemplo, una aplicación móvil con un backend compartido y versiones antiguas instaladas en los teléfonos): cambia los consumidores, el esquema y las etapas, y conserva el procedimiento de cambiar en paralelo, ensayar el retroceso, hacer la ablación de las compuertas y validar el paquete de evidencia. La transferencia está lograda cuando puedes decir qué versión antigua sigue viva y qué fallo solo tiene un guardián, no cuando el diagrama se parece al de la plataforma.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

El equipo de la API de entregas ensambla su camino. Cada versión pasa por la integración con ramas de menos de dos días, el grafo de trabajos con un camino crítico de 14 minutos, las compuertas ordenadas por razón de detección, el escaneo de secretos que siempre bloquea, la política sobre el plan de infraestructura, una preproducción con datos sintéticos, un canario del 5 % con criterio de retroceso automático y la observación de las métricas con intervalos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un fallo grave llega a producción sin ser visto** — causa: fallo con un solo guardián que se desactivó. Corrección: matriz de fallos y ablación periódica. ([SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la tabla de ablación la configuración sin criterio de parada resuelve las seis tareas, pero gasta 12 pasos en cada una (el tope técnico) en vez de 5: el trabajo se hace y se desperdicia. ([SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Bucle del agente](../b/bucle-del-agente.md), [Cambio en paralelo](../c/cambio-en-paralelo.md), [Camino a producción](../c/camino-a-produccion.md), [Criterio de salida](../c/criterio-de-salida.md), [Harness](../h/harness.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

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

[↑ Glosario](../../README.md) · [← ABI](./abi.md) · [Abreviatura de flag →](./abreviatura-de-flag.md)
