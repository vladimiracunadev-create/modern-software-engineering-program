# Producción

[↑ Glosario](../../README.md) · [← Proceso sin estado](./proceso-sin-estado.md) · [Producto →](./producto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

En el vocabulario de métricas del programa, la **producción** (*output*) es lo que el equipo entrega, contable y controlable: líneas de código, versiones, tickets cerrados, funciones lanzadas ([SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)). No es el entorno de producción donde corre el software (ese es otro concepto del glosario), sino el primer eslabón de la cadena producción → actividad → resultado.

## Por qué importa

Es lo más fácil de contar y por eso lo más fácil de convertir en meta. Cambia cómo se evalúa a un equipo: con producción se mide cuánto hizo; con resultado, qué cambió en la vida de quien usa el producto. [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) advierte que un equipo con alta producción y resultados nulos es posible, y que uno con poca producción y alto resultado también.

## Cómo funciona

La producción tiene una virtud y un límite. La virtud: es **controlable por el equipo** y se cuenta sin ambigüedad (un ticket está cerrado o no). El límite: **no dice si lo producido sirvió**. Un ticket cerrado puede resolver un problema real o ser trabajo innecesario; una función lanzada puede ser ignorada.

Por eso sirve para **planificar capacidad** (cuánto puede entregar el equipo en un periodo) y no para evaluar valor. Cuando se convierte en meta se activa la ley de Goodhart: la gente optimiza la cifra. [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) describe dos síntomas con su causa: la meta se cumple y nadie mejora (se premió la producción), y un equipo gana premios con malos resultados (se compararon producciones). La corrección es acompañar o reemplazar la producción con un resultado y su métrica contraria, y comparar equipos por resultado o por una métrica equilibrada.

En la auditoría de métricas de la plataforma, cada métrica se clasifica en producción, actividad, resultado o vanidad, con la decisión que informa y su métrica contraria. Esa clasificación hace visible cuántas métricas del panel son solo producción.

## Ejemplo

El equipo de la plataforma cierra 40 tickets en el trimestre y lanza 6 funciones: es producción. Si la meta fuera «cerrar más tickets», un equipo podría dividir un ticket en tres para triplicar la cifra. Si la meta es «porcentaje de entregas aceptadas a la primera», mejora solo si el trabajo hace que más estudiantes lo logren, y entonces la producción queda como un medio. (Ilustración construida sobre el escenario de la clase.)

## Errores y confusiones comunes

- **Premiar la producción**: la meta se cumple y nadie mejora.
- **Comparar equipos por producción**: un equipo gana premios con malos resultados.
- **Confundirla con el entorno de producción**: son sentidos distintos de la misma palabra.
- **Descartarla del todo**: es útil para capacidad y para ver si el flujo de trabajo funciona.

## Límites y cuándo no aplica

No sirve para medir valor ni calidad. En contextos donde el entregable es el objetivo (una obra por encargo con alcance fijo), la producción es en buena medida el resultado, y la distinción pierde fuerza. Aun así, una entrega contratada puede cumplirse a cabalidad y no resolver el problema de quien la pidió.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Actividad](../a/actividad.md), [Ley de Goodhart](../l/ley-de-goodhart.md), [Métrica de vanidad](../m/metrica-de-vanidad.md), [Resultado](../r/resultado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (259 clases más lo mencionan; las que más):

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «output».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir qué medir a partir de lo que se necesita saber; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) — cómo medir satisfacción como complemento de indicadores de uso; autoridad: Government Digital Service.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — mecanismos por los que una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv (D. Manheim y S. Garrabrant).
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas de entrega; autoridad: DORA (Google Cloud).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Proceso sin estado](./proceso-sin-estado.md) · [Producto →](./producto.md)
