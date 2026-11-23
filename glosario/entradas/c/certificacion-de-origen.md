# Certificación de origen

[↑ Glosario](../../README.md) · [← Ceremonia ritual](./ceremonia-ritual.md) · [Certificado →](./certificado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Declaración de quien contribuye de que tiene derecho a enviar el cambio bajo la licencia del proyecto, expresada con un pie `Signed-off-by`.

Definición de trabajo de [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md).

## Por qué importa

La clase donde se define, [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md), existe con este propósito: la clase existe para que reconozcas cuándo una decisión técnica es también una decisión legal o ética y para que la trates con procesos verificables en vez de con suposiciones.

## Cómo funciona

Según [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md):

El código que entra al repositorio debe tener una persona responsable de su origen. El **Developer Certificate of Origin** (DCO) es un texto breve por el que quien contribuye certifica que escribió el cambio o tiene derecho a enviarlo bajo la licencia del proyecto; se declara con un pie `Signed-off-by: Nombre <correo>` en el mensaje del commit. Un acuerdo de licencia de contribuyente (CLA) es una alternativa más formal. La verificación automática debe ser estricta: un pie es una línea con un formato definido al final del mensaje (`git interpret-trailers`), debe coincidir con la persona que figura como autora y no vale si está a mitad del texto o mal escrito. Hay un límite que ninguna regla de formato supera: la firma certifica, no comprueba.

Según [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md):

El DCO es ligero y verificable por formato; el CLA es más formal, permite cambiar la licencia del proyecto y exige más trámite. La elección depende del proyecto y de su gobernanza. En ambos casos, la firma certifica y no comprueba.

## Ejemplo

Ejemplo de [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) (sección «Preguntas frecuentes»):

El DCO es ligero y verificable por formato; el CLA es más formal, permite cambiar la licencia del proyecto y exige más trámite. La elección depende del proyecto y de su gobernanza. En ambos casos, la firma certifica y no comprueba.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md)) son:

- **Se frena trabajo por una licencia inofensiva** — causa: búsqueda de cadena sin analizar la expresión. Corrección: analizar `AND`, `OR` y `WITH`.
- **Una licencia incompatible llega a producción** — causa: campo vacío tratado como seguro. Corrección: tratar lo desconocido como bloqueado hasta resolverlo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos, no son asesoría legal y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se revisó ningún proyecto, contrato ni historial reales; las expresiones de licencia, el reparto de tipos de commit y los parámetros del flujo de suscripción son construcciones del autor, el analizador es una versión simplificada y nada de esto es asesoría legal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Signed-off-by](../s/signed-off-by.md), [Derecho](../d/derecho.md), [Copyleft](./copyleft.md), [Expresión de licencia](../e/expresion-de-licencia.md), [Licencia de software](../l/licencia-de-software.md), [Patrón oscuro](../p/patron-oscuro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-536 — Propiedad intelectual, contratos y ética](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «DCO».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Developer Certificate of Origin](https://developercertificate.org/) — texto de la certificación de origen; autoridad: Linux Foundation.
- [SPDX, expresiones de licencia](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) — sintaxis de combinación de licencias; autoridad: proyecto SPDX (Linux Foundation).
- [Open Source Initiative, licencias](https://opensource.org/licenses) — licencias aprobadas; autoridad: Open Source Initiative.
- [Open Source Guides, «The Legal Side of Open Source»](https://opensource.guide/legal/) — introducción a propiedad y licencias; autoridad: GitHub y comunidad.
- [Git, `git interpret-trailers`](https://git-scm.com/docs/git-interpret-trailers) — pies de mensaje; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Ceremonia ritual](./ceremonia-ritual.md) · [Certificado →](./certificado.md)
