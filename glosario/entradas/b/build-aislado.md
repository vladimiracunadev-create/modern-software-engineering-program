# Build aislado

[↑ Glosario](../../README.md) · [← Build & Release Engineer](./build-release-engineer.md) · [Build hermético →](./build-hermetico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un **build aislado** es una construcción de paquete que se ejecuta con los **requisitos de build declarados** en el proyecto, en lugar de usar lo que casualmente haya instalado en la máquina de quien construye. En [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md) aparece junto al backend de construcción: el proyecto declara qué herramientas necesita para construirse (por ejemplo en `[build-system]` de `pyproject.toml`) y el constructor las instala en un entorno temporal. Es distinto de un build **reproducible**, que además exige que el resultado sea idéntico byte a byte; aislar es condición necesaria, no suficiente.

## Por qué importa

Si un paquete se construye con el entorno del autor, el resultado depende de detalles invisibles: una versión de herramienta instalada hace meses, una variable de entorno, un archivo local. Otra persona (o el servidor de integración) obtiene otro artefacto o un fallo. La decisión que cambia es qué se considera «el build»: no «lo que sale en mi máquina», sino «lo que sale de las entradas declaradas». Así, los requisitos faltantes se convierten en un error inmediato y no en un defecto que aparece en el equipo de un consumidor.

## Cómo funciona

El mecanismo tiene tres elementos:

- **Declaración.** El proyecto lista los requisitos de construcción y el backend que los usa.
- **Entorno temporal vacío.** El constructor crea un entorno limpio, instala solo lo declarado y ejecuta el backend allí. Cualquier módulo no declarado produce un error de importación en lugar de resolverse con lo que hubiera disponible.
- **Resultado como función de las entradas declaradas.** Lo producido (sdist, wheel) depende de fuentes y requisitos, no del entorno del autor.

[SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md) marca el límite de la idea: aislar no vuelve reproducible. Marcas de tiempo dentro de los archivos, orden de los miembros del archivo comprimido y versión de la cadena de herramientas pueden variar entre construcciones y cambiar los hashes aunque el contenido sea equivalente. Por eso solo se afirma «hash igual» después de **comparar bytes bajo un protocolo declarado** (mismas entradas, misma fecha fijada, mismo entorno), no por haber ejecutado dos veces.

## Ejemplo

En el producto reutilizable con SDK y CLI, el release debe contener artefactos inmutables y procedencia. Un fallo típico que el aislamiento revela es el de un archivo de datos que existe en el árbol de trabajo pero no entra en el paquete: aparece como `FileNotFoundError` solo tras instalar, y la corrección es declarar el archivo en `package-data` y comprobar el contenido de la rueda contra una lista esperada. Otro caso de [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md): `import json` devuelve un objeto raro porque un `json.py` local tapa la biblioteca estándar; se detecta ejecutando con `-I` (modo aislado) o `-P`.

```bash
python -m build            # aísla por defecto: crea un entorno temporal
python -I -c "import json; print(json.__file__)"
```

## Errores y confusiones comunes

- **Tomar «aislado» por «reproducible».** Dos construcciones aisladas pueden producir hashes distintos por marcas de tiempo.
- **Declarar solo dependencias de ejecución.** Las herramientas de construcción también deben declararse, o el build depende del entorno del autor.
- **Afirmar igualdad de hashes sin comparar.** Debe compararse el contenido bajo un protocolo escrito.
- **Dejar archivos locales en la ruta de importación.** Un módulo local con nombre de la biblioteca estándar altera el resultado.

## Límites y cuándo no aplica

Un paquete instalado todavía necesita una interfaz operable y estable ([SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md)). Un build aislado no protege frente a una dependencia comprometida: instala lo que se declara desde donde se declara, sin verificar procedencia. Y para un script personal que nunca se distribuye, el costo de declarar y aislar construcciones no se compensa. El grado de rigor debería corresponder a cuántas personas consumirán el artefacto.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Backend](./backend.md), [Entorno](../e/entorno.md), [Metadata de proyecto](../m/metadata-de-proyecto.md), [Módulo, paquete e importación](../m/modulo-paquete-e-importacion.md), [Publicación y repositorio](../p/publicacion-y-repositorio.md), [Sdist y wheel](../s/sdist-y-wheel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-112 — Paquetes, módulos y publicación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Build & Release Engineer](./build-release-engineer.md) · [Build hermético →](./build-hermetico.md)
