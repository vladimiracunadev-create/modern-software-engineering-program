# Plan

## Definición

En el sentido principal del programa (`SE-402`), un **plan** es el cálculo de las acciones necesarias para llevar lo existente a lo declarado, previo a aplicarlas: en infraestructura como código, la lista de cambios que una herramienta haría. El término es muy general y el programa lo usa con otros sentidos que esta entrada distingue:

- En `SE-486`: la lista de acciones que la herramienta calcularía para llevar el estado registrado y el real al deseado (mismo sentido que `SE-402`).
- En `SE-414`: un paquete comercial con precio, ciclo y derechos (plan de suscripción).
- En `SE-566`: el artefacto que decide cómo se construye (tecnología, arquitectura, restricciones) y que debe citar los requisitos que satisface.

Esta entrada desarrolla el de infraestructura.

## Por qué importa

Aplicar cambios de infraestructura sin verlos antes es actuar a ciegas. El plan separa «qué haría» de «hacerlo» y abre un punto de revisión humana. La decisión que cambia es que todo cambio pase por un plan revisado por una persona distinta de quien lo escribió, antes de aplicarse.

## Cómo funciona

La herramienta compara tres cosas: el **código** (lo declarado), el **estado** que guarda de lo que cree que existe, y la **realidad**. `SE-402` introduce la **deriva**: la diferencia entre lo que el estado cree y lo que existe, nacida de un cambio hecho fuera del código (un arreglo de emergencia, una consola, otra herramienta). Un plan que solo compara el código con el estado no la ve; uno que antes refresca el estado con la realidad la ve y propone revertirla. Ninguna conducta es incorrecta: la primera es rápida y ciega; la segunda es exacta y puede deshacer un arreglo necesario. Lo importante es la decisión explícita: incorporar el cambio al código o revertirlo, tomada por una persona antes del `apply`.

El equipo de la clase guarda el estado en un almacén remoto con bloqueo y cifrado, programa un plan de solo lectura cada noche para detectar deriva y abre una incidencia con cada diferencia; divide la infraestructura en estados separados (red, datos, aplicación) para que un cambio en la aplicación no pueda destruir la base de datos.

## Ejemplo

Un cambio pequeño modifica un atributo de una base de datos. El plan muestra «destruir y recrear» porque ese atributo fuerza reemplazo. Al leerlo, la persona que revisa detiene el cambio y protege el recurso con datos. Sin plan, la base se habría destruido. Caso de `SE-402`.

## Errores y confusiones comunes

- **Un cambio pequeño destruye una base de datos**: atributo que fuerza reemplazo; se corrige leyendo el plan y protegiendo los recursos con datos.
- **El plan propone crear algo que ya existe**: estado perdido o desactualizado; bloqueo y versionado del estado, e importar si falta (`SE-486`).
- **La deriva se descubre semanas después**: sin comprobación periódica; plan sin aplicar cada pocas horas con responsable.
- **Mezclar sentidos**: un plan comercial no es un plan de infraestructura.

## Límites y cuándo no aplica

El plan refleja lo que la herramienta puede ver: no detecta lo que no gestiona. Un plan aprobado sin lectura real es una formalidad. Y «lo existente» depende de que el estado esté actualizado; con un estado perdido, el plan puede ser engañoso. Para entornos desechables de prueba, la revisión humana de cada plan puede ser innecesaria.
