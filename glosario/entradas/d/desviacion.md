# Desviación

[↑ Glosario](../../README.md) · [← Despliegue progresivo](./despliegue-progresivo.md) · [Detección de secretos →](./deteccion-de-secretos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Excepción justificada, revisada y registrada de una regla.

Definición de trabajo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

## Por qué importa

En [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), el tema «Desviaciones» importa porque hacen la política sostenible y auditable.

## Cómo funciona

Según [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

Una regla mecánica también se equivoca. La regla de recursión marca una función `altura` que recorre un árbol llamándose a sí misma, aunque su profundidad esté acotada por la del árbol y sea perfectamente analizable. Si el aviso no se puede descartar con una justificación revisada, el equipo aprende a ignorar los avisos y la política deja de proteger. La respuesta no es abandonar la regla sino ajustarla (permitir recursión con una cota declarada y comprobada) o permitir una **desviación**: una excepción por escrito, con su motivo, su alcance y quién la aprobó.

Según [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

Un equipo adopta un estándar de codificación con un comprobador en la integración continua. El primer día aparecen 4 000 avisos en la base de código existente; el equipo, abrumado, decide silenciar la regla más ruidosa. Una persona de calidad propone otra estrategia: congelar la base existente con un archivo de avisos conocidos, exigir cero avisos nuevos y atacar el archivo por riesgo, empezando por las funciones del limitador. En tres meses, el archivo baja de 4 000 a 900 y las desviaciones registradas son 12, cada una con un motivo y una aprobación. El comprobador deja de ser un obstáculo porque tiene una salida: corregir o desviar con justificación. Lo difícil no fue elegir las reglas, fue sostener el procedimiento.

## Ejemplo

Ejemplo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) (sección «Ejemplo profesional»):

Un equipo adopta un estándar de codificación con un comprobador en la integración continua. El primer día aparecen 4 000 avisos en la base de código existente; el equipo, abrumado, decide silenciar la regla más ruidosa. Una persona de calidad propone otra estrategia: congelar la base existente con un archivo de avisos conocidos, exigir cero avisos nuevos y atacar el archivo por riesgo, empezando por las funciones del limitador. En tres meses, el archivo baja de 4 000 a 900 y las desviaciones registradas son 12, cada una con un motivo y una aprobación. El comprobador deja de ser un obstáculo porque tiene una salida: corregir o desviar con justificación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La respuesta no es abandonar la regla sino ajustarla (permitir recursión con una cota declarada y comprobada) o permitir una **desviación**: una excepción por escrito, con su motivo, su alcance y quién la aprobó. ([SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Excepción](../e/excepcion.md), [Regla](../r/regla.md), [Aserción](../a/asercion.md), [Cota de bucle](../c/cota-de-bucle.md), [Envoltorio de enteros](../e/envoltorio-de-enteros.md), [Estándar de codificación segura](../e/estandar-de-codificacion-segura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (54 clases más lo mencionan; las que más):

[SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Desviaciones».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Despliegue progresivo](./despliegue-progresivo.md) · [Detección de secretos →](./deteccion-de-secretos.md)
