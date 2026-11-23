# Sdk

[↑ Glosario](../../README.md) · [← Sdist y wheel](./sdist-y-wheel.md) · [Sección crítica →](./seccion-critica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un sdk reduce fricción para integrar una capacidad: cliente, modelos, autenticación, ejemplos, tooling y documentación.

Definición de trabajo de [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md).

## Por qué importa

En [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), el tema «SDK» importa porque un SDK reduce fricción para integrar una capacidad: cliente, modelos, autenticación, ejemplos, tooling y documentación.

## Cómo funciona

Según [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), en la sección «SDK»:

Un SDK reduce fricción para integrar una capacidad: cliente, modelos, autenticación, ejemplos, tooling y documentación. Debe representar el contrato remoto sin ocultar timeout, paginación o error. Puede incluir biblioteca y CLI, pero su promesa es experiencia coherente.

## Ejemplo

Ejemplo de [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) (sección «Ejemplo profesional»):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Clasificar un producto por su nombre: «es un SDK porque se llama SDK»** — causa: se clasificó por marketing y no por control ni contrato. Corrección: imprimir la pila desde un callback y decidir por quién ocupa el fondo. ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md))
- **`import mi_sdk` tarda 300 ms y carga más de 100 módulos** — causa: el `__init__` importa un runtime completo aunque se use una función. Corrección: importar de forma perezosa dentro de la función o dividir en extras. ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md))
- **`import mi_sdk` falla en CI sin credenciales** — causa: el módulo lee variables de entorno o abre red al importarse. Corrección: mover los efectos a `connect()` y comprobar con un gancho de auditoría. ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que el SDK decide por defecto lo hereda cada consumidor sin saberlo. ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Autenticación](../a/autenticacion.md), [Capacidad](../c/capacidad.md), [Modelo](../m/modelo.md), [Biblioteca](../b/biblioteca.md), [Framework e inversión de control](../f/framework-e-inversion-de-control.md), [Plataforma](../p/plataforma.md).
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

[↑ Glosario](../../README.md) · [← Sdist y wheel](./sdist-y-wheel.md) · [Sección crítica →](./seccion-critica.md)
