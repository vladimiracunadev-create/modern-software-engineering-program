# Recuperación

## Definición

**Recuperación** tiene cuatro sentidos en el programa. En SE-555 (IA asistida) es la búsqueda que devuelve fragmentos de un índice relevantes para una consulta. En SE-194 (Git) es traer de vuelta lo que parece perdido. En SE-480 (releases) es el conjunto de simulacros de pérdida de una versión publicada (retroceso, y otros). En SE-611 (ML) es la vuelta a un estado sano verificado con la métrica. Esta entrada desarrolla sobre todo el sentido de Git y de release, y señala los otros.

## Por qué importa

Lo que no se ensaya no se sabe que funciona (SE-480). Y recuperar es posible solo dentro de una frontera: saber qué sigue en la base y qué se perdió determina qué comando sirve. Cambia la política de respaldo y de publicación: se decide de antemano qué se puede recuperar y se practica.

## Cómo funciona

**Git (SE-194).** Git solo puede recuperar lo que entró en su base de objetos. Un commit que dejó de ser alcanzable sigue ahí hasta que el **reflog** expira y se poda; se encuentra con `git reflog`. Un archivo agregado al índice crea un blob que `git fsck --lost-found` puede hallar. En cambio, un cambio que **nunca se agregó** y un archivo sin rastrear **no tienen copia**. La política de recuperación empieza por esa frontera: lo que se quiere poder recuperar debe entrar en la base (commit o al menos `git add`). La distinción de fondo es entre «existe» y «es alcanzable».

**Release (SE-480).** Cuatro simulacros examinan cuatro formas de perder algo. El **retroceso** es la más frecuente: la versión nueva tiene un defecto y se quiere la anterior. El verificador, para evitar que un atacante sirva versiones viejas, rechaza una secuencia menor; por tanto el retroceso **no es reinstalar el bundle antiguo**, sino publicar el contenido anterior como una versión nueva (por ejemplo, 1.4.2 con una secuencia mayor que la defectuosa). Los otros simulacros cubren la pérdida de claves y de otros elementos del canal.

**Recuperación (retrieval) en IA (SE-555).** El sistema recupera fragmentos de un índice (por ejemplo con BM25 y fragmentos de 200 palabras con filtro de versión vigente) para dárselos como contexto a un asistente. **ML (SE-611).** La recuperación es volver a un modelo o estado sano y comprobarlo con la métrica.

## Ejemplo

Tras un `git reset --hard HEAD~3`, tres commits dejan de estar en la rama. `git reflog` los lista; se crea una rama en el commit deseado y vuelve el trabajo. En cambio, un archivo nuevo que nunca se añadió con `git add` y se borró con `git clean` no tiene copia en Git. (Comportamiento estándar de Git, tal como lo describe SE-194.)

## Errores y confusiones comunes

- **Creer que Git guarda todo**: solo lo que entró en su base de objetos.
- **Reinstalar el paquete antiguo para retroceder**: el verificador lo rechaza; hay que publicar el contenido anterior como versión nueva.
- **No ensayar la recuperación.**
- **Confundir los cuatro sentidos.**

## Límites y cuándo no aplica

El reflog es local y expira; no protege a otras personas ni a clones. Un procedimiento de recuperación solo vale si se ensayó. En ML, la vuelta a un estado sano exige que haya una versión anterior verificada y una métrica clara para decidir.
