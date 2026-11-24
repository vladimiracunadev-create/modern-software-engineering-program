# Propiedad

[↑ Glosario](../../README.md) · [← Propagación de contexto](./propagacion-de-contexto.md) · [Propiedad de archivos →](./propiedad-de-archivos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

En pruebas, una **propiedad** es una afirmación que debe cumplirse para toda entrada del dominio de una función, y que se comprueba con muchas entradas generadas ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md)). Es la base de las pruebas basadas en propiedades (*property-based testing*). No debe confundirse con la «propiedad de archivos» (ownership, quién es responsable de qué) ni con una propiedad de un objeto o una clase.

## Por qué importa

Dice qué debe cumplirse sin enumerar casos. Una prueba de ejemplos comprueba lo que alguien pensó; una propiedad cubre una región entera del dominio y encuentra entradas en las que nadie pensó. Cambia cómo se diseñan las pruebas: en lugar de «para 3 y 4 devuelve 7», se afirma «la suma de las cantidades repartidas es `n`».

## Cómo funciona

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) da ejemplos de propiedades: la suma de las cantidades repartidas es `n`; normalizar dos veces da lo mismo que normalizar una (idempotencia); invertir una lista dos veces devuelve la original. Un generador produce entradas (por ejemplo, 200 casos aleatorios) y el marco comprueba la propiedad en cada una. Se escribe **sin repetir la implementación**: «el resultado es lo que calcula la función» no comprueba nada.

La clase enumera familias útiles de propiedades: invariantes que se conservan, idempotencia, relaciones entre entradas (si se añade un elemento, el resultado cambia así), comparación con un modelo más simple y propiedades metamórficas. Dos mecanismos hacen utilizable el método. El **generador** debe llegar a las fronteras (listas vacías, valores límite, combinaciones), con sesgo hacia ellas; si no, la propiedad pasa y el defecto sigue ahí. Y la **reducción** (*shrinking*): ante un contraejemplo de 22 elementos, el marco lo reduce a su forma mínima antes de analizarlo, porque un contraejemplo enorme no se entiende ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)).

## Ejemplo

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) incluye un fragmento que comprueba tres propiedades de una función de reparto con 200 casos aleatorios y pide predecir si pasa la versión que olvida el resto. Una propiedad ilustrativa:

```python
@given(st.integers(0, 1000), st.integers(1, 10))
def test_reparto_suma_n(n, k):
    assert sum(repartir(n, k)) == n
```

Si `repartir` pierde el resto de la división, el marco encuentra un contraejemplo pequeño como `n=1, k=2` tras reducir. (Código ilustrativo con la biblioteca Hypothesis; la clase usa su propio fragmento.)

## Errores y confusiones comunes

- **La propiedad pasa y la función tiene un defecto conocido**: el generador no llega a la frontera; corrección: sesgo hacia vacío, límites y combinaciones.
- **La propiedad repite la implementación**: se calcula el esperado con la misma fórmula; corrección: invariantes o un modelo distinto.
- **Contraejemplo ilegible**: no hay reducción.
- **Creer que reemplaza las pruebas de ejemplos**: se complementan; los ejemplos documentan y fijan casos concretos.

## Límites y cuándo no aplica

No toda función tiene propiedades fáciles de enunciar; a veces solo se conoce el resultado esperado para casos concretos. Con generadores mal diseñados da una falsa sensación de cobertura. Las propiedades pasan con 200 casos y pueden fallar con el 201: son pruebas probabilísticas, no demostraciones. Las operaciones lentas o con efectos externos encarecen la ejecución de cientos de casos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Dominio](../d/dominio.md), [Función](../f/funcion.md), [Tipo](../t/tipo.md), [Command](../c/command.md), [Contrato de consumidor](../c/contrato-de-consumidor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (274 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Propiedades».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claessen y Hughes, «QuickCheck: a lightweight tool for random testing of Haskell programs»](https://doi.org/10.1145/351240.351266) — pruebas por propiedades; autoridad: artículo original de ICFP 2000.
- [Documentación de Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de propiedades para Python; autoridad: documentación oficial.
- [Hughes, «How to Specify It!»](https://doi.org/10.1007/978-3-030-47147-7_4) — estrategias para escribir propiedades; autoridad: capítulo del autor.
- [Hypothesis: pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) — comparación con modelos; autoridad: documentación oficial.
- [MacIver et al., «Hypothesis: A new approach to property-based testing»](https://joss.theoj.org/papers/10.21105/joss.01891) — diseño de la biblioteca; autoridad: artículo revisado de JOSS.

---

[↑ Glosario](../../README.md) · [← Propagación de contexto](./propagacion-de-contexto.md) · [Propiedad de archivos →](./propiedad-de-archivos.md)
