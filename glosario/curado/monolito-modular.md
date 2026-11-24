# Monolito modular

## Definición

Un **monolito modular** es un monolito (una sola unidad de despliegue) con fronteras entre módulos que se verifican, de modo que cada módulo expone una API pública y oculta sus detalles (`SE-327`). Es la alternativa intermedia entre un monolito sin estructura interna y una arquitectura de servicios distribuidos.

## Por qué importa

La elección suele plantearse como monolito contra microservicios. El monolito modular propone obtener los beneficios de la modularidad (cambios locales, equipos con áreas claras) sin pagar de inmediato el costo de la distribución (red, consistencia entre servicios, despliegues múltiples). La decisión que cambia es cuándo separar: se empieza con fronteras comprobadas y se separa solo el módulo que lo justifique.

## Cómo funciona

`SE-327` define tres rasgos:

1. **Una única unidad de despliegue**: sigue siendo un solo proceso.
2. **Fronteras impuestas entre módulos**: cada módulo expone una API pública y oculta sus detalles.
3. **Una regla comprobable que prohíbe importar lo demás**: un comprobador de importaciones que falla si un módulo usa lo interno de otro.

Sigue el criterio de Parnas: ocultar la decisión que puede cambiar. Conserva las transacciones locales y las pruebas rápidas, y deja abierta la puerta a separar un módulo más adelante, porque la frontera ya existe y se comprueba. Su riesgo es que la regla se erosione si nadie la verifica; por eso el comprobador es parte de la arquitectura y no un añadido.

La clase conecta los síntomas con la causa. Un cambio pequeño que exige probar todo el sistema señala un monolito sin fronteras internas; la corrección es imponer API públicas y un comprobador de importaciones. Y si la latencia sube al separar un módulo, es que la frontera cruza muchas llamadas por operación: se mide la cantidad de llamadas por operación y se funden o se engruesa la API.

## Ejemplo

Una plataforma organiza el código en módulos de Entregas, Calificaciones y Avisos, cada uno con un paquete público y un interior prohibido para los demás. Una regla en la integración continua falla si Avisos importa algo interno de Calificaciones. Meses después, Avisos requiere escalar aparte: su frontera ya está definida y se extrae a un servicio sin reescribir. Ejemplo ilustrativo de `SE-327`.

## Errores y confusiones comunes

- **Un cambio pequeño exige probar todo el sistema**: monolito sin fronteras internas; se corrige imponiendo API públicas y un comprobador de importaciones.
- **La latencia sube al separar un módulo**: la frontera cruza muchas llamadas por operación; se mide y se funde o engruesa la API.
- **Fronteras solo en el organigrama o el diagrama**: sin comprobador, se erosionan.
- **Creerlo un paso obligatorio hacia microservicios**: puede ser el destino.

## Límites y cuándo no aplica

No resuelve los casos que piden despliegue o escalado independiente desde el inicio, ni aislamiento de fallos entre módulos (un defecto en un módulo puede tumbar el proceso entero). Y su valor depende de mantener el comprobador: sin verificación continua, vuelve a ser un monolito sin estructura. Para sistemas muy pequeños, la modularidad formal puede costar más que lo que ahorra.
