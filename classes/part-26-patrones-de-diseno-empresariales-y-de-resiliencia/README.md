# Parte 26 — Patrones de diseño, empresariales y de resiliencia

La [Parte 25](../part-25-diseno-patrones-y-refactorizacion/README.md) presentó los patrones como vocabulario de diseño y la [Parte 36](../part-36-calidad-rendimiento-y-resiliencia/README.md) trató la resiliencia como cualidad. Esta parte pone ambos bajo la misma pregunta de ingeniería: **¿qué fuerza concreta resuelve este patrón, qué cuesta tenerlo y cómo sabré cuándo retirarlo?** Un patrón es una solución con nombre a un problema recurrente; el nombre ayuda a conversar y la medida ayuda a decidir. Sin la segunda, el catálogo se convierte en una lista de formas que se aplican por costumbre.

## Pregunta rectora

> Para este problema de diseño, ¿qué fuerza lo causa, qué patrón la ataca, qué costo medible añade, qué deja de resolver y bajo qué condición se retira?

## Antes del recorrido clase por clase

La parte trata tres familias que suelen enseñarse por separado y que aquí comparten método. Los **patrones de diseño** (GoF y GRASP) organizan responsabilidades dentro de un programa. Los **patrones empresariales y de integración** (Repository, Unit of Work, Active Record y los de mensajería) organizan la frontera entre el modelo, la base de datos y otros sistemas. Los **patrones de resiliencia** (timeout, retry, circuit breaker, bulkhead, degradación) organizan lo que pasa cuando una dependencia falla o se vuelve lenta. Las tres familias responden a una fuerza y tienen un costo.

El caso conductor es *Avisos*, el servicio de recordatorios de entregas que ya apareció en la [Parte 45](../part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md). Cada clase lo mira con un patrón distinto: canales como estrategia y fábrica, un remitente decorado con reintentos, estados del aviso como máquina de estados, persistencia con repositorio, entrega de mensajes con receptor idempotente y llamadas a un proveedor con timeout, jitter y circuit breaker.

![Diagrama de flujo con 12 pasos. Recorrido: «Criterios para usar un catálogo»; luego «GoF creacionales»; luego «GoF estructurales»; luego «GoF conductuales»; luego «GRASP»; luego «Repository, Unit of Work, Active Record»; luego «Integración empresarial»; luego «Resiliencia I: timeout, retry, breaker»; luego «Resiliencia II: bulkhead, sidecar, degradación»; luego «Antipatrones y deuda»; luego «Taller: refactorizar y medir»; luego «Proyecto: catálogo del sistema». Retornos: «Proyecto: catálogo del sistema» lleva a «Criterios para usar un catálogo» (costos que no se justificaron).](../../site/assets/figures/mermaid-b086d1773d.svg)

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que un catálogo se revisa con la evidencia de los patrones cuyo costo no se justificó.

## Resultados acumulativos

Podrás decidir si un patrón se justifica comparando una fuerza nombrada, el costo en tamaño e indirección y una condición de salida; medir con análisis de sintaxis cuánto cuesta y cuánto simplifica un patrón; y reconocer cuándo el nombre de una clase anuncia un patrón que la estructura no tiene.

Podrás explicar los patrones creacionales, estructurales y conductuales de la Gang of Four por la fuerza que atacan y por el modo en que se estropean: un Singleton con estado que vuelve dependientes las pruebas, una copia superficial que contamina clones, decoradores cuyo orden cambia la política, observadores que no se dan de baja y máquinas de estado reemplazadas por banderas.

Podrás asignar responsabilidades con los criterios de GRASP y comprobarlo con un cambio de regla; usar un repositorio y una unidad de trabajo sin ocultar las consultas ni la atomicidad; y escribir los patrones de mensajería de un sistema (receptor idempotente, cartas muertas, reordenador, correlación) con la garantía de entrega que cada uno compensa.

Podrás configurar timeout, reintentos con jitter y circuit breaker sin crear tormentas de reintentos; aislar dependencias con compartimentos y degradar con honestidad; medir la complejidad de un diseño y distinguir un antipatrón de una incomodidad; refactorizar con un maestro dorado que incluye las fronteras; y escribir un catálogo de patrones de un sistema con evidencia, costo y condición de salida por entrada.

## Prerrequisitos enlazados

