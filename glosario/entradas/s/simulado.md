# Simulado

[↑ Glosario](../../README.md) · [← Simulacro](./simulacro.md) · [Singleton →](./singleton.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Doble programado con expectativas sobre las llamadas que recibirá.

Definición de trabajo de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

## Por qué importa

La clase donde se define, [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), existe con este propósito: la clase existe para que elijas con criterio qué comprueba una prueba: el **resultado** que el servicio deja en el mundo o las **llamadas** que hace a sus colaboradores.

## Cómo funciona

Según [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

Un **doble** es un objeto que ocupa el lugar de un colaborador en una prueba. Fowler distingue varios: un *stub* devuelve respuestas preparadas; un *fake* tiene una implementación real pero simplificada (una base de datos en memoria); un *mock* se programa con expectativas sobre las llamadas que recibirá. En Python, `unittest.mock.Mock` sirve para los tres usos según cómo se configure. Lo importante no es el nombre sino qué se verifica después: si el estado resultante o las llamadas recibidas.

Según [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

Pídele que justifique cada simulado: «¿es un efecto o una consulta?». Las consultas se sustituyen con un doble con estado o con el objeto real.

## Ejemplo

Ejemplo de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) (sección «Preguntas frecuentes»):

Pídele que justifique cada simulado: «¿es un efecto o una consulta?». Las consultas se sustituyen con un doble con estado o con el objeto real.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si el servicio pasa de pedir `pending_deliveries()` a pedir `all_deliveries()` y filtrar, la prueba de Londres que prepara `pending_deliveries.return_value` recibe un objeto simulado sin preparar donde esperaba una lista; el servicio falla. ([SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Doble](../d/doble.md), [Sobre](./sobre.md), [Cambio de contrato](../c/cambio-de-contrato.md), [Fake / doble con estado](../f/fake-doble-con-estado.md), [Verificación de comportamiento](../v/verificacion-de-comportamiento.md), [Verificación de estado](../v/verificacion-de-estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (102 clases más lo mencionan; las que más):

[SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «mock».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Simulacro](./simulacro.md) · [Singleton →](./singleton.md)
