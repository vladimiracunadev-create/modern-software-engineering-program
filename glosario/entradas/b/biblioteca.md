# Biblioteca

[↑ Glosario](../../README.md) · [← Bfs y distancia no ponderada](./bfs-y-distancia-no-ponderada.md) · [Bind mount →](./bind-mount.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Una **biblioteca** (*library*) es un conjunto de funciones o tipos que el programa consumidor **llama y compone**. En la clase [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) se contrasta con framework, runtime, plataforma y SDK, y el criterio que las separa es quién ocupa el fondo de la pila: con una biblioteca el consumidor conserva el flujo principal de su programa y decide cuándo invocar. No es un sinónimo de «paquete» (la unidad de distribución) ni de «módulo» (una unidad de organización del código); una biblioteca se distribuye normalmente como paquete y contiene módulos.

## Por qué importa

Elegir entre biblioteca y framework decide quién manda sobre la estructura del programa. Con una biblioteca el costo de salir es bajo, porque se reemplaza una llamada por otra; con un framework, el programa se organiza alrededor de él y migrar es reescribir. [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) también cuida un error de comunicación: llamar «plataforma» a un conjunto de bibliotecas promete propiedad, soporte, cuotas y política de cambios que nadie ofrece. Nombrar bien el producto fija qué promete el equipo.

## Cómo funciona

El mecanismo es la **dirección de la llamada**. Con una biblioteca, el código del consumidor llama al de la biblioteca y recupera el control al retornar. Con un framework ocurre lo contrario: el framework llama al código del consumidor en puntos que él define (inversión de control, tema que [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) toma de Martin Fowler). Que una biblioteca sea pequeña o grande no cambia la categoría.

Una biblioteca, sin embargo, puede traer efectos o su propio runtime (hilos, conexiones, estado global). Por eso debe declarar en su API la **inicialización**, la **seguridad ante hilos** y el **ciclo de vida**: cuándo se crea, cuándo se cierra y qué pasa si se usa desde dos hilos. Si no lo declara, el consumidor tiene que descubrirlo en producción. La frontera entre lo que la biblioteca promete y lo que no es su API pública, con su versionado.

## Ejemplo

El producto reutilizable de [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) empaqueta el motor de la biblioteca de estructuras y algoritmos como `engineering_sdk`, expone la función `choose_next`, una CLI y un punto de extensión. El consumidor escribe su propio flujo y llama a la función cuando lo decide:

```python
from engineering_sdk import choose_next

for caso in cola:
    elegido = choose_next(caso, politica)   # el consumidor manda el flujo
```

El caso verifica instalación limpia, entrada válida, configuración ausente, plugin incompatible y actualización entre dos versiones, y cambia después una regla para revisar qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio es la que mide si la biblioteca está bien acotada.

## Errores y confusiones comunes

- **Llamar plataforma a un conjunto de bibliotecas.** Una plataforma exige responsable, SLO, cuotas y política de cambios; sin eso, es una biblioteca ([SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)).
- **Distinguir por tamaño o por nombre.** La diferencia con un framework es quién invoca a quién.
- **Ignorar el ciclo de vida.** Una biblioteca con estado global y sin inicialización documentada rompe cuando se usa desde dos hilos o dos veces.
- **Confundir biblioteca con SDK.** Un SDK agrupa bibliotecas con herramientas, documentación y ejemplos para una plataforma o servicio; hay una entrada propia.

## Límites y cuándo no aplica

La categoría es un espectro: una biblioteca que exige registrar *callbacks* y orquesta el flujo se parece ya a un framework. [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) ofrece criterio, no una frontera rígida. Tampoco toda reutilización requiere publicar una biblioteca: copiar veinte líneas puede costar menos que mantener un paquete versionado. Y una biblioteca con pocos consumidores internos no necesita la formalidad de un producto público; el esfuerzo debe corresponder a cuántos dependerán de ella.

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
