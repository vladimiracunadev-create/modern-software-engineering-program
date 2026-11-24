# N+1

[↑ Glosario](../../README.md) · [← Mutante superviviente](../m/mutante-superviviente.md) · [Namespace →](./namespace.md)

> **Tipo:** sigla · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

El **N+1** es el patrón en que una lista de N elementos genera N consultas adicionales además de la inicial: una consulta que trae las filas y una más por cada fila para traer un dato relacionado. Es el sentido de [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) (Repository, Unit of Work y Active Record) y de [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) (consultas, índices y patrones de acceso); [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) lo ve en GraphQL: resolver por campo convierte una lista de N en N+1 consultas si no se agrupan.

## Por qué importa

Cada consulta tiene un costo fijo (ida y vuelta, análisis, plan). N consultas pequeñas son mucho más lentas que una consulta que trae todo, y el problema crece con los datos: funciona con 5 elementos en desarrollo y se arrastra con 5 000 en producción. Es uno de los defectos de rendimiento de acceso a datos más comunes.

## Cómo funciona

El código que lo causa tiene esta forma: se pide una lista (1 consulta) y, al recorrerla, cada elemento accede a algo relacionado que se carga de forma perezosa (N consultas). Ocurre con ORM de carga perezosa, con *Active Record*, y con resolvedores de GraphQL que resuelven un campo por elemento.

La figura de [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) cuenta el número de sentencias que la base recibió para producir el mismo listado: el patrón N+1 con 200 filas llega a 201 sentencias, frente a una o dos si se agrupa con una unión (*join*) o con una consulta por lotes (`WHERE id IN (...)`). Remedios: precargar la relación, usar un *join*, agrupar los accesos (en GraphQL, un cargador por lotes), y **medir las consultas** de todos modos.

## Ejemplo

Esbozo ilustrativo (no de la clase):

```python
pedidos = db.execute("SELECT id FROM pedido").fetchall()      # 1
for p in pedidos:
    db.execute("SELECT * FROM linea WHERE pedido_id = ?", (p["id"],))  # N
```

Con 200 pedidos son 201 sentencias. La forma agrupada pide todas las líneas en una consulta.

## Errores y confusiones comunes

- **Creer que un ORM lo evita por sí solo:** muchos implementan Repository y Unit of Work, y el N+1 sigue pudiendo ocurrir ([SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md)).
- **No contar consultas en las pruebas:** funciona y es lento.
- **Precargarlo todo siempre:** convierte el problema en traer datos que no se usan.
- **Confundirlo con un problema de índices:** una consulta con índice repetida N veces sigue siendo N+1.

## Límites y cuándo no aplica

El 201 de la clase es un caso, no una constante: la base era `sqlite3` en memoria, sin red. Con una base remota cada consulta suma latencia de red y la diferencia se amplifica; con un ORM que precarga por defecto, el problema aparece en otro lugar. Con N pequeño y fijo, el costo puede ser aceptable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Patrón](../p/patron.md), [Resultado](../r/resultado.md), [Active Record](../a/active-record.md), [Alias](../a/alias.md), [Atomicidad](../a/atomicidad.md), [Carga por lotes](../c/carga-por-lotes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GraphQL Specification](https://spec.graphql.org/) — modelo de consulta y resolución de campos; autoridad: GraphQL Foundation.
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) — riesgos de profundidad, coste y exposición del esquema; autoridad: OWASP.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — semántica de métodos y representaciones; autoridad: IETF.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de interfaces de recursos; autoridad: OpenAPI Initiative.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — consultas parametrizadas del experimento; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Mutante superviviente](../m/mutante-superviviente.md) · [Namespace →](./namespace.md)
