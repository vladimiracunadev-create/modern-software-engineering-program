# Cambio compatible

[↑ Glosario](../../README.md) · [← Callbacks, promesas y corrutinas](./callbacks-promesas-y-corrutinas.md) · [Cambio de contrato →](./cambio-de-contrato.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un **cambio compatible** es una modificación del proveedor de una interfaz que **no rompe ningún contrato de un consumidor existente** ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)). En el taller de empaquetado de [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) el ejemplo es agregar una opción sin romper al consumidor anterior: el código antiguo sigue funcionando sin tocarse, y se ejecutan ambas pruebas (la del consumidor antiguo y la que usa la opción nueva) para demostrarlo. Es el caso que justifica subir una versión **menor** en versionado semántico, mientras que un cambio incompatible exige subir la mayor.

## Por qué importa

La compatibilidad permite que proveedores y consumidores evolucionen a ritmos distintos. Si cada cambio obliga a coordinar con todos, el costo de mejorar el producto crece con el número de consumidores. La decisión profesional que cambia es **cómo se clasifica un cambio antes de numerarlo**: [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) lo dice así, «el número se decide después de clasificar el cambio», no antes. Clasificar mal produce versiones que mienten: un parche que rompe, o una versión mayor que alarma sin motivo.

## Cómo funciona

Un cambio es compatible respecto de un contrato concreto. Se razona sobre qué puede depender el consumidor:

- **Añadir** una opción con valor por defecto, un campo opcional en la respuesta o una función nueva suele ser compatible: el consumidor antiguo no la usa.
- **Quitar o renombrar** algo público, **cambiar el tipo** de un valor, **endurecer** una validación (rechazar lo que antes se aceptaba) o **cambiar el orden o el formato** prometidos suele ser incompatible.
- **Ablandar** requisitos de entrada y **endurecer** garantías de salida son compatibles; lo contrario no.

El razonamiento es de sustitución: el consumidor antiguo debe poder usar la versión nueva sin enterarse. Para comprobarlo, [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) pide ejecutar la prueba antigua contra el código nuevo, revisar el changelog y, si hace falta, la guía de migración. Un comparador de API detecta firmas, y las pruebas de contrato escritas desde el consumidor detectan comportamiento.

## Ejemplo

El taller de [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) agrega una opción a la API del paquete reutilizable. El consumidor anterior llama sin la opción y obtiene el comportamiento previo, porque el valor por defecto lo conserva:

```python
# versión 1.2: salida = procesar(datos)
# versión 1.3: salida = procesar(datos, estricto=False)  # nuevo, por defecto igual al anterior
```

Se ejecutan las dos pruebas: la que invoca `procesar(datos)` debe seguir verde y la nueva debe cubrir `estricto=True`. Como la API declarada solo añade, la versión propuesta es la menor (1.3.0) y el changelog lo anota. En [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), la misma idea aparece en componentes: un proveedor que cambia sin romper ningún contrato de consumidor hace un cambio compatible, y el consumidor puede actualizar cuando quiera.

## Errores y confusiones comunes

- **Creer que «solo añadir» siempre es compatible.** Añadir un valor a una enumeración que los consumidores recorren con `switch` exhaustivo puede romperlos.
- **Medir por la firma y no por el comportamiento.** Mantener la firma pero cambiar el orden de los resultados o la excepción lanzada rompe a quien dependía de ellos.
- **Numerar primero y clasificar después.** Se acaba justificando el número en lugar de describir el cambio.
- **No probar con el consumidor antiguo.** Solo la prueba antigua contra el código nuevo demuestra la compatibilidad.

## Límites y cuándo no aplica

La compatibilidad se define frente a los consumidores conocidos y a la API declarada: no puede garantizarse frente a quien dependa de comportamiento no documentado. El taller verifica una versión y un entorno principal ([SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md)); la compatibilidad entre versiones de dependencias y plataformas pide una matriz de compatibilidad. En sistemas donde el proveedor controla a todos los consumidores y los despliega juntos, la distinción pierde peso porque se puede cambiar ambos a la vez.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato de consumidor](./contrato-de-consumidor.md), [Contrato](./contrato.md), [Opción](../o/opcion.md), [Api y cli coherentes](../a/api-y-cli-coherentes.md), [Artefacto e instalación](../a/artefacto-e-instalacion.md), [Contrato dirigido por el consumidor](./contrato-dirigido-por-el-consumidor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Callbacks, promesas y corrutinas](./callbacks-promesas-y-corrutinas.md) · [Cambio de contrato →](./cambio-de-contrato.md)
