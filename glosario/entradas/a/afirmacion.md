# Afirmación

[↑ Glosario](../../README.md) · [← Affordance percibida](./affordance-percibida.md) · [Afirmación refutable →](./afirmacion-refutable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Enunciado que se debe justificar.

Definición de trabajo de [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md).

## Por qué importa

En [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), el tema «Afirmación y estrategia» importa porque fija qué se afirma y cómo se descompone.

## Cómo funciona

Según [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md):

El caso responde tres preguntas: qué se afirma («el *Horno de curado* es aceptablemente seguro para curar muestras en un laboratorio con operadores formados, sobre una mesa, a menos de 250 °C»), por qué se cree (estrategia de argumento: se argumenta por cada peligro identificado, que tiene un control verificado) y con qué evidencia (resultados de pruebas, análisis, revisiones). Lo que lo distingue de un informe es que cada eslabón es visible y desafiable: quien lee puede preguntar «¿y si falla el sensor?» y encontrar qué rama responde. La notación gráfica más usada es la de estructuración de metas (GSN), con nodos de meta, estrategia, solución (evidencia), contexto, supuesto y justificación.

Según [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md):

El equipo entrega el caso de seguridad del horno al comité del laboratorio. Una persona del comité, formada en un laboratorio de química, lee la afirmación «la puerta abierta corta la potencia» y la evidencia: una prueba funcional con el horno vacío. Pregunta qué pasa si la puerta se abre con la carga a 240 °C y el aire caliente sale. El caso no responde: el contexto no menciona la carga térmica y la evidencia no la incluye. El equipo no estaba equivocado: el argumento no cubría un escenario real de uso, que el comité conocía y el equipo no. La respuesta fue añadir el escenario como supuesto de contexto con una prueba, y registrar que el comité había contribuido con ese desafío.

## Ejemplo

Ejemplo de [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) (sección «Ejemplo profesional»):

El equipo entrega el caso de seguridad del horno al comité del laboratorio. Una persona del comité, formada en un laboratorio de química, lee la afirmación «la puerta abierta corta la potencia» y la evidencia: una prueba funcional con el horno vacío. Pregunta qué pasa si la puerta se abre con la carga a 240 °C y el aire caliente sale. El caso no responde: el contexto no menciona la carga térmica y la evidencia no la incluye. El equipo no estaba equivocado: el argumento no cubría un escenario real de uso, que el comité conocía y el equipo no.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una afirmación **sin desarrollar** es una promesa: se declara que se justificará pero no hay nada debajo. ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md))
- Ejecuta un comprobador de afirmaciones sin desarrollar, evidencias huérfanas y únicas. ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Caso de seguridad](../c/caso-de-seguridad.md), [Enlace sospechoso](../e/enlace-sospechoso.md), [Estrategia](../e/estrategia.md), [Evidencia](../e/evidencia.md), [Supuestos](../s/supuestos.md), [Trazabilidad](../t/trazabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (607 clases más lo mencionan; las que más):

[SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «meta».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Affordance percibida](./affordance-percibida.md) · [Afirmación refutable →](./afirmacion-refutable.md)
