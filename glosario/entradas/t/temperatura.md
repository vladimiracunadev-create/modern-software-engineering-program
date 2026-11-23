# Temperatura

[↑ Glosario](../../README.md) · [← Telemetría](./telemetria.md) · [Template Method →](./template-method.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Parámetro de muestreo que concentra o reparte la probabilidad entre las continuaciones posibles.

Definición de trabajo de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Por qué importa

La clase donde se define, [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), existe con este propósito: la clase existe para que dejes de tratar a un modelo generativo como un oráculo o como un compañero con criterio, y lo trates como lo que es: un generador de texto que produce continuaciones plausibles a partir de una distribución de probabilidad, con habilidades útiles y con modos de fallo que no avisan.

## Cómo funciona

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

Un modelo de lenguaje, en el nivel de abstracción que importa para trabajar con él, recibe una secuencia de símbolos (el contexto) y calcula una distribución de probabilidad sobre cuál puede ser el siguiente; se elige uno, se añade a la secuencia y se repite. De ese mecanismo se deducen consecuencias prácticas sin necesidad de conocer la arquitectura interna. La primera es que la salida no es una consulta a una base de hechos: es la continuación probable de un texto, y una continuación probable puede ser falsa. La segunda es que hay una decisión de muestreo entre «tomar siempre lo más probable» y «tomar al azar según la distribución», y ese control, la **temperatura**, desplaza el comportamiento entre repetir con firmeza lo más probable y explorar alternativas.

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

No. Obtienes la respuesta más probable según el modelo, que no es lo mismo que la correcta; y aun con temperatura cero algunos servicios devuelven variaciones por otras fuentes de no determinismo. La temperatura baja da repetibilidad, no corrección.

## Ejemplo

Ejemplo de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra qué ocurre al bajar la temperatura cuando la respuesta correcta no es la más probable. Antes de ejecutarlo, predice qué porcentaje de las veces acertará la mayoría de cinco a temperatura 0,2.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son:

- **Se acepta una respuesta porque «suena segura»** — causa: se confunde tono con calibración. Corrección: medir acierto por tramos con tareas del propio equipo.
- **Se vota entre varias respuestas y se confirma un error** — causa: los errores están correlacionados. Corrección: añadir un comprobador externo (prueba, fuente).

Según [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md): Obtienes la respuesta más probable según el modelo, que no es lo mismo que la correcta; y aun con temperatura cero algunos servicios devuelven variaciones por otras fuentes de no determinismo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La tercera es que dos ejecuciones con la misma entrada pueden diferir: la variación no es un fallo sino la manifestación del muestreo, y se puede reducir (temperatura baja, semilla fija cuando la herramienta la admite) sin que desaparezca del todo en servicios cuya infraestructura introduce otras fuentes de variación. ([SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md))
- Obtienes la respuesta más probable según el modelo, que no es lo mismo que la correcta; y aun con temperatura cero algunos servicios devuelven variaciones por otras fuentes de no determinismo. ([SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md))

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