- [Parte 25 — Diseño, patrones y refactorización](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-25-diseno-patrones-y-refactorizacion/): costuras, inyección de dependencias y refactorización con red de seguridad.
- [Parte 27 — Arquitectura de software y dominio](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-27-arquitectura-de-software-y-dominio/): límites, dominio y decisiones arquitectónicas.
- [Parte 29 — Datos, persistencia y recuperación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-29-datos-persistencia-y-recuperacion/): transacciones, consultas y modelos de datos.
- [Parte 31 — Integración, eventos y mensajería](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-integracion-eventos-y-mensajeria/): colas, eventos y garantías de entrega.
- [Parte 32 — Concurrencia y sistemas distribuidos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-32-concurrencia-y-sistemas-distribuidos/): fallos parciales, tiempo y consenso.
- [Parte 35 — Estrategia y técnicas de prueba](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-35-estrategia-y-tecnicas-de-prueba/): dobles de prueba, valores límite y mutación.
- [Parte 36 — Calidad, rendimiento y resiliencia](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-36-calidad-rendimiento-y-resiliencia/): escenarios de calidad y cualidades de resiliencia.
- [Parte 41 — Observabilidad, SRE e incidentes](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-41-observabilidad-sre-e-incidentes/): señales, saturación e incidentes.
- [Parte 45 — Metodologías de desarrollo: de TDD a ODD](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/): oráculos, mutación y el caso *Avisos*.
- Python 3.11+ y terminal; todos los experimentos usan solo la biblioteca estándar (`ast`, `sqlite3`, `socket`, `random`, `timeit`).

## Bloques y progresión

1. **Elegir y reconocer patrones:** las clases 517 a 520 establecen los criterios para usar un catálogo y recorren los patrones de la Gang of Four con una medida por cada familia.
2. **Responsabilidades y datos:** las clases 521 y 522 asignan responsabilidades con GRASP y tratan el acceso a datos con Repository, Unit of Work y Active Record.
3. **Integración y resiliencia:** las clases 523 a 525 tratan la mensajería como lenguaje común y los dos grupos de patrones que sostienen un sistema cuando una dependencia falla.
4. **Evaluar e integrar:** las clases 526 a 528 miden antipatrones y deuda, refactorizan con un maestro dorado y construyen el catálogo de patrones de un sistema.

## Evidencia medida y límites

Los experimentos de esta parte se ejecutaron con CPython 3.12 en Windows 11, con la biblioteca estándar y sin dependencias externas; los recuentos son deterministas (análisis de sintaxis, bases `sqlite3` en memoria y simulaciones con semilla fija) y los tiempos de reloj se dan como orden de magnitud porque varían de equipo en equipo. **No se invocó ningún modelo de lenguaje** ni se midió ningún equipo humano.

Las medidas principales son estas: una función de tarifas escrita con `if/elif` y con Strategy en 2 a 12 variantes, donde el patrón usa entre 1,5 y 2,1 veces los nodos de sintaxis y mantiene la complejidad ciclomática máxima en 2 mientras la otra crece de 3 a 13 (`SE-313`); un Singleton con estado mutable que hace fallar 18 de las 24 ordenaciones de cuatro pruebas, y una copia superficial que contamina los 1000 clones (`SE-314`); la misma pila de decoradores en dos órdenes, con 97,5 % de éxito y percentil 99 de 240 ms frente a 71,2 % y 80 ms (`SE-315`); cuatro banderas booleanas que dejan en estados imposibles el 69,7 % de 10.000 secuencias aleatorias (`SE-316`); un descuento hecho en un solo lugar que deja dos totales distintos en un diseño y uno consistente en otro (`SE-317`); y 201 consultas frente a 1 en un listado con N+1, con una transacción que deja 0 filas a medias frente a 1 sin ella (`SE-318`).

Siguen un canal con 208 duplicados que infla una suma de pagos en 3077 hasta que se añade un receptor idempotente (`SE-319`); mil clientes que reintentan tras una caída, con picos de 1000 peticiones por cada 100 ms sin jitter y de 537 con jitter completo, y un circuit breaker que ahorra 693 llamadas a una dependencia caída (`SE-320`); un compartimento que mantiene el 100 % de éxito de una dependencia sana mientras otra se degrada (frente al 30,6 % de un grupo compartido), una degradación que sube las respuestas útiles de 60,0 % a 87,5 % y un salto adicional por sockets locales que duplica una latencia de unas decenas de microsegundos (`SE-321`); una clase con 37 de 45 pares de métodos sin estado compartido y un ciclo de tres módulos (`SE-322`); un refactor que baja la complejidad máxima de 15 a 3 con 44 % más de nodos y un maestro dorado que detecta 3 de 6 mutantes con 5000 entradas al azar y 6 de 6 con 384 entradas de frontera (`SE-323`); y dos detectores de patrones sobre un corpus etiquetado de 14 fragmentos, con 29 % de precisión por nombre y 86 % por estructura (`SE-324`).

