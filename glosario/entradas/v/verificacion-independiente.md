# Verificación independiente

[↑ Glosario](../../README.md) · [← Verificación de estado](./verificacion-de-estado.md) · [Verificador →](./verificador.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Conjunto de comprobaciones escrito y ejecutado sin compartir el contexto de quien construyó el producto.

Definición de trabajo de [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

## Por qué importa

La clase donde se define, [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), existe con este propósito: el proyecto final existe para que demuestres, con un producto pequeño pero completo, que sabes construir con agentes desde una especificación y que sabes decir con qué evidencia el producto está terminado.

## Cómo funciona

Según [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md):

La autodeclaración del agente es el informe que escribe tras ejecutar sus propias pruebas. En este proyecto esas pruebas cubren los tres primeros requisitos, que son los del camino feliz: comprueban que se envían los tres avisos y que no se repiten ni se envían a entregas ya entregadas. La verificación independiente ejecuta las pruebas por requisito, incluidas las de reinicio y copia. La diferencia entre las dos es la medida del problema: lo que el agente comprobó y lo que el producto debía cumplir no coinciden, y la brecha se mide con variantes defectuosas. Para que el proceso sea honesto, la verificación independiente la escribe y la ejecuta alguien que no comparte el contexto del agente: otra persona, otra sesión o un conjunto escrito antes de implementar.

Según [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega el paquete de *Avisos*. La especificación tiene diez requisitos con identificador y criterio, tres principios de constitución y un registro de dos decisiones. El plan cita requisitos y el analizador de `SE-566` no encuentra incoherencias formales. El agente implementó con autoridad mínima: herramientas de lectura, escritura en el directorio del proyecto y ejecución de las pruebas, con un gancho previo que falla cerrado y un confinamiento de rutas probado con veinte intentos. Las herramientas de terceros están fijadas por huella y el agente en cuarentena es el único que lee notas de docentes. Las acciones irreversibles (enviar el primer lote real) tienen una solicitud con cinco datos y una pausa.

## Ejemplo

Ejemplo de [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega el paquete de *Avisos*. La especificación tiene diez requisitos con identificador y criterio, tres principios de constitución y un registro de dos decisiones. El plan cita requisitos y el analizador de `SE-566` no encuentra incoherencias formales. El agente implementó con autoridad mínima: herramientas de lectura, escritura en el directorio del proyecto y ejecución de las pruebas, con un gancho previo que falla cerrado y un confinamiento de rutas probado con veinte intentos. Las herramientas de terceros están fijadas por huella y el agente en cuarentena es el único que lee notas de docentes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md)) son:

- **El informe dice «cumplido» y la revisión encuentra fallos** — causa: autodeclaración con pruebas del camino feliz. Corrección: pruebas por requisito escritas antes de implementar y ejecutadas por un tercero.
- **Todas las pruebas pasan y no se sabe si valen** — causa: ninguna variante defectuosa las ha roto. Corrección: variante por requisito y matriz con lo que falta.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para que el proceso sea honesto, la verificación independiente la escribe y la ejecuta alguien que no comparte el contexto del agente: otra persona, otra sesión o un conjunto escrito antes de implementar. ([SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Contextos](../c/contextos.md), [Producto](../p/producto.md), [LIMITES.md](../l/limites-md.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [Paquete de evidencia](../p/paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación; autoridad: IEEE Transactions on Software Engineering.
- [Google SRE: objetivos de nivel de servicio](https://sre.google/sre-book/service-level-objectives/) — indicadores y objetivos; autoridad: libro de Google SRE.

---

[↑ Glosario](../../README.md) · [← Verificación de estado](./verificacion-de-estado.md) · [Verificador →](./verificador.md)
