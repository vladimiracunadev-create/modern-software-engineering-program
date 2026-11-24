# Migración

[↑ Glosario](../../README.md) · [← MicroVM](./microvm.md) · [Migración reversible →](./migracion-reversible.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Una **migración** es un cambio versionado del esquema o de los datos que se aplica en orden y deja registro de que se aplicó. Es el sentido principal de la clase [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) (generación de pruebas, documentación y migraciones). [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) lo usa en aplicaciones: la transformación explícita de un estado guardado por una versión anterior a la forma que espera la versión actual. El común es que algo guardado con una forma antigua debe pasar a una nueva sin perderse.

## Por qué importa

Una conversión sin error no es una conversión correcta. El riesgo está en los valores que no encajan, y esos pasan las comprobaciones habituales. Cambia la decisión de qué se verifica después de migrar: no basta que el script termine.

## Cómo funciona

[SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) describe el mecanismo del fallo silencioso: SQLite convierte con `CAST` el prefijo numérico de un texto y devuelve cero si no hay ninguno, sin error ni aviso; otros motores lanzan error o devuelven nulos, y cada uno tiene sus reglas. Un script generado sin conocer los valores reales convierte «NP», cadenas vacías o «5,5,0» en ceros o en números parciales plausibles, y el recuento de filas coincide: las comprobaciones habituales no lo ven.

De ahí un procedimiento defendible:

1. **Perfilar** los valores reales antes de escribir la conversión.
2. **Definir** qué hacer con cada clase de valor que no encaja (rechazar, marcar, mapear).
3. **Aplicar en orden**, con registro de versión aplicada.
4. **Verificar** contra reglas del dominio, no solo recuentos.

En [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), al reanudar una aplicación, el estado guardado por una versión anterior pasa por una migración explícita antes de usarse.

## Ejemplo

Ilustración propia basada en el riesgo de la clase: una columna de notas en texto, con valores «NP» (no presentó) y «5,5». Una conversión directa a número las transforma en 0 o en 5, y el número de filas sigue igual. Una migración cuidada trata «NP» como ausencia, normaliza la coma y falla con un informe de las filas no convertibles.

## Errores y confusiones comunes

- **Confiar en que el recuento de filas valida la migración.**
- **Aplicar un script generado sin revisar los valores reales** ([SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md)).
- **Migrar sin versión registrada,** de modo que no se sabe qué se aplicó.
- **Confundirla con una reescritura o con el cambio de plataforma.**

## Límites y cuándo no aplica

Una migración que modifica datos no siempre es reversible; conviene copia previa y plan de vuelta atrás. Las reglas de conversión dependen del motor concreto. Y para esquemas que cambian de forma compatible (añadir una columna opcional), el costo es menor, pero sigue necesitando orden y registro.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Esquema](../e/esquema.md), [Estado](../e/estado.md), [Registro](../r/registro.md), [Ciclo de vida](../c/ciclo-de-vida.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (104 clases más lo mencionan; las que más):

[SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Migraciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — migraciones pequeñas y versionadas; autoridad: autores del texto.
- [Jia y Harman, «An Analysis and Survey of the Development of Mutation Testing»](https://doi.org/10.1109/TSE.2010.62) — pruebas de mutación; autoridad: IEEE Transactions on Software Engineering.
- [Barr et al., «The Oracle Problem in Software Testing: A Survey»](https://doi.org/10.1109/TSE.2014.2372785) — el problema del oráculo; autoridad: IEEE Transactions on Software Engineering.
- [Python: doctest](https://docs.python.org/3/library/doctest.html) — ejecución de ejemplos en docstrings; autoridad: documentación de Python.
- [SQLite: datatypes](https://www.sqlite.org/datatype3.html) — tipificación y afinidad; autoridad: documentación de SQLite.

---

[↑ Glosario](../../README.md) · [← MicroVM](./microvm.md) · [Migración reversible →](./migracion-reversible.md)
