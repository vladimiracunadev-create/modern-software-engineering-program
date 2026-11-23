# Prueba unitaria

[↑ Glosario](../../README.md) · [← Prueba que pasa de inmediato](./prueba-que-pasa-de-inmediato.md) · [Pseudolocalización →](./pseudolocalizacion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Comprobación de una unidad pequeña cuyo resultado no depende de recursos que la prueba no controla.

Definición de trabajo de [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md).

## Por qué importa

En [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), el tema «Qué comprueba una prueba unitaria» importa porque distingue ejecutar una línea de afirmar un resultado.

## Cómo funciona

Según [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md):

Una prueba unitaria llama a una unidad con una entrada conocida y afirma algo sobre el resultado o el efecto visible. La unidad suele ser una función o una clase pequeña; lo decisivo es que el resultado no dependa de nada que la prueba no controle. Ejecutar una línea no es comprobarla: una prueba sin aserciones, o con una aserción que no puede fallar, «cubre» código sin protegerlo. Cada prueba debe poder responder qué cambio del código la haría fallar, y si la respuesta es «ninguno», es ruido.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md):

El equipo de la plataforma separa la función de cierre en tres: `calcular_nota(bruta, horas)` (pura), `horas_tarde(plazo, ahora)` (aritmética de fechas) y `cerrar(entregas, ahora, guardar, avisar)`, que orquesta. La hora real se lee en un único punto, el controlador que llama a `cerrar`. Para cada regla por tramos, una tabla de casos lista el tramo, la frontera, el valor esperado y la razón de negocio («una entrega a las 24 horas exactas sigue en el primer tramo porque la política dice "hasta 24 horas"»).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)) son:

- **La cobertura es 100 % y un cambio de operador no rompe ninguna prueba** — causa: casos típicos sin valores en las fronteras. Corrección: tabla de fronteras y medida con mutantes.
- **Una prueba falla de vez en cuando sin cambios en el código** — causa: depende del reloj, del azar o del orden. Corrección: inyectar la hora y la semilla; ver `SE-428` y `SE-430`.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con una función sintética en Windows y Ubuntu (WSL2) con salidas idénticas. Los mutantes son cambios mecánicos y no defectos humanos; el modelo de pausas de la prueba con reloj real es un supuesto. No se midió tiempo de ejecución ni se usó un marco de pruebas distinto de `assert`.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Resultado](../r/resultado.md), [Costura](../c/costura.md), [Frontera](../f/frontera.md), [Mutante equivalente](../m/mutante-equivalente.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Documentación de unittest](https://docs.python.org/3/library/unittest.html) — organización de pruebas; autoridad: documentación oficial de Python.
- [Documentación de unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — dobles; autoridad: documentación oficial de Python.
- [Documentación del módulo ast](https://docs.python.org/3/library/ast.html) — árbol sintáctico; autoridad: documentación oficial de Python.
- [Martin Fowler, «UnitTest»](https://martinfowler.com/bliki/UnitTest.html) — qué es una unidad; autoridad: autor del texto.
- [xUnit Patterns: Test Double](http://xunitpatterns.com/Test%20Double.html) — tipos de dobles; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Prueba que pasa de inmediato](./prueba-que-pasa-de-inmediato.md) · [Pseudolocalización →](./pseudolocalizacion.md)
