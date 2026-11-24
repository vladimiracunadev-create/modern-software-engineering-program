# Acceso de emergencia

[↑ Glosario](../../README.md) · [← Abstracción de rama](./abstraccion-de-rama.md) · [Accessibility Engineer →](./accessibility-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

El **acceso de emergencia** es una concesión excepcional de permisos mayores a los habituales, limitada en el tiempo, justificada y registrada ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)). Es la válvula de un sistema de mínimo privilegio: reconoce que a veces hay que actuar en producción con más poder del cotidiano, y define bajo qué condiciones se puede hacer sin abrir un hueco permanente.

## Por qué importa

Cuando algo falla en producción la presión empuja a dar permisos amplios «por ahora» y a no volver a quitarlos. La decisión profesional que cambia este concepto es dejar de elegir entre dos malos extremos: bloquear al equipo de guardia cuando más lo necesita, o repartir administración permanente. Con un acceso de emergencia bien diseñado, la rapidez se compra con trazabilidad y con una fecha de caducidad, no con confianza ciega.

## Cómo funciona

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) describe cuatro propiedades que lo definen y que se pueden comprobar:

1. **Excepcional**: no es el camino normal. Si se usa a diario, el problema son los permisos de base, que se quedaron cortos.
2. **Limitado en el tiempo**: el permiso expira solo; no depende de que alguien se acuerde de revocarlo.
3. **Justificado**: quien lo pide declara por qué, de modo que la revisión posterior tenga contra qué comparar.
4. **Registrado y revisado por otra persona**: el registro lo revisa alguien distinto de quien actuó.

La causa de fondo de la cuarta propiedad es la **separación de funciones**: quien usa el acceso no debería poder borrar su propio rastro. Por eso [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) corrige el error típico («el acceso de emergencia no deja rastro») ubicando el registro en una cuenta de auditoría separada, que quien actúa no puede escribir ni borrar. Sin esa separación, el acceso de emergencia es, en palabras de la clase, un administrador permanente con otro nombre.

## Ejemplo

Un servicio cae a las tres de la madrugada y la persona de guardia necesita leer y modificar un recurso para el que su rol diario no tiene permiso. Solicita el acceso indicando el incidente; recibe permisos ampliados por un plazo corto; cada acción queda en el registro de una cuenta de auditoría separada; al expirar el plazo vuelve sola a sus permisos habituales; al día siguiente otra persona revisa el registro frente a la justificación. Ilustración construida a partir del mecanismo de [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), no un caso medido.

## Errores y confusiones comunes

- **Registro escribible por quien lo usa**: es el error que nombra [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md). Se corrige con el registro en una cuenta de auditoría aparte.
- **Convertirlo en rutina**: si cada semana hace falta, no es una emergencia sino un rol mal definido.
- **Confundirlo con un permiso de administrador «por si acaso»**: la diferencia es el plazo, la justificación y la revisión; sin ellas es solo un permiso amplio.
- **Pensar que reemplaza el mínimo privilegio**: lo complementa; lo habitual sigue siendo mínimo.

## Límites y cuándo no aplica

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) fija el límite explícitamente: no debe volverse el camino normal ni deshacer la separación de funciones. No sustituye el diseño de permisos del día a día ni sirve para trabajo planificado, que debe pasar por el flujo ordinario de cambios. Tampoco da por sí solo seguridad: depende de que alguien revise realmente el registro; un registro que nadie lee solo documenta el abuso a posteriori.

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
