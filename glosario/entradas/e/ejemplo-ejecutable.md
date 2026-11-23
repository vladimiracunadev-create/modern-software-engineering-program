# Ejemplo ejecutable

[↑ Glosario](../../README.md) · [← Ejemplo de aceptación](./ejemplo-de-aceptacion.md) · [Ejemplos concretos →](./ejemplos-concretos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Ejemplo de uso cuya salida declarada se compara con la real de forma automática.

Definición de trabajo de [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md).

## Por qué importa

En [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), el tema «Ejemplos ejecutables» importa porque un ejemplo que se ejecuta es una prueba; uno que no, una promesa.

## Cómo funciona

Según [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md):

Es fácil medir que una función tiene docstring; es difícil medir que el docstring sirve. Una métrica de presencia detecta lo que falta del todo, y es útil como alarma; no dice nada sobre si el texto explica los parámetros, los errores o los casos límite. Por eso la medición de cobertura se combina con una revisión humana de una muestra y con los ejemplos ejecutables. Una documentación puede tener cobertura del 100 % y ser inútil, o del 60 % y bastar si cubre lo que se usa.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md):

La plataforma de entregas publica su API con una descripción OpenAPI mantenida junto al código, una referencia generada de ella y una página de errores con los siete códigos que el servidor puede devolver, cada uno con su causa y su remedio. Los diez ejemplos de la documentación se ejecutan en la integración continua contra el servicio de pruebas. La página declara qué rutas son estables (las de entregas), cuáles experimentales (las de importación) y cuáles internas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md)) son:

- **El ejemplo de la documentación devuelve algo distinto** — causa: se escribió a mano y no se ejecuta. Corrección: ejecutarlo en la integración continua contra el servicio de pruebas.
- **Los clientes reciben un código que la página no menciona** — causa: solo se documentó el camino feliz. Corrección: registrar los códigos observados y documentar causa y remedio.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las especificaciones enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos tras corregir la lectura del cuerpo en el servidor. No se auditó ninguna API real ni se midió a ningún consumidor: la API es una función en proceso, el servidor es de juguete, las peticiones aleatorias exageran los errores y la cobertura de docstrings mide presencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura de documentación](../c/cobertura-de-documentacion.md), [Código de estado](../c/codigo-de-estado.md), [Contrato publicado](../c/contrato-publicado.md), [Referencia de API](../r/referencia-de-api.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-210 — API docs, ejemplos y contratos publicados](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md).

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

[↑ Glosario](../../README.md) · [← Ejemplo de aceptación](./ejemplo-de-aceptacion.md) · [Ejemplos concretos →](./ejemplos-concretos.md)
