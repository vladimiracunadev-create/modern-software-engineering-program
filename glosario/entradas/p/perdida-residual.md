# Pérdida residual

[↑ Glosario](../../README.md) · [← Percentil 95](./percentil-95.md) · [Pérdida selectiva de telemetría →](./perdida-selectiva-de-telemetria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Pérdida esperada que queda después de aplicar un reparto de pruebas.

Definición de trabajo de [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md).

## Por qué importa

En [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), el tema «Reparto del presupuesto» importa porque el mismo número de horas produce una pérdida residual distinta según el criterio.

## Cómo funciona

Según [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md):

Reproduce el fallo clásico de la clase: **repartir por el tamaño del código y concluir que se «cubrió lo importante»**. Calcula el reparto proporcional a las líneas y compara la pérdida residual con el uniforme.

## Ejemplo

Ejemplo de [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la pérdida residual de dos repartos con tres componentes. Antes de ejecutarlo, predice cuál es menor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)) son:

- **«Probamos todo» y aun así hay incidentes en producción** — causa: se confunde cobertura de líneas con detección de defectos. Corrección: medir con mutantes y listar qué clases de fallo no tienen nivel asignado.
- **El reparto cambia cada trimestre sin explicación** — causa: las estimaciones viven en la cabeza de alguien. Corrección: documentar p, impacto y su fuente; reestimar tras un incidente.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)) son: Las definiciones son operativas para esta clase y no sustituyen el vocabulario de las normas citadas en las fuentes. Se ejecutaron tres experimentos con modelos del autor y datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se midió ningún sistema real, equipo ni defecto: probabilidad, impacto, dificultad, costos por nivel y la forma exponencial de la detección son supuestos. El conjunto mínimo de niveles es una consecuencia de la matriz que escribí, no un resultado empírico.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Exclusión](../e/exclusion.md), [Nivel de prueba](../n/nivel-de-prueba.md), [Riesgo](../r/riesgo.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — atributos de calidad del producto; autoridad: ISO/IEC.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — evaluación de riesgos; autoridad: NIST.
- [Martin Fowler, «TestPyramid»](https://martinfowler.com/bliki/TestPyramid.html) — reparto por nivel; autoridad: autor del texto.
- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) — costo de las pruebas lentas; autoridad: equipo de pruebas de Google.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.

---

[↑ Glosario](../../README.md) · [← Percentil 95](./percentil-95.md) · [Pérdida selectiva de telemetría →](./perdida-selectiva-de-telemetria.md)
