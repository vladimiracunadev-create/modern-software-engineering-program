# PaaS

## Definición

**PaaS** (plataforma como servicio) es el servicio que entrega un entorno de ejecución gestionado donde el cliente despliega su propio código sin operar el sistema operativo ni los servidores (`SE-397`). La plataforma ofrece lenguajes, bibliotecas y servicios soportados por el proveedor.

## Por qué importa

Entre alquilar máquinas (IaaS) y usar una aplicación ya hecha (SaaS) está el modelo en que el equipo escribe y despliega código, pero otro opera lo que hay debajo. La decisión que cambia es qué trabajo operativo se abandona y qué control se cede a cambio: se gana seguridad y velocidad, se pierde control sobre las versiones.

## Cómo funciona

En PaaS, el consumidor despliega su código y el proveedor se ocupa del entorno de ejecución, con sus versiones y parches. `SE-397` señala el trueque con precisión:

- **Lo que se gana**: desaparece una familia de vulnerabilidades del lado del cliente, la de mantener al día el sistema operativo y el tiempo de ejecución.
- **Lo que se pierde**: el control de la versión. El proveedor retira un tiempo de ejecución en una fecha que no eliges.

Por eso la dependencia no es solo técnica sino de **calendario**, y el contrato de versiones es parte del diseño. Si el proveedor retira una versión y el equipo no sigue el calendario, el tiempo de ejecución deja de recibir parches y nadie se entera. La corrección que da la clase es suscribirse a los avisos del proveedor y planificar el cambio de versión.

En el reparto de responsabilidades, PaaS está entre IaaS (el cliente parchea el sistema operativo) y SaaS (el proveedor opera también la aplicación). Sigue siendo del cliente el código, sus dependencias y la configuración del servicio; un depósito o un panel quedan abiertos tras migrar si se asume que el proveedor configura lo que solo el cliente puede decidir.

## Ejemplo

Un equipo despliega una aplicación en un servicio PaaS con un tiempo de ejecución de cierta versión. Elimina la tarea de parchear servidores. Un año después el proveedor anuncia el retiro de esa versión; el equipo, suscrito a los avisos, planifica la actualización con meses de margen. Otro equipo, sin suscripción, descubre al retirarse la versión que su servicio ya no recibe parches. Ejemplo ilustrativo de lo que describe `SE-397`.

## Errores y confusiones comunes

- **Un tiempo de ejecución deja de recibir parches y nadie se entera**: el proveedor retira la versión y el equipo no sigue el calendario; se corrige suscribiéndose a los avisos y planificando el cambio de versión.
- **Creer que el proveedor se hace cargo de todo**: el código y su configuración siguen siendo del cliente.
- **Confundirlo con IaaS o SaaS**: el límite lo marca quién opera el sistema operativo y quién la aplicación.
- **Ignorar el costo de salida** de usar servicios propios de la plataforma.

## Límites y cuándo no aplica

PaaS limita lo que se puede instalar y configurar: si la aplicación necesita un sistema operativo, un componente de red o una versión que la plataforma no ofrece, IaaS es la opción. `SE-397` también advierte que su modelo de exposición usa supuestos del autor y que el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantiene el cliente.
