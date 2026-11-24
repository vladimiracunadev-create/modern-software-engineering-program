# Reemplazo

## Definición

En infraestructura como código, un **reemplazo** es una acción que destruye un recurso y lo vuelve a crear porque una propiedad no se puede cambiar en sitio (`SE-486`).

## Por qué importa

Un cambio que parece menor en el código declarativo puede traducirse en destruir y recrear. Si el recurso tiene estado (una base de datos), el reemplazo borra datos. La revisión de un plan debe separar cambios en sitio de reemplazos y borrados.

## Cómo funciona

La herramienta compara el **estado deseado** que declara el código con el **estado real** y calcula un plan. Para cada propiedad, el proveedor decide si admite modificación en sitio o exige recrear. El plan marca el reemplazo (en algunas herramientas con un símbolo propio), y solo quien lo lee atentamente lo detecta. Una política automática que marque borrados y reemplazos, y una copia verificada antes de aplicar, convierten la revisión en control.

## Ejemplo

Cambiar el nombre de una base de datos o su motor puede exigir reemplazo. `SE-486` documenta el caso de «se destruyó una base de datos con un cambio menor»: el reemplazo no fue revisado.

## Errores y confusiones comunes

Revisar el diff del código y no el plan; asumir que cambiar una propiedad es siempre una modificación.

## Límites y cuándo no aplica

Qué cambios son en sitio y cuáles son reemplazos lo decide cada proveedor; los porcentajes de la clase (25 % de recursos con estado, etc.) son supuestos del autor.
