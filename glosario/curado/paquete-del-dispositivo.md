# Paquete del dispositivo

## Definición

El **paquete del dispositivo** es un documento que reúne las decisiones de identidad, versiones, reversión, claves, umbrales, reintentos, despliegue, vigilancia, responsabilidad y revisión de un dispositivo. Es el artefacto de `SE-276` (proyecto: dispositivo simulado operable y actualizable). No es un paquete de software ni un instalador: es la documentación de decisiones que hace revisable al dispositivo.

## Por qué importa

Reúne decisiones dispersas en un lugar revisable. En un dispositivo que vivirá años, esas decisiones se toman en clases, piezas de código y conversaciones distintas; si no se reúnen, nadie ve el conjunto ni detecta las que se contradicen. `SE-276` precisa que no sustituye al código: lo hace revisable.

## Cómo funciona

El paquete tiene **nueve secciones**, que responden:

1. Cómo se **identifica** el dispositivo.
2. Qué **versión** corre y cómo **vuelve atrás**.
3. Cómo **rota sus claves**.
4. Qué **umbrales** usa.
5. Cómo **reintenta**.
6. Cómo se **despliega** una versión.
7. Cuál es el plazo de su **temporizador de vigilancia**.
8. **Quién responde** por él.
9. **Cuándo se revisa.**

La clase lo apoya en dos fuentes: NISTIR 8259A, que enumera capacidades que un dispositivo debe ofrecer, y los registros breves de decisión de Nygard. Tiene un **validador** que comprueba la forma, y una **simulación** que prueba que las decisiones funcionan juntas.

## Ejemplo

El nodo ambiental de una sala de estudio cierra en `SE-276` su caso conductor de la Parte 22. El proyecto deja el duodécimo artefacto: el paquete del dispositivo operable y actualizable, con su validador, su simulación y sus límites, que reúne los once anteriores. Cambiar una sola decisión, el tamaño de la primera etapa del despliegue, muestra qué fallos dejan de detectarse.

## Errores y confusiones comunes

- **Un paquete que pasa el validador y falla en la flota:** el validador comprueba forma; hacen falta reglas de sentido y revisión humana (`SE-276`).
- **Escribirlo una vez y no revisarlo:** la novena sección existe por eso.
- **Tratarlo como sustituto del código o de las pruebas.**
- **Confundirlo con la operabilidad:** esta es la propiedad; el paquete es el documento que la hace revisable.

## Límites y cuándo no aplica

Es un documento sobre un dispositivo *simulado*: no demuestra que un dispositivo físico cumpla lo escrito. Para productos sin dispositivos desplegables a largo plazo, algunas secciones pierden sentido. Su valor depende de que lo escrito se mantenga al día con el código.
