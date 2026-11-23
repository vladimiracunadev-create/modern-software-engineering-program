# Ventana de exposición

[↑ Glosario](../../README.md) · [← Ventana de deprecación](./ventana-de-deprecacion.md) · [Ventana de gracia →](./ventana-de-gracia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Tiempo transcurrido entre la publicación de un aviso de seguridad y el momento en que el sistema deja de usar la versión afectada.

Definición de trabajo de [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md): Tiempo que transcurre entre que existe una vulnerabilidad y que se corrige o se mitiga.

## Por qué importa

En [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), el tema «Ventana de exposición» importa porque la política determina cuántos días un aviso queda abierto.

## Cómo funciona

Según [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), en la sección «Ventana de exposición»:

Cuando se publica un aviso de seguridad sobre una dependencia, el tiempo hasta que tu sistema deje de usar la versión afectada tiene tres tramos: hasta que el proveedor publica una versión corregida, hasta que tu política decide aplicarla y hasta que el cambio llega a producción. El primer tramo no depende de ti; los otros dos, sí. Una política **continua** (actualizar en cuanto hay corrección, tras una breve verificación) reduce el segundo tramo a días; una por **lotes** (mensual, trimestral, anual) lo ata al calendario: en promedio, un aviso espera a la mitad del periodo y, en el peor caso, al periodo completo. La política puede combinarse con prioridad: avisos con explotación activa conocida (como los de un catálogo de vulnerabilidades explotadas) se atienden fuera del lote.

## Ejemplo

Caso medido en la sección «Ventana de exposición» de [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md):

Cuando se publica un aviso de seguridad sobre una dependencia, el tiempo hasta que tu sistema deje de usar la versión afectada tiene tres tramos: hasta que el proveedor publica una versión corregida, hasta que tu política decide aplicarla y hasta que el cambio llega a producción. El primer tramo no depende de ti; los otros dos, sí.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)) son:

- **La actualización «de una hora» dura semanas** — causa: se acumularon cambios incompatibles. Corrección: actualizar en pasos pequeños con una cadencia.
- **Un aviso queda abierto meses** — causa: política por lotes sin prioridad. Corrección: añadir un carril rápido para avisos con explotación conocida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La política se escribe, se revisa con datos (ventana de exposición real, rezago medio) y admite excepciones documentadas, como una dependencia que se mantiene en una versión por razones de compatibilidad con un sistema externo. ([SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Seguridad](../s/seguridad.md), [Versión](./version.md), [Vulnerabilidad](./vulnerabilidad.md), [Archivo de bloqueo](../a/archivo-de-bloqueo.md), [Dependencia atrasada](../d/dependencia-atrasada.md), [Dependencia sin soporte](../d/dependencia-sin-soporte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-397 — IaaS, PaaS, SaaS y responsabilidad compartida](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Versionado semántico 2.0.0](https://semver.org/) — convención de versiones con cambios incompatibles en la mayor; autoridad: especificación de la comunidad.
- [OSV](https://osv.dev/) — registro abierto de vulnerabilidades por paquete y versión; autoridad: proyecto abierto respaldado por Google.
- [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — vulnerabilidades con explotación conocida; autoridad: agencia de ciberseguridad de Estados Unidos.
- [NIST SP 800-218, SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas para componentes de terceros y respuesta a vulnerabilidades; autoridad: NIST.
- [Google, «Software Engineering at Google»: Dependency Management](https://abseil.io/resources/swe-book/html/ch21.html) — por qué es difícil gestionar dependencias; autoridad: libro de ingeniería de Google.

---

[↑ Glosario](../../README.md) · [← Ventana de deprecación](./ventana-de-deprecacion.md) · [Ventana de gracia →](./ventana-de-gracia.md)
