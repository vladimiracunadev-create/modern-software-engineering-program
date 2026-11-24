# Prueba de regresión

[↑ Glosario](../../README.md) · [← Prueba de recorrido](./prueba-de-recorrido.md) · [Prueba de resistencia →](./prueba-de-resistencia.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Una **prueba de regresión** es una prueba que falla ante el defecto original y pasa con la corrección, y que se conserva para detectar si el defecto reaparece. [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) (pruebas tempranas y diseño por ejemplos) es la clase donde se define; [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) y [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) la reutilizan en talleres de reparación de una API y de un control de seguridad. No es lo mismo que «volver a ejecutar todas las pruebas»: aquí el término nombra una prueba concreta nacida de un defecto concreto.

## Por qué importa

Evita que un defecto reparado reaparezca. Un defecto que ya costó una vez una investigación es el más barato de proteger: cuesta una prueba y su ejecución automática. Sin ella, la corrección depende de que nadie vuelva a tocar esa parte.

## Cómo funciona

[SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) fija la secuencia:

1. **Escribir primero el caso que falla.**
2. **Verificar rojo por la razón correcta:** que falla por el defecto, no por un error de la prueba.
3. **Corregir.**
4. **Conservar la prueba** en la suite.

Dos precisiones de la clase: la **cobertura** indica ejecución, no calidad de los oráculos (una línea ejecutada no es una línea comprobada), y se priorizan decisiones y riesgos, no líneas.

En [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), el equipo recibe una API con diez defectos: escribe suites, mide qué falla, repara por orden de riesgo, añade una prueba de regresión por cada reparación, **reintroduce cada defecto y registra qué suite lo detecta**, y publica la lista de defectos dormidos. Ese paso final comprueba que la prueba realmente protege.

## Ejemplo

Ilustración propia del paso 2: un defecto en el cálculo de la nota final con entrega tardía. La prueba de regresión fija una entrega con un día de retraso y comprueba la penalización esperada. Se ejecuta antes de corregir (rojo, y falla por la penalización ausente), se corrige y pasa (verde). Si alguien reintroduce el defecto, vuelve a fallar.

## Errores y confusiones comunes

- **Un defecto reparado reaparece:** no se dejó una prueba que lo atrape ([SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md)).
- **Una prueba que nunca estuvo en rojo:** no se sabe si detecta el defecto.
- **Confundirla con pruebas de humo o con ejecutar toda la suite tras cada cambio.**
- **Considerar suficiente la cobertura** sin comprobar que los oráculos detectan el defecto.

## Límites y cuándo no aplica

Protege contra el defecto conocido, no contra el siguiente. Una suite de regresión que crece sin poda se vuelve lenta y frágil. Para defectos que dependen de condiciones difíciles de reproducir (carreras, fallos de infraestructura), la prueba puede ser inestable o requerir inyección de fallos.

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
