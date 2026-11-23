# Registro encadenado

[↑ Glosario](../../README.md) · [← Registro de solo anexado](./registro-de-solo-anexado.md) · [Registro estructurado →](./registro-estructurado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Secuencia de entradas donde cada una incluye el resumen de la anterior.

Definición de trabajo de [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md): Registro en que cada entrada incluye la huella de la anterior.

## Por qué importa

En [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), el tema «Registro encadenado» importa porque hace detectable la alteración y el borrado.

## Cómo funciona

Según [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md):

Elige una carga de tu sistema que hoy ejecute código de terceros o configuración de clientes. Escribe su modelo de amenazas, la tabla amenaza-mecanismo-prueba, el contrato de ejecución y la política de fallo. Implementa la mínima plataforma que haga cumplir el contrato con registro encadenado y entrega el expediente con una sección «no cubierto» que otra persona pueda discutir.

Según [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md):

El equipo de *Avisos-ML* crea el expediente de gobierno antes de aceptar los dos usos nuevos. Empieza por un inventario de tres sistemas de IA con uso, dueño y datos. Aplica el triaje: el recordatorio queda en riesgo limitado; la priorización de llamadas se marca para revisión, porque afecta el acceso a apoyo; la asignación de plazas de refuerzo queda como candidata a alto riesgo, y el comité decide no proceder con ese uso hasta consultar al área jurídica. Construye la tabla de evidencia: de los veinte elementos de documentación, once existen y apuntan a artefactos, cinco están en preparación y cuatro (la supervisión humana y la transparencia ante la persona) no existen.

## Ejemplo

Ejemplo de [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) (sección «Ejemplo mínimo»):

Un registro encadenado en siete líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Implementa la mínima plataforma que haga cumplir el contrato con registro encadenado y entrega el expediente con una sección «no cubierto» que otra persona pueda discutir. ([SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md))

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
