# Prueba unitaria

[↑ Glosario](../../README.md) · [← Prueba que pasa de inmediato](./prueba-que-pasa-de-inmediato.md) · [Pseudolocalización →](./pseudolocalizacion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Una **prueba unitaria** es la comprobación de una unidad pequeña cuyo resultado no depende de recursos que la prueba no controla ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)). Llama a la unidad (una función o una clase pequeña) con una entrada conocida y afirma algo sobre el resultado o el efecto visible.

## Por qué importa

Es la prueba más barata y rápida, y la base de la pirámide, pero solo vale por lo que *protege*. [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) lo dice así: ejecutar una línea no es comprobarla; una prueba sin aserciones, o con una aserción que no puede fallar, «cubre» código sin protegerlo.

## Cómo funciona

Lo decisivo es que el resultado no dependa de nada que la prueba no controle: reloj, azar, red, orden de ejecución. Si depende, se inyecta (la hora, la semilla). Cada prueba debe poder responder qué cambio del código la haría fallar; si la respuesta es «ninguno», es ruido. Una forma de medir si una suite protege es el **análisis de mutantes**: cambiar un operador y ver si alguna prueba falla.

## Ejemplo

```python
def test_aprueba_en_la_frontera():
    assert aprobado(4.0) is True
    assert aprobado(3.9) is False
```

Los valores 4,0 y 3,9 están en la frontera; una prueba con solo 6,0 no detectaría un cambio de `>=` a `>`.

## Errores y confusiones comunes

- **La cobertura es 100 % y un cambio de operador no rompe ninguna prueba.** Casos típicos sin valores de frontera; tabla de fronteras y medida con mutantes ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)).
- **Una prueba falla de vez en cuando sin cambios en el código.** Depende del reloj, del azar o del orden; inyectar la hora y la semilla.

## Límites y cuándo no aplica

No ve defectos de integración entre piezas (para eso, pruebas de integración y de contrato). Una suite muy acoplada a la implementación se rompe con cada refactor sin proteger comportamiento.

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
