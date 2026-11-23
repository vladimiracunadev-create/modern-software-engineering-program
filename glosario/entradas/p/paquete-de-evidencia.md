# Paquete de evidencia

[↑ Glosario](../../README.md) · [← Paquete de capa de datos](./paquete-de-capa-de-datos.md) · [Paquete de informe →](./paquete-de-informe.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Conjunto de datos que prueban cómo se construyó, verificó, aprobó y ensayó una versión.

Definición de trabajo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md): Archivo que asocia cada prueba con el defecto que detecta y el resultado de ejecutarla con y sin él.
- En [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md): Conjunto de artefactos y comprobaciones con enlaces y huellas que permite repetir una verificación.
- En [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md): Conjunto de artefactos que permite a otra persona revisar y operar el producto.
- En [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md): Conjunto versionado de requisitos, controles, pruebas y evidencias con fecha, alcance y huella.

## Por qué importa

En [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), el tema «Paquete de evidencia» importa porque un paquete válido en forma puede ser falso en contenido.

## Cómo funciona

Según [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

El equipo de la API de entregas ensambla su camino. Cada versión pasa por la integración con ramas de menos de dos días, el grafo de trabajos con un camino crítico de 14 minutos, las compuertas ordenadas por razón de detección, el escaneo de secretos que siempre bloquea, la política sobre el plan de infraestructura, una preproducción con datos sintéticos, un canario del 5 % con criterio de retroceso automático y la observación de las métricas con intervalos. Los cambios de esquema siguen el cambio en paralelo: el equipo ensaya el retroceso cada mes en preproducción, con la versión anterior leyendo los datos que escribió la nueva, y la contracción es un cambio aparte, treinta días después, con aprobación de una segunda persona.

Según [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md):

Traslada el proyecto a otro sistema (por ejemplo, una aplicación móvil con un backend compartido y versiones antiguas instaladas en los teléfonos): cambia los consumidores, el esquema y las etapas, y conserva el procedimiento de cambiar en paralelo, ensayar el retroceso, hacer la ablación de las compuertas y validar el paquete de evidencia. La transferencia está lograda cuando puedes decir qué versión antigua sigue viva y qué fallo solo tiene un guardián, no cuando el diagrama se parece al de la plataforma.

## Ejemplo

Ejemplo de [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas ensambla su camino. Cada versión pasa por la integración con ramas de menos de dos días, el grafo de trabajos con un camino crítico de 14 minutos, las compuertas ordenadas por razón de detección, el escaneo de secretos que siempre bloquea, la política sobre el plan de infraestructura, una preproducción con datos sintéticos, un canario del 5 % con criterio de retroceso automático y la observación de las métricas con intervalos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El paquete de evidencia pasa y es falso** — causa: solo valida forma. Corrección: capas de cruce y verosimilitud; muestra revisada por una persona. ([SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md))
- **El paquete de evidencia nunca se re-ejecuta** — causa: se trata como documento. Corrección: validador en la integración continua. ([SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md)) son: Las definiciones son operativas para el proyecto de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con cifras publicadas idénticas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Artefacto](../a/artefacto.md), [Conjunto](../c/conjunto.md), [Ensayo](../e/ensayo.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-492 — Proyecto: camino a producción con rollback](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).

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

[↑ Glosario](../../README.md) · [← Paquete de capa de datos](./paquete-de-capa-de-datos.md) · [Paquete de informe →](./paquete-de-informe.md)
