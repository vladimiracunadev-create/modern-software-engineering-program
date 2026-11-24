# Poscondición

[↑ Glosario](../../README.md) · [← Portal documental](./portal-documental.md) · [Postcondición →](./postcondicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Una **poscondición** es la propiedad que una operación garantiza al terminar, siempre que se haya cumplido su contrato ([SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md)). [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) la formula como lo que la rutina garantiza al terminar. Es la mitad del contrato que obliga al proveedor; la otra mitad, la precondición, obliga a quien llama.

## Por qué importa

Una operación sin poscondición explícita no se puede probar ni consumir con seguridad: nadie sabe qué esperar. Con ella, el cliente puede apoyarse en el resultado y las pruebas tienen un oráculo. [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) la usa para que, cuando una función falla, se sepa quién se equivocó: sin contrato escrito, el defecto cae en un limbo.

## Cómo funciona

La poscondición relaciona estado previo, entrada y salida ([SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md)). La diferencia entre débil y contrastable es el valor práctico:

- **Débil:** «devuelve una lista».
- **Contrastable:** «devuelve solo pruebas autorizadas y toda hipótesis descartada cita evidencia».

Una operación puede garantizar distintas poscondiciones para éxito y para error: por ejemplo, en éxito el estado cambió y se devuelve el nuevo valor; en error, el estado no cambió y se informa la causa. Lo que la implementación garantiza incluye también lo que no oculta: en la clase, las observaciones contradictorias se informan, no se esconden. La poscondición se puede ejecutar como afirmación (`assert`), como prueba basada en propiedades o como contrato en tiempo de ejecución ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) la trata como parte de un contrato ejecutable).

## Ejemplo

```python
def descartar(hipotesis, evidencia):
    assert hipotesis in estado.abiertas                     # precondición
    resultado = _descartar(hipotesis, evidencia)
    assert resultado.cita == evidencia and hipotesis not in estado.abiertas   # poscondición
    return resultado
```

La poscondición dice qué es verdad después: la hipótesis ya no está abierta y el resultado cita la evidencia.

## Errores y confusiones comunes

- **La función falla sin decir quién se equivocó.** Causa: contrato implícito; corrección: escribir precondición, invariante y poscondición ([SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md)).
- **Poscondición vacía.** «Devuelve algo» no permite decidir si el resultado es correcto.
- **Confundirla con la precondición.** La poscondición es obligación del proveedor; la precondición, del cliente.

## Límites y cuándo no aplica

Una poscondición bien escrita puede ser cara de comprobar en producción: se verifica en pruebas y se desactiva o se muestrea después. Algunas propiedades (equidad, calidad de una recomendación) no se expresan como un predicado simple. Y la poscondición solo vale si la precondición se cumplió: si el cliente la violó, el proveedor no promete nada ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)).

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato](../c/contrato.md), [Propiedad](./propiedad.md), [Composición](../c/composicion.md), [Contrato del consumidor](../c/contrato-del-consumidor.md), [Dominio](../d/dominio.md), [Estado válido](../e/estado-valido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Portal documental](./portal-documental.md) · [Postcondición →](./postcondicion.md)
