# Separación de funciones

[↑ Glosario](../../README.md) · [← Sensibilidad global](./sensibilidad-global.md) · [Serializable →](./serializable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **separación de funciones** es el principio de que ninguna persona complete sola una actividad crítica ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)). Es un control de NIST: quien propone un cambio no es quien lo aprueba, quien despliega no puede alterar el registro de auditoría, quien crea usuarios no puede asignarles administración.

## Por qué importa

Si una sola persona puede iniciar, aprobar y ocultar una acción, un error o un abuso pasa sin que nadie lo detecte. La decisión que cambia es cómo se reparten los permisos: se diseñan pares de funciones que no deben coincidir en una misma persona, y esa regla se comprueba, no solo se declara.

## Cómo funciona

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) propone expresar cada **par prohibido** como una regla comprobable sobre los **permisos efectivos**. Ejemplos de pares: proponer y aprobar un cambio; desplegar y alterar el registro de auditoría; crear usuarios y asignarles administración. La regla se evalúa automáticamente contra la configuración de permisos real.

La dificultad que señala la clase es la **combinación**: un rol puede ser inocuo y la suma de dos, no. Por eso se revisa la **unión** de los roles de cada persona y no cada rol por separado. Una persona con el rol A y el rol B puede tener, en conjunto, los dos permisos que el par prohíbe aunque ninguno de sus roles lo haga individualmente.

Conecta con otros mecanismos del mismo tema. El **acceso de emergencia** es la excepción controlada: concede permisos mayores por tiempo limitado, pero sin deshacer la separación (quien lo usa no debería poder borrar su registro). El **radio de explosión** acota el daño de un error o de una credencial comprometida. Y la **promoción** de cambios entre entornos por un proceso definido permite que quien aprueba sea distinto de quien escribe.

## Ejemplo

Una regla dice: ninguna identidad puede tener a la vez «desplegar a producción» y «modificar el registro de auditoría». El verificador calcula los permisos efectivos de cada persona (suma de todos sus roles) y detecta que una persona, por pertenecer a dos grupos, tiene ambos. Se corrige antes de que ocurra un incidente. Mecanismo descrito en [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md).

## Errores y confusiones comunes

- **Un script de desarrollo afecta producción**: misma cuenta y prefijos como frontera; se corrige con una cuenta por entorno con políticas heredadas.
- **Revisar cada rol por separado**: la suma de dos inocuos puede violar la regla.
- **Confundirla con el mínimo privilegio**: este limita cuánto puede una persona; la separación impide que una sola complete una actividad crítica.
- **Dejar que quien actúa escriba su propio registro**.

## Límites y cuándo no aplica

En equipos muy pequeños puede no haber dos personas para cada función; entonces se compensa con registros inmutables y revisión posterior, y se declara el límite. La separación añade fricción y tiempo de espera: se aplica a las actividades críticas, no a todas. [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) aclara que sus experimentos son sintéticos (12 permisos y 6 pares de ejemplo) y no evalúan ninguna organización real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actividad](../a/actividad.md), [Acceso de emergencia](../a/acceso-de-emergencia.md), [Paridad de entornos](../p/paridad-de-entornos.md), [Promoción](../p/promocion.md), [Radio de explosión](../r/radio-de-explosion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — catálogo de controles, incluida la separación de funciones; autoridad: NIST.
- [AWS: Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) — separación en varias cuentas; autoridad: documentación del proveedor.
- [Google Cloud: jerarquía de recursos](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) — organización, carpetas y proyectos; autoridad: documentación del proveedor.
- [The Twelve-Factor App: dev/prod parity](https://12factor.net/dev-prod-parity) — paridad entre entornos; autoridad: metodología publicada por sus autores.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Sensibilidad global](./sensibilidad-global.md) · [Serializable →](./serializable.md)
