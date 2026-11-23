# Estrategia de pruebas

[↑ Glosario](../../README.md) · [← Estrategia de caché](./estrategia-de-cache.md) · [Estrategia voraz →](./estrategia-voraz.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Conjunto de decisiones sobre qué probar, con qué nivel, con cuánto esfuerzo y qué excluir, con sus razones.

Definición de trabajo de [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md).

## Por qué importa

La clase donde se define, [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), existe con este propósito: el proyecto integra la parte en un artefacto: una estrategia de pruebas ejecutable para la plataforma de entregas, con riesgos y su reparto de horas, el nivel de prueba de cada clase de fallo, las pruebas que lo sostienen y su demostración, los criterios de bloqueo, las exclusiones con caducidad y los límites.

## Cómo funciona

[SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la parte. Esta clase deja el artefacto final: la estrategia de pruebas ejecutable con su validador, su simulación y sus límites. La [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) toma esos riesgos y los convierte en atributos de calidad medibles, en rendimiento y en resiliencia. Cambia después una sola decisión, la caducidad máxima de las exclusiones de 90 a 30 días, y observa cuántas del paquete vencen y qué revisión exigen.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)) son:

- **La estrategia es un documento que nadie ejecuta** — causa: no hay validador ni vínculo con la integración continua. Corrección: paquete estructurado y validado en cada cambio.
- **Un riesgo alto queda sin horas o sin nivel que lo vea** — causa: falta de reglas de coherencia. Corrección: reglas de riesgo en el validador.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con un simulador, un paquete y un validador escritos por el autor en Windows y Ubuntu (WSL2), con salidas idénticas. La probabilidad de defecto, el impacto, la distribución de los cambios y el costo de un escape son supuestos; las reglas del validador se ajustaron con las mismas mutaciones que lo miden. No se midió ningún equipo, integración continua ni incidente real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Sobre](../s/sobre.md), [Escape](./escape.md), [Exclusión](./exclusion.md), [Exposición](./exposicion.md), [Gate](../g/gate.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de verificación; autoridad: NIST.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — atributos de calidad; autoridad: ISO/IEC.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — evaluación de riesgos; autoridad: NIST.
- [Libro de SRE de Google: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas y fiabilidad; autoridad: Google SRE.
- [DORA: automatización de pruebas](https://dora.dev/capabilities/test-automation/) — capacidad de pruebas automatizadas; autoridad: DORA.

---

[↑ Glosario](../../README.md) · [← Estrategia de caché](./estrategia-de-cache.md) · [Estrategia voraz →](./estrategia-voraz.md)
