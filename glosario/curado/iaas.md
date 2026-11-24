# IaaS

## Definición

**IaaS** (infraestructura como servicio) es el servicio que entrega cómputo, red y almacenamiento virtualizados sobre los que el cliente instala y opera su propio sistema operativo y software (`SE-397`). La definición del programa sigue la de NIST: la capacidad de aprovisionar procesamiento, almacenamiento y redes en los que el consumidor puede ejecutar software arbitrario, incluidos sistemas operativos y aplicaciones.

## Por qué importa

Pasar a una nube no traslada todas las responsabilidades al proveedor. IaaS es el modelo que menos traslada: el proveedor aporta el hardware y la virtualización, y el cliente conserva lo que corre encima. La decisión que cambia es qué se espera del proveedor y qué sigue siendo propio, sobre todo en seguridad y operación.

## Cómo funciona

`SE-397` precisa el reparto. El consumidor no gestiona la infraestructura subyacente, pero sí el sistema operativo, el almacenamiento y las aplicaciones desplegadas y, de forma limitada, algunos componentes de red como los cortafuegos. En la práctica, una máquina virtual de un proveedor es una máquina que otra organización alimenta, refrigera y virtualiza, pero cuyo sistema operativo parcheas tú.

Por eso la clase llega a una consecuencia concreta: la lista de parches pendientes no se reduce al pasar a IaaS; se queda con el cliente. Frente a ello, PaaS traslada al proveedor el sistema operativo y el tiempo de ejecución, y SaaS traslada además la aplicación. En el modelo de exposición de la clase, pasar de IaaS a SaaS recorta la exposición a un tercio y deja en pie casi el 61 % del resto; el efecto real depende de cuánto tarda cada proveedor y de cuántos ajustes mantiene el cliente. Es la base de la **responsabilidad compartida**: el proveedor protege la nube, el cliente protege lo que pone en ella.

## Ejemplo

Una organización migra su servidor de aplicaciones a una máquina virtual de un proveedor. El proveedor se ocupa del hardware, la energía y la virtualización; la organización sigue aplicando parches al sistema operativo, configurando el cortafuegos y actualizando la aplicación. Si esperaba que el proveedor aplicara los parches, tiene una vulnerabilidad abierta. Ejemplo ilustrativo del reparto de `SE-397`.

## Errores y confusiones comunes

- **Un depósito o un panel quedan abiertos tras migrar**: se asumió que el proveedor configura lo que solo el cliente puede decidir; se corrige asignando dueño y revisión a la configuración del servicio.
- **Creer que la nube elimina el trabajo de parches**: en IaaS se queda con el cliente.
- **Confundirlo con PaaS**: en PaaS el proveedor retira versiones y el equipo debe seguir su calendario, o el tiempo de ejecución deja de recibir parches sin aviso.
- **Tratar «la nube» como un único modelo de responsabilidad**.

## Límites y cuándo no aplica

`SE-397` presenta un modelo de exposición con supuestos del autor; no mide proveedores reales. IaaS da el máximo control y flexibilidad (cualquier sistema operativo, cualquier software), pero ese control es justo lo que se paga con trabajo operativo; si el equipo no puede asumirlo, un modelo más alto (PaaS o SaaS) puede ser más seguro aunque limite la configuración.
