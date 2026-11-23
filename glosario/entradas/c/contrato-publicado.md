# Contrato publicado

[↑ Glosario](../../README.md) · [← Contrato multicapa](./contrato-multicapa.md) · [Contrato público →](./contrato-publico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Conjunto de comportamientos que el proveedor declara estables y que los clientes pueden asumir.

Definición de trabajo de [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md).

## Por qué importa

En [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), el tema «Contrato publicado» importa porque la documentación fija lo que no puede cambiarse sin aviso.

## Cómo funciona

[SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el portal; no reemplazan las de las especificaciones enlazadas abajo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md):

La plataforma de entregas publica su API con una descripción OpenAPI mantenida junto al código, una referencia generada de ella y una página de errores con los siete códigos que el servidor puede devolver, cada uno con su causa y su remedio. Los diez ejemplos de la documentación se ejecutan en la integración continua contra el servicio de pruebas. La página declara qué rutas son estables (las de entregas), cuáles experimentales (las de importación) y cuáles internas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md)) son:

- **El ejemplo de la documentación devuelve algo distinto** — causa: se escribió a mano y no se ejecuta. Corrección: ejecutarlo en la integración continua contra el servicio de pruebas.
- **Los clientes reciben un código que la página no menciona** — causa: solo se documentó el camino feliz. Corrección: registrar los códigos observados y documentar causa y remedio.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las especificaciones enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos tras corregir la lectura del cuerpo en el servidor. No se auditó ninguna API real ni se midió a ningún consumidor: la API es una función en proceso, el servidor es de juguete, las peticiones aleatorias exageran los errores y la cobertura de docstrings mide presencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Cobertura de documentación](./cobertura-de-documentacion.md), [Código de estado](./codigo-de-estado.md), [Ejemplo ejecutable](../e/ejemplo-ejecutable.md), [Referencia de API](../r/referencia-de-api.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción formal de interfaces HTTP; autoridad: OpenAPI Initiative.
- [RFC 9110, semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos y códigos de estado; autoridad: IETF.
- [RFC 9457, detalles de problema para APIs HTTP](https://www.rfc-editor.org/rfc/rfc9457) — formato común de errores; autoridad: IETF.
- [PEP 257, convenciones de docstrings](https://peps.python.org/pep-0257/) — qué debe contener un docstring; autoridad: Python Software Foundation.
- [Python: `doctest`](https://docs.python.org/3/library/doctest.html) — ejecución de ejemplos en la documentación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Contrato multicapa](./contrato-multicapa.md) · [Contrato público →](./contrato-publico.md)
