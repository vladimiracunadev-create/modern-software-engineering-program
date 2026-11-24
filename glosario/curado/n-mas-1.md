# N+1

## Definición

El **N+1** es el patrón en que una lista de N elementos genera N consultas adicionales además de la inicial: una consulta que trae las filas y una más por cada fila para traer un dato relacionado. Es el sentido de `SE-318` (Repository, Unit of Work y Active Record) y de `SE-353` (consultas, índices y patrones de acceso); `SE-243` lo ve en GraphQL: resolver por campo convierte una lista de N en N+1 consultas si no se agrupan.

## Por qué importa

Cada consulta tiene un costo fijo (ida y vuelta, análisis, plan). N consultas pequeñas son mucho más lentas que una consulta que trae todo, y el problema crece con los datos: funciona con 5 elementos en desarrollo y se arrastra con 5 000 en producción. Es uno de los defectos de rendimiento de acceso a datos más comunes.

## Cómo funciona

El código que lo causa tiene esta forma: se pide una lista (1 consulta) y, al recorrerla, cada elemento accede a algo relacionado que se carga de forma perezosa (N consultas). Ocurre con ORM de carga perezosa, con *Active Record*, y con resolvedores de GraphQL que resuelven un campo por elemento.

La figura de `SE-318` cuenta el número de sentencias que la base recibió para producir el mismo listado: el patrón N+1 con 200 filas llega a 201 sentencias, frente a una o dos si se agrupa con una unión (*join*) o con una consulta por lotes (`WHERE id IN (...)`). Remedios: precargar la relación, usar un *join*, agrupar los accesos (en GraphQL, un cargador por lotes), y **medir las consultas** de todos modos.

## Ejemplo

Esbozo ilustrativo (no de la clase):

```python
pedidos = db.execute("SELECT id FROM pedido").fetchall()      # 1
for p in pedidos:
    db.execute("SELECT * FROM linea WHERE pedido_id = ?", (p["id"],))  # N
```

Con 200 pedidos son 201 sentencias. La forma agrupada pide todas las líneas en una consulta.

## Errores y confusiones comunes

- **Creer que un ORM lo evita por sí solo:** muchos implementan Repository y Unit of Work, y el N+1 sigue pudiendo ocurrir (`SE-318`).
- **No contar consultas en las pruebas:** funciona y es lento.
- **Precargarlo todo siempre:** convierte el problema en traer datos que no se usan.
- **Confundirlo con un problema de índices:** una consulta con índice repetida N veces sigue siendo N+1.

## Límites y cuándo no aplica

El 201 de la clase es un caso, no una constante: la base era `sqlite3` en memoria, sin red. Con una base remota cada consulta suma latencia de red y la diferencia se amplifica; con un ORM que precarga por defecto, el problema aparece en otro lugar. Con N pequeño y fijo, el costo puede ser aceptable.
