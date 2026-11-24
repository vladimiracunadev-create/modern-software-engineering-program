# Responsabilidad compartida

## Definición

La **responsabilidad compartida** es el reparto de qué seguridad y operación corresponde al proveedor de nube y al cliente, y que cambia con el tipo de servicio (`SE-397`). No es un reparto 50-50: es una frontera que se mueve según uses IaaS, PaaS o SaaS.

## Por qué importa

Migrar a la nube no traslada toda la responsabilidad al proveedor. Los incidentes más comunes aparecen en lo que el cliente asumió que otro hacía. La decisión que cambia es que cada tarea de seguridad y operación tiene un responsable nombrado, sabiendo en qué lado de la frontera cae según el servicio contratado.

## Cómo funciona

`SE-397` recoge lo que coinciden los documentos de los proveedores: el proveedor responde de la seguridad **de** la nube (instalaciones, hardware, virtualización) y el cliente de la seguridad **en** la nube (datos, identidades, configuración). Entre ambos hay **capas compartidas**, como las copias de seguridad o el registro de eventos, donde el proveedor ofrece el mecanismo y el cliente decide si lo activa, qué conserva y quién lo mira.

La frontera se desplaza según el servicio. En IaaS, el cliente mantiene el sistema operativo, el almacenamiento y las aplicaciones; en PaaS, el proveedor asume el sistema operativo y el tiempo de ejecución, y el cliente conserva el código y la configuración; en SaaS, el proveedor opera también la aplicación, y al cliente le quedan sus datos, sus usuarios y la configuración. La clase modela cuánta exposición queda según el tipo: pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto (valores del modelo de la clase).

La utilidad práctica es la **matriz**: una tabla de tareas por servicio con una persona o un equipo nombrado para cada celda. Una celda sin nombre es la que se incendia.

## Ejemplo

Una organización pasa un depósito de archivos a un servicio gestionado. El proveedor protege la infraestructura, pero la decisión de dejarlo público o privado es del cliente. En la matriz, la celda «configuración del servicio de almacenamiento» tiene un dueño y una revisión periódica; sin eso, un depósito queda abierto tras migrar. Caso de `SE-397`.

## Errores y confusiones comunes

- **Un depósito o un panel quedan abiertos tras migrar**: se asumió que el proveedor configura lo que solo el cliente puede decidir; se corrige asignando dueño y revisión a la celda.
- **Un tiempo de ejecución deja de recibir parches y nadie se entera**: en PaaS, el proveedor retira la versión y el equipo no sigue el calendario.
- **Leerlo como 50-50**.
- **Asumir que la certificación del proveedor cubre al cliente**.

## Límites y cuándo no aplica

El modelo concreto varía por proveedor y por servicio: los documentos oficiales de cada uno mandan sobre cualquier resumen. `SE-397` aclara que su modelo numérico usa supuestos del autor. En un sistema local, sin proveedor, no hay reparto: todo es del operador. Y la matriz es un punto de partida: debe revisarse al cambiar de servicio o de proveedor.
