# Componente

[↑ Glosario](../../README.md) · [← Compliance Engineer](./compliance-engineer.md) · [Componente fuertemente conexo →](./componente-fuertemente-conexo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Elemento con responsabilidades e interfaces delimitadas.

Definición de trabajo de [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md).

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md):

Un **sistema** es un conjunto de elementos relacionados que coopera para producir una capacidad. Sus propiedades no se deducen sumando propiedades aisladas. Una base de datos rápida, una interfaz accesible y un equipo atento pueden formar un sistema lento si la aprobación manual acumula trabajo sin señal de capacidad. Ese retraso es **emergente**: aparece por la relación entre tasa de entrada, reglas, cola y autoridad, no por un único componente defectuoso.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md):

En matrícula, «cupos disponibles» proviene de un legado que actualiza cada quince minutos. Mostrarlo como tiempo real genera decisiones erróneas. Las opciones son ocultarlo, declarar antigüedad o crear reserva transaccional. Si el equipo controla solo visualización, explicita la dependencia; si posee el flujo, diseña consistencia y recuperación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)) son:

- **el mapa contiene solo servicios y bases de datos** — causa: se confundió sistema con arquitectura técnica. Corrección: añade personas, reglas, datos, decisiones y el resultado que conecta los elementos.
- **la frontera coincide exactamente con el organigrama** — causa: se modeló autoridad formal, no causalidad. Corrección: sigue una solicitud real y mueve la frontera según la pregunta que necesitas responder.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ese retraso es **emergente**: aparece por la relación entre tasa de entrada, reglas, cola y autoridad, no por un único componente defectuoso. ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Interfaz](../i/interfaz.md), [Responsabilidad](../r/responsabilidad.md), [Capacidad](./capacidad.md), [Entorno](../e/entorno.md), [Frontera](../f/frontera.md), [Stakeholder](../s/stakeholder.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.

**También se usa en** (187 clases más lo mencionan; las que más):

[SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Compliance Engineer](./compliance-engineer.md) · [Componente fuertemente conexo →](./componente-fuertemente-conexo.md)
