# Vulnerabilidad

[↑ Glosario](../../README.md) · [← Votación](./votacion.md) · [Warm-up →](../w/warm-up.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Debilidad en un sistema que una persona atacante puede aprovechar para vulnerar una propiedad de seguridad.

Definición de trabajo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md).

## Por qué importa

La clase donde se define, [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), existe con este propósito: la clase existe para que sepas qué hacer cuando alguien, dentro o fuera del equipo, encuentra una vulnerabilidad: cómo se recibe el reporte, cómo se puntúa sin engañarse, cómo se decide qué corregir primero, cómo se coordina la divulgación y cómo se aprende del caso.

## Cómo funciona

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

La puerta de entrada de las vulnerabilidades es una decisión de diseño. El archivo `security.txt` (RFC 9116), publicado en `/.well-known/security.txt`, declara al menos un `Contact` y una fecha de `Expires`, y puede apuntar a la política de divulgación y a una clave de cifrado. Un buzón dedicado atendido por personas con nombre y suplente vale más que un correo general. La política escrita dice qué está dentro del alcance (qué dominios, qué tipos de prueba), qué está prohibido (acceder a datos de otras personas más allá de lo necesario para demostrar el defecto, degradar el servicio), cuándo se acusa recibo, cuándo se responde con una evaluación y cuánto se espera para corregir.

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

Cuando la vulnerabilidad afecta a un producto que otras organizaciones usan y que ellas deben actualizar. Para el código propio de una plataforma alojada que nadie más ejecuta, un registro interno y un aviso suelen bastar.

## Ejemplo

Ejemplo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) (sección «Preguntas frecuentes»):

Cuando la vulnerabilidad afecta a un producto que otras organizaciones usan y que ellas deben actualizar. Para el código propio de una plataforma alojada que nadie más ejecuta, un registro interno y un aviso suelen bastar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md)) son:

- **Un reporte se publica sin respuesta** — causa: canal sin responsable ni plazo. Corrección: `security.txt`, buzón con suplentes y acuse automático.
- **Se discute el puntaje en vez del riesgo** — causa: CVSS tratado como medida. Corrección: vector a la vista, puntaje ambiental y evidencia de explotación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para las vulnerabilidades propias de la plataforma no hay catálogo, y la señal de explotación sale de los propios registros: intentos sobre ese endpoint, anomalías de acceso, reportes duplicados (varias personas lo encontraron: probablemente otros también). ([SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad de seguridad](../p/propiedad-de-seguridad.md), [Propiedad](../p/propiedad.md), [Seguridad](../s/seguridad.md), [CVSS](../c/cvss.md), [Divulgación coordinada](../d/divulgacion-coordinada.md), [Explotación conocida](../e/explotacion-conocida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (53 clases más lo mencionan; las que más):

[SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CISA: catálogo KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — vulnerabilidades explotadas conocidas; autoridad: CISA.
- [FIRST: CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document) — fórmula y métricas; autoridad: FIRST.
- [FIRST: EPSS](https://www.first.org/epss/) — probabilidad de explotación; autoridad: FIRST.
- [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116) — archivo `security.txt`; autoridad: IETF.
- [CERT/CC: divulgación coordinada](https://vuls.cert.org/confluence/display/CVD) — guía del proceso; autoridad: CERT/CC.

---

[↑ Glosario](../../README.md) · [← Votación](./votacion.md) · [Warm-up →](../w/warm-up.md)
