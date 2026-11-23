# Mecanismo de falla

[↑ Glosario](../../README.md) · [← Mecanismo](./mecanismo.md) · [Medición →](./medicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Categoría de evento real que la falla representa: red, recursos, dependencias, reloj, discos o procesos.

Definición de trabajo de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md).

## Por qué importa

La clase donde se define, [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), existe con este propósito: la clase existe para que elijas qué falla inyectar según el evento real que representa, para que sepas qué señal mueve cada tipo de falla (su huella) y para que distingas fallas que parecen iguales desde fuera y se corrigen de forma distinta.

## Cómo funciona

[SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md):

Supón, como caso hipotético y no como medición, que el equipo ordena su catálogo para la API de entregas con doce filas. De red: «latencia de 100 ms entre la API y el almacenamiento» (hipótesis: el p99 sube, la tasa de error no) y «corte de 12 s» (los reintentos con pausa mantienen 99 % de entregas aceptadas). De recursos: «mitad de los hilos del almacenamiento» y «memoria al 90 %». De dependencias:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md)) son:

- **«La prueba de latencia pasó» y el servicio cae en producción** — causa: se probó latencia de red y no lentitud de la dependencia. Corrección: separar los dos mecanismos en el catálogo.
- **Dos fallas se corrigen con el mismo parche** — causa: se nombraron por el síntoma. Corrección: nombrar por mecanismo y señal.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se tocó ningún reloj, red ni disco reales; el servicio de 8 hilos, las seis fallas, la vida de 300 s de los tokens, el búfer y la parada de 2 s son construcciones del autor, y los umbrales de la huella se eligieron para clasificar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Evento](../e/evento.md), [Proceso](../p/proceso.md), [Recurso](../r/recurso.md), [Desfase de reloj](../d/desfase-de-reloj.md), [Falla inyectada](../f/falla-inyectada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

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

[↑ Glosario](../../README.md) · [← Mecanismo](./mecanismo.md) · [Medición →](./medicion.md)