Los parámetros (los fragmentos de código, las 24 ordenaciones, los 10.000 recorridos, las tasas de duplicados y de fallos, las latencias lognormales, la capacidad del servidor simulado, los seis mutantes del refactor y el corpus de 14 fragmentos) los eligió el autor y las simulaciones son modelos, no sistemas reales. Lo que **no se hizo**: no se midió ningún sistema en producción ni ningún equipo; no se comparó el efecto de usar patrones en la mantenibilidad percibida; los tiempos de sockets son de un equipo y de un protocolo trivial; el modelo del interés de la deuda es una ilustración con supuestos y no una medición; y no se usó ningún conjunto de datos externo. Las cifras deben leerse como la demostración de un método de medir, no como proporciones generales.

## Guía razonada clase por clase

### Bloque 1 — Elegir y reconocer patrones

#### SE-313 — Criterios para usar un catálogo de patrones

Enseña a tratar un patrón como una decisión con costo y no como una virtud: nombrar la fuerza, comprobar que la variación existe hoy, medir el costo en nodos e indirección y escribir la condición de salida. Aparece primero porque las demás clases aplican el mismo criterio. Produce un `criterio-de-patron.md` con una comparación medida de una función antes y después de un patrón.

#### SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype

Enseña cómo se crean los objetos y cuándo cada patrón creacional añade o quita problemas: un Singleton con estado, un Builder que en Python compite con los argumentos con nombre, una fábrica con registro y un Prototype con la trampa de la copia superficial. Aparece después de los criterios porque cada patrón se somete a ellos. Produce un cuaderno con las medidas de orden de pruebas y de contaminación de clones.

#### SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite

Enseña a envolver y componer objetos sin romper su interfaz, y a ver que el orden de los decoradores es una decisión de política. Aparece tras los creacionales porque trabaja con objetos ya creados. Produce un cuaderno con la comparación de dos órdenes de la misma pila y una prueba de contrato común a dos adaptadores.

#### SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method

Enseña a mover decisiones de condicionales a objetos y a controlar los modos de fallo propios de cada uno: oyentes que no se dan de baja, un fallo que impide el resto de las notificaciones, estados representados con banderas. Aparece después de los estructurales porque combina objetos ya envueltos con reglas de comportamiento. Produce una tabla de transiciones con un fuzzing de secuencias.

### Bloque 2 — Responsabilidades y datos

#### SE-317 — GRASP y asignación de responsabilidades

Enseña los nueve criterios de GRASP como respuestas a la pregunta «¿a quién le toca esto?» y los verifica con un cambio de regla en dos diseños. Aparece aquí porque los patrones anteriores son consecuencias de asignar bien responsabilidades. Produce una tabla de responsabilidades con un cambio de regla comprobado.

#### SE-318 — Repository, Unit of Work y Active Record

Enseña a separar el modelo de la persistencia sin esconder consultas ni transacciones: contar las consultas con un gancho, agrupar cambios en una unidad de trabajo y reconocer cuándo un Active Record basta. Aparece después de GRASP porque es una decisión de dónde vive la responsabilidad de guardar. Produce un cuaderno con consultas contadas y atomicidad comprobada.

### Bloque 3 — Integración y resiliencia

#### SE-319 — Enterprise Integration Patterns como lenguaje común

Enseña los patrones de mensajería como respuestas a las garantías débiles de un canal: receptor idempotente, enrutador por contenido, cartas muertas, reordenador e identificador de correlación. Aparece después del acceso a datos porque los mensajes son otro modo de cambiar estado. Produce una simulación con suma de control.

#### SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker

Enseña los tres patrones que acotan el tiempo y el esfuerzo de una llamada a una dependencia, y a ver la amplificación multiplicativa de los reintentos entre capas. Aparece aquí porque reutiliza decoradores (`SE-315`) y la medida de latencia de las clases previas. Produce una simulación con cuatro políticas de espera y un circuit breaker.

#### SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación

