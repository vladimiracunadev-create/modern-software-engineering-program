# Compatibilidad hacia atrás

[↑ Glosario](../../README.md) · [← Compatibilidad hacia adelante](./compatibilidad-hacia-adelante.md) · [Compatibilidad hacia atrás y hacia adelante →](./compatibilidad-hacia-atras-y-hacia-adelante.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Un cambio es **compatible hacia atrás** (*backward compatible*) cuando lo que ya funcionaba con la versión anterior sigue funcionando con la nueva. El programa lo usa en dos planos que conviene no mezclar. En el plano de una **API o paquete** ([SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md)), una versión nueva es compatible hacia atrás si los consumidores válidos anteriores siguen funcionando bajo el contrato publicado. En el plano de **datos y mensajes** ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)), lo es si un lector que usa el esquema nuevo puede leer datos escritos con el esquema viejo. Es el opuesto direccional de la compatibilidad **hacia adelante**, en que un lector viejo entiende datos nuevos; un cambio que cumple ambas es **completo**.

## Por qué importa

Los sistemas reales no se actualizan todos a la vez: hay clientes sin migrar, colas con mensajes retenidos, registros de meses y consumidores que se despliegan antes que sus productores. La compatibilidad es la propiedad que permite cambiar una parte sin coordinar el instante exacto de cambio de todas las demás. Decide, además, cuánto tiempo hay que mantener una versión: [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) observa que un log retenido durante meses exige compatibilidad hacia atrás durante meses, y esa duración, no el código, fija cuánto vive cada versión.

## Cómo funciona

La compatibilidad no es una propiedad solo del esquema; depende de cómo lee el consumidor y de en qué dirección viaja el dato ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)).

- **Qué dirección necesitas.** Cuando hay datos viejos que leer (un almacén que se lee con código nuevo, una cola atrasada, un consumidor que se despliega primero) necesitas compatibilidad hacia atrás. Cuando hay lectores viejos activos mientras los productores ya escriben con el esquema nuevo (una API que se actualiza primero en el servidor) necesitas compatibilidad hacia adelante.
- **Lector tolerante o estricto.** Un lector tolerante usa los campos que conoce e ignora los demás; uno estricto rechaza cualquier campo desconocido. Con el primero, añadir un campo es compatible hacia adelante; con el segundo, no.
- **Orden de despliegue.** Con un cambio compatible hacia atrás se despliegan primero los consumidores (leen lo nuevo y lo viejo) y después los productores; con uno compatible solo hacia adelante, primero los productores; con uno incompatible no hay orden seguro y hay que dividirlo en fases ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)).
- **Comprobación automática.** El número de versión comunica intención, pero nadie verifica que diga la verdad: [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) insiste en comparar esquemas en integración continua y exigir versión mayor para las rupturas, y [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) describe el registro de esquemas que rechaza un cambio incompatible antes de publicarlo.

## Ejemplo

[SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) aplicó diez cambios a un esquema de cuatro campos (`id` y `nota` requeridos, `estado` requerido con dos valores y `comentario` opcional) y midió cuántos de 2 000 documentos se leían sin error. Quitar un campo opcional se leyó en las tres situaciones. Añadir un campo requerido se leyó para el lector viejo tolerante, pero el lector nuevo no pudo leer ninguno de los documentos viejos (0 de 2 000): ese cambio no es compatible hacia atrás. Renombrar un campo no se leyó en ninguna situación, lo que muestra que «renombrar» no es un cambio sino una eliminación seguida de una adición. Los números provienen de datos sintéticos de la clase.

## Errores y confusiones comunes

- **«Solo agrega» y rompe a un cliente.** El cliente es estricto con campos o valores desconocidos. Corrección ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)): documentar que los consumidores deben tolerar lo desconocido y probar con un valor nuevo.
- **El número de versión sube y los clientes se rompen igual.** Se versionó por intención y no se comprobó la compatibilidad. Corrección: comparar esquemas en integración continua.
- **Añadir un valor de enumeración.** Ningún registro de formas lo detecta: ambos lectores viejos rechazan el valor nuevo, y la política del consumidor ante lo desconocido decide si es un incidente o una pérdida silenciosa ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)).
- **Confundir las dos direcciones.** Atrás habla del lector nuevo y los datos viejos; adelante, del lector viejo y los datos nuevos. Muchos cambios son compatibles en una sola.
- **Una ventana de deprecación que termina con clientes activos.** Parte de los consumidores no migra sola; hay que medir quién usa lo viejo y decidir el corte con un responsable ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)).

## Límites y cuándo no aplica

Cumplir una regla de compatibilidad no garantiza que un cambio sea seguro: [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md) advierte que agregar un parámetro opcional puede romper reflexión, mocks o serialización, de modo que la evaluación necesita pruebas reales y no solo la intuición de quien cambia. SemVer es un lenguaje común, no una prueba: una «versión menor» que cambia el significado de un campo rompe igual ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)). El registro de esquemas conoce la forma, no el sentido, y no sustituye el ensayo con consumidores reales. Y mantener compatibilidad tiene un costo: cuanto más tiempo se sostiene una versión, más caminos de código y datos viejos hay que conservar.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato](./contrato.md), [Esquema](../e/esquema.md), [Propiedad](../p/propiedad.md), [Versión](../v/version.md), [API pública](../a/api-publica.md), [Compatibilidad hacia adelante](./compatibilidad-hacia-adelante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md).

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

[↑ Glosario](../../README.md) · [← Compatibilidad hacia adelante](./compatibilidad-hacia-adelante.md) · [Compatibilidad hacia atrás y hacia adelante →](./compatibilidad-hacia-atras-y-hacia-adelante.md)
