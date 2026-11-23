# Monolito

## Definición

Un **monolito** es un sistema que se despliega como una sola unidad (`SE-327`). El término no habla del tamaño del código sino de la unidad de despliegue. `SE-327` lo contrasta con el **monolito modular**, que mantiene una única unidad de despliegue pero impone fronteras entre módulos, y con los servicios o microservicios, que se despliegan por separado.

## Por qué importa

Elegir entre monolito, monolito modular y servicios es una decisión de fronteras y de costos operativos. `SE-327` enumera las ventajas prácticas del monolito: las llamadas entre módulos son llamadas de función, una transacción de base de datos cubre varias entidades, una prueba de extremo a extremo corre en un proceso y el equipo opera una sola cosa.

## Cómo funciona

El defecto característico del monolito no es el tamaño sino la **falta de fronteras internas**: cuando cualquier módulo puede importar cualquier otro, un cambio en uno afecta a todos y desplegar una corrección pequeña exige probar el sistema entero. Dice `SE-327`: un monolito sin fronteras no es una decisión, es la ausencia de una.

El **monolito modular** mantiene la unidad de despliegue pero cada módulo expone una API pública y oculta sus detalles, y una regla comprobable prohíbe importar lo demás. Sigue el criterio de Parnas de ocultar la decisión que puede cambiar. Conserva las transacciones locales y las pruebas rápidas y deja abierta la puerta a separar un módulo más adelante, porque la frontera ya existe y se comprueba. Su riesgo es que la regla se erosione si nadie la verifica: por eso el comprobador es parte de la arquitectura.

## Ejemplo

En `SE-327`, un cambio pequeño exige probar todo el sistema porque el monolito no tiene fronteras internas; la corrección es imponer API públicas y un comprobador de importaciones, es decir, pasar a un monolito modular, sin pagar el costo de la red.

## Errores y confusiones comunes

- **Creer que «monolito» y «microservicios» son dos bandos.** Son extremos de un continuo de fronteras, y la mayor parte del beneficio de una frontera (límites claros entre módulos) puede obtenerse sin pagar el costo de la red (`SE-327`).
- **Un monolito sin fronteras internas.** Un cambio pequeño exige probar todo el sistema.
- **Fronteras sin comprobador.** La regla se erosiona si nadie la verifica.

## Límites y cuándo no aplica

El monolito modular conserva una sola unidad de despliegue: si se necesita desplegar o escalar partes por separado, hay que cruzar fronteras de red, con los costos que `SE-340` trata. El ejemplo de la clase es sintético y no prescribe cuándo conviene cada opción.
