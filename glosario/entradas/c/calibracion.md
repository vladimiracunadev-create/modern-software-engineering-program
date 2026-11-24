# Calibración

[↑ Glosario](../../README.md) · [← Calentamiento](./calentamiento.md) · [Calidad de servicio →](./calidad-de-servicio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

**Calibración** es la correspondencia entre la confianza que anuncia un pronóstico y la frecuencia con que se cumple. El sentido principal es el de [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md): un pronóstico está calibrado si el resultado real cae por debajo de su percentil 85 el 85 % de las veces. El programa lo reutiliza con el mismo núcleo en [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (probabilidad predicha frente a frecuencia observada en un modelo), en [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) (confianza declarada de una respuesta generativa frente a su tasa de acierto) y en [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) (probabilidad declarada en una revisión de decisión frente a lo que ocurrió).

## Por qué importa

Cambia si un número se puede usar para decidir. Un percentil o una probabilidad solo valen si significan lo que dicen: si «85 %» se cumple el 60 % de las veces, quien planifica con él está asumiendo un riesgo mayor del que cree. La calibración es la prueba de que el lenguaje de la incertidumbre, ya sea fechas de entrega o probabilidades de un modelo, es fiable.

## Cómo funciona

Se comprueba contra la realidad, no con argumentos. [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) propone una retrospectiva: simular muchos proyectos con un proceso conocido, pronosticar cada uno con su historia y contar cuántas veces se cumplió el pronóstico. Es, según la clase, la única manera de saber si «85 %» significa 85 %.

Dos fuentes de descalibración dominan en la planificación. La primera es la **historia corta**: con pocas semanas de datos se subestima la incertidumbre sobre la propia media, y el intervalo sale demasiado estrecho. La segunda son los **efectos que el modelo no incluye**, como el crecimiento del alcance: un pronóstico hecho solo con la historia de rendimiento supone que el trabajo pendiente no cambia. La corrección es ensanchar el intervalo o apoyarse en una clase de referencia cuando la historia es de menos de unas doce semanas.

En modelos ([SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md)) la lógica es idéntica: se agrupan las predicciones por probabilidad declarada y se compara con la frecuencia observada en cada grupo.

## Ejemplo

En el taller de [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) se simulan muchos proyectos con un proceso conocido. Para cada uno se pronostica la fecha con la historia disponible y se cuenta en cuántos el real quedó por debajo del percentil 85. Si el cumplimiento resulta inferior al 85 %, el pronóstico está sobreconfiado, y el taller muestra cuánto con el propio proceso. La clase observa que, cuanta más historia, mejor, pero con pocas semanas conviene ensanchar el intervalo.

## Errores y confusiones comunes

- **Confundir calibración con precisión.** Un pronóstico puede ser impreciso (intervalo ancho) y estar bien calibrado; uno estrecho puede estar descalibrado.
- **Creer que un percentil «vale» sin comprobarlo.** Sin retrospectiva, «85 %» es una etiqueta.
- **Ignorar el crecimiento del alcance.** El modelo con solo rendimiento histórico sobreestima su confianza.
- **Evaluar con una sola ocurrencia.** Un acierto o fallo aislado no dice nada: la calibración es una propiedad de muchas predicciones.

## Límites y cuándo no aplica

Requiere muchas predicciones comparables; con pocos casos la frecuencia observada es ruidosa y no permite concluir. Las clases lo practican con procesos simulados de proceso conocido, que no incluyen todas las perturbaciones de un proyecto real. Y no sustituye a la discriminación: un modelo bien calibrado puede ser inútil si da la misma probabilidad a todo. Es una condición necesaria para confiar en una probabilidad, no suficiente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confianza](./confianza.md), [Relación](../r/relacion.md), [Colchón de proyecto](./colchon-de-proyecto.md), [Ejercicio previo al fallo](../e/ejercicio-previo-al-fallo.md), [Expansión del trabajo](../e/expansion-del-trabajo.md), [Expediente de la decisión](../e/expediente-de-la-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.
- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Therac-25](../../../casos/fallo/therac-25.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Guo et al., «On Calibration of Modern Neural Networks»](https://arxiv.org/abs/1706.04599) — calibración y error de calibración esperado; autoridad: ICML 2017.
- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo; autoridad: The Annals of Statistics.
- [Malcolm et al., «Application of a technique for research and development program evaluation» (Operations Research, 1959)](https://doi.org/10.1287/opre.7.5.646) — PERT y combinación de varianzas; autoridad: Operations Research.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — clases de referencia y optimismo; autoridad: Project Management Journal.
- [Buehler, Griffin y Ross, «Exploring the planning fallacy» (Journal of Personality and Social Psychology, 1994)](https://doi.org/10.1037/0022-3514.67.3.366) — subestimación del tiempo propio; autoridad: Journal of Personality and Social Psychology.

---

[↑ Glosario](../../README.md) · [← Calentamiento](./calentamiento.md) · [Calidad de servicio →](./calidad-de-servicio.md)
