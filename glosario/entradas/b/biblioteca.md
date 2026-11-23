# Biblioteca

[↑ Glosario](../../README.md) · [← Bfs y distancia no ponderada](./bfs-y-distancia-no-ponderada.md) · [Bind mount →](./bind-mount.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Una biblioteca ofrece funciones o tipos que el programa consumidor llama y compone.

Definición de trabajo de [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md).

## Por qué importa

En [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), el tema «Biblioteca» importa porque una biblioteca ofrece funciones o tipos que el programa consumidor llama y compone.

## Cómo funciona

Según [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), en la sección «Biblioteca»:

Una biblioteca ofrece funciones o tipos que el programa consumidor llama y compone. El consumidor conserva el flujo principal. Una biblioteca puede traer efectos o runtime, pero debe declarar inicialización, thread safety y ciclo de vida en su API.

## Ejemplo

Ejemplo de [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) (sección «Caso conductor»):

El producto reutilizable con SDK y CLI empaqueta el motor de la biblioteca de estructuras y algoritmos como `engineering_sdk`, expone `choose_next`, una CLI y un punto de extensión. Ejecuta instalación limpia, entrada válida, configuración ausente, plugin incompatible y actualización entre dos versiones. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El producto se anuncia como «plataforma» pero no tiene responsable ni SLO** — causa: se confundió conjunto de librerías con plataforma. Corrección: escribir propiedad, soporte, cuotas y política de cambios, o llamarlo biblioteca. ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La diferencia entre biblioteca y framework no está en el tamaño ni en el nombre sino en quién ocupa el fondo de la pila. ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Función](../f/funcion.md), [Tipo](../t/tipo.md), [Framework e inversión de control](../f/framework-e-inversion-de-control.md), [Plataforma](../p/plataforma.md), [Runtime](../r/runtime.md), [Sdk](../s/sdk.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-109 — Biblioteca, framework, runtime, plataforma y SDK](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

**También se usa en** (535 clases más lo mencionan; las que más):

[SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler: Inversion of Control](https://martinfowler.com/bliki/InversionOfControl.html) — define la inversión de control y la distingue del uso de una biblioteca; es una explicación de práctica, no una norma.
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Bfs y distancia no ponderada](./bfs-y-distancia-no-ponderada.md) · [Bind mount →](./bind-mount.md)
