# Costo del experimento

[↑ Glosario](../../README.md) · [← Costo de un experimento](./costo-de-un-experimento.md) · [Costo estructural →](./costo-estructural.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Peticiones dañadas (o minutos equivalentes de caída total) que el experimento consume del presupuesto de error.

Definición de trabajo de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

## Por qué importa

En [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), el tema «Costo del experimento» importa porque el daño se contabiliza en peticiones y en presupuesto de error.

## Cómo funciona

[SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe la especificación del experimento «almacenamiento con 20 % de errores»: radio de 2 % del tráfico durante 10 minutos, aborto si el grupo experimental falla más de 50 % en 10 s o si el servicio global baja de 99,5 % en 30 s, reversión «quitar la regla del proxy» probada la víspera con un tiempo de 4 s, responsable la guardia de la API, ventana de martes a jueves de 10:00 a 16:00 y nunca en una semana de cierre de plazo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)) son:

- **El experimento no detecta nada y se declara confirmado** — causa: radio sin potencia suficiente. Corrección: calcular la fracción mínima y declarar el efecto mínimo detectable.
- **El experimento aborta de inmediato** — causa: condición global consumida por la falla esperada. Corrección: medir el grupo experimental y separar el umbral de aborto del de la hipótesis.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se dañó ninguna petición real; el servicio de 8 hilos, el 5 % de errores, la sorpresa a los 60 s, las 60 repeticiones y los umbrales de aborto son construcciones del autor, y las condiciones se evaluaron con el mismo escenario con que se diseñaron.

## Relación con otros conceptos

- **Prerrequisito:** [Presupuesto de error](../p/presupuesto-de-error.md).
- **Ver también:** [Presupuesto](../p/presupuesto.md), [Condición de aborto](./condicion-de-aborto.md), [Especificación del experimento](../e/especificacion-del-experimento.md), [Radio de explosión](../r/radio-de-explosion.md), [Retroceso](../r/retroceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — minimizar el radio de explosión; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Netflix: «ChAP: Chaos Automation Platform»](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — tamaño de experimento, control y experimento, interruptor del experimento; autoridad: blog de ingeniería de Netflix.
- [AWS FIS: stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) — condiciones de parada basadas en alarmas; autoridad: documentación de Amazon Web Services.
- [Chaos Mesh: Define the Scope of Chaos Experiments](https://chaos-mesh.org/docs/define-chaos-experiment-scope/) — selectores y radio de explosión; autoridad: documentación del proyecto Chaos Mesh.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Costo de un experimento](./costo-de-un-experimento.md) · [Costo estructural →](./costo-estructural.md)
