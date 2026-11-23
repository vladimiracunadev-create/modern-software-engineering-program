# Producto operable

[↑ Glosario](../../README.md) · [← Producto de datos](./producto-de-datos.md) · [Profundidad →](./profundidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Producto que se puede reiniciar, copiar, restaurar, vigilar y detener con evidencia ejecutable de que lo hace.

Definición de trabajo de [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

## Por qué importa

La clase donde se define, [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), existe con este propósito: el proyecto final existe para que demuestres, con un producto pequeño pero completo, que sabes construir con agentes desde una especificación y que sabes decir con qué evidencia el producto está terminado.

## Cómo funciona

Según [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md):

Un producto operable se reinicia sin repetir lo hecho (`RF-09`), se copia sin detenerse y se restaura a un estado consistente (`RF-10`). SQLite ofrece una interfaz de copia de seguridad en línea que produce una copia consistente de una base mientras se usa. Lo que la copia no da es continuidad: al restaurar una copia de hace seis horas se pierden las pasadas de esas seis horas, y el servicio, al reanudar, no sabe que ya envió esos avisos y los envía otra vez. La frecuencia de copia es, por lo tanto, una decisión de **objetivo de punto de recuperación**: cuánto trabajo se acepta perder, y se traduce a un número de avisos duplicados que reciben los estudiantes.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega el paquete de *Avisos*. La especificación tiene diez requisitos con identificador y criterio, tres principios de constitución y un registro de dos decisiones. El plan cita requisitos y el analizador de `SE-566` no encuentra incoherencias formales. El agente implementó con autoridad mínima: herramientas de lectura, escritura en el directorio del proyecto y ejecución de las pruebas, con un gancho previo que falla cerrado y un confinamiento de rutas probado con veinte intentos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md)) son:

- **El informe dice «cumplido» y la revisión encuentra fallos** — causa: autodeclaración con pruebas del camino feliz. Corrección: pruebas por requisito escritas antes de implementar y ejecutadas por un tercero.
- **Todas las pruebas pasan y no se sabe si valen** — causa: ninguna variante defectuosa las ha roto. Corrección: variante por requisito y matriz con lo que falta.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un producto operable se reinicia sin repetir lo hecho (`RF-09`), se copia sin detenerse y se restaura a un estado consistente (`RF-10`). ([SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia ejecutable](../e/evidencia-ejecutable.md), [Evidencia](../e/evidencia.md), [Producto](./producto.md), [LIMITES.md](../l/limites-md.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [Paquete de evidencia](./paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación; autoridad: IEEE Transactions on Software Engineering.
- [Google SRE: objetivos de nivel de servicio](https://sre.google/sre-book/service-level-objectives/) — indicadores y objetivos; autoridad: libro de Google SRE.

---

[↑ Glosario](../../README.md) · [← Producto de datos](./producto-de-datos.md) · [Profundidad →](./profundidad.md)
