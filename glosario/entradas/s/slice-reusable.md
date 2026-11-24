# Slice reusable

[↑ Glosario](../../README.md) · [← SLI](./sli.md) · [Slicing, vistas y copias →](./slicing-vistas-y-copias.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un **slice reusable** (porción reutilizable) es, en el taller de [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), la **capacidad pequeña** que se extrae de un sistema para empaquetarla y consumirla por separado, elegida porque tiene **entrada, salida, errores y dependencias claros**. «Slice» significa rebanada: no se empaqueta todo el sistema, sino una parte con una frontera nítida. El término es propio del programa; en otros contextos se habla de extraer un módulo o un componente.

## Por qué importa

La tentación al crear una biblioteca es extraer «todo lo que sirva». Pero [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) advierte que **extraer todo el sistema crea una API extensa antes de entender a los consumidores**: cada función expuesta es una promesa que mantener, y se promete sin saber qué se usará. La decisión que cambia es el tamaño del primer paso: una capacidad pequeña, probada de punta a punta como paquete instalable, que enseña qué hace falta antes de ampliar. Es una forma de aprender barato.

## Cómo funciona

Un buen *slice* cumple cuatro condiciones:

- **Entrada y salida claras:** tipos y formatos conocidos, sin depender de estado global del producto original.
- **Errores definidos:** sabe fallar de forma que el consumidor lo entienda.
- **Dependencias acotadas:** pocas y declaradas, de modo que instalar el paquete no arrastre medio sistema.
- **Semántica conservada:** el comportamiento es el mismo que en el producto original; el paquete no «mejora» ni cambia reglas al extraerlo.

Lo que no es parte de la capacidad (acceso a la base de datos del producto, configuración específica, formato de archivos propio) se queda como **adaptadores en el producto original**: el producto llama al paquete a través de ellos. Así la dependencia va en una dirección (el producto depende del paquete) y el paquete no conoce al producto.

El *slice* se valida con el procedimiento del taller: construir sdist y wheel, instalarlos en un entorno limpio y probar desde fuera del repositorio con solo importaciones públicas. Dos defectos típicos aparecen aquí: el paquete instalado no encuentra su archivo de datos porque falta `package-data`, y `ModuleNotFoundError` solo en un entorno limpio porque una dependencia no está declarada.

## Ejemplo

Del motor de la biblioteca de estructuras y algoritmos se extrae solo la elección del siguiente caso:

```text
paquete:    engineering_sdk
capacidad:  choose_next(casos, politica) -> caso
entrada:    lista de casos con id, prioridad, dependencias, llegada
salida:     un caso o None si no hay elegible
errores:    ValueError si un caso no tiene id; CicloDeDependencias
dependencias: ninguna fuera de la biblioteca estándar
queda en el producto: lectura de archivos, formato de salida, configuración
```

Es pequeña, tiene frontera clara y se puede probar desde un directorio externo. No incluye el planificador completo, el formato de reportes ni la configuración, que seguirán en el producto y se extraerán, si hace falta, cuando se entiendan los consumidores.

## Errores y confusiones comunes

- **Extraer todo.** Se promete una API grande sin conocer su uso.
- **Arrastrar el estado global del producto.** El paquete queda acoplado a su origen.
- **Cambiar el comportamiento al extraer.** El producto original y el paquete divergen.
- **No declarar dependencias.** Falla en entorno limpio.

## Límites y cuándo no aplica

El taller verifica una versión y un entorno principal ([SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md)); la compatibilidad entre versiones y plataformas la construye el proyecto siguiente. Si la capacidad solo se usa en un lugar, empaquetarla es esfuerzo sin retorno. Un *slice* demasiado pequeño (una función de tres líneas) cuesta más mantener como paquete que copiar. Y a veces la frontera no es nítida: si la capacidad está entrelazada con el resto, la primera tarea es separar, no empaquetar.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Capacidad](../c/capacidad.md), [Dependencia](../d/dependencia.md), [Api y cli coherentes](../a/api-y-cli-coherentes.md), [Artefacto e instalación](../a/artefacto-e-instalacion.md), [Cambio compatible](../c/cambio-compatible.md), [Diseño desde consumidor](../d/diseno-desde-consumidor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← SLI](./sli.md) · [Slicing, vistas y copias →](./slicing-vistas-y-copias.md)
