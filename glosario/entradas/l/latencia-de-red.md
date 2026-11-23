# Latencia de red

[↑ Glosario](../../README.md) · [← Latencia de cola](./latencia-de-cola.md) · [Latencia de un evento →](./latencia-de-un-evento.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Retraso en la entrega de los datos que no retiene recursos del servidor.

Definición de trabajo de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md).

## Por qué importa

La clase donde se define, [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), existe con este propósito: la clase existe para que elijas qué falla inyectar según el evento real que representa, para que sepas qué señal mueve cada tipo de falla (su huella) y para que distingas fallas que parecen iguales desde fuera y se corrigen de forma distinta.

## Cómo funciona

Según [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md):

**Cómo leer la figura.** Cada fila es una falla y cada columna una señal; el texto de la celda dice cuánto se movió frente a la línea base («no se mueve», «moderado», «grande» o «sin datos» si no hay peticiones correctas con las que calcular el p99). La latencia de red de 100 ms mueve solo el p99 (de 87 a 187 ms, 2,2 veces) y deja intactos errores, intentos y utilización: nadie la nota excepto quien mide la latencia. La falta de respuesta produce 97,5 % de errores, un p99 de 774 ms en las pocas peticiones que pasan y casi 3 intentos por petición, y **baja** la utilización a 0,67 veces, porque la dependencia no recibe trabajo útil.

Según [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md):

Porque producen daños distintos. La latencia de red retrasa la respuesta pero no retiene hilos del servidor: el cliente sufre sus esperas y nadie más. La lentitud del servidor mantiene ocupados los hilos de la dependencia, y con tráfico alto la satura. Una prueba con solo la primera da una falsa sensación de resistencia.

## Ejemplo

Ejemplo de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sección «Preguntas frecuentes»):

Porque producen daños distintos. La latencia de red retrasa la respuesta pero no retiene hilos del servidor: el cliente sufre sus esperas y nadie más. La lentitud del servidor mantiene ocupados los hilos de la dependencia, y con tráfico alto la satura. Una prueba con solo la primera da una falsa sensación de resistencia.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«La prueba de latencia pasó» y el servicio cae en producción** — causa: se probó latencia de red y no lentitud de la dependencia. Corrección: separar los dos mecanismos en el catálogo. ([SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La latencia de red de 100 ms mueve solo el p99 (de 87 a 187 ms, 2,2 veces) y deja intactos errores, intentos y utilización: nadie la nota excepto quien mide la latencia. ([SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md))
- La latencia de red retrasa la respuesta pero no retiene hilos del servidor: el cliente sufre sus esperas y nadie más. ([SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Desfase de reloj](../d/desfase-de-reloj.md), [Falla inyectada](../f/falla-inyectada.md), [Huella de una falla](../h/huella-de-una-falla.md), [Lentitud de la dependencia](./lentitud-de-la-dependencia.md), [Mecanismo de falla](../m/mecanismo-de-falla.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y priorizar por impacto o frecuencia; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Chaos Mesh: Simulate Network Faults](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/) — tipos de falla de red y lista de tipos de experimento; autoridad: documentación del proyecto Chaos Mesh.
- [Linux tc-netem(8)](https://man7.org/linux/man-pages/man8/tc-netem.8.html) — emulación de retraso, pérdida, corrupción, duplicación y reordenamiento; autoridad: páginas del manual de Linux.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — recursos y lentitud en las cascadas; autoridad: libro de ingeniería de confiabilidad de Google.
- [IETF RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) — validez temporal de certificados, ejemplo de dependencia del reloj; autoridad: Internet Engineering Task Force.

---

[↑ Glosario](../../README.md) · [← Latencia de cola](./latencia-de-cola.md) · [Latencia de un evento →](./latencia-de-un-evento.md)
