# Organización

[↑ Glosario](../../README.md) · [← Ordenamiento de tarjetas](./ordenamiento-de-tarjetas.md) · [Origen →](./origen.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

La estructura de equipos es una fuerza más.

Es uno de los temas de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), donde se enseña como «Organización».

## Por qué importa

En [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), el tema «Organización» importa porque la estructura de equipos es una fuerza más.

En [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), el tema «Organización» importa porque el estilo funciona si hay equipos que lo justifican.

## Cómo funciona

Según [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

Conway planteó que los sistemas copian la estructura de comunicación de quienes los construyen. Un equipo de seis personas no necesita desplegar de forma independiente porque no hay con quién coordinarse; doce equipos sí. Por eso el atributo «despliegue independiente» pesa 0,05 en el primer perfil y 0,30 en el segundo. Esta fuerza no se mide con un benchmark: se mide contando equipos y dependencias entre ellos, y se revisa cuando la organización cambia.

Según [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md):

La descripción más citada del estilo enumera rasgos: componentes que son servicios que se despliegan solos, organización por capacidad de negocio y no por capa técnica, propiedad de los datos por servicio, infraestructura automatizada, diseño para el fallo y evolución del conjunto. Lo que compra es autonomía: un equipo cambia, prueba y despliega su servicio sin pedir permiso a los demás. Esa autonomía tiene sentido cuando hay varios equipos cuyos ciclos de cambio se estorban; con un equipo no hay a quién estorbar. Por eso `SE-337` dio pesos distintos al despliegue independiente según el contexto.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Esta fuerza no se mide con un benchmark: se mide contando equipos y dependencias entre ellos, y se revisa cuando la organización cambia. ([SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md))
- La descripción más citada del estilo enumera rasgos: componentes que son servicios que se despliegan solos, organización por capacidad de negocio y no por capa técnica, propiedad de los datos por servicio, infraestructura automatizada, diseño para el fallo y evolución del conjunto. ([SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Camino crítico](../c/camino-critico.md), [Contrato compatible](../c/contrato-compatible.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Estilo arquitectónico](../e/estilo-arquitectonico.md), [Latencia de cola](../l/latencia-de-cola.md), [Lector tolerante](../l/lector-tolerante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (121 clases más lo mencionan; las que más):

[SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ordenamiento de tarjetas](./ordenamiento-de-tarjetas.md) · [Origen →](./origen.md)
