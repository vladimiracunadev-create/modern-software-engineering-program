# Registro encadenado

[↑ Glosario](../../README.md) · [← Registro de solo anexado](./registro-de-solo-anexado.md) · [Registro estructurado →](./registro-estructurado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Un **registro encadenado** es una secuencia de entradas donde cada una incluye el resumen (huella, *hash*) de la anterior. [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md) (proyecto: plataforma de ejecución aislada con evidencia) lo usa como mecanismo de evidencia, y [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) (gobierno de IA y regulación) lo define como el registro en que cada entrada incluye la huella de la anterior. Es la misma idea de una cadena de bloques, sin consenso distribuido ni minería.

## Por qué importa

Hace detectable la alteración y el borrado. Cambiar o eliminar una entrada del pasado rompe la huella de todas las siguientes, de modo que quien revisa el registro lo nota. Es una forma barata de dar credibilidad a un registro de auditoría.

## Cómo funciona

Cada entrada contiene los datos del evento y el hash de la entrada anterior. La huella de la entrada *n* se calcula sobre sus datos más la huella de la *n−1*. Para verificar:

1. Se recorre el registro desde el principio.
2. Se recalcula la huella de cada entrada con los datos y la huella anterior.
3. Si alguna no coincide con la almacenada o con la que cita la siguiente, hubo alteración.

Qué detecta y qué no: **detecta** modificación y borrado intermedios, e inserciones. **No detecta** el borrado de las últimas entradas ni la reescritura completa de todo el registro por quien controla el almacenamiento, a menos que la última huella se publique o se guarde fuera de su alcance. Por eso el patrón se acompaña de anclar la cabeza de la cadena en otro lugar.

En [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), el expediente de la plataforma de ejecución aislada incluye un registro encadenado y una sección «no cubierta» que otra persona pueda discutir.

## Ejemplo

El proyecto de [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md) pide implementar la mínima plataforma que haga cumplir el contrato de ejecución de código de terceros, con registro encadenado y un expediente con lo que no cubre. En [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), el equipo de *Avisos-ML* construye una tabla de evidencia de gobierno; un registro encadenado respalda que las decisiones de aprobación no se modificaron después. Ilustración propia: tres entradas A, B, C; si se cambia B, la huella de C ya no corresponde.

## Errores y confusiones comunes

- **Pensar que impide la alteración:** solo la hace detectable.
- **No anclar la última huella,** de modo que quien controla el registro lo reescribe entero.
- **Confundirlo con firma:** el encadenado prueba integridad de secuencia, no procedencia.
- **Confundirlo con una cadena de bloques con consenso.**

## Límites y cuándo no aplica

No garantiza que lo registrado sea verdadero, solo que no se alteró después. Verificar exige recorrer el registro. Si el volumen es muy alto, se agrupan entradas en lotes. Y no sustituye controles de acceso al almacenamiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](../h/huella.md), [Registro](./registro.md), [Secuencia](../s/secuencia.md), [Alto riesgo](../a/alto-riesgo.md), [Cabeza de la cadena](../c/cabeza-de-la-cadena.md), [Contrato de ejecución](../c/contrato-de-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Registro de solo anexado](./registro-de-solo-anexado.md) · [Registro estructurado →](./registro-estructurado.md)
