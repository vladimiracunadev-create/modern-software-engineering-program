# Volumen

## Definición

**Volumen** tiene dos sentidos en el programa:

- **De datos** (`SE-365`): el número de filas de una carga o de una partición; la primera comprobación de calidad es si llegaron las filas esperadas.
- **De almacenamiento** (`SE-026`): una unidad lógica con un espacio de nombres y un sistema de archivos asociados.

Esta entrada desarrolla el primero y menciona el segundo.

## Por qué importa

Una carga parcial o una tabla vacía son fallos silenciosos: el pipeline termina sin error, la tabla existe, y los paneles muestran la mitad de los datos. Controlar el volumen es la defensa más barata contra esos fallos. `SE-365` cuenta el caso: el lunes, el panel muestra la mitad de las entregas y las alertas de volumen no sonaron; revisar qué comprobaciones existían mostró que la tabla solo tenía validación de esquema.

## Cómo funciona

`SE-365` lista seis comprobaciones de calidad de datos, cada una con su propia pregunta: **volumen** (¿llegaron las filas esperadas?), **unicidad** (¿hay claves repetidas?), **nulos** (¿falta lo que debería estar?), **integridad referencial** (¿cada clave extranjera apunta a algo?), **frescura** (¿es reciente el dato más nuevo?) y **distribución** (¿se parecen los valores a lo habitual?).

En el laboratorio, una tabla de 5 000 pedidos recibió seis variantes defectuosas. La carga parcial falló el volumen; los duplicados, volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; y los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. La variante limpia no falló ninguna. Ninguna comprobación vio más de dos variantes: su ceguera es tan importante como su vista.

El umbral de volumen se calibra contra lo habitual (por ejemplo, la mediana por día de la semana), no contra un número fijo.

## Ejemplo

```sql
SELECT COUNT(*) AS filas FROM lecturas WHERE dia = :dia;
-- alerta si filas < 0.8 * mediana_mismo_dia_de_semana
```

El equipo de *Avisos* prioriza por impacto: el hecho de lecturas recibe volumen, unicidad, nulos y frescura; el mart ejecutivo, distribución además de volumen. Define que unicidad y volumen detienen la publicación y la distribución publica con una marca.

## Errores y confusiones comunes

- **Solo validar el esquema.** Una tabla con el esquema correcto y la mitad de las filas pasa la validación.
- **Un umbral fijo.** El volumen varía por día de la semana y por temporada; hay que recalibrarlo.
- **Alertas que nadie atiende.** `SE-365` propone una métrica del propio sistema: el porcentaje de alertas que terminaron en una acción; si baja, se recalibra antes de que alguien silencie el canal.

## Límites y cuándo no aplica

El volumen detecta ausencia o exceso, no corrección de los valores: una tabla con el número exacto de filas puede tener todos los importes errados (eso lo ve la distribución). Los umbrales son del equipo y se ajustan con datos reales. Y en el sentido de almacenamiento (`SE-026`), un volumen es una unidad lógica de montaje: no tiene relación con el conteo de filas.
