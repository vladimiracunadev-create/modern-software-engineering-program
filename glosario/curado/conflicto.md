# Conflicto

## Definición

**Conflicto** designa, en el programa, una situación de incompatibilidad que se resuelve decidiendo, no ignorando. El sentido base es de `SE-059`: objetivos o restricciones incompatibles. Se concreta en otros contextos:

- **En control de versiones** (`SE-195`): dos cambios afectan líneas contiguas respecto de una base común.
- **En réplicas** (`SE-260`): dos réplicas modificaron el mismo dato sin ver el cambio de la otra, y existen varios estados finales razonables.

## Por qué importa

Un conflicto es información: dice que dos decisiones no caben juntas. Ocultarlo en favor de un resultado limpio produce un modelo falso (`SE-059`). Y resolverlo mal, o creer que no existe porque no hay marcas, entrega un programa roto. La pregunta que cambia: ¿qué estado es el correcto?

## Cómo funciona

- **Texto** (`SE-195`): Git marca ambas versiones; el estilo `diff3` añade la base. Resolver es decidir el estado correcto: uno de los lados, una combinación o algo nuevo.
- **Fusión sin marcas** (`SE-195`, `SE-197`): dos cambios pueden fusionarse sin conflicto textual y romper el programa, porque la compatibilidad semántica no es textual.
- **Réplicas** (`SE-260`): al sincronizar datos editados sin conexión, el sistema necesita una política (la última escritura gana, fusión por campos, resolución por el usuario) y debe elegirla de forma explícita.
- **Restricciones** (`SE-059`): se resuelve comprobando si existe alguna implementación válida; si no existe, hay una contradicción real que hay que devolver a quien decide.

## Ejemplo

Dos ramas cambian la misma función: una renombra un parámetro y otra añade una llamada con el nombre antiguo. Git puede fusionarlas sin marcas, pero el programa falla; solo una prueba lo detecta. Ilustración de marcas con `diff3`:

```text
<<<<<<< HEAD
tope = 5
||||||| base
tope = 3
=======
tope = 10
>>>>>>> rama
```

## Errores y confusiones comunes

- **El conflicto reaparece.** Causa: rama de larga vida con el mismo rebase repetido; corrección: acortarla o activar `rerere` y revisar las resoluciones (`SE-195`).
- **Se oculta una observación contradictoria.** Causa: se prefiere un resultado limpio; corrección: hacer fallar el modelo con el conflicto (`SE-059`).
- **Tratar un conflicto de recursos como contradicción.** Causa: confusión de conceptos; corrección: comprobar si existe alguna implementación válida (`SE-059`).

## Límites y cuándo no aplica

La ausencia de conflicto no prueba corrección (`SE-195`). Los conflictos textuales no existen en datos binarios o generados de la misma forma, y en réplicas no hay una única solución «correcta» sin una regla de negocio. La palabra no significa lo mismo en las tres clases: fija siempre de cuál hablas.
