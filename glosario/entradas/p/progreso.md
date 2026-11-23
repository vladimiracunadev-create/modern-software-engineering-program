# Progreso

[↑ Glosario](../../README.md) · [← Programa de experimentos](./programa-de-experimentos.md) · [Promesa declarada →](./promesa-declarada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Cambio que acerca a la terminación.

Definición de trabajo de [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md).

## Por qué importa

La clase donde se define, [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), existe con este propósito: la clase existe para elegir iteración, recursión o recorrido manteniendo una invariante explícita.

## Cómo funciona

Según [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md):

`for` recorre un iterable; `while` repite mientras una condición sea verdadera. `for` comunica mejor un dominio finito conocido. `while` requiere una variable de progreso visible; depender de un evento externo exige deadline o cancelación.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md):

La CLI diagnóstica recorre un grafo con pila explícita y `visited`. Cada extracción consume un nodo y cada nodo se añade una vez. Un límite de nodos produce `INCOMPLETE` con cursor; no finge resultado completo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md)) son:

- **el resultado cambia según los datos, sin error** — causa: se elimina de la lista que se recorre. Corrección: construir una lista nueva o iterar sobre una copia.
- **`RuntimeError: dictionary changed size`** — causa: se añaden o quitan claves durante el recorrido. Corrección: recorrer `list(d)` o construir un diccionario nuevo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `while` requiere una variable de progreso visible; depender de un evento externo exige deadline o cancelación. ([SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Terminación](../t/terminacion.md), [Caso base](../c/caso-base.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md), [Invariante de bucle](../i/invariante-de-bucle.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (31 clases más lo mencionan; las que más):

[SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Programa de experimentos](./programa-de-experimentos.md) · [Promesa declarada →](./promesa-declarada.md)
