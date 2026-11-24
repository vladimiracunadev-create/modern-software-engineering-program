# Generación determinista

[↑ Glosario](../../README.md) · [← Generación](./generacion.md) · [Generación estática →](./generacion-estatica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

La **generación determinista** es la propiedad de un generador que produce salida idéntica para la misma entrada ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)). Un generador (de clientes, de documentación, de diagramas, de índices) es determinista si ejecutarlo dos veces sobre la misma fuente da exactamente los mismos bytes.

## Por qué importa

Un generador que no es reproducible hace imposible comparar y revisar lo generado. Si cada regeneración produce un resultado distinto aunque la fuente no cambió, el diff está lleno de ruido, no se puede comprobar si lo comprometido coincide con lo que genera la fuente, y los cambios reales se pierden entre los falsos. Cambia el diseño de un generador y de su integración continua.

## Cómo funciona

[SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) señala las **fuentes habituales de no determinación**:

- **Iterar estructuras sin orden garantizado**: en Python, el orden de iteración de un conjunto de cadenas puede cambiar entre procesos porque el valor de hash de las cadenas se aleatoriza por proceso; recorrerlo y emitir en ese orden da salidas distintas.
- **Marcas de tiempo** o **rutas absolutas** incrustadas en la salida.
- **Configuración regional**: formatos de fecha, número y orden alfabético que dependen del entorno.

La regla de diseño es **ordenar todo lo que se emite** (claves, nodos, aristas, archivos) con un criterio explícito y estable, eliminar o normalizar lo dependiente del entorno (fechas, rutas) y fijar la semilla de hash cuando se comprueba.

La comprobación de que funciona es mecánica: regenerar y comparar huellas con lo comprometido; si hay diferencias, la integración continua falla. En la plataforma de entregas, los clientes se generan desde el documento OpenAPI (spec-as-source) con un generador que ordena toda su salida y **marca la región generada**; una comprobación regenera y compara huellas.

El segundo fallo que la clase enlaza es la **regeneración que borra trabajo manual**: se editó dentro de lo generado. La corrección es delimitar la región generada y mover lo manual fuera. La generación determinista es también la base de la construcción reproducible: sin ella, comparar artefactos no dice nada.

## Ejemplo

Un generador emite un diagrama con las dependencias de un conjunto de servicios iterando un `set` de Python. En cada ejecución las aristas salen en distinto orden y el archivo cambia, así que cada regeneración produce un diff de decenas de líneas aunque nada cambió. Al ordenar nodos y aristas alfabéticamente antes de emitir, la salida es idéntica y el diff vacío. (Ilustración del mecanismo de [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) y [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md).)

## Errores y confusiones comunes

- **Cada regeneración produce un diff enorme**: el generador no ordena su salida.
- **Incluir la fecha de generación** en el archivo.
- **Rutas absolutas** del equipo que genera.
- **Editar a mano dentro de lo generado.**

## Límites y cuándo no aplica

El determinismo se pierde si cambian la versión del generador o sus dependencias; hay que fijarlas. Para salidas que deben incluir una marca de tiempo por razones de negocio, se separa del contenido comparado. Un generador determinista puede generar algo incorrecto; solo garantiza reproducibilidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generador](./generador.md), [Propiedad](../p/propiedad.md), [Deriva](../d/deriva.md), [Spec-anchored](../s/spec-anchored.md), [Spec-as-source](../s/spec-as-source.md), [Spec-first](../s/spec-first.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Böckeler, «Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl»](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — distinción entre spec-first, spec-anchored y spec-as-source; autoridad: martinfowler.com.
- [GitHub: spec-kit](https://github.com/github/spec-kit) — herramienta de código abierto de flujo guiado por especificación; autoridad: GitHub.
- [OpenAPI Generator](https://openapi-generator.tech/) — generación de clientes y servidores desde un documento de especificación; autoridad: proyecto OpenAPI Generator.
- [Python: `PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED) — aleatorización del hash y semilla fija; autoridad: documentación de Python.
- [Python: `inspect`](https://docs.python.org/3/library/inspect.html) — lectura de firmas de funciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Generación](./generacion.md) · [Generación estática →](./generacion-estatica.md)
