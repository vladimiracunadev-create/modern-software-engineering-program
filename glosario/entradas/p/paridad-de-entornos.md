# Paridad de entornos

[↑ Glosario](../../README.md) · [← Paridad](./paridad.md) · [Paridad demográfica →](./paridad-demografica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **paridad de entornos** es el grado en que los entornos (desarrollo, preproducción, producción) coinciden en forma, versiones y configuración que afecta al comportamiento ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)). La idea viene de la metodología de las doce factores. No es identidad: el tamaño, los datos y los secretos son distintos y deben serlo.

## Por qué importa

Un entorno de preproducción que ya no se parece a producción da una falsa seguridad: pasa pruebas que producción no pasaría. La decisión que cambia es qué se mantiene igual a propósito y qué se deja diferir: se invierte en que lo que afecta al comportamiento coincida, para que lo que se prueba sea lo que se despliega.

## Cómo funciona

La metodología de las doce factores identifica tres brechas que la paridad intenta cerrar, y [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) las recoge:

- **De tiempo**: el código tarda semanas en llegar a producción.
- **De personal**: quien escribe el código no lo despliega.
- **De herramientas**: se usa una base distinta en desarrollo que en producción.

El criterio práctico es distinguir qué debe coincidir y qué no. Debe coincidir **la forma, las versiones y la configuración que afecta al comportamiento**. No debe coincidir el tamaño (preproducción puede ser más pequeña), los datos (no se copian datos reales de personas sin motivo) ni los secretos (cada entorno tiene los suyos).

Los síntomas que da la clase muestran por qué importa y cómo se pierde. «Preproducción pasa y producción falla» ocurre cuando las configuraciones divergieron; la corrección es promoción periódica (llevar los cambios de configuración por la misma ruta a todos los entornos) y comparación semanal. «Un script de desarrollo afecta producción» ocurre cuando la frontera entre entornos es una convención (misma cuenta, prefijos en los nombres); se corrige con una cuenta por entorno con políticas heredadas. Ambas ideas se conectan con el radio de explosión y la separación de funciones.

## Ejemplo

Preproducción usa una versión menor de la base y una configuración de caché distinta de producción. Una consulta que pasa las pruebas allí falla en producción porque la versión de producción optimiza distinto. La comparación semanal de configuración habría mostrado la divergencia. Ejemplo ilustrativo del patrón de [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md).

## Errores y confusiones comunes

- **Un script de desarrollo afecta producción**: misma cuenta y prefijos como frontera; se corrige con una cuenta por entorno.
- **Preproducción pasa y producción falla**: configuraciones que divergieron; se corrige con promoción periódica y comparación semanal.
- **Confundir paridad con copia exacta**: los datos y los secretos deben ser distintos.
- **Mantenerla solo la primera vez**: la divergencia se acumula sin comprobación.

## Límites y cuándo no aplica

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) precisa que sus experimentos son sintéticos: los 24 recursos, el 5 % de acciones comodín, la frecuencia de edición manual, los 12 permisos y los 6 pares son supuestos del autor, y no se evaluó ninguna organización real. La paridad completa puede ser demasiado cara (replicar la capacidad de producción); se elige qué diferencias se aceptan y se documentan. Y no sustituye observar producción: algunas fallas solo ocurren con carga y datos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Versión](../v/version.md), [Acceso de emergencia](../a/acceso-de-emergencia.md), [Promoción](./promocion.md), [Radio de explosión](../r/radio-de-explosion.md), [Separación de funciones](../s/separacion-de-funciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

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

[↑ Glosario](../../README.md) · [← Paridad](./paridad.md) · [Paridad demográfica →](./paridad-demografica.md)
