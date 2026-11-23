# Parámetro

[↑ Glosario](../../README.md) · [← Paralelismo](./paralelismo.md) · [Paridad →](./paridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Nombre local declarado por una función.

Definición de trabajo de [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md).

## Por qué importa

La clase donde se define, [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), existe con este propósito: la clase existe para usar funciones como contratos con parámetros, retorno, efectos y alcance localizables.

## Cómo funciona

Según [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md):

`def` crea una función; la llamada enlaza argumentos a parámetros y ejecuta un nuevo marco. `return` termina y entrega un valor; sin `return` explícito devuelve `None`. Imprimir un resultado no equivale a retornarlo: impide composición y pruebas simples.

Según [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md):

Pasa una referencia a un objeto, por valor. Mutar el objeto es visible para quien llama; reasignar el parámetro no. Medido: la lista quedó `[1, 9]` tras mutar y reasignar.

## Ejemplo

Ejemplo de [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md) (sección «Preguntas frecuentes»):

Pasa una referencia a un objeto, por valor. Mutar el objeto es visible para quien llama; reasignar el parámetro no. Medido: la lista quedó `[1, 9]` tras mutar y reasignar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`UnboundLocalError` al leer un nombre que «existe»** — causa: una asignación posterior lo hace local en toda la función. Corrección: renombrar, pasar como parámetro o declarar `nonlocal`/`global` con razón. ([SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md))
- **`TypeError` por argumentos posicionales de más** — causa: firma con parámetros solo por nombre o con barra. Corrección: pasar por nombre y leer `inspect.signature`. ([SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los parámetros solo por nombre son una herramienta de diseño: una llamada como `evaluate(spec, budget=5)` documenta la unidad en el sitio de uso y no se rompe si se reordenan los parámetros. ([SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Función](../f/funcion.md), [Alcance](../a/alcance.md), [Argumento](../a/argumento.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (168 clases más lo mencionan; las que más):

[SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Paralelismo](./paralelismo.md) · [Paridad →](./paridad.md)
