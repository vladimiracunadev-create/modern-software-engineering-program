# Framework e inversión de control

[↑ Glosario](../../README.md) · [← Frame](./frame.md) · [Framing →](./framing.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un framework define estructura y llama código del usuario en puntos de extensión.

Definición de trabajo de [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md).

## Por qué importa

En [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), el tema «Framework e inversión de control» importa porque un framework define estructura y llama código del usuario en puntos de extensión.

## Cómo funciona

Según [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), en la sección «Framework e inversión de control»:

Un framework define estructura y llama código del usuario en puntos de extensión. Esa inversión permite convenciones y lifecycle común, pero aumenta acoplamiento. Usar una utilidad del framework no convierte automáticamente todo el producto en framework.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)) son:

- **Clasificar un producto por su nombre: «es un SDK porque se llama SDK»** — causa: se clasificó por marketing y no por control ni contrato. Corrección: imprimir la pila desde un callback y decidir por quién ocupa el fondo.
- **`import mi_sdk` tarda 300 ms y carga más de 100 módulos** — causa: el `__init__` importa un runtime completo aunque se use una función. Corrección: importar de forma perezosa dentro de la función o dividir en extras.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Nombrar el producto no define qué cambios son compatibles. La siguiente clase delimita API pública y usa SemVer como comunicación, no como garantía automática.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Punto de extensión](../p/punto-de-extension.md), [Estructura](../e/estructura.md), [Extensión](../e/extension.md), [Biblioteca](../b/biblioteca.md), [Plataforma](../p/plataforma.md), [Runtime](../r/runtime.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Frame](./frame.md) · [Framing →](./framing.md)
