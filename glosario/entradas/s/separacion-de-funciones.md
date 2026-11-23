# Separación de funciones

[↑ Glosario](../../README.md) · [← Sensibilidad global](./sensibilidad-global.md) · [Serializable →](./serializable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Principio de que ninguna persona complete sola una actividad crítica.

Definición de trabajo de [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md).

## Por qué importa

En [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), el tema «Separación de funciones» importa porque quien escribe, aprueba y audita no debe ser la misma persona.

## Cómo funciona

Según [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), en la sección «Separación de funciones»:

El control de separación de funciones de NIST busca que una actividad crítica no la complete una sola persona: quien propone un cambio no es quien lo aprueba, quien despliega no puede alterar el registro de auditoría, quien crea usuarios no puede asignarles administración. Cada par prohibido se escribe como una regla comprobable sobre los permisos efectivos. La dificultad es la combinación: un rol puede ser inocuo y la suma de dos, no. Por eso se revisa la unión de los roles de cada persona y no cada rol por separado.

## Ejemplo

Ejemplo de [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md). Esta clase deja el séptimo artefacto: el mapa de cuentas, la promoción y las separaciones de funciones. `SE-404` pregunta cuánta capacidad hay en cada entorno y cuánto cuesta. Cambia una estructura, por ejemplo fusionar preproducción y producción, y mira cuánto crece el porcentaje de errores que cruzan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)) son:

- **Un script de desarrollo afecta producción** — causa: misma cuenta y prefijos como frontera. Corrección: una cuenta por entorno con políticas heredadas.
- **Preproducción pasa y producción falla** — causa: configuraciones que divergieron. Corrección: promoción periódica y comparación semanal.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El control de separación de funciones de NIST busca que una actividad crítica no la complete una sola persona: quien propone un cambio no es quien lo aprueba, quien despliega no puede alterar el registro de auditoría, quien crea usuarios no puede asignarles administración. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))

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
