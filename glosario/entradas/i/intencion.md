# Intención

[↑ Glosario](../../README.md) · [← Integridad y dependency confusion](./integridad-y-dependency-confusion.md) · [Intención declarada y estrategia de ejecución →](./intencion-declarada-y-estrategia-de-ejecucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Deseo o necesidad de alguien, expresado sin comprometer un comportamiento observable.

Definición de trabajo de [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md): Acción única que quiere lograr el cliente, identificada por una clave.

## Por qué importa

En [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), el tema «Intención, especificación, plan y código» importa porque mezclarlos hace que el «cómo» se cuele en el «qué» y que las razones se pierdan.

## Cómo funciona

Según [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md):

La intención es el deseo de alguien: «que los estudiantes no pierdan entregas por olvido». La especificación declara qué comportamiento observable debe tener el sistema para satisfacerla y por qué importa: «cuando falten 72, 24 y 1 hora para el vencimiento y la entrega esté pendiente, el sistema enviará un aviso». El plan decide con qué se construye: una cola en SQLite, un proceso que despierta cada cinco minutos. Las tareas ordenan el trabajo. El código y las pruebas son el resultado. Cada nivel responde una pregunta distinta y, cuando se mezclan, aparecen dos fallos conocidos.

Según [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md):

La clave la genera el cliente por *intención* (una por cada «quiero crear esta entrega»), y se reutiliza en cada intento de esa intención. El servidor la guarda junto con el efecto y la respuesta, **en la misma transacción**, y una restricción única impide dos filas con la misma clave. Si la misma clave llega con una carga distinta, es un error del cliente (422) y no una repetición. La huella de la carga (un hash de su contenido canónico) permite distinguirlos.

## Ejemplo

Caso medido en la sección «Intención, especificación, plan y código» de [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md):

La intención es el deseo de alguien: «que los estudiantes no pierdan entregas por olvido». La especificación declara qué comportamiento observable debe tener el sistema para satisfacerla y por qué importa: «cuando falten 72, 24 y 1 hora para el vencimiento y la entrega esté pendiente, el sistema enviará un aviso». El plan decide con qué se construye: una cola en SQLite, un proceso que despierta cada cinco minutos. Las tareas ordenan el trabajo. El código y las pruebas son el resultado. Cada nivel responde una pregunta distinta y, cuando se mezclan, aparecen dos fallos conocidos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Entregas duplicadas tras un error de red** — causa: POST sin clave de idempotencia. Corrección: clave por intención y restricción única. ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos; no se invocó ningún modelo de lenguaje ni se observó ningún equipo o sistema reales. Las 125 frases, las ocho decisiones abiertas, la independencia entre ellas, los 24 requisitos y los 12 defectos son construcciones del autor, y el revisor se escribió conociendo las frases que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Necesidades](../n/necesidades.md), [Ambigüedad](../a/ambiguedad.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Deriva](../d/deriva.md), [Dispersión](../d/dispersion.md), [Especificación](../e/especificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (106 clases más lo mencionan; las que más):

[SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — significado de DEBE, NO DEBE y DEBERÍA en especificaciones; autoridad: IETF.
- [Mavin et al., «Easy Approach to Requirements Syntax (EARS)»](https://doi.org/10.1109/RE.2009.9) — plantillas de requisitos; autoridad: IEEE International Requirements Engineering Conference, 2009.
- [Cucumber: Gherkin](https://cucumber.io/docs/gherkin/) — sintaxis de criterios de aceptación ejecutables; autoridad: documentación del proyecto.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y jitter; autoridad: Amazon Builders' Library.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes y reintentos; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Integridad y dependency confusion](./integridad-y-dependency-confusion.md) · [Intención declarada y estrategia de ejecución →](./intencion-declarada-y-estrategia-de-ejecucion.md)
