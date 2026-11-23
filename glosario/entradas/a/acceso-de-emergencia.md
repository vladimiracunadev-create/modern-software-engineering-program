# Acceso de emergencia

[↑ Glosario](../../README.md) · [← Abstracción de rama](./abstraccion-de-rama.md) · [Accessibility Engineer →](./accessibility-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Concesión excepcional, limitada en el tiempo y registrada, de permisos mayores a los habituales.

Definición de trabajo de [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md).

## Por qué importa

En [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), el tema «Acceso de emergencia» importa porque la excepción debe ser rápida, acotada y visible.

## Cómo funciona

Según [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), en la sección «Acceso de emergencia»:

Cuando algo falla en producción hay que poder actuar rápido, y los permisos mínimos del día a día no bastan. El acceso de emergencia es una excepción deliberada: concede más permisos por un tiempo limitado, exige una justificación y deja un registro que otra persona revisa después. Lo que no debe hacer es convertirse en el camino normal, ni deshacer la separación de funciones: quien usa el acceso de emergencia no debería poder borrar su registro. Un acceso de emergencia sin registro es un administrador permanente con otro nombre.

## Ejemplo

Ejemplo de [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma crea tres cuentas, una por entorno, administradas desde una organización que fija políticas comunes: ningún usuario puede desactivar el registro, y los depósitos de producción deniegan el borrado masivo. Los cambios llegan a preproducción por promoción automática tras las pruebas y a producción solo con la aprobación de una persona que no escribió el cambio. Un proceso compara cada semana las 72 claves compartidas entre preproducción y producción y abre una incidencia con cada diferencia. Las 8 diferencias declaradas (tamaño de las instancias, nombres, volumen de datos) están en un archivo revisable.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El acceso de emergencia no deja rastro** — causa: registro escribible por quien lo usa. Corrección: registro en una cuenta de auditoría separada. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que no debe hacer es convertirse en el camino normal, ni deshacer la separación de funciones: quien usa el acceso de emergencia no debería poder borrar su registro. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Permiso](../p/permiso.md), [Paridad de entornos](../p/paridad-de-entornos.md), [Promoción](../p/promocion.md), [Radio de explosión](../r/radio-de-explosion.md), [Separación de funciones](../s/separacion-de-funciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS: Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) — separación en varias cuentas; autoridad: documentación del proveedor.
- [Google Cloud: jerarquía de recursos](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) — organización, carpetas y proyectos; autoridad: documentación del proveedor.
- [The Twelve-Factor App: dev/prod parity](https://12factor.net/dev-prod-parity) — paridad entre entornos; autoridad: metodología publicada por sus autores.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — catálogo de controles, incluida la separación de funciones; autoridad: NIST.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Abstracción de rama](./abstraccion-de-rama.md) · [Accessibility Engineer →](./accessibility-engineer.md)
