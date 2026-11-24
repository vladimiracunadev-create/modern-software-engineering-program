# Prueba de regresión

## Definición

Una **prueba de regresión** es una prueba que falla ante el defecto original y pasa con la corrección, y que se conserva para detectar si el defecto reaparece. `SE-069` (pruebas tempranas y diseño por ejemplos) es la clase donde se define; `SE-251` y `SE-467` la reutilizan en talleres de reparación de una API y de un control de seguridad. No es lo mismo que «volver a ejecutar todas las pruebas»: aquí el término nombra una prueba concreta nacida de un defecto concreto.

## Por qué importa

Evita que un defecto reparado reaparezca. Un defecto que ya costó una vez una investigación es el más barato de proteger: cuesta una prueba y su ejecución automática. Sin ella, la corrección depende de que nadie vuelva a tocar esa parte.

## Cómo funciona

`SE-069` fija la secuencia:

1. **Escribir primero el caso que falla.**
2. **Verificar rojo por la razón correcta:** que falla por el defecto, no por un error de la prueba.
3. **Corregir.**
4. **Conservar la prueba** en la suite.

Dos precisiones de la clase: la **cobertura** indica ejecución, no calidad de los oráculos (una línea ejecutada no es una línea comprobada), y se priorizan decisiones y riesgos, no líneas.

En `SE-251`, el equipo recibe una API con diez defectos: escribe suites, mide qué falla, repara por orden de riesgo, añade una prueba de regresión por cada reparación, **reintroduce cada defecto y registra qué suite lo detecta**, y publica la lista de defectos dormidos. Ese paso final comprueba que la prueba realmente protege.

## Ejemplo

Ilustración propia del paso 2: un defecto en el cálculo de la nota final con entrega tardía. La prueba de regresión fija una entrega con un día de retraso y comprueba la penalización esperada. Se ejecuta antes de corregir (rojo, y falla por la penalización ausente), se corrige y pasa (verde). Si alguien reintroduce el defecto, vuelve a fallar.

## Errores y confusiones comunes

- **Un defecto reparado reaparece:** no se dejó una prueba que lo atrape (`SE-251`).
- **Una prueba que nunca estuvo en rojo:** no se sabe si detecta el defecto.
- **Confundirla con pruebas de humo o con ejecutar toda la suite tras cada cambio.**
- **Considerar suficiente la cobertura** sin comprobar que los oráculos detectan el defecto.

## Límites y cuándo no aplica

Protege contra el defecto conocido, no contra el siguiente. Una suite de regresión que crece sin poda se vuelve lenta y frágil. Para defectos que dependen de condiciones difíciles de reproducir (carreras, fallos de infraestructura), la prueba puede ser inestable o requerir inyección de fallos.
