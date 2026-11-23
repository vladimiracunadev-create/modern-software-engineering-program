# Dependencias y distribución

[↑ Glosario](../../README.md) · [← Dependencias de proyecto y herramientas](./dependencias-de-proyecto-y-herramientas.md) · [Deprecación →](./deprecacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Obligaciones pueden cambiar al distribuir binario, ofrecer servicio o enlazar componentes según licencia y jurisdicción.

Definición de trabajo de [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md).

## Por qué importa

En [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), el tema «Dependencias y distribución» importa porque obligaciones pueden cambiar al distribuir binario, ofrecer servicio o enlazar componentes según licencia y jurisdicción.

## Cómo funciona

Según [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), en la sección «Dependencias y distribución»:

Obligaciones pueden cambiar al distribuir binario, ofrecer servicio o enlazar componentes según licencia y jurisdicción. La clase enseña triage técnico, no asesoría legal. Dudas se escalan con inventario preciso, no con suposiciones.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md)) son:

- **El inventario de licencias tiene cientos de filas «desconocidas»** — causa: las dependencias usan texto libre en vez de expresiones SPDX. Corrección: normalizar con una tabla revisada por humanos y exigir `License-Expression` en lo propio.
- **Se copió un archivo a otro repositorio y se perdió su licencia** — causa: la declaración está solo en la raíz. Corrección: cabecera SPDX por archivo o mapeo REUSE; conservar el aviso original.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Cumplir metadata y licencias no garantiza que el producto sea fácil de adoptar. La siguiente clase mide la experiencia desde descubrimiento hasta recuperación.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Componente](../c/componente.md), [Servicio](../s/servicio.md), [Copyright y licencia](../c/copyright-y-licencia.md), [Identificadores y expresiones spdx](../i/identificadores-y-expresiones-spdx.md), [Procedencia](../p/procedencia.md), [Reuse y verificación](../r/reuse-y-verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Dependencias de proyecto y herramientas](./dependencias-de-proyecto-y-herramientas.md) · [Deprecación →](./deprecacion.md)
