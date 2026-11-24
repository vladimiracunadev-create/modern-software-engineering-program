# Compromisos entre atributos

## Definición

Los **compromisos entre atributos** (en inglés, *trade-offs*) son las relaciones en las que mejorar un atributo de calidad cuesta otro. Es el sentido de `SE-147`: la calidad no se compra por atributos aislados, porque rendimiento, seguridad, disponibilidad, costo o simplicidad compiten por los mismos recursos y decisiones de diseño.

## Por qué importa

Cambia el momento en que se descubre el choque. `SE-147` lo resume así: descubrirlo al redactar el requisito cuesta una conversación; descubrirlo en producción cuesta un incidente. Un requisito de calidad aislado («que sea muy seguro», «que esté siempre disponible») es una promesa sin precio: quien lo escribe no ha decidido qué está dispuesto a perder para obtenerlo.

## Cómo funciona

`SE-147` da dos ejemplos del mecanismo. Una derivación de contraseña más costosa protege mejor frente a un ataque de fuerza bruta, pero hace más lento cada acceso legítimo: el mismo trabajo que encarece el ataque encarece el uso. Más réplicas aumentan la disponibilidad, pero también el costo de mantener la consistencia entre ellas. En ambos casos el atributo mejora porque se gasta otro.

La especificación debe, por eso, mostrar con qué otro atributo compite cada requisito y quién decide cuál cede. La forma operativa es escribir cada atributo como escenario verificable (estímulo, medida, umbral) y revisar los escenarios por pares buscando los que tiran en direcciones opuestas. Los umbrales deben fijar percentil y ventana: un objetivo con media oculta una cola lenta que concentra el daño, y una disponibilidad anual del 99,9 % puede cumplirse con un mes catastrófico si la ventana diluye una caída larga; por eso se declara la ventana mensual o se añade un tope de caída continua.

## Ejemplo

En `SE-147`, el requisito conductor de la plataforma de entregas se escribe con tres escenarios de calidad verificables. Al ponerlos juntos, el de latencia de la subida y el de seguridad del acceso compiten por presupuesto de tiempo de cada petición; el registro nombra quién decide cuál cede cuando chocan, en lugar de dejar que lo decida el primero que lo implemente.

## Errores y confusiones comunes

- **El tablero está verde y la gente se queja.** El objetivo usa la media y la cola concentra el daño; fijar percentil y fracción de peticiones.
- **Se cumple el 99,9 % anual con un mes catastrófico.** La ventana anual diluye la caída; declarar la ventana.
- **Pedir todos los atributos al máximo.** Es una especificación sin decisión.
- **Creer que un compromiso es un defecto.** Es una propiedad del problema; el defecto es no decidirlo.

## Límites y cuándo no aplica

No todos los atributos compiten en cada sistema: algunos compromisos desaparecen con otra arquitectura o más presupuesto, y el análisis debe distinguir un conflicto real de uno supuesto. Los experimentos de `SE-147` usan datos sintéticos y no midieron un sistema real, de modo que las cifras ilustran el mecanismo y no establecen magnitudes. Y el compromiso lo cierra una decisión de negocio documentada, no el instinto de quien programa.
