# Espía

[↑ Glosario](../../README.md) · [← Espera exponencial con aleatoriedad](./espera-exponencial-con-aleatoriedad.md) · [Espiral de la muerte →](./espiral-de-la-muerte.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Doble que registra las llamadas que recibe para consultarlas después.

Definición de trabajo de [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md).

## Por qué importa

La clase donde se define, [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), existe con este propósito: la clase existe para que decidas qué reemplazar en una prueba (un doble, una base en memoria, un contenedor, una máquina virtual) y cuánto te cuesta esa decisión en fidelidad, en acoplamiento a la implementación y en diferencias de entorno que cambian el resultado.

## Cómo funciona

Según [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md):

Un *dummy* rellena un parámetro que no se usa; un *stub* devuelve respuestas fijas; un *spy* registra las llamadas que recibe para que la prueba las consulte después; un *mock* tiene expectativas preprogramadas y falla si no se cumplen; un *fake* es una implementación funcional más simple (una base en memoria, un diccionario con reglas). La diferencia útil es qué verifica la prueba: con un stub o un fake, el estado resultante; con un mock, la interacción. Los dobles de estado envejecen mejor, porque no dependen de cómo se llegó al resultado.

Según [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md):

El equipo de la plataforma define una carpeta `contrato/` con una batería de ocho comprobaciones del repositorio de entregas y la ejecuta dos veces en la integración continua: contra SQLite en memoria y contra el fake del repositorio que usan las pruebas de servicio; si el fake no supera una comprobación que la base supera, la compilación falla. Las pruebas del servicio de avisos usan el fake y un espía de correo, verifican el estado (qué se envió y a quién) y solo conservan una prueba de interacción: la que comprueba que no se envían correos a estudiantes con nota. La integración continua fija `PYTHONHASHSEED`, abre todos los archivos con codificación y salto de línea explícitos, y ejecuta la batería en Windows y Ubuntu.

## Ejemplo

Ejemplo de [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma define una carpeta `contrato/` con una batería de ocho comprobaciones del repositorio de entregas y la ejecuta dos veces en la integración continua: contra SQLite en memoria y contra el fake del repositorio que usan las pruebas de servicio; si el fake no supera una comprobación que la base supera, la compilación falla. Las pruebas del servicio de avisos usan el fake y un espía de correo, verifican el estado (qué se envió y a quién) y solo conservan una prueba de interacción: la que comprueba que no se envían correos a estudiantes con nota.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se usa un servicio real en las pruebas y envía correos** — causa: no hay doble ni entorno aislado. Corrección: espía o servidor de pruebas y limpieza. ([SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un *dummy* rellena un parámetro que no se usa; un *stub* devuelve respuestas fijas; un *spy* registra las llamadas que recibe para que la prueba las consulte después; un *mock* tiene expectativas preprogramadas y falla si no se cumplen; un *fake* es una implementación funcional más simple (una base en memoria, un diccionario con reglas). ([SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Doble](../d/doble.md), [Doble de prueba](../d/doble-de-prueba.md), [Fake](../f/fake.md), [Fidelidad](../f/fidelidad.md), [Prueba de contrato](../p/prueba-de-contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-427 — Dobles, virtualización y entornos de prueba](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «spy».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [xUnit Patterns: Test Double](http://xunitpatterns.com/Test%20Double.html) — taxonomía de dobles; autoridad: autor del libro.
- [Martin Fowler, «TestDouble»](https://martinfowler.com/bliki/TestDouble.html) — resumen de dobles; autoridad: autor del texto.
- [Martin Fowler, «Mocks Aren't Stubs»](https://martinfowler.com/articles/mocksArentStubs.html) — estado frente a comportamiento; autoridad: autor del texto.
- [Documentación de unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — dobles en Python; autoridad: documentación oficial de Python.
- [Testcontainers](https://testcontainers.com/) — dependencias reales en contenedores desechables; autoridad: sitio oficial del proyecto.

---

[↑ Glosario](../../README.md) · [← Espera exponencial con aleatoriedad](./espera-exponencial-con-aleatoriedad.md) · [Espiral de la muerte →](./espiral-de-la-muerte.md)
