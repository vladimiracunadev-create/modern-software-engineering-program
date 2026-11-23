# Expediente

[↑ Glosario](../../README.md) · [← Expansión y contracción](./expansion-y-contraccion.md) · [Expediente de la decisión →](./expediente-de-la-decision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Conjunto de evidencia reproducible con sus límites.

Definición de trabajo de [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md): Conjunto de documentos y evidencias que permiten revisar la plataforma.

## Por qué importa

La clase donde se define, [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), existe con este propósito: la clase existe para que demuestres, con un producto pequeño y con evidencia que otra persona pueda repetir, que sabes sostener las invariantes que hacen sostenible a un SaaS: que un cliente no vea ni degrade a otro, que dar de alta sea repetible, que el estado de la suscripción y el uso medido sean exactos, que los derechos se hagan cumplir donde ocurre la operación, que el dinero deje un libro que cuadra y que la promesa de servicio se pueda medir.

## Cómo funciona

Según [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md):

Los defectos de carrera no aparecen en pruebas secuenciales. La comprobación de concurrencia lanza 20 hilos que arrancan a la vez contra 5 unidades y verifica la invariante («pedidos ≤ existencias»), no un resultado exacto: con el defecto, aceptó pedidos de más; sin él, exactamente 5. La prueba debe ejecutarse contra el motor de producción y con suficiente presión para abrir la ventana; en el taller, una pausa de 2 ms entre leer y escribir la ensancha y hace el defecto repetible. Declara en el expediente que una prueba verde de concurrencia no demuestra ausencia de carreras, solo que esta no se manifestó con esta presión.

Según [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md):

El expediente final incluye: la arquitectura de seis piezas, las siete invariantes, la matriz con la columna nueva, la salida limpia repetida tres veces, la medición de la latencia de los otros clientes durante la ráfaga de un cliente de prueba con y sin cuotas, el SLI por inquilino del mes de ensayo con su peor inquilino, y una página de límites: sin identidad real, sin carga de producción, sin procesador real, sin evaluación de seguridad externa, sin certificación. El comprador firma, y el hueco descubierto en la sesión es el motivo: valoró más que el equipo mostrara un defecto que no esperaba que que ninguno apareciera.

## Ejemplo

Ejemplo de [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) (sección «Ejemplo profesional»):

El expediente final incluye: la arquitectura de seis piezas, las siete invariantes, la matriz con la columna nueva, la salida limpia repetida tres veces, la medición de la latencia de los otros clientes durante la ráfaga de un cliente de prueba con y sin cuotas, el SLI por inquilino del mes de ensayo con su peor inquilino, y una página de límites: sin identidad real, sin carga de producción, sin procesador real, sin evaluación de seguridad externa, sin certificación. El comprador firma, y el hueco descubierto en la sesión es el motivo: valoró más que el equipo mostrara un defecto que no esperaba que que ninguno apareciera.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Declara en el expediente que una prueba verde de concurrencia no demuestra ausencia de carreras, solo que esta no se manifestó con esta presión. ([SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md))
- Implementa la mínima plataforma que haga cumplir el contrato con registro encadenado y entrega el expediente con una sección «no cubierto» que otra persona pueda discutir. ([SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Documento](../d/documento.md), [Evidencia](./evidencia.md), [Límite](../l/limite.md), [Cabeza de la cadena](../c/cabeza-de-la-cadena.md), [Contrato de ejecución](../c/contrato-de-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Expansión y contracción](./expansion-y-contraccion.md) · [Expediente de la decisión →](./expediente-de-la-decision.md)
