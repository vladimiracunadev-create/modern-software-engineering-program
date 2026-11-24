# Cobertura

[↑ Glosario](../../README.md) · [← Coalescencia](./coalescencia.md) · [Cobertura combinatoria →](./cobertura-combinatoria.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

**Cobertura** designa en el programa una fracción de lo que se debía detectar o cubrir que realmente se detectó o cubrió. Tiene tres sentidos en esta serie: en [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) (pruebas de mutación y reglas), las mutaciones detectadas sobre las mutaciones inyectadas; en [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) (revisión asistida por IA), la fracción de los defectos reales que el revisor marca (en inglés *recall*); en [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) (estimación), la fracción de veces que un intervalo contiene el resultado real: un intervalo está calibrado si su cobertura es la anunciada. No es la cobertura de código (líneas o ramas ejecutadas).

## Por qué importa

Dice cuánto de lo que importa se está viendo. Una suite o un revisor con mucha precisión y poca cobertura es fiable cuando habla, pero calla casi siempre. Cambia cómo se interpreta una alarma o una ausencia de alarma: la ausencia solo tranquiliza si la cobertura es alta.

## Cómo funciona

[SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) lo explica con el compromiso entre precisión y cobertura. Un revisor automático emite una puntuación de sospecha por cambio y un umbral decide cuáles se marcan. La **precisión** es la fracción de lo marcado que era un defecto real; la **cobertura** (recall), la fracción de los defectos reales que se marcaron. **Subir el umbral sube la precisión y baja la cobertura**; bajarlo hace lo contrario. No existe un umbral correcto en abstracto: depende del costo de una falsa alarma (tiempo de lectura) frente al de un defecto que pasa.

El ejemplo de la clase fija el umbral en 0,60 tras medir, en doscientos cambios etiquetados del año anterior, 58 % de precisión y 72 % de cobertura; la persona que revisa lee primero las alarmas y después el diff completo, y la aprobación nombra a quien responde. Eso muestra por qué la cobertura debe medirse: el 28 % restante son defectos que el revisor no marca y que la lectura humana debe encontrar.

En el sentido de intervalos ([SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md)), la cobertura se comprueba con retrospectiva: si el intervalo del 85 % contiene el resultado real el 85 % de las veces, está calibrado; si cubre el 60 %, el intervalo es demasiado estrecho. En el sentido de mutación ([SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md)), la cobertura dice qué familias de defectos ve cada regla.

## Ejemplo

De cien defectos reales en una muestra de cambios, el revisor marca 72: cobertura del 72 %. De 124 cambios que marca, 72 eran defectos y 52 falsas alarmas: precisión del 58 %. Con el mismo revisor, bajar el umbral podría subir la cobertura al 85 % a cambio de 40 alarmas falsas más. (Cifras de [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) completadas con una aritmética ilustrativa.)

## Errores y confusiones comunes

- **Confundir cobertura con precisión**: una dice cuántos defectos se encontraron; la otra, cuántas alarmas eran reales.
- **Confundirla con cobertura de código**: ejecutar una línea no es detectar un defecto.
- **Medir con datos que el revisor ya vio.**
- **Hablar de cobertura sin decir de qué población.**

## Límites y cuándo no aplica

La cobertura depende de la muestra de defectos etiquetados, que puede no ser representativa. Los datos de [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) son un escenario hipotético, construido para la clase. Una cobertura alta no sustituye la revisión humana en los cambios críticos.

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
