# Diseño desde consumidor

[↑ Glosario](../../README.md) · [← Diseño de errores](./diseno-de-errores.md) · [Diseño pareado →](./diseno-pareado.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

El **diseño desde consumidor** es, en el taller de [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), la práctica de escribir la prueba de un paquete **desde un directorio externo al repositorio, usando solo imports públicos**, y sin *mocks* de internals. La prueba se coloca en la posición de quien consume el producto: no conoce la estructura interna, no puede importar módulos privados y depende solo de lo que el paquete publica. Es una técnica del programa asociada a las pruebas de contrato escritas «desde el consumidor».

## Por qué importa

Quien escribe una biblioteca sabe cosas que el consumidor ignora: qué módulo contiene cada función, qué argumentos tienen valores razonables por defecto, qué excepción se espera. Esas suposiciones se cuelan en las pruebas hechas desde dentro, que pasan aunque el uso real sea incómodo o imposible. La decisión que cambia es qué prueba cuenta como evidencia de que el paquete es usable: la que ejecuta alguien que solo tiene lo público. [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) dice que esto revela **nombres, defaults, errores y documentación** que el autor daba por supuestos.

## Cómo funciona

Cuatro reglas hacen que la prueba sea de consumidor de verdad:

- **Directorio externo.** La prueba vive fuera del árbol de código del paquete, para que Python no resuelva imports contra el código fuente y se use el paquete **instalado**.
- **Solo imports públicos.** Se importa lo que la API declara; si hace falta entrar a un módulo interno para algo corriente, falta un símbolo público.
- **Sin mocks de internals.** Si se simulan funciones privadas, se prueba la implementación, no la promesa. Se pueden simular recursos externos (red, disco), pero no el interior del paquete.
- **Entorno limpio.** Se instala el artefacto en un entorno vacío, de modo que una dependencia no declarada aparezca como fallo.

Cada fricción que aparece es información: un nombre confuso, un parámetro obligatorio que debería tener valor por defecto, un error que no dice qué hacer. La causa de que el método encuentre esto es que elimina el conocimiento privilegiado del autor.

## Ejemplo

En el taller de [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), la prueba del paquete reutilizable vive fuera del repositorio y solo hace esto:

```python
# prueba_consumidor.py  (en un directorio aparte, con el paquete instalado)
from engineering_sdk import choose_next      # único import: público

def test_elige_el_mas_urgente():
    casos = [{"id": 1, "prioridad": 2}, {"id": 2, "prioridad": 1}]
    assert choose_next(casos)["id"] == 2
```

Si para escribirla hace falta importar `engineering_sdk._interno.reglas`, o pasar cinco argumentos que el autor siempre usa igual, el diseño tiene un defecto de uso. Los dos fallos documentados por la clase aparecen aquí: el archivo de datos no encontrado (falta `package-data`) y el `ModuleNotFoundError` solo en entorno limpio (dependencia no declarada).

## Errores y confusiones comunes

- **Prueba dentro del paquete.** Importa por rutas relativas y oculta problemas de instalación.
- **Mockear internals.** La prueba pasa aunque el comportamiento público esté roto.
- **Usar el código fuente en lugar del instalado.** El resultado no representa lo que recibe el consumidor.
- **Reescribir la prueba del autor y llamarla de consumidor.** Si usa los mismos atajos, no aporta información nueva.

## Límites y cuándo no aplica

El taller verifica una versión y un entorno principal ([SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md)); no cubre otros sistemas ni versiones de dependencias, tarea de la matriz de compatibilidad. La prueba de consumidor encuentra problemas de usabilidad en lo que ejercita, pero no sustituye las pruebas unitarias del interior, que localizan defectos con más precisión. Para módulos internos no publicados, que nadie consume desde fuera, el enfoque no tiene sentido.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Api y cli coherentes](../a/api-y-cli-coherentes.md), [Artefacto e instalación](../a/artefacto-e-instalacion.md), [Cambio compatible](../c/cambio-compatible.md), [Slice reusable](../s/slice-reusable.md).
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

[↑ Glosario](../../README.md) · [← Diseño de errores](./diseno-de-errores.md) · [Diseño pareado →](./diseno-pareado.md)
