# Desfase de reloj

[↑ Glosario](../../README.md) · [← Desechabilidad y persistencia](./desechabilidad-y-persistencia.md) · [Desigualdad de Mosca →](./desigualdad-de-mosca.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Diferencia entre la hora de un componente y la hora de referencia.

Definición de trabajo de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md).

## Por qué importa

La clase donde se define, [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), existe con este propósito: la clase existe para que elijas qué falla inyectar según el evento real que representa, para que sepas qué señal mueve cada tipo de falla (su huella) y para que distingas fallas que parecen iguales desde fuera y se corrigen de forma distinta.

## Cómo funciona

Según [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md):

Con mucho cuidado, porque un desfase de reloj afecta a certificados, tokens, tareas programadas y replicación, y se extiende a todo lo que corre en el nodo. Lo habitual es inyectarlo en un entorno de prueba, o simularlo en la prueba (un reloj que se pasa como dependencia) y reservar la inyección real para un nodo aislado.

## Ejemplo

Ejemplo de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sección «Preguntas frecuentes»):

Con mucho cuidado, porque un desfase de reloj afecta a certificados, tokens, tareas programadas y replicación, y se extiende a todo lo que corre en el nodo. Lo habitual es inyectarlo en un entorno de prueba, o simularlo en la prueba (un reloj que se pasa como dependencia) y reservar la inyección real para un nodo aislado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Rechazos intermitentes de tokens** — causa: desfase de reloj en uno de varios nodos. Corrección: medir el desfase y fijar una tolerancia acorde. ([SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se tocó ningún reloj, red ni disco reales; el servicio de 8 hilos, las seis fallas, la vida de 300 s de los tokens, el búfer y la parada de 2 s son construcciones del autor, y los umbrales de la huella se eligieron para clasificar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Referencia](../r/referencia.md), [Falla inyectada](../f/falla-inyectada.md), [Huella de una falla](../h/huella-de-una-falla.md), [Latencia de red](../l/latencia-de-red.md), [Lentitud de la dependencia](../l/lentitud-de-la-dependencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

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

[↑ Glosario](../../README.md) · [← Desechabilidad y persistencia](./desechabilidad-y-persistencia.md) · [Desigualdad de Mosca →](./desigualdad-de-mosca.md)
