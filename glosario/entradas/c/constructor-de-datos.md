# Constructor de datos

[↑ Glosario](../../README.md) · [← Construcción reproducible](./construccion-reproducible.md) · [Consulta parametrizada →](./consulta-parametrizada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Función que crea un dato de prueba con valores por defecto y permite cambiar solo lo relevante.

Definición de trabajo de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md).

## Por qué importa

La clase donde se define, [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), existe con este propósito: la clase existe para que prepares el estado de cada prueba de forma que el resultado dependa solo del código y de los datos declarados, y para que identifiques y elimines las fuentes de no determinismo (orden de ejecución, azar, hora, identificadores, orden de colecciones).

## Cómo funciona

Según [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md):

Un conjunto de reglas evita discusiones y accidentes: los datos son sintéticos y nunca copias de producción; cada prueba declara solo los datos que le importan (el resto toma valores por defecto de un constructor); los valores con significado de negocio se nombran (`plazo_vencido`, `nota_en_el_limite`) y no se escriben como números sueltos; y toda fuente de azar recibe una semilla que se registra. Los constructores de datos de prueba (builders) reducen el acoplamiento a los cambios de esquema respecto de grandes archivos de datos compartidos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md):

El equipo de la plataforma adopta cuatro reglas. Primera: cada prueba de servicio abre una transacción sobre una base creada una vez por proceso y la deshace al terminar; las pruebas de migración, que hacen commit, crean su propia base. Segunda: la suite se ejecuta cada noche en un orden aleatorio con semilla impresa; un fallo se repite con `--semilla`. Tercera: toda prueba con datos aleatorios recibe un generador con semilla de un único punto, y la semilla va en el informe.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)) son:

- **Las pruebas pasan una a una y fallan juntas** — causa: estado compartido mutable. Corrección: transacción con retroceso o base nueva por prueba.
- **Una prueba falla una vez de cada diez** — causa: datos aleatorios sin semilla o propiedad mal enunciada. Corrección: registrar la semilla y revisar la propiedad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con una base SQLite en memoria, una propiedad con datos sintéticos y procesos locales en Windows y Ubuntu (WSL2) con salidas idénticas salvo las cifras que dependen del sistema o de la ejecución, declaradas arriba. Cinco de las doce pruebas dependen del estado compartido por diseño, y la propiedad falla por un efecto del redondeo escogido por el autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor por defecto](../v/valor-por-defecto.md), [Función](../f/funcion.md), [Valor](../v/valor.md), [Dependencia del orden](../d/dependencia-del-orden.md), [Determinismo](../d/determinismo.md), [Fixture](../f/fixture.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «builder».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas del no determinismo; autoridad: autor del texto.
- [pytest: cómo usar fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — ámbitos y limpieza; autoridad: documentación oficial de pytest.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` y `ROLLBACK`; autoridad: documentación oficial de SQLite.
- [Documentación del módulo random](https://docs.python.org/3/library/random.html) — semillas y límites; autoridad: documentación oficial de Python.
- [Martin Fowler, «ObjectMother»](https://martinfowler.com/bliki/ObjectMother.html) — fábricas de datos de prueba; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Construcción reproducible](./construccion-reproducible.md) · [Consulta parametrizada →](./consulta-parametrizada.md)
