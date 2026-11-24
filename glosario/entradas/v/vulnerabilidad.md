# Vulnerabilidad

[↑ Glosario](../../README.md) · [← Votación](./votacion.md) · [Warm-up →](../w/warm-up.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Una **vulnerabilidad** es una debilidad en un sistema que una persona atacante puede aprovechar para vulnerar una propiedad de seguridad ([SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md)): confidencialidad, integridad o disponibilidad.

## Por qué importa

La palabra se usa para todo, desde un error teórico hasta una brecha explotada; lo que cambia la decisión es cuán explotable es en *tu* contexto y qué activo pone en riesgo. Confundir presencia con riesgo lleva a discutir puntajes en vez de actuar.

## Cómo funciona

[SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) trata la gestión: un canal de reporte con responsable y plazo (por ejemplo, un archivo `security.txt`, un buzón con suplentes y acuse automático) y una evaluación que no se reduce al puntaje CVSS. CVSS describe la gravedad técnica de un defecto en abstracto; el riesgo depende además de la exposición, de si hay explotación conocida y del activo afectado. Por eso la clase pide dejar el vector a la vista, calcular el puntaje ambiental y adjuntar evidencia de explotación.

## Ejemplo

Dos dependencias vulnerables con el mismo puntaje base: una está en un servicio expuesto a internet y la otra en una herramienta interna sin datos. Se corrige primero la expuesta.

## Errores y confusiones comunes

- **Un reporte se publica sin respuesta.** El canal no tiene responsable ni plazo; `security.txt`, buzón con suplentes y acuse automático.
- **Se discute el puntaje en vez del riesgo.** CVSS tratado como medida; vector a la vista, puntaje ambiental y evidencia de explotación.

## Límites y cuándo no aplica

Una vulnerabilidad conocida no implica que haya sido explotada, ni su ausencia en una base pública que el sistema sea seguro: solo se reportan las que alguien encontró y publicó.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad de seguridad](../p/propiedad-de-seguridad.md), [Propiedad](../p/propiedad.md), [Seguridad](../s/seguridad.md), [CVSS](../c/cvss.md), [Divulgación coordinada](../d/divulgacion-coordinada.md), [Explotación conocida](../e/explotacion-conocida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (53 clases más lo mencionan; las que más):

[SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

**Aparece en los casos de estudio:** [Cloudflare](../../../casos/exito/cloudflare.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

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
