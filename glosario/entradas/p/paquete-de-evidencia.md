# Paquete de evidencia

[↑ Glosario](../../README.md) · [← Paquete de capa de datos](./paquete-de-capa-de-datos.md) · [Paquete de informe →](./paquete-de-informe.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Un **paquete de evidencia** es un conjunto de datos que prueban cómo se construyó, verificó, aprobó y ensayó una versión. El programa usa el término en varias clases con matices: en [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), un archivo que asocia cada prueba con el defecto que detecta y el resultado de ejecutarla con y sin él; en [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), artefactos y comprobaciones con enlaces y huellas que permiten repetir una verificación; en [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), el conjunto que permite a otra persona revisar y operar el producto; en [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), un conjunto versionado de requisitos, controles, pruebas y evidencias con fecha, alcance y huella.

## Por qué importa

Una afirmación («está probado», «es seguro», «está listo») sin evidencia es opinión. El paquete convierte la afirmación en algo que otra persona puede repetir y revisar. [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) advierte el reverso: un paquete válido en forma puede ser falso en contenido, así que hace falta mirar qué prueban realmente los artefactos.

## Cómo funciona

El hilo común de los usos del programa:

1. **Cada afirmación enlaza con un artefacto** (una prueba, un resultado, un registro).
2. **Los artefactos llevan huella** (hash) y fecha, para detectar cambios.
3. **El alcance está declarado:** qué cubre la evidencia y qué no.
4. **Es repetible:** otra persona puede volver a ejecutar la verificación.

En [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), la evidencia clave para una prueba es que *detecta* el defecto: se asocia cada prueba con el defecto que atrapa y se registra el resultado con y sin él. En [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), el camino a producción reúne integración con ramas cortas, un grafo de trabajos con camino crítico de 14 minutos, compuertas, escaneo de secretos, política sobre el plan de infraestructura, preproducción con datos sintéticos, un canario del 5 % con retroceso automático y ensayo mensual del retroceso.

## Ejemplo

Ilustración propia con el sentido de [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md): una fila «el servicio exige autenticación en todas las rutas» enlaza con la prueba que lo comprueba, su resultado de la última ejecución con fecha y la huella del commit evaluado. Si el commit cambia, la huella ya no coincide y la evidencia queda caduca.

## Errores y confusiones comunes

- **Un paquete completo en forma y falso en contenido** ([SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md)): se valida la estructura, no el sentido.
- **Evidencia sin fecha ni alcance.**
- **Confundirlo con documentación:** el paquete son pruebas y registros, no explicaciones.
- **Reutilizar evidencia de una versión anterior** sin volver a ejecutarla.

## Límites y cuándo no aplica

La evidencia prueba lo que se midió, no que no existan otros defectos. Los proyectos de la clase son escenarios didácticos y no constituyen una certificación. Y reunir evidencia tiene costo: debe ser proporcional al riesgo.

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
