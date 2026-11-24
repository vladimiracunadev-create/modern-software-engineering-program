# Inyección

## Definición

La **inyección** es una vulnerabilidad en la que datos controlados por quien ataca se interpretan como instrucciones por un intérprete que los recibe junto con ellas (`SE-460`). Los ejemplos clásicos son SQL, órdenes del sistema y plantillas.

## Por qué importa

Es una de las clases de vulnerabilidad más repetidas y su causa es de diseño, no de descuido: mezclar datos e instrucciones en el mismo canal. La defensa efectiva no depende de recordar escapar cada caso.

## Cómo funciona

Si una consulta se construye concatenando texto del usuario, el intérprete no sabe dónde terminan las instrucciones del programador y dónde empiezan los datos. La carga `' OR 1=1 --` cierra el literal y añade lógica propia. La defensa correcta **separa los canales**: parámetros enlazados, de modo que el valor viaja aparte y nunca se interpreta como sintaxis. Una lista blanca se reserva para identificadores (nombres de columnas) que no pueden parametrizarse.

## Ejemplo

```python
# vulnerable
cur.execute("SELECT * FROM notas WHERE id = " + entrada)
# seguro
cur.execute("SELECT * FROM notas WHERE id = ?", (entrada,))
```

## Errores y confusiones comunes

- **Se escapan comillas y una consulta numérica sigue vulnerable.** La defensa de literal no sirve para un número; usar parámetros enlazados para todos los valores (`SE-460`).
- **Una lista de palabras no detiene `' OR 1=1 --`.** La carga no contiene ninguna palabra de la lista; separar canales.

## Límites y cuándo no aplica

Los parámetros enlazados protegen los *valores*, no los identificadores ni las estructuras de la consulta. El mismo principio se extiende a otros intérpretes (órdenes, plantillas, instrucciones a modelos), donde separar datos de instrucciones es más difícil.
