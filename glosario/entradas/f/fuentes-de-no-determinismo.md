# Fuentes de no determinismo

[↑ Glosario](../../README.md) · [← Fuente única](./fuente-unica.md) · [Fuerza →](./fuerza.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Las principales son: la hora actual, el azar sin semilla, los identificadores aleatorios, el orden de iteración de conjuntos y diccionarios con claves de cadena (que cambia con la semilla de hash por proceso), el orden de un listado de directorio (que depende del sistema de archivos), la suma de números de coma flotante en un orden que cambia, y los identificadores de memoria.

Explicación de la sección «Fuentes de no determinismo» de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md).

## Por qué importa

En [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), el tema «Fuentes de no determinismo» importa porque cada una tiene un remedio distinto.

En [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), el tema «Fuentes de no determinismo» importa porque una salida que varía entre ejecuciones invalida la comparación.

## Cómo funciona

Según [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), en la sección «Fuentes de no determinismo»:

Las principales son: la hora actual, el azar sin semilla, los identificadores aleatorios, el orden de iteración de conjuntos y diccionarios con claves de cadena (que cambia con la semilla de hash por proceso), el orden de un listado de directorio (que depende del sistema de archivos), la suma de números de coma flotante en un orden que cambia, y los identificadores de memoria. Cada una se elimina con una técnica distinta: inyectar el reloj, fijar o inyectar la semilla, inyectar el generador de identificadores, ordenar antes de comparar, sumar en orden fijo y no usar la identidad de los objetos como dato.

Según [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), en la sección «Fuentes de no determinismo»:

Para que una comparación de salidas sea válida, la salida debe depender solo de la entrada. Hay causas comunes que no son la lógica: el **orden de iteración de un conjunto o diccionario** (en Python el de conjuntos de cadenas cambia entre procesos por la semilla de hash), la **hora actual**, los **números aleatorios**, los **identificadores generados**, el **orden de archivos** devueltos por el sistema y la **zona horaria o configuración regional**. El método es siempre el mismo: detectar la variación (repetir la ejecución con condiciones distintas), localizar su fuente y normalizarla en la frontera de la prueba, ordenando, fijando semillas o inyectando el reloj. Normalizar demasiado oculta defectos reales: si la función debería devolver los alumnos en un orden específico por contrato, ordenar en la prueba lo esconde.

## Ejemplo

Ejemplo de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor. Esta clase deja el octavo artefacto: las reglas de fixtures del equipo, la transacción por prueba y el inventario de fuentes de no determinismo. `SE-429` pasa de lo que se puede automatizar a la exploración con criterio humano. Cambia después una sola decisión, el orden de ejecución a aleatorio con semilla, y observa si aparece una dependencia que nadie había notado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)) son:

- **Las pruebas pasan una a una y fallan juntas** — causa: estado compartido mutable. Corrección: transacción con retroceso o base nueva por prueba.
- **Una prueba falla una vez de cada diez** — causa: datos aleatorios sin semilla o propiedad mal enunciada. Corrección: registrar la semilla y revisar la propiedad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otra suite (por ejemplo, las pruebas de un sistema de reservas): ejecútalas en órdenes aleatorios, mide qué estrategia de fixture aísla mejor y a qué costo, e inventaría las fuentes de no determinismo. ([SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Constructor de datos](../c/constructor-de-datos.md), [Costura](../c/costura.md), [Dependencia del orden](../d/dependencia-del-orden.md), [Determinismo](../d/determinismo.md), [Fixture](./fixture.md), [Maestro dorado](../m/maestro-dorado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas del no determinismo; autoridad: autor del texto.
- [pytest: cómo usar fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — ámbitos y limpieza; autoridad: documentación oficial de pytest.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` y `ROLLBACK`; autoridad: documentación oficial de SQLite.
- [Documentación del módulo random](https://docs.python.org/3/library/random.html) — semillas y límites; autoridad: documentación oficial de Python.
- [Martin Fowler, «ObjectMother»](https://martinfowler.com/bliki/ObjectMother.html) — fábricas de datos de prueba; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Fuente única](./fuente-unica.md) · [Fuerza →](./fuerza.md)
