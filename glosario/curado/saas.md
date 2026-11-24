# SaaS

## Definición

**SaaS** (software como servicio) es, en el sentido de `SE-397`, la aplicación completa operada por el proveedor, de la que el cliente solo configura, administra identidades y es dueño de sus datos. `SE-409` lo usa desde el lado del producto: un producto operado por el proveedor, entregado de forma continua a muchos clientes y pagado por suscripción o consumo.

## Por qué importa

Es el extremo en el que más se delega, y por eso es fácil olvidar lo que no se delega. La decisión que cambia es cómo se piensa la seguridad y la gobernanza: aunque el equipo no opere un solo servidor, sigue siendo responsable de quién tiene acceso, qué datos se suben, cómo se exportan y qué pasa al terminar el contrato.

## Cómo funciona

`SE-397` la sitúa en el extremo de la cadena de responsabilidad compartida. En SaaS el consumidor usa una aplicación que corre en infraestructura del proveedor y solo controla configuraciones limitadas. El proveedor opera infraestructura, plataforma y aplicación; al cliente le quedan cuatro cuestiones:

- **Acceso**: quién entra y con qué permisos (identidades y su administración).
- **Datos**: qué se sube y con qué sensibilidad.
- **Exportación**: cómo salen los datos si se cambia de proveedor.
- **Fin del contrato**: qué se conserva o se borra al terminar.

La clase da el ejemplo de una plataforma educativa externa que guarda las entregas de los estudiantes: el equipo sigue siendo responsable de su tratamiento aunque no opere ni un servidor. Comparando modelos, pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto (cifra del modelo de la clase); el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantiene el cliente.

Desde el lado de quien ofrece SaaS (`SE-409`), el modelo implica entregar de forma continua a muchos clientes, con métricas propias del negocio de suscripción: baja, expansión y contracción, costo de adquisición. Es una forma de producto, además de un modelo de servicio.

## Ejemplo

Una universidad contrata una plataforma SaaS para recibir entregas. El proveedor opera todo. La universidad define quién es administrador, revisa accesos de personal que se fue, comprueba que puede exportar las entregas y establece cuánto tiempo se conservan. Si no lo hace, «ya no necesitamos seguridad» deja sin dueño esas tareas. Ejemplo de `SE-397`.

## Errores y confusiones comunes

- **«Pasamos a SaaS y ya no necesitamos seguridad»**: se confunde delegar la operación con delegar la responsabilidad por los datos; se mantiene revisión de accesos, exportación y retención.
- **No planear la salida**: la exportación se prueba antes de necesitarla.
- **Asumir que el proveedor cumple por el cliente** las obligaciones sobre datos personales.
- **Confundir SaaS con cualquier aplicación web**: lo define quién la opera y cómo se entrega.

## Límites y cuándo no aplica

SaaS limita la personalización a lo que el proveedor permite; si el requisito exige control sobre el entorno, el código o la ubicación de los datos, PaaS o IaaS pueden ser necesarios. Las cifras de `SE-397` son de un modelo con supuestos del autor, no de proveedores reales.
