# Disparador de revisión

[↑ Glosario](../../README.md) · [← Disparador](./disparador.md) · [Dispersión →](./dispersion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Un **disparador de revisión** es una condición medible (métrica, umbral y duración) que reabre una decisión ([SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md)). [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) lo usa en un sentido vecino: la condición (un cambio, un incidente) que obliga a revisar el paquete de evidencia de un sistema crítico. En ambos casos responde a la pregunta «¿qué tendría que pasar para que esta decisión deje de valer?».

## Por qué importa

Una decisión de arquitectura se toma con la información de un momento. Sin disparador, solo se revisa cuando alguien se acuerda o cuando ya hay un problema. La decisión que cambia es tratar una decisión como válida hasta que una señal concreta diga lo contrario, y dejar esa señal escrita junto con la decisión, no en la memoria de alguien.

## Cómo funciona

En [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), el disparador es una de las siete secciones que debe tener un registro de decisión (contexto, decisión, alternativas consideradas, consecuencias, reversibilidad, disparador de revisión y evidencia). La clase define once criterios que un analizador puede comprobar; cuatro son propiedades de contenido, y una de ellas exige un disparador con un número. Aplicados a tres registros de ejemplo: el ADR-A (monolito modular con extracción del módulo de avisos si el p99 supera 200 ms) cumple 11 de 11; el ADR-B («Usar microservicios… porque son la mejor práctica») cumple 3 de 11 y no tiene ninguna alternativa, consecuencia negativa, número, reversibilidad, disparador ni evidencia.

El mecanismo que lo hace útil es que **vuelve comprobable** la revisión: una métrica con umbral y duración se puede vigilar con una alerta, de modo que reabrir la decisión es un evento, no una iniciativa.

[SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) lo extiende a sistemas críticos: el paquete se actualiza con cada cambio de requisitos, diseño, entorno o uso, y con cada incidente; la integración continua ejecuta el comprobador y falla si hay huecos nuevos o evidencia obsoleta sin una decisión registrada. Los disparadores están escritos (un cambio de proveedor del sensor, una actualización de una biblioteca, un incidente).

## Ejemplo

Una decisión elige un monolito modular, y su disparador dice: «si el p99 del módulo de avisos supera 200 ms durante siete días, se estudia su extracción». Cuando la métrica cruza el umbral por ese tiempo, se reabre la decisión con los datos a la vista. Es el caso del ADR-A de [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Errores y confusiones comunes

- **Disparador sin número**: «si crece mucho» no es comprobable.
- **Registro de decisión sin disparador**: la decisión se vuelve permanente por inercia.
- **Escribirlo y no vigilarlo**: sin alerta ni revisión, la condición no dispara nada.
- **Un paquete de evidencia hecho una vez para una auditoría**: equivale al archivo de riesgos que nunca se actualizó ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md)).

## Límites y cuándo no aplica

El disparador reabre la decisión, no la cambia: alguien debe evaluar si la condición realmente invalida lo decidido. Un umbral mal elegido genera falsas revisiones o revisiones tardías. Los once criterios y los tres registros de [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) son un ejercicio didáctico, no una norma. Para decisiones triviales y baratas de revertir, escribir un disparador es más costoso que la decisión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Incidente](../i/incidente.md), [Métrica](../m/metrica.md), [Paquete](../p/paquete.md), [ADR](../a/adr.md), [Consecuencia negativa](../c/consecuencia-negativa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Disparador](./disparador.md) · [Dispersión →](./dispersion.md)
