# Código de estado

[↑ Glosario](../../README.md) · [← Código de control](./codigo-de-control.md) · [Código de salida →](./codigo-de-salida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Número de tres cifras que indica el resultado de una petición HTTP según la semántica de HTTP.

Definición de trabajo de [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md).

## Por qué importa

La clase donde se define, [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), existe con este propósito: la clase existe para que documentes una API de modo que quien la consume pueda usarla sin leer el código, y para que sepas qué parte de esa documentación se comprueba sola (ejemplos ejecutables, firmas, códigos de respuesta) y qué parte depende de que alguien la escriba y la mantenga.

## Cómo funciona

Según [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md):

La documentación suele cubrir el camino feliz. Pero quien integra una API pasa la mayor parte del tiempo equivocándose, y la respuesta a un error decide si puede corregirse sola o debe abrir una incidencia. La semántica de los códigos de estado HTTP está definida (404 no encontrado, 405 método no permitido, 422 entidad no procesable) y un formato común para el cuerpo del error, como el de «detalles de problema», permite que los clientes traten los fallos de forma uniforme. Documentar errores significa listar los códigos que la API puede devolver, qué los provoca y qué debe hacer el cliente, no solo cuáles existen.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md):

La plataforma de entregas publica su API con una descripción OpenAPI mantenida junto al código, una referencia generada de ella y una página de errores con los siete códigos que el servidor puede devolver, cada uno con su causa y su remedio. Los diez ejemplos de la documentación se ejecutan en la integración continua contra el servicio de pruebas. La página declara qué rutas son estables (las de entregas), cuáles experimentales (las de importación) y cuáles internas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md)) son:

- **El ejemplo de la documentación devuelve algo distinto** — causa: se escribió a mano y no se ejecuta. Corrección: ejecutarlo en la integración continua contra el servicio de pruebas.
- **Los clientes reciben un código que la página no menciona** — causa: solo se documentó el camino feliz. Corrección: registrar los códigos observados y documentar causa y remedio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La semántica de los códigos de estado HTTP está definida (404 no encontrado, 405 método no permitido, 422 entidad no procesable) y un formato común para el cuerpo del error, como el de «detalles de problema», permite que los clientes traten los fallos de forma uniforme. ([SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Semántica](../s/semantica.md), [Cobertura de documentación](./cobertura-de-documentacion.md), [Contrato publicado](./contrato-publicado.md), [Ejemplo ejecutable](../e/ejemplo-ejecutable.md), [Referencia de API](../r/referencia-de-api.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9110, semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos y códigos de estado; autoridad: IETF.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción formal de interfaces HTTP; autoridad: OpenAPI Initiative.
- [RFC 9457, detalles de problema para APIs HTTP](https://www.rfc-editor.org/rfc/rfc9457) — formato común de errores; autoridad: IETF.
- [PEP 257, convenciones de docstrings](https://peps.python.org/pep-0257/) — qué debe contener un docstring; autoridad: Python Software Foundation.
- [Python: `doctest`](https://docs.python.org/3/library/doctest.html) — ejecución de ejemplos en la documentación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Código de control](./codigo-de-control.md) · [Código de salida →](./codigo-de-salida.md)
