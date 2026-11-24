# Punto de extensión

[↑ Glosario](../../README.md) · [← Punto de equilibrio de costo](./punto-de-equilibrio-de-costo.md) · [Punto de no retorno →](./punto-de-no-retorno.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un **punto de extensión** es un lugar declarado de un sistema donde se pueden **añadir variantes o complementos sin editar el código existente**. El programa lo define de tres maneras que coinciden: [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) lo describe como una interfaz con ciclo de vida, errores y compatibilidad definidos; [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), como el lugar donde se pueden añadir variantes sin editar el código existente (la idea de «abierto a la extensión» de SOLID); [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), como el lugar declarado donde un complemento puede engancharse. Lo esencial es que está **declarado**: el sistema promete aceptar extensiones allí y en ningún otro sitio.

## Por qué importa

Una cadena de condicionales que crece con cada regla nueva obliga a reabrir la misma función cada vez, con el riesgo de romper lo existente. Un punto de extensión mueve esa variabilidad a un lugar estable. [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) documenta el síntoma: cada regla nueva reabre la misma función por una cadena de condicionales sin punto de extensión; la corrección es registrar reglas y escribir la política de combinación en un solo sitio. La decisión que cambia es dónde se paga el costo de añadir una variante: con el punto de extensión, en el archivo nuevo; sin él, en el núcleo.

## Cómo funciona

Un punto de extensión define cuatro cosas ([SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md)):

- **Interfaz:** qué debe ofrecer un complemento (qué funciones, qué datos).
- **Ciclo de vida:** cuándo se crea, se activa, se usa y se cierra.
- **Errores:** qué ocurre si el complemento falla o lanza una excepción, sin derribar al anfitrión.
- **Compatibilidad:** qué versión del contrato soporta cada complemento y cuál es la política de cambios.

Es **más estrecho que exponer los internos**: en lugar de dejar que los complementos modifiquen cualquier parte del sistema, se les da una superficie pequeña y estable. Esa estrechez es lo que permite evolucionar el sistema sin romper complementos. [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) advierte que los *hooks* (ganchos) **sin orden o reentrancia documentada producen interacciones invisibles entre plugins**: si dos complementos se enganchan al mismo evento, el orden en que se ejecutan y si uno puede disparar al otro cambian el resultado, y nadie lo sabe.

## Ejemplo

El SDK del programa expone `choose_next` y un punto de extensión para reglas de prioridad. Un registro de reglas:

```python
REGLAS = []

def regla(f):
    REGLAS.append(f)          # punto de extensión: registrar una regla
    return f

def combinar(casos):          # política de combinación: un solo sitio
    puntaje = {c["id"]: 0 for c in casos}
    for r in REGLAS:
        for c in casos:
            puntaje[c["id"]] += r(c)
    return max(casos, key=lambda c: puntaje[c["id"]])
```

Añadir una regla de descuento no toca `combinar`. [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) agrega la salvedad: para «añadir una regla» se puede cerrar el cálculo detrás de este punto, pero para «cambiar cómo se combinan las reglas» ese mismo punto no ayuda: la extensión protege solo contra la variación que se previó.

## Errores y confusiones comunes

- **Exponer internos como si fueran un punto de extensión.** Cualquier cambio posterior rompe complementos.
- **Ganchos sin orden documentado.** Interacciones impredecibles entre plugins.
- **Sin manejo de errores.** Un complemento roto derriba al anfitrión.
- **Prever la extensión equivocada.** El punto no ayuda con la variación que no anticipó.

## Límites y cuándo no aplica

Con dos o tres variantes previsibles y un solo equipo, un condicional o una interfaz con implementaciones en el mismo repositorio es más simple que un mecanismo de extensión ([SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md)). Cada punto de extensión es una API pública que hay que mantener, documentar y versionar. Si nadie ajeno va a extender el sistema, es complejidad sin retorno.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Complemento](../c/complemento.md), [Extensión](../e/extension.md), [Interfaz](../i/interfaz.md), [Variante](../v/variante.md), [Capacidades y aislamiento](../c/capacidades-y-aislamiento.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md).

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

[↑ Glosario](../../README.md) · [← Punto de equilibrio de costo](./punto-de-equilibrio-de-costo.md) · [Punto de no retorno →](./punto-de-no-retorno.md)
