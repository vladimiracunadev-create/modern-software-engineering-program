# Cobertura

[↑ Glosario](../../README.md) · [← Coalescencia](./coalescencia.md) · [Cobertura combinatoria →](./cobertura-combinatoria.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Mutaciones detectadas sobre mutaciones inyectadas.

Definición de trabajo de [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md): Fracción de los defectos reales que el revisor marca.
- En [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md): Fracción de veces que un intervalo contiene el resultado real; un intervalo está calibrado si su cobertura es la anunciada.

## Por qué importa

En [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), el tema «Cobertura» importa porque dice qué familia ve cada regla.

## Cómo funciona

Según [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md):

Un revisor automático emite una puntuación de sospecha por cambio y un umbral decide cuáles se marcan. Dos cantidades describen el resultado. La **precisión** es la fracción de lo marcado que era un defecto real; la **cobertura** (o recall), la fracción de los defectos reales que se marcaron. Subir el umbral sube la precisión y baja la cobertura; bajarlo hace lo contrario. No existe un umbral correcto en abstracto: depende del costo de una alarma falsa (tiempo de lectura y desgaste de la atención) frente al costo de un defecto omitido (un incidente en producción). Hay un efecto añadido: cuando la precisión cae, las personas aprenden a ignorar las alarmas, y entonces la cobertura efectiva del proceso se hunde por debajo de la del revisor.

Según [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones define un procedimiento para los cambios asistidos. El revisor automático se fija con umbral 0,60 tras medir, en doscientos cambios etiquetados del año anterior, 58 % de precisión y 72 % de cobertura; la persona que revisa lee primero las alarmas y después el diff completo, y la aprobación nombra a quien responde. Para una refactorización de la agrupación por curso, el equipo exige una comparación diferencial con 5 000 entradas generadas con fronteras (cursos repetidos, nota 0,0, lista de un elemento, más de cinco notas por curso) y la ejecución de las pruebas de caracterización; el diff debe ser menor de 40 líneas y no incluir cambios de estilo.

## Ejemplo

Ejemplo de [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones define un procedimiento para los cambios asistidos. El revisor automático se fija con umbral 0,60 tras medir, en doscientos cambios etiquetados del año anterior, 58 % de precisión y 72 % de cobertura; la persona que revisa lee primero las alarmas y después el diff completo, y la aprobación nombra a quien responde.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se pierden defectos que el revisor sí podía marcar** — causa: umbral alto sin medir la cobertura. Corrección: elegir el umbral con costos explícitos. ([SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una persona que ha visto cientos de alarmas inútiles tiende a ignorar el revisor, y entonces el umbral bajo ya no da cobertura. ([SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo](../i/intervalo.md), [Mutación](../m/mutacion.md), [Resultado](../r/resultado.md), [Sobre](../s/sobre.md), [Clase de referencia](./clase-de-referencia.md), [Control](./control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (104 clases más lo mencionan; las que más):

[SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Airbnb](../../../casos/exito/airbnb.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «recall».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bacchelli y Bird](https://doi.org/10.1109/ICSE.2013.6606617) — revisión de código moderna: expectativas, resultados y desafíos; autoridad: ICSE 2013.
- [Google: Engineering Practices, code review](https://google.github.io/eng-practices/review/) — guía pública de revisión; autoridad: documentación de Google.
- [Fowler, «Refactoring»](https://refactoring.com/) — definición y práctica de la refactorización; autoridad: autor del texto.
- [Claessen y Hughes, «QuickCheck»](https://doi.org/10.1145/351240.351266) — pruebas de propiedades con entradas aleatorias; autoridad: ICFP 2000.
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de pruebas de propiedades para Python; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Coalescencia](./coalescencia.md) · [Cobertura combinatoria →](./cobertura-combinatoria.md)
