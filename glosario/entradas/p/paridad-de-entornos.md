# Paridad de entornos

[↑ Glosario](../../README.md) · [← Paridad](./paridad.md) · [Paridad demográfica →](./paridad-demografica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Grado en que los entornos coinciden en forma, versiones y configuración que afecta al comportamiento.

Definición de trabajo de [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md).

## Por qué importa

En [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), el tema «Paridad de entornos» importa porque un entorno que no se parece a producción no predice su comportamiento.

## Cómo funciona

Según [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), en la sección «Paridad de entornos»:

La metodología de las doce factores sostiene que los entornos deben parecerse en lo posible para evitar las brechas de tiempo (código que tarda semanas en llegar a producción), de personal (quien escribe no despliega) y de herramientas (una base distinta en desarrollo). Un entorno de preproducción que ya no se parece a producción da una falsa seguridad: pasa pruebas que producción no pasaría. La paridad no es identidad: el tamaño, los datos y los secretos son distintos y deben serlo; lo que debe coincidir es la forma, las versiones y la configuración que afecta al comportamiento.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md):

El equipo de la plataforma crea tres cuentas, una por entorno, administradas desde una organización que fija políticas comunes: ningún usuario puede desactivar el registro, y los depósitos de producción deniegan el borrado masivo. Los cambios llegan a preproducción por promoción automática tras las pruebas y a producción solo con la aprobación de una persona que no escribió el cambio. Un proceso compara cada semana las 72 claves compartidas entre preproducción y producción y abre una incidencia con cada diferencia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)) son:

- **Un script de desarrollo afecta producción** — causa: misma cuenta y prefijos como frontera. Corrección: una cuenta por entorno con políticas heredadas.
- **Preproducción pasa y producción falla** — causa: configuraciones que divergieron. Corrección: promoción periódica y comparación semanal.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada proveedor y cada norma usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna organización ni estructura real: los 24 recursos, el 5 % de acciones comodín, la frecuencia de edición manual, los 12 permisos y los 6 pares son supuestos del autor. La siguiente clase mira cuánta capacidad necesita cada entorno y cuánto cuesta: escalado, capacidad y costos.

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
