# Dependencia

## Definición

**Dependencia** es una palabra con varios sentidos en el programa, todos con la idea de «algo que necesita de otra cosa». Las clases distinguen:

- **De software instalable** (`SE-032`): un componente requerido bajo una relación y una restricción declaradas (por ejemplo, una versión).
- **Entre componentes** (`SE-068`): el conocimiento de un componente sobre otro; es el acoplamiento visto como relación.
- **De orden de trabajo** (`SE-141`, `SE-186`): una relación por la cual un elemento no puede empezar o terminar hasta que otro llegue a cierto estado.
- **Entre requisitos** (`SE-150`): una relación por la cual un requisito no puede entregarse, probarse o usarse sin otro.

El sentido común es una relación dirigida: A depende de B. Al leer la palabra hay que confirmar qué clase de relación es.

## Por qué importa

Una dependencia ignorada produce planes que no se pueden cumplir o sistemas que se rompen al cambiar una pieza. `SE-150` lo muestra en la planificación: ordenar por valor sin comprobar dependencias produce planes que prometen lo que no se puede construir con lo comprometido. `SE-186` lo muestra en la entrega: si el camino crítico pasa por una dependencia externa, todo el equipo espera la misma entrega.

## Cómo funciona

`SE-150` modela las dependencias entre requisitos como un grafo dirigido. Si hay un ciclo, los requisitos implicados son en realidad uno solo o están mal separados. Un conjunto es **entregable** si está cerrado bajo las dependencias: si contiene un requisito, contiene también todo aquello de lo que depende; por eso se verifica el cierre antes de aprobar un plan. `SE-186` trata las dependencias externas con una práctica: acordar con cada proveedor una fecha de aviso y un doble (una alternativa o un contrato que permita avanzar sin la entrega), y revisar el diagrama de dependencias en cada ciclo con el avance real. `SE-141` lo aplica al orden: se enumera o resuelve el orden con las dependencias, y no se hace primero lo de mayor valor propio.

## Ejemplo

En `SE-150`, un requisito de alto valor nunca se hace porque su dependencia está fuera del presupuesto; la corrección es hacer visible la dependencia y decidir si se incluye o se retira el requisito. En `SE-186`, todo el equipo espera la misma entrega externa porque el camino crítico pasa por ella; se divide el trabajo para que avance sin ella, con un contrato o un doble.

## Errores y confusiones comunes

- **El plan aprobado no se puede construir.** Se ordenó por valor sin comprobar dependencias; corrección (`SE-150`): verificar el cierre del conjunto.
- **Una dependencia «casi lista» que llega tarde.** No se pidió fecha de aviso ni alternativa (`SE-186`).
- **Un diagrama de dependencias desactualizado.** Se dibujó una vez; hay que revisarlo cada ciclo.

## Límites y cuándo no aplica

Un grafo de dependencias solo contiene las relaciones que alguien declaró: las no declaradas aparecen como sorpresas. Las clases tratan las dependencias de requisitos (`SE-150`) y de plan (`SE-186`) en contextos de planificación con ejemplos sintéticos, y las de software y de componentes en otros contextos; no se pueden trasladar sus reglas de un sentido a otro sin comprobar que la relación es la misma.
