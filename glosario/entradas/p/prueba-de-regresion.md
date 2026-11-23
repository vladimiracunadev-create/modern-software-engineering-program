# Prueba de regresión

[↑ Glosario](../../README.md) · [← Prueba de recorrido](./prueba-de-recorrido.md) · [Prueba de resistencia →](./prueba-de-resistencia.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Prueba que falla ante el defecto original y pasa con la corrección.

Definición de trabajo de [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md): Prueba que falla si se reintroduce un defecto ya reparado.
- En [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md): Prueba que falla con el defecto y pasa con la corrección, y que se conserva para detectar su reaparición.

## Por qué importa

La clase donde se define, [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), existe con este propósito: la clase existe para usar ejemplos para descubrir particiones y propiedades antes de fijar implementación.

## Cómo funciona

Según [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), en la sección «Prueba de regresión»:

Al corregir un defecto se añade primero el caso que falla, se verifica rojo por la razón correcta, se corrige y se conserva. Cobertura indica ejecución, no calidad de oráculos. Se priorizan decisiones y riesgos.

## Ejemplo

Ejemplo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sección «Ejemplo profesional»):

El equipo recibe la API con los diez defectos y trabaja en seis pasos: escribe las tres suites; mide qué falla; repara por orden de riesgo (D3, D1, D10, D2, D4, D8, D6, D7, D9, D5); añade una prueba de regresión para cada reparación; reintroduce cada defecto y registra qué suite lo detecta; y publica la lista de defectos dormidos. Compara con el original en tres casos: un usuario normal, un integrador con un script y alguien que prueba la API sin permiso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un defecto reparado reaparece** — causa: no hay prueba de regresión que falle sin la reparación. Corrección: reintroducir el defecto y comprobar que falla. ([SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No es necesariamente el mínimo global, pero suele ser lo bastante corto como para entenderse y para fijar la prueba de regresión. ([SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md))
- Porque una prueba de regresión solo vale si falla cuando el defecto vuelve. ([SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asignación masiva](../a/asignacion-masiva.md), [Camino feliz](../c/camino-feliz.md), [Consulta parametrizada](../c/consulta-parametrizada.md), [Corte](../c/corte.md), [Defecto dormido](../d/defecto-dormido.md), [Falso verde](../f/falso-verde.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (400 clases más lo mencionan; las que más):

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: unittest](https://docs.python.org/3/library/unittest.html) — pruebas de regresión ejecutables; autoridad: documentación de Python.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Zeller y Hildebrandt, «Simplifying and isolating failure-inducing input»](https://doi.org/10.1109/32.988498) — reducción por delta; autoridad: artículo original (2002).
- [Musuvathi et al., CHESS](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/musuvathi/musuvathi.pdf) — planificador controlado y exploración sistemática; autoridad: artículo de OSDI (2008).

---

[↑ Glosario](../../README.md) · [← Prueba de recorrido](./prueba-de-recorrido.md) · [Prueba de resistencia →](./prueba-de-resistencia.md)
