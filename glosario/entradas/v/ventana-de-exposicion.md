# Ventana de exposición

[↑ Glosario](../../README.md) · [← Ventana de deprecación](./ventana-de-deprecacion.md) · [Ventana de gracia →](./ventana-de-gracia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **ventana de exposición** es el tiempo transcurrido entre la publicación de un aviso de seguridad y el momento en que el sistema deja de usar la versión afectada ([SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)). [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md) la formula en un sentido más amplio: el tiempo que transcurre entre que existe una vulnerabilidad y que se corrige o se mitiga.

## Por qué importa

Mientras la ventana está abierta, el sistema es vulnerable a una falla ya conocida y, a menudo, explotable. Reducirla es una de las pocas defensas que dependen enteramente de la organización. La decisión que cambia es la política de actualización de dependencias: no «cuando se pueda», sino con una cadencia que acote cuánto tiempo se permanece expuesto.

## Cómo funciona

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) descompone la ventana en tres tramos:

1. Hasta que el **proveedor publica** una versión corregida.
2. Hasta que **tu política decide** aplicarla.
3. Hasta que **el cambio llega a producción**.

El primer tramo no depende de ti; los otros dos, sí. Una política **continua** (actualizar en cuanto hay corrección, tras una breve verificación) reduce el segundo tramo a días. Una política por **lotes** (mensual, trimestral, anual) lo ata al calendario: en promedio, un aviso espera a la mitad del periodo y, en el peor caso, al periodo completo. La política puede combinarse con prioridad: un carril rápido para avisos con explotación activa conocida, y el lote regular para el resto.

La clase explica por qué las actualizaciones espaciadas son más difíciles: se acumulan cambios incompatibles, y la actualización «de una hora» dura semanas; actualizar en pasos pequeños con una cadencia mantiene bajo el costo y la ventana. La política se escribe, se revisa con datos (ventana de exposición real, rezago medio) y admite excepciones documentadas, como una dependencia que se mantiene en una versión por razones de compatibilidad con un sistema externo.

## Ejemplo

Se publica un aviso crítico sobre una biblioteca. El proveedor libera la corrección al día siguiente. Con política mensual, el equipo la aplica en la próxima ventana (hasta 30 días después); con política continua y carril rápido para explotación conocida, la aplica en un par de días. La diferencia es el tamaño del segundo tramo. Aplicación del razonamiento de [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

## Errores y confusiones comunes

- **La actualización «de una hora» dura semanas**: se acumularon cambios incompatibles; se corrige actualizando en pasos pequeños con una cadencia.
- **Un aviso queda abierto meses**: política por lotes sin prioridad; se añade un carril rápido para avisos con explotación conocida.
- **Medir solo la fecha de publicación del aviso**: la ventana incluye el despliegue.
- **No medir la ventana real**.

## Límites y cuándo no aplica

El primer tramo (que el proveedor publique una corrección) escapa al control del equipo, y para dependencias sin soporte puede no cerrarse nunca; ahí corresponde mitigar o reemplazar. Una política continua exige pruebas fiables: sin ellas, actualizar rápido es arriesgado. [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) presenta la cadencia como decisión con compromisos, no como una cifra única.

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
