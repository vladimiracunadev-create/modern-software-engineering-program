# Causa común

## Definición

Una **causa común** es un solo evento o condición que degrada varios canales que se suponían independientes. El programa lo usa con el mismo núcleo en varias clases: `SE-445` (riesgo y seguridad funcional) la presenta como lo que rompe el producto de probabilidades; `SE-274`, como origen único de fallos de varios componentes redundantes; `SE-440`, como evento único que provoca el fallo simultáneo; `SE-325`, como fallo por algo compartido (despliegue, configuración, dependencia); `SE-499`, como origen compartido que hace que los fallos dejen de ser independientes.

## Por qué importa

La redundancia solo ayuda si los canales fallan por separado. Si dos réplicas comparten fuente de energía, versión de software o configuración, su probabilidad conjunta de fallar no es el producto de las individuales. `SE-446` dice que la causa común limita lo que gana la redundancia. Cambia la decisión de diseño: en lugar de añadir una réplica más, se pregunta qué comparten las existentes.

## Cómo funciona

Si dos canales fallan cada uno con probabilidad *p* de forma independiente, ambos fallan con *p²*. Con causa común, una fracción de los fallos afecta a los dos a la vez y esa fracción domina. `SE-446` lo modela con el parámetro β, la fracción de causa común. Con λ = 2 × 10⁻⁶ por hora, intervalo de prueba de un año y β = 0,05, el laboratorio da 8,76 × 10⁻³ para 1oo1, 5,30 × 10⁻⁴ para 1oo2 y 7,15 × 10⁻⁴ para 2oo3. Con pruebas cada cinco años: 4,38 × 10⁻², 4,50 × 10⁻³ y 9,12 × 10⁻³. Notación: «1oo2» son dos canales donde basta uno para cortar; «2oo3», tres donde cortan si dos coinciden.

`SE-445` indica buscar al menos una causa común al construir un árbol de fallos; `SE-274` propone diversidad de principio, de alimentación y de software; `SE-325` y `SE-440`, enumerar lo que comparten las réplicas y aislarlo.

## Ejemplo

`SE-274`: «tenemos tres sensores» y fallan los tres, porque compartían principio de medida o alimentación. `SE-440`: el sistema cae más de lo que da la cuenta porque las capas comparten algo. Ilustración propia: dos servidores en zonas distintas, pero ambos con el mismo despliegue defectuoso, fallan juntos.

## Errores y confusiones comunes

- **Multiplicar probabilidades de componentes sin verificar independencia.**
- **Contar réplicas como protección cuando comparten dependencia** (`SE-325`).
- **Confundirla con falla en cascada:** la cascada propaga de un componente a otro; la causa común afecta a varios simultáneamente por un origen compartido.

## Límites y cuándo no aplica

El valor de β es una estimación, no una constante medible fácilmente; los números de `SE-446` son un laboratorio con parámetros elegidos, no datos de un sistema. Y el análisis solo encuentra las causas comunes que alguien se pregunta; una no imaginada sigue ahí. Si los canales son realmente diversos y aislados, el modelo independiente es una aproximación razonable.
