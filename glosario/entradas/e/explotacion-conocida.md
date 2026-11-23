# Explotación conocida

[↑ Glosario](../../README.md) · [← Explosión de estados](./explosion-de-estados.md) · [Exposición →](./exposicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Evidencia de que una vulnerabilidad se está aprovechando contra sistemas reales.

Definición de trabajo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md).

## Por qué importa

La clase donde se define, [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), existe con este propósito: la clase existe para que sepas qué hacer cuando alguien, dentro o fuera del equipo, encuentra una vulnerabilidad: cómo se recibe el reporte, cómo se puntúa sin engañarse, cómo se decide qué corregir primero, cómo se coordina la divulgación y cómo se aprende del caso.

## Cómo funciona

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

Parchear todo lo de CVSS 7 o más exige 1 076 acciones y deja 43 explotadas sin cubrir; la lista de explotación conocida cubre las 83 con 83 acciones, pero solo conoce lo ya explotado.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

El equipo publica `/.well-known/security.txt` con un `Contact` a un buzón con dos responsables y suplentes y un `Expires` a un año vista, y una política con alcance, reglas para quien prueba y plazos: acuse en 24 horas hábiles automáticamente y de una persona en 48, evaluación en 5 días hábiles, corrección o mitigación de las críticas en 14 días y de las altas en 30, y divulgación coordinada a los 90 días o antes si hay parche.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md)) son:

- **Un reporte se publica sin respuesta** — causa: canal sin responsable ni plazo. Corrección: `security.txt`, buzón con suplentes y acuse automático.
- **Se discute el puntaje en vez del riesgo** — causa: CVSS tratado como medida. Corrección: vector a la vista, puntaje ambiental y evidencia de explotación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Parchear todo lo de CVSS 7 o más exige 1 076 acciones y deja 43 explotadas sin cubrir; la lista de explotación conocida cubre las 83 con 83 acciones, pero solo conoce lo ya explotado. ([SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](./evidencia.md), [Vulnerabilidad](../v/vulnerabilidad.md), [CVSS](../c/cvss.md), [Divulgación coordinada](../d/divulgacion-coordinada.md), [Triaje](../t/triaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [FIRST: CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document) — fórmula y métricas; autoridad: FIRST.
- [CISA: catálogo KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — vulnerabilidades explotadas conocidas; autoridad: CISA.
- [FIRST: EPSS](https://www.first.org/epss/) — probabilidad de explotación; autoridad: FIRST.
- [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116) — archivo `security.txt`; autoridad: IETF.
- [CERT/CC: divulgación coordinada](https://vuls.cert.org/confluence/display/CVD) — guía del proceso; autoridad: CERT/CC.

---

[↑ Glosario](../../README.md) · [← Explosión de estados](./explosion-de-estados.md) · [Exposición →](./exposicion.md)
