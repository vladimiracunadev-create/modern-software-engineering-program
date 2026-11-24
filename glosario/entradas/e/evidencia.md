# Evidencia

[↑ Glosario](../../README.md) · [← Evento, productor y manejador](./evento-productor-y-manejador.md) · [Evidencia de cumplimiento →](./evidencia-de-cumplimiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

**Evidencia** es un resultado concreto que sostiene una afirmación ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md)). [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) lo precisa para el cumplimiento: el resultado de una prueba o inspección con fecha, versión y huella que permite a otra persona verificar un control. No es una opinión ni un «confía en mí»: es algo que se puede mirar, repetir y atribuir a una versión.

## Por qué importa

Toda decisión de seguridad o de calidad es una afirmación («es aceptablemente seguro», «cumple») y sin evidencia es una creencia. La evidencia permite que alguien distinto del autor revise y desafíe. En sistemas críticos ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md)), es el eslabón que convierte un argumento en un caso defendible.

## Cómo funciona

En un caso de seguridad, [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) estructura tres preguntas: qué se afirma, por qué se cree (la estrategia de argumento) y con qué evidencia (resultados de pruebas, análisis, revisiones). Cada eslabón es visible y desafiable: quien lee puede preguntar «¿y si falla el sensor?» y hallar qué rama lo cubre. En la notación GSN, la evidencia es el nodo *solución*. [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) añade requisitos para que la evidencia sea utilizable: **fecha**, **versión** del objeto probado y **huella** del resultado, para que no se confunda con evidencia de otra versión. Y separa lo demostrable de lo que decide una persona competente: la evidencia técnica no equivale a conformidad.

## Ejemplo

[SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md): un comité lee la afirmación «la puerta abierta corta la potencia» y su evidencia, una prueba funcional con el horno vacío. Pregunta qué pasa con la carga a 240 °C. El caso no responde: el contexto no menciona la carga térmica y la evidencia no la incluye. El equipo no estaba equivocado; el argumento no cubría un escenario real. La respuesta fue añadir el escenario como supuesto de contexto con una prueba, y registrar la contribución del comité. Ilustración de un registro:

```text
prueba: puerta_abierta_corta_potencia | version: 1.4.2 | fecha: 2026-03-04 | huella: ver artefacto
```

## Errores y confusiones comunes

- **La evidencia es de hace seis meses.** Causa: pruebas manuales y esporádicas; corrección: automatizar y guardar resultado con fecha y huella por versión ([SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md)).
- **Declarar «cumple» sin revisión.** Causa: se confunde evidencia técnica con conformidad; corrección: separar lo demostrable de lo que decide una persona competente ([SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md)).
- **Evidencia huérfana.** Resultados que no sostienen ninguna afirmación; [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) usa un comprobador que detecta afirmaciones sin desarrollar y evidencias huérfanas.

## Límites y cuándo no aplica

La evidencia sostiene una afirmación acotada a un contexto y a una versión; no prueba lo que no cubre. Una gran cantidad de evidencia irrelevante no sustituye a la pertinente. Y el comprobador de [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) verifica la estructura del argumento, no la calidad de la evidencia ni si el caso es suficiente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Control](../c/control.md), [Huella](../h/huella.md), [Resultado](../r/resultado.md), [ADR](../a/adr.md), [Amenaza a validez](../a/amenaza-a-validez.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-024 — Proyecto: informe reproducible de comportamiento y recursos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (607 clases más lo mencionan; las que más):

[SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «solución».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Evento, productor y manejador](./evento-productor-y-manejador.md) · [Evidencia de cumplimiento →](./evidencia-de-cumplimiento.md)
