# Flujo huérfano

[↑ Glosario](../../README.md) · [← Flujo de datos y dependencias](./flujo-de-datos-y-dependencias.md) · [Flujo manual →](./flujo-manual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Automatización que sigue ejecutándose sin ninguna persona responsable activa.

Definición de trabajo de [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md).

## Por qué importa

En [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), el tema «Propiedad y gobernanza» importa porque evita flujos huérfanos y accesos olvidados.

## Cómo funciona

[SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la automatización de avisos. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md):

El equipo de la plataforma establece cuatro condiciones para aceptar una automatización en producción. Primera: un documento de una página con qué hace, qué datos toca y qué cuota consume. Segunda: un conjunto de pruebas de pares sobre un entorno de prueba con datos sintéticos, con el resultado archivado. Tercera: un receptor idempotente que guarda el identificador del evento durante 24 horas, medido a partir de la cola de re-entregas del proveedor.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md)) son:

- **Un caso inusual no recibe aviso** — causa: combinación de decisiones sin probar. Corrección: conjunto de pruebas de pares con los factores relevantes.
- **Los avisos se envían dos veces** — causa: disparador al menos una vez sin receptor idempotente. Corrección: guardar identificadores de evento con un tiempo medido.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md)) son: Las definiciones son operativas para la automatización de avisos. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna plataforma de automatización, conector, proveedor ni organización: los flujos, los defectos, los retrasos y las tasas de salida son construcciones del autor. La siguiente clase es un taller que compara los riesgos de todos los dominios de la parte.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura de pares](../c/cobertura-de-pares.md), [Low-code](../l/low-code.md), [No-code](../n/no-code.md), [Receptor idempotente](../r/receptor-idempotente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kuhn, Kacker y Lei, NIST SP 800-142, «Practical Combinatorial Testing»](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de pares; autoridad: NIST.
- [Stripe, documentación de webhooks](https://docs.stripe.com/webhooks) — entrega repetida de eventos y receptores idempotentes; autoridad: documentación del proveedor.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: Enterprise Integration Patterns.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Flujo de datos y dependencias](./flujo-de-datos-y-dependencias.md) · [Flujo manual →](./flujo-manual.md)
