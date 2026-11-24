# Exclusión

[↑ Glosario](../../README.md) · [← Excepción registrada](./excepcion-registrada.md) · [Exhaustividad →](./exhaustividad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

En una estrategia de pruebas, una **exclusión** es la decisión explícita de no probar un componente o una clase de fallo, con razón, responsable y fecha de revisión ([SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)).

## Por qué importa

Todo equipo deja cosas sin probar; la diferencia profesional es saberlo. [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) lo resume: lo que no se prueba nadie lo sabe cuando la omisión es silenciosa. Una exclusión escrita convierte un descuido en una decisión asumida.

## Cómo funciona

El paquete de estrategia de [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) incluye una lista de exclusiones con razón y **caducidad**. Una exclusión sin caducidad se convierte en una omisión; una con caducidad vence y obliga a revisarla. La estructura permite que un programa valide que cada exclusión tiene fecha.

## Ejemplo

[SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md): el paquete de la plataforma lista nueve componentes probados y tres exclusiones con razón y caducidad a 75 días; una de ellas es la búsqueda.

## Errores y confusiones comunes

- **Las exclusiones nunca se revisan.** Sin caducidad; fecha menor de 90 días y revisión.
- **Lo que no se prueba nadie lo sabe.** Omisión silenciosa; lista de exclusiones con razón, responsable y caducidad.

## Límites y cuándo no aplica

Una exclusión justificada no elimina el riesgo, solo lo hace visible. Excluir componentes de impacto alto exige aprobación de quien asume el riesgo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fecha de revisión](../f/fecha-de-revision.md), [Componente](../c/componente.md), [Revisión](../r/revision.md), [Escape](./escape.md), [Estrategia de pruebas](./estrategia-de-pruebas.md), [Exposición](./exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (25 clases más lo mencionan; las que más):

[SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md).

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

[↑ Glosario](../../README.md) · [← Excepción registrada](./excepcion-registrada.md) · [Exhaustividad →](./exhaustividad.md)
