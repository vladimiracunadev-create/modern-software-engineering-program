# Postura del dispositivo

[↑ Glosario](../../README.md) · [← Postmortem sin culpa](./postmortem-sin-culpa.md) · [Potencia →](./potencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Estado verificable de una máquina o carga de trabajo.

Definición de trabajo de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md).

## Por qué importa

La clase donde se define, [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), existe con este propósito: la clase existe para que «confianza cero» deje de ser una etiqueta de producto y se convierta en un conjunto de decisiones comprobables sobre un sistema: cada petición se autentica y se autoriza con identidad y contexto, ninguna ubicación de red concede acceso por sí sola, las credenciales duran poco y valen para un destinatario, y el daño de una credencial robada se mide en servicios alcanzables y en minutos de uso, no se supone pequeño.

## Cómo funciona

Según [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md):

En el laboratorio, un token es un objeto JSON con el sujeto, la audiencia, la expiración y un indicador de postura del dispositivo, codificado y firmado con HMAC-SHA-256. Se emitió uno para el sujeto `servicio-avisos` con audiencia `calificaciones` y vida de 300 segundos. Resultados: presentado a `calificaciones`, aceptado; presentado a `pagos`, rechazado por audiencia incorrecta; seis minutos después, rechazado por vencido; con la firma alterada, rechazado por firma inválida. Cada rechazo corresponde a una propiedad. La audiencia impide que un token robado de un servicio sirva en otro; la expiración acota cuánto tiempo sirve; la firma impide fabricar o modificar.

## Ejemplo

Caso medido en la sección «Postura del dispositivo y contexto» de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md):

Las políticas más ricas incorporan el estado del dispositivo (versión, cifrado de disco, presencia de agente), la ubicación, la hora y el patrón de uso. La atestación de `SE-283` aporta una forma verificable de la postura de una carga de trabajo: el emisor solo da credenciales si la medición coincide con una referencia aceptada. El costo es la complejidad de mantener esas señales y la tentación de convertir cada señal en un bloqueo: una política con demasiadas condiciones produce denegaciones que nadie entiende y excepciones permanentes que la vacían.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md)) son: Se verificaron tokens firmados con HMAC y se modelaron el radio de daño y la ventana de uso indebido con supuestos del autor; no se ejecutó ningún emisor de identidad, punto de decisión, malla de servicios ni revocación. El siguiente paso, `SE-287`, es el taller: una batería de comportamientos hostiles contra tres formas de ejecutar código ajeno, con el resultado a la vista.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Trabajo](../t/trabajo.md), [Audiencia](../a/audiencia.md), [Confianza cero](../c/confianza-cero.md), [Credencial de vida corta](../c/credencial-de-vida-corta.md), [Identidad de carga de trabajo](../i/identidad-de-carga-de-trabajo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Postmortem sin culpa](./postmortem-sin-culpa.md) · [Potencia →](./potencia.md)
