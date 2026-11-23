# Identidad de carga de trabajo

[↑ Glosario](../../README.md) · [← Idempotente](./idempotente.md) · [Identidad de una versión →](./identidad-de-una-version.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Identidad verificable de un servicio, distinta de la de una persona.

Definición de trabajo de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md).

## Por qué importa

La clase donde se define, [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), existe con este propósito: la clase existe para que «confianza cero» deje de ser una etiqueta de producto y se convierta en un conjunto de decisiones comprobables sobre un sistema: cada petición se autentica y se autoriza con identidad y contexto, ninguna ubicación de red concede acceso por sí sola, las credenciales duran poco y valen para un destinatario, y el daño de una credencial robada se mide en servicios alcanzables y en minutos de uso, no se supone pequeño.

## Cómo funciona

Según [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md):

No necesariamente. Una malla facilita la identidad de carga de trabajo y la autenticación mutua entre servicios; los mismos resultados se consiguen con bibliotecas y un emisor de identidad. Lo importante son las propiedades, no el producto.

## Ejemplo

Ejemplo de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) (sección «Preguntas frecuentes»):

No necesariamente. Una malla facilita la identidad de carga de trabajo y la autenticación mutua entre servicios; los mismos resultados se consiguen con bibliotecas y un emisor de identidad. Lo importante son las propiedades, no el producto.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md)) son: Se verificaron tokens firmados con HMAC y se modelaron el radio de daño y la ventana de uso indebido con supuestos del autor; no se ejecutó ningún emisor de identidad, punto de decisión, malla de servicios ni revocación. El siguiente paso, `SE-287`, es el taller: una batería de comportamientos hostiles contra tres formas de ejecutar código ajeno, con el resultado a la vista.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Audiencia](../a/audiencia.md), [Confianza cero](../c/confianza-cero.md), [Credencial de vida corta](../c/credencial-de-vida-corta.md), [Postura del dispositivo](../p/postura-del-dispositivo.md), [Punto de decisión (PDP) y de aplicación](../p/punto-de-decision-pdp-y-de-aplicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Idempotente](./idempotente.md) · [Identidad de una versión →](./identidad-de-una-version.md)