Enseña a limitar el radio del daño con compartimentos, a sacar políticas de red de la aplicación con un intermediario y a degradar con honestidad. Aparece después de la clase anterior porque se pregunta qué pasa cuando los límites de tiempo no bastan. Produce una simulación de compartimentos y una medida real del costo de un salto.

### Bloque 4 — Evaluar e integrar

#### SE-322 — Antipatrones y deuda de diseño

Enseña a reconocer antipatrones por sus síntomas medibles (cohesión, acoplamiento, ciclos) y a distinguirlos de una incomodidad, y a hablar de deuda con un modelo explícito de interés. Aparece aquí porque se necesitan los patrones antes para saber qué se desvía de ellos. Produce un informe de métricas.

#### SE-323 — Taller: refactorizar con patrones y medir su costo

Enseña a refactorizar una función con una cadena de condiciones a Strategy con un maestro dorado, a descubrir qué mutantes escapan y a decidir con medidas si el patrón se queda. Produce un registro del taller con la decisión y la condición de salida.

#### SE-324 — Proyecto: catálogo de patrones de un sistema real

Integra la parte: se hace el inventario de patrones de un sistema, se verifica cada candidato y se escribe un catálogo con fuerza, evidencia, costo y condición de salida. Produce el catálogo y la revisión de por qué se descartó cada patrón rechazado.

## Resumen operativo del recorrido

| Clase | Núcleo profesional | Aporte acumulativo |
|---|---|---|
| [SE-313](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/) | Criterios para usar un catálogo de patrones | Produce un `criterio-de-patron.md` con una comparación medida de una función antes y después de un patrón |
| [SE-314](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/) | GoF creacionales: Factory, Builder, Singleton y Prototype | Produce un cuaderno con las medidas de orden de pruebas y de contaminación de clones |
| [SE-315](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/) | GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite | Produce un cuaderno con la comparación de dos órdenes de la misma pila y una prueba de contrato común a dos adaptadores |
| [SE-316](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/) | GoF conductuales: Strategy, Observer, Command, State y Template Method | Produce una tabla de transiciones con un fuzzing de secuencias |
| [SE-317](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/) | GRASP y asignación de responsabilidades | Produce una tabla de responsabilidades con un cambio de regla comprobado |
| [SE-318](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/) | Repository, Unit of Work y Active Record | Produce un cuaderno con consultas contadas y atomicidad comprobada |
| [SE-319](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/) | Enterprise Integration Patterns como lenguaje común | Produce una simulación con suma de control |
| [SE-320](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/) | Resiliencia: timeout, retry con jitter y circuit breaker | Produce una simulación con cuatro políticas de espera y un circuit breaker |
| [SE-321](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/) | Resiliencia: bulkhead, sidecar, ambassador y degradación | Produce una simulación de compartimentos y una medida real del costo de un salto |
| [SE-322](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/) | Antipatrones y deuda de diseño | Produce un informe de métricas |
| [SE-323](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/) | Taller: refactorizar con patrones y medir su costo | Produce un registro del taller con la decisión y la condición de salida |
| [SE-324](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/) | Proyecto: catálogo de patrones de un sistema real | Produce el catálogo y la revisión de por qué se descartó cada patrón rechazado |

## Fuentes

- Gamma, E., Helm, R., Johnson, R. y Vlissides, J. [«Design Patterns: Elements of Reusable Object-Oriented Software»](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610).
- Fowler, M. [«Catalog of Patterns of Enterprise Application Architecture»](https://martinfowler.com/eaaCatalog/).
- Hohpe, G. y Woolf, B. [«Enterprise Integration Patterns»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/).
- Nygard, M. [«Release It!, 2.ª edición»](https://pragprog.com/titles/mnee2/release-it-second-edition/).
- Microsoft. [«Cloud Design Patterns»](https://learn.microsoft.com/azure/architecture/patterns/).
- Amazon Web Services. [«Timeouts, retries and backoff with jitter»](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/).
- Google. [«Addressing Cascading Failures»](https://sre.google/sre-book/addressing-cascading-failures/).
- Python Software Foundation. [«Python 3 Documentation»](https://docs.python.org/3/).

## Criterios de aceptación de la parte

La parte se considera cumplida cuando existen las doce clases con las dieciséis secciones del contrato, tres figuras por clase con su lectura y sus límites, experimentos reproducibles con la salida declarada, fuentes vinculadas a afirmaciones concretas y la evidencia propia de cada clase. No se afirma revisión humana de la parte: los experimentos y los resultados citados son los que produce el código del repositorio.
