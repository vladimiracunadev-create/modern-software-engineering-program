# Postcondición

[↑ Glosario](../../README.md) · [← Poscondición](./poscondicion.md) · [Postmortem →](./postmortem.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Una **postcondición** es una condición que una operación garantiza al terminar, siempre que se haya cumplido su precondición ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)). Es la mitad de un contrato de diseño en el sentido de Meyer: la precondición es lo que el cliente debe cumplir; la postcondición, lo que el proveedor garantiza a cambio.

## Por qué importa

Fija lo que el cliente puede suponer tras la llamada sin tener que mirar cómo se calculó. Sin postcondiciones, quien usa la operación depende de lo que observó que hacía, y ese comportamiento puede cambiar sin aviso. Cambia dos cosas: cómo se documenta una operación (qué queda garantizado) y cómo se razona sobre herencia y sustitución.

## Cómo funciona

[SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) ilustra con `calificar`: tras la llamada, la nota está en el rango permitido y el estado es «calificada». Meyer presenta la postcondición como el **beneficio del cliente** a cambio de cumplir la precondición. Sirve a dos lectores: a la persona, que sabe qué puede suponerse; y al comprobador, que puede verificar en ejecución (con aserciones) o en pruebas que se cumple, sin conocer el cálculo.

La regla que conecta con la sustitución es la de la herencia: una subclase puede **aceptar al menos lo mismo** (precondición igual o más débil) y **garantizar al menos lo mismo** (postcondición igual o más fuerte). Si refuerza una precondición o debilita una postcondición, los clientes de la clase base se rompen aunque el código compile: es el síntoma que [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) señala. Es la base contractual del principio de sustitución de Liskov, y conecta con el subtipado conductual.

Su límite lo declara la clase: la postcondición solo afirma lo que está escrito. Una operación que duplica una prórroga sin pasar del tope cumple todas las postcondiciones que nadie escribió. Por eso conviene acompañar las postcondiciones con invariantes de clase y con pruebas.

## Ejemplo

[SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) declara una precondición y una postcondición para la prórroga y pide predecir cuál de dos llamadas falla. Una formulación equivalente, a modo de ilustración:

```python
def conceder_prorroga(entrega, horas):
    assert 0 < horas <= 72            # precondición
    anterior = entrega.plazo
    entrega.plazo = anterior + horas  # (horas, simplificado)
    assert entrega.plazo > anterior   # postcondición
```

La llamada con `horas = 0` viola la precondición (culpa del cliente); si la operación no mueve el plazo, viola la postcondición (culpa del proveedor).

## Errores y confusiones comunes

- **La subclase compila y rompe a los clientes de la base**: reforzó una precondición o debilitó una postcondición.
- **Postcondiciones que repiten la implementación**: no comprueban nada nuevo.
- **No escribir las que importan**: la operación cumple todas las que nadie escribió.
- **Confundirla con la precondición**: la primera obliga al proveedor; la segunda, al cliente.

## Límites y cuándo no aplica

Muchos lenguajes no tienen soporte nativo de contratos y las aserciones se desactivan en producción; entonces las postcondiciones sirven como documentación y como pruebas. No sustituyen la validación de entradas de fuentes externas. Algunas postcondiciones (por ejemplo, sobre estado externo, tiempo o concurrencia) son difíciles de expresar y de comprobar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Operación](../o/operacion.md), [Precondición](./precondicion.md), [Contrato ejecutable](../c/contrato-ejecutable.md), [Invariante](../i/invariante.md), [Invariante de clase](../i/invariante-de-clase.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Postcondiciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hoare, «An axiomatic basis for computer programming» (CACM, 1969)](https://doi.org/10.1145/363235.363259) — tripleta precondición–instrucción–postcondición; autoridad: Communications of the ACM.
- [Meyer, «Applying design by contract» (IEEE Computer, 1992)](https://doi.org/10.1109/2.161279) — formulación del diseño por contrato; autoridad: IEEE Computer.
- [Liskov y Wing, «A behavioral notion of subtyping» (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipado conductual y reglas de sustitución; autoridad: ACM TOPLAS.
- [Eiffel: Design by Contract](https://www.eiffel.com/values/design-by-contract/) — descripción del mecanismo en el lenguaje que lo introdujo; autoridad: Eiffel Software.
- [Python: sentencia `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) — semántica de `assert` y su desactivación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Poscondición](./poscondicion.md) · [Postmortem →](./postmortem.md)
