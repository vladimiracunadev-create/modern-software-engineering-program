# Huérfano

[↑ Glosario](../../README.md) · [← Huella reproducible](./huella-reproducible.md) · [I/O bloqueante →](../i/i-o-bloqueante.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Commit sin motivo registrado o issue sin cambio asociado.

Definición de trabajo de [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md).

## Por qué importa

La clase donde se define, [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), existe con este propósito: la clase existe para que cada cambio del repositorio se pueda atar al motivo que lo originó y cada motivo a los cambios que lo atendieron, de modo que alguien pueda preguntar «¿por qué está esto así?» y «¿qué falta de lo que se pidió?» sin depender de la memoria de nadie.

## Cómo funciona

Según [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md):

Una matriz de trazabilidad relaciona cambios con motivos y expone huérfanos en ambos sentidos: commits sin motivo (¿por qué existe esto?) e issues sin cambio (¿se atendió?). No exige que todo commit tenga issue, pero exige decidir cuáles pueden no tenerlo. Medirla desde el historial real es la única forma de saber si el proceso funciona, y es sensible a cómo se integran los cambios.

Según [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md):

Traslada el análisis a otro sistema donde un cambio debe atarse a su motivo (por ejemplo, cambios de infraestructura y tickets de operación): decide qué sería la referencia, qué paso podría borrarla y cómo medirías los huérfanos. La transferencia está lograda cuando puedes explicar qué parte de la regla dependía de la plataforma, no cuando las palabras clave se parecen.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md):

En la plataforma, la plantilla de issue pide versión, pasos con los valores exactos, resultado esperado y observado. Los commits llevan un pie `Refs: #42` y la descripción del PR repite `Fixes #42` en la forma documentada. Un trabajo de integración continua construye la matriz de trazabilidad cada semana: cuenta commits de `main` sin referencia, issues cerrados sin commit en `main` y cierres cuyo PR se integró con squash sin cuerpo. El resultado alimenta una conversación sobre el proceso, no un indicador de personas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md)) son:

- **El issue no se cierra al integrar** — causa: la sintaxis no es la reconocida o falta la palabra por cada issue. Corrección: repetir la palabra clave para cada número y usar la forma documentada.
- **El vínculo desaparece tras el squash** — causa: el mensaje final no copia el cuerpo. Corrección: generar el mensaje del squash desde la descripción del PR.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una matriz de trazabilidad relaciona cambios con motivos y expone huérfanos en ambos sentidos: commits sin motivo (¿por qué existe esto?) e issues sin cambio (¿se atendió?). ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Issue](../i/issue.md), [Pie de commit](../p/pie-de-commit.md), [Referencia de cierre](../r/referencia-de-cierre.md), [Trazabilidad](../t/trazabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: vincular un PR con un issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) — palabras clave, sintaxis y condiciones; autoridad: GitHub Docs.
- [GitHub: plantillas de issues y PR](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) — plantillas para pedir contexto; autoridad: GitHub Docs.
- [git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers) — pies de commit estructurados; autoridad: documentación de Git.
- [Gotel y Finkelstein, «An analysis of the requirements traceability problem» (ICRE, 1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad; autoridad: IEEE ICRE.
- [git-log](https://git-scm.com/docs/git-log) — consulta del historial para la matriz; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Huella reproducible](./huella-reproducible.md) · [I/O bloqueante →](../i/i-o-bloqueante.md)
