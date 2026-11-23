# Confianza

[↑ Glosario](../../README.md) · [← Confabulación](./confabulacion.md) · [Confianza cero →](./confianza-cero.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Un complemento ejecuta con los privilegios del núcleo.

Es uno de los temas de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), donde se enseña como «Confianza».

## Por qué importa

En [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), el tema «Confianza» importa porque es el producto cuando los participantes no se conocen.

En [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), el tema «Confianza» importa porque un complemento ejecuta con los privilegios del núcleo.

## Cómo funciona

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

Comprar a un desconocido es arriesgado: puede no entregar, entregar algo distinto o no funcionar. Las plataformas construyen confianza con capas: verificación de identidad de quien vende, reseñas bidireccionales con reglas contra manipulación, pagos protegidos (el dinero se retiene hasta que se confirma), garantías o políticas de reembolso y un canal de disputa. Según los casos del curso, Mercado Pago nació como producto de custodia para dar confianza en pagos entre desconocidos, y Airbnb construyó pronto un sistema de pagos propio, reseñas y una garantía económica para anfitriones. En ambos casos el producto central del mercado es la reducción de la incertidumbre entre las partes, y la técnica (búsqueda, pagos, reseñas) se evalúa por cuánto la reduce.

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

No hay solución única: se combinan reseñas solo de quienes compraron, verificación de identidad, detección de patrones (muchas reseñas desde la misma red), reseñas bidireccionales y revisión de casos sospechosos. Se mide el costo en falsos positivos: eliminar reseñas legítimas daña la confianza tanto como dejar las falsas.

## Ejemplo

Ejemplo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) (sección «Caso conductor»):

*Tablero* lanzó «Plantillas» con 14 plantillas y comprobó que el buscador no era el problema. Esta clase da el modelo de liquidez, el reparto del dinero y el flujo de custodia, y conecta con los casos del curso: Airbnb (arranque lento y confianza), Mercado Libre (custodia como origen de un ecosistema de pagos) y Uber (más de dos lados y la diferencia entre ventas brutas e ingresos). `SE-417` toma el dinero que la plataforma retiene y reparte y lo registra con idempotencia y conciliación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- ¿qué lado fue más difícil de atraer?, ¿qué mecanismo de confianza usa?, ¿cuánto se queda y de qué depende?, ¿qué haría falta para que tú transaccionaras fuera? ([SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Adaptador de compatibilidad](../a/adaptador-de-compatibilidad.md), [Aislamiento](../a/aislamiento.md), [Arranque en frío](../a/arranque-en-frio.md), [Comisión](./comision.md), [Complemento](./complemento.md), [Contrato](./contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (154 clases más lo mencionan; las que más):

[SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Confabulación](./confabulacion.md) · [Confianza cero →](./confianza-cero.md)
