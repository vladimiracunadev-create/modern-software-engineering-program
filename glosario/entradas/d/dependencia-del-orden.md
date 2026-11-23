# Dependencia del orden

[↑ Glosario](../../README.md) · [← Dependencia circular](./dependencia-circular.md) · [Dependencia directa →](./dependencia-directa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Resultado de una prueba que cambia según qué pruebas se ejecutaron antes.

Definición de trabajo de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md).

## Por qué importa

La clase donde se define, [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), existe con este propósito: la clase existe para que prepares el estado de cada prueba de forma que el resultado dependa solo del código y de los datos declarados, y para que identifiques y elimines las fuentes de no determinismo (orden de ejecución, azar, hora, identificadores, orden de colecciones).

## Cómo funciona

[SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra dependencia del orden con una base compartida. Antes de ejecutarlo, predice qué orden falla.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)) son:

- **Las pruebas pasan una a una y fallan juntas** — causa: estado compartido mutable. Corrección: transacción con retroceso o base nueva por prueba.
- **Una prueba falla una vez de cada diez** — causa: datos aleatorios sin semilla o propiedad mal enunciada. Corrección: registrar la semilla y revisar la propiedad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con una base SQLite en memoria, una propiedad con datos sintéticos y procesos locales en Windows y Ubuntu (WSL2) con salidas idénticas salvo las cifras que dependen del sistema o de la ejecución, declaradas arriba. Cinco de las doce pruebas dependen del estado compartido por diseño, y la propiedad falla por un efecto del redondeo escogido por el autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Constructor de datos](../c/constructor-de-datos.md), [Determinismo](./determinismo.md), [Fixture](../f/fixture.md), [Semilla](../s/semilla.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md).

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

[↑ Glosario](../../README.md) · [← Dependencia circular](./dependencia-circular.md) · [Dependencia directa →](./dependencia-directa.md)
