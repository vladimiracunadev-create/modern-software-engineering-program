# Aserción

[↑ Glosario](../../README.md) · [← Artefacto inmutable](./artefacto-inmutable.md) · [Aserción semántica →](./asercion-semantica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Comprobación en ejecución de un supuesto del programa.

Definición de trabajo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

## Por qué importa

En [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), el tema «Aserciones y retornos» importa porque convierten supuestos y errores en comprobaciones.

## Cómo funciona

Según [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

Los lenguajes de uso general permiten construcciones difíciles de razonar: recursión sin cota, bucles que dependen de datos externos, punteros que se redirigen sin control, comportamientos indefinidos del lenguaje. Un estándar de codificación segura prohíbe o restringe esas construcciones para que el programa que queda sea analizable por herramientas y por personas. La idea de las reglas de Holzmann es notable por su economía: diez reglas que caben en una página, escritas para que una herramienta las compruebe. Entre ellas: flujo de control simple (sin saltos arbitrarios ni recursión), todos los bucles con una cota fija comprobable, funciones que caben en una página, un mínimo de aserciones por función, y comprobar siempre el valor de retorno de las funciones que pueden fallar.

Según [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

Las ideas sí (cotas, comprobación de retornos, aserciones, sin excepciones vacías); las reglas de C sobre punteros o el preprocesador no aplican. El laboratorio usa Python por conveniencia y por eso emula la aritmética de C. Para código de seguridad real se usan lenguajes y subconjuntos con semántica definida.

## Ejemplo

Ejemplo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) (sección «Preguntas frecuentes»):

Las ideas sí (cotas, comprobación de retornos, aserciones, sin excepciones vacías); las reglas de C sobre punteros o el preprocesador no aplican. El laboratorio usa Python por conveniencia y por eso emula la aritmética de C. Para código de seguridad real se usan lenguajes y subconjuntos con semántica definida.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Entre ellas: flujo de control simple (sin saltos arbitrarios ni recursión), todos los bucles con una cota fija comprobable, funciones que caben en una página, un mínimo de aserciones por función, y comprobar siempre el valor de retorno de las funciones que pueden fallar. ([SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Supuestos](../s/supuestos.md), [Cota de bucle](../c/cota-de-bucle.md), [Desviación](../d/desviacion.md), [Envoltorio de enteros](../e/envoltorio-de-enteros.md), [Estándar de codificación segura](../e/estandar-de-codificacion-segura.md), [Falso positivo](../f/falso-positivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (30 clases más lo mencionan; las que más):

[SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Artefacto inmutable](./artefacto-inmutable.md) · [Aserción semántica →](./asercion-semantica.md)
