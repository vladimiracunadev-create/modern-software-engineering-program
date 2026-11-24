# GraphQL

## Definición

**GraphQL** es un lenguaje de consulta con sistema de tipos en el que el cliente elige los campos que recibe (SE-163). El servidor expone un esquema tipado y un único punto de entrada; el cliente escribe una consulta que selecciona campos y relaciones, y recibe exactamente esa forma.

## Por qué importa

Reduce el sobreenvío de datos y los viajes de ida y vuelta, y **traslada al servidor el control del coste**. Cambia una decisión de diseño de API: en lugar de que el servidor decida qué devuelve cada ruta, el cliente decide qué pide, y el servidor debe protegerse de consultas caras.

## Cómo funciona

GraphQL expone un **sistema de tipos** y un único endpoint. El cliente escribe una consulta como esta (ilustración):

```graphql
{ entrega(id: 12) { estado estudiante { nombre } archivos { nombre tamano } } }
```

y obtiene un resultado con esa forma. Frente a una API de rutas fijas, donde obtener lo mismo exige varias llamadas o recibir campos sobrantes, la ventaja es que cada cliente pide lo que necesita.

El costo está del lado del servidor. SE-163 advierte que una consulta anidada puede costar miles de llamadas: si se pide cada estudiante con sus entregas, cada entrega con sus archivos y cada archivo con sus versiones, la cantidad de lecturas multiplica con cada nivel. **La especificación no fija límites de profundidad ni de coste**, de modo que las guías de seguridad recomiendan imponerlos: profundidad máxima, coste máximo por consulta y paginación. Sin ellos, una consulta pequeña puede tardar segundos o servir como vector de denegación de servicio.

El contrato (el esquema) se describe y se versiona como en otros contratos de API, y se comprueba con pruebas contractuales, como el documento OpenAPI de una API REST. A diferencia de REST, la evolución suele hacerse añadiendo campos y marcando los viejos como obsoletos, en lugar de numerar versiones.

## Ejemplo

Una consulta que pide `estudiantes { entregas { archivos { versiones { ... } } } }` en un curso de 200 estudiantes con cinco entregas, tres archivos y cuatro versiones cada uno implica del orden de 200 × 5 × 3 × 4 = 12.000 lecturas de versiones. Con un límite de profundidad de tres niveles o un coste máximo, el servidor la rechaza y el cliente debe paginar. (Cálculo ilustrativo.)

## Errores y confusiones comunes

- **Una consulta pequeña tarda segundos**: no hay límite de profundidad ni de coste; corrección: fijar profundidad máxima, coste máximo y paginación (SE-163).
- **Creer que GraphQL es «más rápido» por defecto.**
- **Exponer el esquema completo sin control de autorización por campo.**
- **Confundirlo con una base de datos**: es una capa de consulta sobre cualquier fuente.

## Límites y cuándo no aplica

Para APIs simples con pocos clientes y respuestas fijas, REST con OpenAPI es más sencillo y se cachea mejor con HTTP estándar. GraphQL complica el caché, la autorización fina y el control de coste. Los límites recomendados son una decisión de cada servicio, no una propiedad del lenguaje.
