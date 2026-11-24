# Punto ciego

[↑ Glosario](../../README.md) · [← Punto caliente](./punto-caliente.md) · [Punto de captura →](./punto-de-captura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Un **punto ciego** es una familia de cambios que ninguna regla detecta ([SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md)). [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) la precisa para pruebas: una clase de defecto que un oráculo no puede ver. Dos mecanismos de comprobación que miran lo mismo desde el mismo ángulo comparten el punto ciego.

## Por qué importa

Un conjunto de comprobaciones verde no dice que todo esté bien, sino que lo que miran está bien. La decisión que cambia es cómo se combinan las defensas: no se acumulan comprobaciones del mismo tipo, sino de ángulos distintos, con puntos ciegos distintos y un costo proporcional al riesgo.

## Cómo funciona

[SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) observa que cada oráculo mira una parte del comportamiento:

- Las **pruebas de ejemplo** miran los casos que alguien imaginó.
- El **contrato** mira propiedades generales, no valores concretos.
- Los **escenarios con reloj** miran secuencias en el tiempo, pero eligen horas concretas.
- El **modelo de referencia** compara contra una segunda escritura de la regla y comparte con la primera cualquier malentendido de la especificación.

El punto ciego aparece donde ninguno mira. En el laboratorio de la clase, las ocho pruebas y los escenarios dejan vivo el mismo mutante, uno que avisa en el instante exacto del vencimiento, porque ninguno prueba esa hora exacta. Ese cambio no lo ve ningún oráculo, aunque cada uno sea razonable por separado.

La consecuencia, según la clase, es que la pregunta «¿cuál oráculo basta?» no tiene respuesta única, porque mezcla preguntas distintas. Ninguna técnica mata todos los mutantes por sí sola, salvo el modelo de referencia, que comparte los malentendidos de la especificación. Lo defendible es una combinación con puntos ciegos distintos. [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) lo aplica a datos: familias de cambios que ninguna regla de calidad detecta.

## Ejemplo

Un recordatorio debe avisar antes del vencimiento. Un mutante cambia la comparación para avisar también en el instante exacto. Las pruebas de ejemplo no usan esa hora; el contrato no la fija; los escenarios eligen horas distintas. Solo un caso de borde en el instante exacto lo detectaría. Esa hora es el punto ciego de todo el conjunto. Es el caso del laboratorio de [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

## Errores y confusiones comunes

- **Suponer que más pruebas del mismo tipo cierran el punto ciego**: lo comparten.
- **Confiar en un modelo de referencia** sin ver que hereda los malentendidos de la especificación.
- **Confundirlo con baja cobertura**: puede haber cobertura de líneas y aun así un punto ciego de sentido.
- **No medir con mutantes**: es la forma de hacerlo visible.

## Límites y cuándo no aplica

El punto ciego se conoce solo cuando se encuentra: no existe un método para listar todos los de un conjunto. La medición con mutantes revela los que los mutantes cubren, no los demás. Y no todos los puntos ciegos merecen cerrarse: el costo de ver una clase de defecto debe ser proporcional al riesgo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Oráculo](../o/oraculo.md), [Regla](../r/regla.md), [Cobertura](../c/cobertura.md), [Control](../c/control.md), [Evidencia](../e/evidencia.md), [Evidencia de ejecución](../e/evidencia-de-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Punto caliente](./punto-caliente.md) · [Punto de captura →](./punto-de-captura.md)
