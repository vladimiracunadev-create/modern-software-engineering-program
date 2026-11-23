# Deprecación y migración

[↑ Glosario](../../README.md) · [← Deprecación](./deprecacion.md) · [Deque y ventanas →](./deque-y-ventanas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Deprecar anuncia reemplazo, ventana y señal antes de remover.

Definición de trabajo de [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md).

## Por qué importa

En [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), el tema «Deprecación y migración» importa porque deprecar anuncia reemplazo, ventana y señal antes de remover.

## Cómo funciona

Según [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), en la sección «Deprecación y migración»:

Deprecar anuncia reemplazo, ventana y señal antes de remover. Warning debe ser accionable y no inundar. Una guía muestra antes/después, compatibilidad temporal y rollback; mantener alias indefinido también tiene costo que se decide explícitamente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md)) son:

- **`pip` instala 1.10.0 como más antigua que 1.9.0 en un script propio** — causa: se ordenaron versiones como texto. Corrección: usar `packaging.version.Version` y comparar objetos.
- **Una versión SemVer con guion se rechaza al publicar** — causa: no es una versión PEP 440 válida (`1.0.0-alpha.beta`). Corrección: normalizar al esquema de Python o cambiar de esquema y documentarlo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. SemVer describe una versión del producto, no cómo varias restricciones seleccionan dependencias. La siguiente clase abre el resolvedor y el lockfile.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Reemplazo](../r/reemplazo.md), [Señal](../s/senal.md), [Ventana](../v/ventana.md), [API pública](../a/api-publica.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Prerelease y metadata](../p/prerelease-y-metadata.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Deprecación](./deprecacion.md) · [Deque y ventanas →](./deque-y-ventanas.md)
