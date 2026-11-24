# Temperatura

[↑ Glosario](../../README.md) · [← Telemetría](./telemetria.md) · [Template Method →](./template-method.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

La **temperatura** es el parámetro de muestreo de un modelo de lenguaje que concentra o reparte la probabilidad entre las continuaciones posibles ([SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)).

## Por qué importa

Un modelo recibe un contexto y calcula una distribución de probabilidad sobre el siguiente símbolo; se elige uno, se añade y se repite. De ahí [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) deduce: la salida no es una consulta a una base de hechos, es la continuación *probable* de un texto, y una continuación probable puede ser falsa. La temperatura decide cuánto se arriesga al elegir.

## Cómo funciona

Con temperatura baja, la distribución se concentra y se elige casi siempre lo más probable; con temperatura alta, se reparte y aparecen alternativas. Bajarla reduce la variación entre ejecuciones; con semilla fija, cuando la herramienta la admite, se reduce más. Aun así, en servicios cuya infraestructura introduce otras fuentes de variación, no desaparece del todo.

## Ejemplo

Para extraer un campo estructurado se usa temperatura baja; para generar variantes de un texto, mayor. La respuesta de temperatura cero es la más probable según el modelo.

## Errores y confusiones comunes

- **Creer que temperatura cero da la respuesta correcta.** [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md): es la más probable, no la correcta; da repetibilidad, no corrección.
- **Se acepta una respuesta porque «suena segura».** Tono no es calibración; medir acierto por tramos con tareas del equipo.
- **Votar entre varias respuestas y confirmar un error.** Los errores están correlacionados; añadir un comprobador externo.

## Límites y cuándo no aplica

La temperatura no existe como control en todos los modelos o servicios. No sustituye a una verificación externa de lo que el modelo afirma.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Muestreo](../m/muestreo.md), [Parámetro](../p/parametro.md), [Calibración](../c/calibracion.md), [Confabulación](../c/confabulacion.md), [Modelo generativo](../m/modelo-generativo.md), [Modo de fallo](../m/modo-de-fallo.md).
- **Se confunde con:** Obtienes la respuesta más probable según el modelo, que no es lo mismo que la correcta; y aun con temperatura cero algunos servicios devuelven variaciones por otras fuentes de no determinismo.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Holtzman et al., «The Curious Case of Neural Text Degeneration»](https://arxiv.org/abs/1904.09751) — generación como muestreo y degeneración al elegir lo más probable; autoridad: ICLR 2020.
- [Wang et al., «Self-Consistency Improves Chain of Thought Reasoning»](https://arxiv.org/abs/2203.11171) — votar entre muestras de razonamiento; autoridad: ICLR 2023.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación de código con pruebas; autoridad: preprint de OpenAI.
- [Guo et al., «On Calibration of Modern Neural Networks»](https://arxiv.org/abs/1706.04599) — calibración y error de calibración esperado; autoridad: ICML 2017.
- [Liu et al., «Lost in the Middle»](https://arxiv.org/abs/2307.03172) — uso de la información según su posición en el contexto; autoridad: Transactions of the ACL.

---

[↑ Glosario](../../README.md) · [← Telemetría](./telemetria.md) · [Template Method →](./template-method.md)
