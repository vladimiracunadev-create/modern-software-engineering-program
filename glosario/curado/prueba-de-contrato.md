# Prueba de contrato

## Definición

Una **prueba de contrato** es una prueba, o una batería de pruebas, escrita contra una interfaz o un puerto y ejecutada contra todas sus implementaciones, para comprobar que cumplen lo mismo. `SE-315` la define como la batería común que debe pasar toda implementación de una interfaz, `SE-302` como la prueba que se ejecuta contra todas las implementaciones y `SE-328` como la escrita contra un puerto y ejecutada contra todas sus implementaciones. `SE-228` la usa con otro matiz: ejecutar la herramienta como lo haría un consumidor y comprobar código de salida, flujos y efectos. El núcleo común es comprobar lo que un consumidor puede esperar.

## Por qué importa

Sin ella, cada implementación es una promesa privada. `SE-315` lo ilustra con el patrón adaptador: la prueba de contrato es la pieza que mantiene honesto al patrón, porque obliga a que cualquier adaptador nuevo pase la misma batería. También protege a los dobles de prueba: un doble que no se contrasta con la implementación real acaba diciendo algo falso.

## Cómo funciona

Se escribe una sola batería contra el contrato (la interfaz o el puerto) y se parametriza por implementación. En `SE-315`, la aplicación *Avisos* integra dos proveedores: uno expone `enviar(to, body)` y devuelve un diccionario con `id` y `status`; el otro, `push(destinatario, texto, prioridad)` y devuelve una tupla `(id, código HTTP)`. Dos adaptadores presentan a ambos la interfaz única `send(to, body)` que devuelve `(id, aceptado)`, y la prueba de contrato comprueba que con una misma llamada ambos devuelven la misma forma. La causa de su utilidad es que el contrato queda ejecutable: un cambio en un proveedor rompe la prueba y no al usuario.

## Ejemplo

`SE-315`: con una misma llamada, los adaptadores devuelven `('a1', True)` y `('b1', True)`: forma idéntica, valores propios de cada proveedor. Si un tercer adaptador devolviera otra forma, la batería común lo detectaría antes de integrarlo. En `SE-302`, una subclase pasa los ejemplos y falla con datos reales; la corrección es ejecutar una prueba de contrato con azar y bordes contra todas las subclases.

## Errores y confusiones comunes

- **Contrato no escrito como prueba, o probado solo con el camino feliz.** Una subclase pasa los ejemplos y falla con datos reales (`SE-302`).
- **Cada adaptador con su propia prueba.** Es una promesa privada sin una batería común (`SE-315`).
- **Confundirla con una prueba del consumidor.** `SE-228` y `SE-423` usan el término del lado del consumidor; lo común es que el contrato sea verificable.

## Límites y cuándo no aplica

La prueba de contrato comprueba lo que el contrato dice: si el contrato omite un comportamiento, ninguna implementación será juzgada por él. Los ejemplos de las clases son sintéticos (dos proveedores de mensajería ficticios). Y como el término se usa en sentidos cercanos (entre implementaciones, entre consumidor y proveedor, de una herramienta), conviene confirmar cuál aplica en cada clase.
